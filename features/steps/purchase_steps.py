from behave import when, then
from core.payload_factory import (
    purchase_minimal,
    purchase_without_workflow
)
from core.config import BASE_URL

@when("I create a purchase payment with minimal required fields")
def step_purchase_minimal(context):
    payload = purchase_minimal()
    context.response = context.client.post(BASE_URL, context.headers, payload)
    context.payment_response = context.response.json()

@when("I create a purchase payment using a valid card")
def step_purchase_valid_card(context):
    payload = purchase_minimal()
    context.response = context.client.post(BASE_URL, context.headers, payload)
    context.payment_response = context.response.json()

@when("I create a purchase payment with customer and additional data")
def step_purchase_full_payload(context):
    payload = purchase_minimal()
    payload["customer_payer"] = {
        "id": "cust_123",
        "email": "test@yuno.com"
    }
    payload["additional_data"] = {
        "ip_address": "127.0.0.1"
    }
    context.response = context.client.post(BASE_URL, context.headers, payload)
    context.payment_response = context.response.json()

@when("I retry the same purchase request using the same idempotency key")
def step_purchase_idempotency(context):
    payload = purchase_minimal()
    context.response = context.client.post(BASE_URL, context.headers, payload)
    context.second_response = context.client.post(BASE_URL, context.headers, payload)

@when("I create a purchase payment without workflow")
def step_purchase_without_workflow(context):
    payload = purchase_without_workflow()
    context.response = context.client.post(BASE_URL, context.headers, payload)

@then('workflow should be "{workflow}"')
def step_verify_workflow(context, workflow):
    assert context.payment_response.get("workflow") == workflow
