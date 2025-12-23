import uuid

def get_headers():
    return {
        "public-api-key": "YOUR_PUBLIC_KEY",
        "private-secret-key": "YOUR_SECRET_KEY",
        "x-idempotency-key": str(uuid.uuid4()),
        "Content-Type": "application/json"
    }

