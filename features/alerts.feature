Feature: I want to validate alerts into my application
  Scenario: Validate that I can accept an alert
    Given I am on the herokuapp homepage
    When I click on the Java Script Alerts link
    And I click on the JS Alert button
    And I accept the alert
    Then I should see the text "You successfully clicked an alert"
