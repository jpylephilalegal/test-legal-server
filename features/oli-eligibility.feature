Feature: Pro bono divorce on-line intake triage system
  Test that the on-line intake system for divorce screens people appropriately

  Scenario: Applicant is outside of Philadelphia
    I run the template "oli-start.feature"
    Then I should see the phrase "Residence"
    And I set "Do you live in Philadelphia?" to "No"
    Then I should see the phrase "We are sorry, but you are not eligible for this service. Free attorneys are only available for residents of Philadelphia."

  Scenario: Divorce is already pending
    I run the template "oli-start.feature"
    Then I should see the phrase "Residence"
    And I set "Do you live in Philadelphia?" to "Yes"
    Then I should see the phrase "Questions about your case"
    And I set "Is there already a divorce case involving you and your spouse?" to "Yes"
    Then I should see the phrase "If divorce papers have already been filed, we cannot help you. We only provide assistance with preparing divorce papers."

  Scenario: Neither party has been in Philadelphia for six months
    I run the template "oli-start.feature"
    Then I should see the phrase "Residence"
    And I set "Do you live in Philadelphia?" to "Yes"
    Then I should see the phrase "Questions about your case"
    And I set "Is there already a divorce case involving you and your spouse?" to "No"
    And I set "Have you been living in Pennsylvania for the past six months?" to "No"
    And I set "Has your spouse been living in Pennsylvania for the past six months?" to "No"
    Then I should see the phrase "In order to file for divorce in Philadelphia, either you or your spouse needs to have lived in Pennsylvania for the past six months."

  Scenario: Spouse whereabouts unknown
    I run the template "oli-start.feature"
    Then I should see the phrase "Residence"
    And I set "Do you live in Philadelphia?" to "Yes"
    Then I should see the phrase "Questions about your case"
    And I set "Is there already a divorce case involving you and your spouse?" to "No"
    And I set "Have you been living in Pennsylvania for the past six months?" to "Yes"
    And I set "Are you currently living in the same house or apartment as your spouse?" to "No"
    And I set "Have you been living in a different place from your spouse for more than two years?" to "Yes"
    And I set "Is your spouse in prison?" to "No"
    And I set "Do you know the address where your spouse lives?" to "No"
    And I set "Do you or your spouse own any significant property, such as a house or a pension?" to "No"
    And I set "Do you or your spouse have significant debts (e.g., mortgage, significant credit card debt)" to "No"
    And I set "Do you and your spouse have any children together who are under the age of 18?" to "No"
    And I set "What was the date of your marriage?" to "04/04/2010"
    And I set "Where did the marriage take place?" to "Philadelphia, PA"
    And I click "No" under "Is your spouse currently in the military?"
    And I click "No" under "Has there ever been a Protection From Abuse (PFA) order against you, or against your spouse?"
    And I click the continue button
    Then I should see the phrase "Based on your answers to our questions, you appear to be eligible for free legal services with your divorce."

  Scenario: Couple has significant property
    I run the template "oli-start.feature"
    Then I should see the phrase "Residence"
    And I set "Do you live in Philadelphia?" to "Yes"
    Then I should see the phrase "Questions about your case"
    And I set "Is there already a divorce case involving you and your spouse?" to "No"
    And I set "Have you been living in Pennsylvania for the past six months?" to "Yes"
    And I set "Are you currently living in the same house or apartment as your spouse?" to "No"
    And I set "Is your spouse in prison?" to "No"
    And I set "Do you or your spouse own any significant property, such as a house or a pension?" to "Yes"
    Then I should see the phrase "We are sorry, but you are not eligible for this service. Free attorneys are only available for cases that do not involve the division of assets. We recommend that you hire an attorney to assist you."
