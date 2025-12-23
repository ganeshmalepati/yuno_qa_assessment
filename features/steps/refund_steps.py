from behave import given, when, then
from core.payload_factory import purchase_minimal
from core.config import BASE_URL

@given("a successful payment exists")
def step_successful_payment(context):
    payload = purchase_minimal()
    context.response = context.client.post(BASE_URL, context.headers, payload)
    context.payment_id = context.response.json().get("payment_id")

@when("I refund the purchase payment")
def step_refund_payment(context):
    refund_url = f"{BASE_URL}/{context.payment_id}/refund"
    context.response = context.client.post(refund_url, context.headers, {})

@when("I refund the full payment amount")
def step_refund_full(context):
    refund_url = f"{BASE_URL}/{context.payment_id}/refund"
    context.response = context.client.post(refund_url, context.headers, {
        "amount": 1000
    })

@when("I refund a partial amount")
def step_refund_partial(context):
    refund_url = f"{BASE_URL}/{context.payment_id}/refund"
    context.response = context.client.post(refund_url, context.headers, {
        "amount": 500
    })

@when("I refund more than the captured amount")
def step_refund_excess(context):
    refund_url = f"{BASE_URL}/{context.payment_id}/refund"
    context.response = context.client.post(refund_url, context.headers, {
        "amount": 2000
    })

@when("I refund using an invalid payment id")
def step_refund_invalid_id(context):
    refund_url = f"{BASE_URL}/invalid_id/refund"
    context.response = context.client.post(refund_url, context.headers, {})
