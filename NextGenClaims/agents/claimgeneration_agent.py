# agents/claimgeneration_agent.py
import json

def claimgeneration_agent(state: dict) -> dict:
    """
    Simulate claim registration.
    In reality, this would call claim generation API or use Playwright.
    """
    
    # Generate a mock claim ID
    import hashlib
    claim_data = json.dumps(state["extracted_fields"], sort_keys=True)
    mock_claim_id = "CLAIM-" + hashlib.md5(claim_data.encode()).hexdigest()[:8].upper()
    
    print(f"✅ Claim Agent: Claim registered with ID {mock_claim_id}")
    
    return {
        **state,
        "claim_id": mock_claim_id,
        "status": "CLAIM_CREATED"
    }
