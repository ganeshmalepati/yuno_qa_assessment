Feature: Purchase Payment API

  @sanity
  Scenario: Purchase with minimal fields
    Given valid request headers
    When I send purchase request with minimal payload
    Then response status should be 200
    And payment status should be "AUTHORIZED"

  @negative
  Scenario: Purchase without workflow
    Given valid request headers
    When I send purchase request without workflow
    Then response status should be 400


