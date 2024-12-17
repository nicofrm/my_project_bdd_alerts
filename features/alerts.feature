Feature: I want to validate alerts into my application

  Background:
    Given I am on the herokuapp homepage
    When I click on the Java Script Alerts link

  Scenario: Validate that I can accept an alert
    When I click on the JS Alert Button
    And I accept the alert
    Then I should see the text "You successfully clicked an alert"

  Scenario: Validate that I can cancel an alert
    When I click on the JS Confirm Button
    And I cancel the alert
    Then I should see the text "You clicked: Cancel"

  Scenario: Validate that I can cancel an alert
    When I click on the JS Prompt Button
    And I insert text "I insert a test text" into the alert prompt and I click ok
    Then I should see the text "You entered: I insert a test text"
