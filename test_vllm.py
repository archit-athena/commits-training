#!/usr/bin/env python3
"""
test_vllm.py - Test vLLM server connection
"""

import requests
import json

def test_vllm_connection():
    url = "http://10.11.7.31:8000/v1/chat/completions"

    payload = {
        "model": "zai-org/GLM-4.6-FP8",
        "messages": [
            {"role": "user", "content": "Hello! Please respond with 'Connection successful' if you can read this."}
        ],
        "max_tokens": 50,
        "temperature": 0.7
    }

    print("🔌 Testing vLLM server connection...")
    print(f"📍 URL: {url}")
    print(f"🤖 Model: {payload['model']}\n")

    try:
        print("⏳ Sending request (this may take a while)...")
        response = requests.post(
            url,
            json=payload,
            headers={"Content-Type": "application/json"},
            timeout=120  # Increased timeout
        )

        print(f"📊 Status Code: {response.status_code}")

        if response.status_code == 200:
            result = response.json()
            print("\n✅ Connection successful!")
            print("\n📝 Response:")
            print(json.dumps(result, indent=2))

            if "choices" in result and len(result["choices"]) > 0:
                content = result["choices"][0]["message"]["content"]
                print(f"\n💬 Generated text: {content}")
        else:
            print(f"\n❌ Request failed")
            print(f"Response: {response.text}")

    except requests.exceptions.ConnectionError:
        print("❌ Connection error: Cannot reach vLLM server")
        print("   Make sure the server is running at http://10.11.7.31:8000")
    except requests.exceptions.Timeout:
        print("❌ Timeout: Server took too long to respond")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_vllm_connection()
