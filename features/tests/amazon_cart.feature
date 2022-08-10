# Created by owner at 7/23/2022
Feature: Amazon Empty Cart Test


  Scenario: User can see they have an empty cart
    Given Open Amazon page
    When Click on cart
    Then Verify empty cart

  Scenario: User can view product in cart
    Given Open Amazon page
    When Search for Cat Goth Tumbler on amazon
    And Click on Product
    And Click on Add to Cart button
    And Open Cart Page
    Then Verify cart has 1 item(s)

