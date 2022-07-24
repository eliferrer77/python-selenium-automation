# Created by owner at 7/23/2022
Feature: Amazon Empty Cart Test


  Scenario: User can see they have an empty cart
    Given Launch Amazon website
    When Click on cart
    Then Verify empty cart