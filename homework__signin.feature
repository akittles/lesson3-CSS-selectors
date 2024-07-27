# Created by Owner at 7/26/2024
Feature: Sign In page opens
  # Enter feature description here

  Scenario: User can open sign in page
    Given Open target main page
    When Click on sign in
    When Click on window sign in
    Then Verify sign page opens
