Feature: Making a case note
  Test that the Add Case Notes function is working

  Scenario: I need to add a case note to a case
    Given I log in to pla.legalserver.org as jpyle
    And I open case ID 17-0273663
    And I click the menu link "Case Questions"
    Then I should see that "Legal Problem Code" is "76 Unemployment Compensation"
    And I click the button "Expand Notes"
    And I wait forever
    And I click the menu link "Add Case Notes"
    And I set "Subject" to "A test subject"
    And I set "Body" to "A test Note"
    And I click the continue button
    Then I should see the phrase "A test Note"
    And I log out
