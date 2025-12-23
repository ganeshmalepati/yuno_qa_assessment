from behave import given, then
from utils.headers import get_headers
from core.api_client import ApiClient

@given("valid request headers")
def step_valid_headers(context):
    context.headers = get_headers()
    context.client = ApiClient()

@then("response status should be {status:d}")
def step_verify_response_status(context, status):
    assert context.response.status_code == status, \
        f"Expected {status}, got {context.response.status_code}"

@then('error message should contain "{message}"')
def step_verify_error_message(context, message):
    response_body = context.response.json()
    assert message.lower() in str(response_body).lower()

@then('payment status should be "{expected_status}"')
def step_verify_payment_status(context, expected_status):
    response_body = context.response.json()
    assert response_body.get("status") == expected_status

