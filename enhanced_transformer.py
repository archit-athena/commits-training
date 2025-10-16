#!/usr/bin/env python3
"""
Enhanced transformer that creates Product Abstraction → Code Pattern mappings

This combines:
1. archit11/hyperswitch-rust-commits-final2 (commit → detailed file changes)
2. juspay/hyperswitch (problem statement → patch)

To create training data that teaches:
"When implementing X product feature, you typically modify Y code patterns"
"""

from datasets import load_dataset
import json
import re
from typing import Dict, List, Optional
from pathlib import Path


class ProductCodeMapper:
    """Extract product abstractions and code patterns from commits"""

    def __init__(self, vllm_client=None):
        self.vllm_client = vllm_client

    def extract_file_hierarchy(self, patch: str) -> Dict[str, List[str]]:
        """
        Extract files organized by architectural layer

        Returns:
            {
                'api_models': ['customers.rs'],
                'database': ['query/customers.rs'],
                'domain': ['customer.rs'],
                'core': ['customers.rs'],
                ...
            }
        """
        files = re.findall(r'diff --git a/(.+?) b/', patch)

        hierarchy = {
            'api_models': [],
            'database': [],
            'domain': [],
            'core_business': [],
            'connectors': [],
            'types': [],
            'utils': [],
            'tests': [],
            'config': [],
            'other': []
        }

        for file in files:
            if 'api_models' in file:
                hierarchy['api_models'].append(file)
            elif 'diesel_models' in file or 'query' in file or 'schema' in file:
                hierarchy['database'].append(file)
            elif 'domain_models' in file or 'hyperswitch_domain' in file:
                hierarchy['domain'].append(file)
            elif 'router/src/core' in file or 'core' in file:
                hierarchy['core_business'].append(file)
            elif 'connector' in file:
                hierarchy['connectors'].append(file)
            elif 'types' in file or '_types' in file:
                hierarchy['types'].append(file)
            elif 'utils' in file or 'helpers' in file:
                hierarchy['utils'].append(file)
            elif 'test' in file:
                hierarchy['tests'].append(file)
            elif 'config' in file or '.yml' in file or '.toml' in file:
                hierarchy['config'].append(file)
            else:
                hierarchy['other'].append(file)

        # Remove empty categories
        return {k: v for k, v in hierarchy.items() if v}

    def extract_change_types(self, patch: str) -> Dict[str, int]:
        """
        Analyze what kind of changes were made

        Returns counts of:
        - struct additions
        - function additions
        - enum additions
        - field additions to existing structs
        - query modifications
        - validation additions
        """
        changes = {
            'structs_added': len(re.findall(r'\+\s*(?:pub\s+)?struct\s+\w+', patch)),
            'functions_added': len(re.findall(r'\+\s*(?:pub\s+)?(?:async\s+)?fn\s+\w+', patch)),
            'enums_added': len(re.findall(r'\+\s*(?:pub\s+)?enum\s+\w+', patch)),
            'fields_added': len(re.findall(r'\+\s+(?:pub\s+)?\w+:\s+', patch)),
            'imports_added': len(re.findall(r'\+\s*use\s+', patch)),
            'conditionals_added': len(re.findall(r'\+\s*if\s+', patch)),
            'database_queries': len(re.findall(r'(\.filter|\.eq\(|SELECT|INSERT|UPDATE)', patch)),
        }
        return {k: v for k, v in changes.items() if v > 0}

    def extract_product_intent(self, problem_statement: str, hints_text: str = "") -> Dict:
        """
        Extract product-level information from problem statement and PR description

        Returns:
            {
                'feature_type': 'search' | 'payment' | 'auth' | 'refund' | ...,
                'action': 'add' | 'fix' | 'enhance' | 'refactor',
                'entities': ['customer', 'payment', ...],
                'business_goal': extracted goal text
            }
        """
        combined_text = (problem_statement + " " + hints_text).lower()

        # Detect feature type
        feature_type = 'unknown'
        if any(word in combined_text for word in ['search', 'filter', 'query', 'find']):
            feature_type = 'search_filter'
        elif any(word in combined_text for word in ['payment', 'card', 'charge', 'transaction']):
            feature_type = 'payment'
        elif any(word in combined_text for word in ['auth', 'login', 'token', 'session']):
            feature_type = 'authentication'
        elif any(word in combined_text for word in ['refund', 'cancellation', 'void']):
            feature_type = 'refund'
        elif any(word in combined_text for word in ['connector', 'integration', 'provider']):
            feature_type = 'connector_integration'
        elif any(word in combined_text for word in ['webhook', 'callback', 'notification']):
            feature_type = 'webhook'
        elif any(word in combined_text for word in ['validation', 'verify', 'check']):
            feature_type = 'validation'

        # Detect action type
        action = 'unknown'
        if any(word in combined_text for word in ['[feat]', 'add', 'implement', 'new feature']):
            action = 'add_feature'
        elif any(word in combined_text for word in ['[bug]', 'fix', 'resolve', 'issue']):
            action = 'fix_bug'
        elif any(word in combined_text for word in ['enhance', 'improve', 'optimization']):
            action = 'enhance'
        elif any(word in combined_text for word in ['refactor', 'restructure']):
            action = 'refactor'

        # Extract entities (simplified)
        entities = []
        entity_patterns = ['customer', 'payment', 'merchant', 'user', 'order', 'refund',
                          'connector', 'webhook', 'session', 'token', 'card', 'transaction']
        for entity in entity_patterns:
            if entity in combined_text:
                entities.append(entity)

        return {
            'feature_type': feature_type,
            'action': action,
            'entities': entities[:3],  # Top 3 entities
        }

    def create_enhanced_prompt_from_juspay(self, example: Dict) -> str:
        """
        Create a natural, product-focused prompt from juspay/hyperswitch data

        Combines problem_statement + hints to create a realistic dev query
        """
        problem = example.get('problem_statement', '')
        hints = example.get('hints_text', '')

        # Extract the core question
        # Remove markdown headers and boilerplate
        problem_clean = re.sub(r'###\s+.*?\n', '', problem)
        problem_clean = re.sub(r'Bug:|Feature:|FEAT:|BUG:', '', problem_clean)
        problem_clean = problem_clean.strip()

        # Get the description section if it exists
        desc_match = re.search(r'Description:?\s*\n+(.*?)(?=\n###|\nSolution:|\Z)', problem, re.DOTALL | re.IGNORECASE)
        if desc_match:
            description = desc_match.group(1).strip()
        else:
            # Use first paragraph
            lines = [l.strip() for l in problem_clean.split('\n') if l.strip() and not l.startswith('[')]
            description = lines[0] if lines else problem_clean

        return description

    def create_enhanced_response_from_juspay(self, example: Dict) -> str:
        """
        Create a digestible, pattern-aware response from juspay/hyperswitch data

        Shows: Architecture layers touched + what kind of changes + why
        """
        patch = example.get('patch', '')
        problem = example.get('problem_statement', '')
        hints = example.get('hints_text', '')

        hierarchy = self.extract_file_hierarchy(patch)
        change_types = self.extract_change_types(patch)
        intent = self.extract_product_intent(problem, hints)

        # Build natural language response
        response_parts = []

        # Add intent context
        response_parts.append(f"To implement this **{intent['feature_type']}** feature, you'll need to modify these architectural layers:\n")

        # Describe each layer
        layer_descriptions = {
            'api_models': 'API Request/Response Models',
            'database': 'Database Layer (Queries & Schema)',
            'domain': 'Domain Models (Business Logic Types)',
            'core_business': 'Core Business Logic',
            'connectors': 'External Connector Integration',
            'types': 'Type Definitions',
            'config': 'Configuration Files',
        }

        for i, (layer, files) in enumerate(hierarchy.items(), 1):
            layer_name = layer_descriptions.get(layer, layer.replace('_', ' ').title())
            response_parts.append(f"\n**{i}. {layer_name}**")

            # Group files by directory
            for file in files[:3]:  # Show top 3 files per layer
                file_short = file.split('/')[-1]
                response_parts.append(f"   - `{file}`")

            if len(files) > 3:
                response_parts.append(f"   - ... and {len(files) - 3} more files")

        # Add change patterns
        if change_types:
            response_parts.append("\n**Code Patterns Applied:**")
            pattern_descriptions = {
                'structs_added': 'Define new data structures',
                'functions_added': 'Implement new functions',
                'fields_added': 'Extend existing types with new fields',
                'conditionals_added': 'Add conditional logic for feature flags or filtering',
                'database_queries': 'Modify database queries',
            }
            for change, count in change_types.items():
                if change in pattern_descriptions:
                    response_parts.append(f"- {pattern_descriptions[change]} ({count} changes)")

        return '\n'.join(response_parts)

    def create_enhanced_prompt_from_commit(self, commit_msg: str, response: str) -> str:
        """
        Create a natural prompt from archit11 commit message

        Transform: feat(connector): [PlaceToPay] Implement Cards
        Into: How do I add card payment support for PlaceToPay?
        """
        # Remove boilerplate
        clean = re.sub(r'Signed-off-by:.*', '', commit_msg, flags=re.DOTALL)
        clean = re.sub(r'Co-authored-by:.*', '', clean, flags=re.DOTALL)
        clean = clean.strip()

        # Extract the core action
        # Pattern: feat(scope): [Component] Action
        match = re.match(r'(feat|fix|chore|refactor)\(([^)]+)\):\s*\[?([^\]]+)\]?\s*(.+)', clean, re.IGNORECASE)

        if match:
            action_type, scope, component, description = match.groups()

            # Convert to natural question
            if action_type.lower() == 'feat':
                return f"How do I implement {description.lower()} for {component}?"
            elif action_type.lower() == 'fix':
                return f"How do I fix {description.lower()} in {component}?"
            else:
                return f"How do I {action_type.lower()} {description.lower()} for {component}?"

        # Fallback: use first line
        first_line = clean.split('\n')[0]
        return f"How do I: {first_line}"

    def create_enhanced_response_from_commit(self, commit_msg: str, response: str) -> str:
        """
        Transform archit11 technical response into digestible patterns

        From:
          **placetopay.rs**
            Add:
              - function: private::validate_capture_method

        To:
          Modify placetopay.rs:
          - Add validation for capture methods (validate_capture_method)
          - Add request builders (get_headers, get_request_body)
        """
        result_parts = []

        # Parse the response structure
        current_file = None
        current_action = None
        file_changes = {}

        for line in response.split('\n'):
            # Detect file
            file_match = re.match(r'\*\*([^*]+)\*\*', line)
            if file_match:
                current_file = file_match.group(1)
                file_changes[current_file] = {'add': [], 'remove': [], 'modify': []}
                continue

            # Detect action
            if line.strip() in ['Add:', 'Remove:', 'Modify:']:
                current_action = line.strip().rstrip(':').lower()
                continue

            # Extract items
            if current_file and current_action:
                item_match = re.match(r'\s*-\s*(function|struct|enum|impl):\s*(.+)', line)
                if item_match:
                    item_type, item_name = item_match.groups()
                    # Simplify name
                    simple_name = item_name.split('::')[-1] if '::' in item_name else item_name
                    file_changes[current_file][current_action].append((item_type, simple_name))

        # Build natural description
        for file, changes in file_changes.items():
            result_parts.append(f"**{file}:**")

            if changes['add']:
                grouped = {}
                for item_type, name in changes['add']:
                    grouped.setdefault(item_type, []).append(name)

                for item_type, names in grouped.items():
                    if len(names) == 1:
                        result_parts.append(f"  - Add {item_type}: `{names[0]}`")
                    else:
                        result_parts.append(f"  - Add {len(names)} {item_type}s: {', '.join([f'`{n}`' for n in names[:3]])}")

            if changes['remove']:
                result_parts.append(f"  - Remove: {', '.join([f'`{n}`' for _, n in changes['remove']])}")

            if changes['modify']:
                result_parts.append(f"  - Modify: {', '.join([f'`{n}`' for _, n in changes['modify']])}")

            result_parts.append("")  # Blank line between files

        return '\n'.join(result_parts)


def main():
    """Test the enhanced mapping"""
    print("=" * 80)
    print("🧬 Enhanced Product-Code Pattern Mapper")
    print("=" * 80)

    mapper = ProductCodeMapper()

    # Load juspay example
    print("\n📦 Loading juspay/hyperswitch dataset...")
    juspay_ds = load_dataset("juspay/hyperswitch")

    # Find the customer search example
    example = None
    for item in juspay_ds['train']:
        if 'juspay__hyperswitch-9642' in item['instance_id']:
            example = item
            break

    if not example:
        example = juspay_ds['train'][0]

    print(f"\n✨ Example: {example['instance_id']}")

    # Create enhanced prompt/response
    enhanced_prompt = mapper.create_enhanced_prompt_from_juspay(example)
    enhanced_response = mapper.create_enhanced_response_from_juspay(example)

    print("\n" + "=" * 80)
    print("📤 ENHANCED PROMPT (Product Level)")
    print("=" * 80)
    print(enhanced_prompt)

    print("\n" + "=" * 80)
    print("📤 ENHANCED RESPONSE (Code Patterns)")
    print("=" * 80)
    print(enhanced_response)

    # Save example
    output = {
        'prompt': enhanced_prompt,
        'response': enhanced_response,
        'metadata': {
            'instance_id': example['instance_id'],
            'intent': mapper.extract_product_intent(example['problem_statement'], example['hints_text']),
            'hierarchy': mapper.extract_file_hierarchy(example['patch']),
            'change_types': mapper.extract_change_types(example['patch'])
        }
    }

    with open('enhanced_example.json', 'w') as f:
        json.dump(output, f, indent=2)

    print("\n💾 Saved to: enhanced_example.json")


if __name__ == "__main__":
    main()
