# Created by owner at 7/19/2022
Feature: Amazon Product Search Tests

  Scenario: User can search for a product
   Given Open Amazon page
    When Search for coffee on amazon
    Then Results for coffee shown