# Created by owner at 7/19/2022
Feature: Amazon Product Search Tests

  Scenario: User can search for a product
   Given Open Amazon page
    When Search for coffee on amazon
    Then Results for coffee shown

  Scenario: Verify that user sees hamburger menu on main page
    Given Open Amazon page
    Then Verify hamburger menu is present

  Scenario: Verify all footer links are shown
    Given Open Amazon page
    Then Verify 38 footer links are shown



