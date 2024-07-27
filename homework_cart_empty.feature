# Created by Owner at 7/25/2024
Feature: Target empty cart message
  # Enter feature description here

  Scenario: User checks if cart is empty
    Given Open target main page
    When Click on cart icon
    Then Verify your cart is empty message is shown
