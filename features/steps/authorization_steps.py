from behave import given, when, then
from core.payload_factory import purchase_minimal
from core.config import BASE_URL

@given("an authorized payment exists")
def step_authorized_payment(context):
    payload = purchase_minimal()
    context.response = context.client.post(BASE_URL, context.headers, payload)
    context.payment_id = context.response.json().get("payment_id")

@when("I create an authorization payment with minimal fields")
def step_create_authorization(context):
    payload = purchase_minimal()
    context.response = context.client.post(BASE_URL, context.headers, payload)

@when("I capture the authorized payment")
def step_capture_payment(context):
    capture_url = f"{BASE_URL}/{context.payment_id}/capture"
    context.response = context.client.post(capture_url, context.headers, {})

@when("I cancel the payment")
def step_cancel_payment(context):
    cancel_url = f"{BASE_URL}/{context.payment_id}/cancel"
    context.response = context.client.post(cancel_url, context.headers, {})

@when("I capture a non-authorized payment")
def step_capture_without_auth(context):
    fake_payment_id = "invalid_payment_id"
    capture_url = f"{BASE_URL}/{fake_payment_id}/capture"
    context.response = context.client.post(capture_url, context.headers, {})
