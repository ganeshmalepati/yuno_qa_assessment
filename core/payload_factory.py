def purchase_minimal():
    return {
        "account_id": "TEST_ACCOUNT",
        "amount": 1000,
        "currency": "USD",
        "payment_method": {
            "type": "CARD",
            "card": {
                "number": "4111111111111111",
                "expiration_month": "12",
                "expiration_year": "2030",
                "security_code": "123"
            }
        },
        "workflow": "DIRECT"
    }

def purchase_without_workflow():
    payload = purchase_minimal()
    payload.pop("workflow")
    return payload
