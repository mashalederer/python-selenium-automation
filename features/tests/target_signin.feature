# Created by mashalederer at 9/18/25
Feature: Test Scenarios for Target sign in

  Scenario: User can sign in
    Given Open Target page
    When click on sign in button
    And From right side navigation menu click sign in button
    Then Sign In form opened
