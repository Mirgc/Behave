Feature: OrangeHRM Logo
  Scenario: Logo presence on OrangeHRM home Page
    Given launch chrome browser
    When open orange hrm home
    Then verify that the logo present on page
    And close browser