Feature: OrangeHRM Logo
  Scenario: Login to OrangeHRM with valid parameters
    Given I launch chrome browser
    When I open orange HRM Homepage
    And Enter username "Admin" and password "admin123"
    And Click on login button
    Then User must successfully login to the Dashboard page