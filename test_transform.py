#!/usr/bin/env python3
"""
test_transform.py - Test the transformation on a single example
"""

from granular_generator import GranularDatasetGenerator

# Sample data from alo.py
sample = {
    "prompt": "feat(connector): [PlaceToPay] Implement Cards for PlaceToPay (#3117)\n\nSigned-off-by: chikke srujan <121822803+srujanchikke@users.noreply.github.com>\nCo-authored-by: hyperswitch-bot[bot] <148525504+hyperswitch-bot[bot]@users.noreply.github.com>",
    "response": """Files to modify:


**placetopay.rs**
  Remove:
    - function: private::get_auth_header
    - impl: impl ConnectorValidation for Placetopay
  Add:
    - function: private::validate_capture_method
    - function: private::get_request_body
    - function: private::get_headers
    - function: private::get_content_type
    - function: private::get_url
    - function: private::get_request_body
    - function: private::build_request
    - function: private::handle_response
    - function: private::get_error_response
    - impl: impl ConnectorValidation for Placetopay

**transformers.rs**
  Remove:
    - struct: pub::PlacetopayAuthType
    - enum: pub::PlacetopayPaymentStatus
  Add:
    - struct: pub::PlacetopayAuthType
    - struct: pub::PlacetopayAuth
    - struct: pub::PlacetopayPayment
    - struct: pub::PlacetopayAmount
    - struct: pub::PlacetopayInstrument
    - enum: pub::PlacetopayAuthorizeAction

**utils.rs**
  Add:
    - function: pub::generate_random_bytes"""
}

def main():
    print("=" * 80)
    print("🧪 Testing Transformation")
    print("=" * 80)

    # Create generator in transform mode
    generator = GranularDatasetGenerator(
        dataset_name="test",
        output_dir="test_output",
        vllm_url="http://10.11.7.31:8000/v1",
        model="zai-org/GLM-4.6-FP8",
        mode="transform"
    )

    print("\n📥 Original prompt:")
    print(sample["prompt"][:100] + "...")
    print("\n📥 Original response:")
    print(sample["response"][:200] + "...")

    print("\n🤖 Calling LLM for transformation...")
    transformed = generator.transform_commit(sample)

    print("\n" + "=" * 80)
    print("✨ TRANSFORMED RESULT")
    print("=" * 80)

    print("\n📤 New prompt:")
    print(transformed["prompt"])

    print("\n📤 New response:")
    print(transformed["response"])

    print("\n" + "=" * 80)

if __name__ == "__main__":
    main()
