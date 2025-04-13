Feature: Target search test case

  Scenario: User can search for the product on Target
    Given Open target main page
    When Search for tea
    Then Verify correct search results shown
    Then click on the cart icon
    Then Verify your cart is empty
    Then Select to sign in
    Then Click Sign in or Create account button
    Then Verify Sign in page is open

