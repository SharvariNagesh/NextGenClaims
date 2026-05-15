# config/settings.py
import os
from dotenv import load_dotenv

load_dotenv()

# AWS
S3_BUCKET = os.getenv("S3_BUCKET")
AWS_REGION = os.getenv("AWS_REGION")

# Bedrock
BEDROCK_MODEL_ID = os.getenv("BEDROCK_MODEL")
BEDROCK_RUNTIME= os.getenv("BEDROCK_RUNTIME")

POLICY_PDF = os.getenv("POLICY_PDF")
AWS_REGION = os.getenv("AWS_REGION")
AWS_REGION = os.getenv("AWS_REGION")

# Streamlit
STREAMLIT_PAGE_TITLE = "Claims Processing Center"
STREAMLIT_PAGE_ICON = "📋"
