Feature: Customer and Payment Method Management

  Background:
    Given valid request headers

  @sanity
  Scenario: Create customer with minimal details
    When I create a customer with minimal details
    Then response status should be 200
    And customer should be created successfully

  @regression
  Scenario: Create customer with full details
    When I create a customer with full profile details
    Then response status should be 200
    And customer should be created successfully

  @integration
  Scenario: Enroll payment method for existing customer
    Given a customer exists
    When I enroll a card payment method for the customer
    Then response status should be 200
    And payment method should be enrolled successfully

  @negative
  Scenario: Enroll payment method for non-existing customer
    When I enroll payment method with invalid customer id
    Then response status should be 404

  @negative
  Scenario: Create customer without mandatory fields
    When I create a customer without mandatory fields
    Then response status should be 400
