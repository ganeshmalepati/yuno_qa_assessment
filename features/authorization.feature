Feature: Authorization Payment Flow

  Background:
    Given valid request headers

  @sanity
  Scenario: Authorization with minimal required fields
    When I create an authorization payment with minimal fields
    Then response status should be 200
    And payment status should be "AUTHORIZED"

  @regression
  Scenario: Authorization with maximum fields
    When I create an authorization payment with full payload
    Then response status should be 200
    And payment status should be "AUTHORIZED"

  @integration
  Scenario: Capture an authorized payment
    Given an authorized payment exists
    When I capture the authorized payment
    Then response status should be 200
    And payment status should be "CAPTURED"

  @integration
  Scenario: Refund a captured payment
    Given a captured payment exists
    When I refund the captured payment
    Then response status should be 200
    And refund status should be "SUCCEEDED"

  @negative
  Scenario: Capture without authorization
    When I capture a non-authorized payment
    Then response status should be 400

  @negative
  Scenario: Cancel an already captured payment
    Given a captured payment exists
    When I cancel the payment
    Then response status should be 400
