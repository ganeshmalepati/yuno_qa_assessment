Feature: Refund Payment API

  Background:
    Given valid request headers

  @sanity
  Scenario: Refund a successful purchase
    Given a successful payment exists
    When I refund the full payment amount
    Then response status should be 200
    And refund status should be "SUCCEEDED"

  @regression
  Scenario: Partial refund
    Given a successful payment exists
    When I refund a partial amount
    Then response status should be 200
    And refund status should be "SUCCEEDED"

  @negative
  Scenario: Refund more than captured amount
    Given a successful payment exists
    When I refund more than the captured amount
    Then response status should be 400

  @negative
  Scenario: Refund an already refunded payment
    Given a fully refunded payment exists
    When I refund the payment again
    Then response status should be 409

  @negative
  Scenario: Refund with invalid payment id
    When I refund using an invalid payment id
    Then response status should be 404
