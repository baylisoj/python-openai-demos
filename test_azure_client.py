import os
import azure.identity
import openai
from dotenv import load_dotenv

load_dotenv(override=True)

# Test with AzureOpenAI client (proper way)
token_provider = azure.identity.get_bearer_token_provider(
    azure.identity.DefaultAzureCredential(), 
    "https://cognitiveservices.azure.com/.default"
)

# The endpoint should NOT include /openai/v1 when using it as azure_endpoint
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT", "").replace("/openai/v1", "")
print(f"Using endpoint: {endpoint}")

try:
    client = openai.AzureOpenAI(
        azure_endpoint=endpoint,
        azure_ad_token_provider=token_provider,
        api_version="2024-08-01-preview"
    )
    
    response = client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT"),
        messages=[{"role": "user", "content": "Say 'Hello, Azure!'"}],
        max_tokens=10
    )
    
    print(f"\nSuccess! Response: {response.choices[0].message.content}")
except Exception as e:
    print(f"\nError: {type(e).__name__}: {e}")
