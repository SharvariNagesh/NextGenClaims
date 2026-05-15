# agents/validation_agent.py
import boto3
import json

from tools.aws_tools import REQUIRED_FIELDS
from config.settings import AWS_REGION, BEDROCK_RUNTIME, BEDROCK_MODEL_ID

session = boto3.Session(profile_name="default")
bedrock = session.client(
    BEDROCK_RUNTIME, region_name=AWS_REGION, verify=False)


def extract_fields_with_llm(raw_text: str) -> dict:
    """Use Claude to extract structured fields from raw text."""

    prompt = f"""
You are a claims processing assistant. Extract the following fields from the claim document text below.
Return ONLY a valid JSON object. If a field is not found, set its value to null.
Required fields: {json.dumps(REQUIRED_FIELDS)}
Document text:
---
{raw_text[:3000]}
---
Return only the JSON, nothing else.
"""

    response = bedrock.converse(
        modelId=BEDROCK_MODEL_ID,
        messages=[
            {
                "role": "user",
                "content": [
                    {"text": prompt}
                ]
            }
        ],
        inferenceConfig={
            "maxTokens": 2000,
            "temperature": 0.5
        }
    )
    json_text = response["output"]["message"]["content"][1]["text"]
    extracted_text = json.loads(json_text)
    # Parse JSON response
    try:
        extracted_fields = extracted_text
    except json.JSONDecodeError:
        extracted_fields = {}

    return extracted_fields


def validation_agent(state: dict) -> dict:
    """Validate all required fields are present."""

    extracted = extract_fields_with_llm(state["raw_text"])

    missing_fields = [
        field for field in REQUIRED_FIELDS
        if not extracted.get(field)
    ]

    print(f"✅ Validation complete: {len(missing_fields)} missing fields")

    return {
        **state,
        "extracted_fields": extracted,
        "missing_fields": missing_fields,
        "status": "VALIDATION_COMPLETE"
    }
