# Created by mashalederer at 9/18/25
Feature: Test Scenarios for Target Cart

  Scenario: User can check the shopping cart
    Given Open Target page
    When click on Cart icon
    Then see cart is empty