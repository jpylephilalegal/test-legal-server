Feature: Divorce on-line intake
  Ensure divorce on-line intake interview is working properly

  Scenario: Client is eligible
    Given I log in to pla.legalserver.org as jpyle
    And I open case ID 17-0273663
    And I click the menu link "Add Case Notes"
    And I set "Subject" to "A test subject"
    And I set "Body" to "A test Note"
    And I click the continue button
    Then I should see the phrase "A test Note"
    And I log out
    And I wait forever