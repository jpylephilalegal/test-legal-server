Feature: Make case notes in a series of cases
  Using data from a CSV file, make case notes in a series of cases in
  Legal Server.

  Scenario: I need to add case notes to cases
    Given I log in to abc.legalserver.org as jsmith
    Then I run "add-case-note.template" using "test-data.csv"
    And I log out
