import os
from dotenv import load_dotenv
import azure.identity

load_dotenv(override=True)

print(f"API_HOST: {os.getenv('API_HOST')}")
print(f"AZURE_OPENAI_ENDPOINT: {os.getenv('AZURE_OPENAI_ENDPOINT')}")
print(f"AZURE_OPENAI_CHAT_DEPLOYMENT: {os.getenv('AZURE_OPENAI_CHAT_DEPLOYMENT')}")

# Test if we can get Azure credentials
try:
    credential = azure.identity.DefaultAzureCredential()
    print("\nAzure credential created successfully")
    print(f"Credential type: {type(credential)}")
except Exception as e:
    print(f"\nError creating Azure credential: {e}")
