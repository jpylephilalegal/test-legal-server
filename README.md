# test-legal-server

## Prerequisites

This documentation assumes that you are using Windows.  If you are
using another platform, you should be able to figure out what to do
from the instructions below.

You will need to install the [Chrome] web browser.

You need to have Python installed on your computer.  To get Python,
download [Anaconda] (choose the 2.7 version -- this is important).

You will also need Python packages for [Selenium] an [Lettuce].  To
get these, open the **Anaconda Prompt** and run:

```
pip install selenium lettuce lettuce_webdriver
```

Next, you will need to [download ChromeDriver].  This is an
application that [Selenium] uses to remote-control [Chrome].  When you
[download ChromeDriver], you will get a file called
`chromedriver.exe`.  Save this in your home directory (e.g.,
`C:\Users\JSmith`).

You will also need a text editor.  [Notepad++] and [Sublime Text] are
good ones.  You can also use the text editor that is built in to
[Jupyter Notebook], which comes with [Anaconda].

## Installation

[Download the Zip file] and extract it into your Documents folder, so
that you have a folder called `test-legal-server-1.0` in your `Documents`
folder.

## How to run

Open the **Anaconda Prompt** and navigate to `Documents\test-legal-server-1.0`:

```
cd Documents\test-legal-server-1.0
```

Now you can run [Lettuce]:

```
lettuce features\casenote.feature
```

The first time you run [Lettuce], you will get an error, because there
are some things you need to set up before it will work.

First, you will need to edit the password file, which is a file called
`ls-passwords.yml` in your home directory (e.g.,
`C:\Users\JSmith\ls-passwords.yml`).  (This file was created for you
when you ran `lettuce` and got an error.)  Use your favorite text
editor to edit this file.

The contents of the file look like this:

```
abc.legalserver.org:
  jsmith: xxsecretxx
```

This indicates that on the Legal Server instance at
`https://abc.legalserver.org`, there is a user who logs in as `jsmith`
with the password `xxsecretxx`.

Edit this file so that it works with your own instance of Legal
Server and your account on that instance.

Second, you will need to edit the file `features\casenote.feature`.

Initially, the file looks like this:

```
Feature: Making a case note
  Test that the Add Case Notes function is working

  Scenario: I need to add a case note to a case
    Given I log in to abc.legalserver.org as jsmith
    And I open case ID 17-0273663
    And I click the menu link "Add Case Notes"
    And I set "Subject" to "A test subject"
    And I set "Body" to "A test Note"
    And I click the continue button
    Then I should see the phrase "A test Note"
    And I log out
```

Note that the words "Making a case note," "Test that the Add Case
Notes function is working," and "I need to add a case note to a case"
are purely descriptive, but the other lines are computer code, which
must be composed with precision.

You will need to change `abc.legalserver.org` to the name of your own
instance of Legal Server, and change `jsmith` to your user name.
Also, change the case ID to a case ID that exists on your system,
which you want to edit.

(By the way, the password is in a separate file, rather than included
in this "feature" file, because passwords are very secret, and you may
want to share your "feature" files with other people.)

Now try running the test again:

```
lettuce features\casenote.feature
```

If all goes well, you will see [Chrome] open on your computer and see
it log into Legal Server and make a case note in a file.

If the test succeeds, it will end with:

```
1 feature (1 passed)
1 scenario (1 passed)
8 steps (8 passed)
Total of 1 of 1 scenarios passed!
```

This is how you know that your scenario is valid.  If the test did not
succeed, you would get an error.

If you wanted to run all of the `.feature` files in the `features`
folder, you could simply run:

```
lettuce
```

## Using Lettuce for automation

It is possible to use [Lettuce] to automate repetitive data entry
tasks in Legal Server.

The `batch.feature` file in the `features` folder demonstrates this.
It takes a data file, `test-data.csv`, which is in the `data` folder,
and goes through it one line at a time.  For each line, it runs the
steps from the `add-case-note.template` file in the `templates`
folder, substituting information from the data file into particular
places.

Here are the contents of the `batch.feature` file:

```
Feature: Make case notes in a series of cases
  Use a CSV file exported from Legal Server to make case notes
  in a series of cases.

  Scenario: I need to add a case note to a case
    Given I log in to pla.legalserver.org as jpyle
    Then I run "add-case-note.template" using "test-data.csv"
    And I log out
```

Here are the contents of the `test-data.csv` file:

```
"caseid","note"
"17-0273663","This is a case note."
"17-0279103","This is another case note."
```

Here are the contents of the `add-case-note.template` file:

```
I open case ID {caseid}
I click the menu link "Add Case Notes"
I set "Body" to "{note}"
I click the continue button
```

When `batch.feature` runs, it first logs in, and then goes through
`test-data.csv` line-by-line, running the four steps in
`add-case-note.template` for each line, substituting the `caseid` and
`note` values from the data file.  Note that the names in curly
brackets must correspond exactly with the names of columns indicated
in the first ("header") line of the comma-separated-values (CSV) file.

## Step syntax

The following are the types of steps you can use in your scenarios.

    I log in to <server> as <username>

Logs into Legal Server.

    I click the "<option>" option under "<label>"

Selects an option from a pull-down selector.

    I click the continue button

Clicks the standard Legal Server "Continue" button.

    I click the button "<button>"

Clicks a particular button based on the button's display name.

    I click the link "<link name>"

Clicks a particular link based on the link's display name.

    If I see it, I will click the link "<>"

Clicks a particular link based on the link's display name, but if the
link does not exist, do nothing.

    I click the menu link "<link name>"

Clicks a link in the Legal Server "action menu" or similar menu.

    I log out

Clicks the "Logout" button

    I open case ID <caseid>

Goes to the Search menu, opens "Case ID," and searches for the given
Case ID.

    I run "<template file name>" using "<data file name>"

For each of the rows in the data file, it runs the steps in the given template.

    I select "<option>" as the "<label>"

For a pull-down selector labeled with the `<label>`, selects the option
labeled `<option>`.  E.g., `I select "Massachusetts" as the "State"`

    I set "<label>" to "<value>"

For a text box labeled with the `<label>`, types in the text
`<value>`.  E.g., "I set "Body" to "This case should be rejected as a duplicate."

    I should see the phrase "<phrase>"

If the text `<phrase>` does not exist anywhere on the screen, the test
should fail.  If it does exist, move on to the next step.

    I should not see the phrase "<phrase>"

If the text `<phrase>` exists anywhere on the screen, the test
should fail.

    I should see "<url>" as the URL of the page

If the location bar for the current screen is not `<url>`, the test
should fail.

    I should see "<title>" as the title of the page

If the title of the page (which is visible in the web browser tab) is
not `<title>`, the test should fail.

    I should see that "<label>" is "<value>"

If the value of the field designated by `<label>` is not `<value>`,
the test should fail.

    I upload the file "<file>"

Uploads the file `<file>` from the current directory.  E.g., `I upload
the file "petition.pdf"`.

    I wait <seconds> seconds

Waits `<seconds>` seconds.  E.g., "I wait 5 seconds" or "I wait 1 second".

    I wait forever

Pauses indefinitely.  This is helpful when you want to use a test to
bring you to a specific situation, from which you can take control of
the browser.  To stop the test, type Ctrl-c in the **Anaconda Prompt**
window.

To add your own "step" controls, edit the file `legalserver.py` in the
`steps` folder.

## Warnings

You may get a warning that suggests you install the
`python-Levenshtein` package.  You can try that if you want, but it
requires installing additional dependencies, so it is a little bit
complicated.

[Selenium]: http://selenium-python.readthedocs.io/
[Lettuce]: http://lettuce.it/index.html
[Anaconda]: https://www.anaconda.com/download/#windows
[Chrome]: https://www.google.com/chrome/browser/desktop/index.html
[Notepad++]: https://notepad-plus-plus.org/
[Sublime Text]: https://www.sublimetext.com/
[Jupyter Notebook]: jupyter.org
[Download the Zip file]: https://github.com/jpylephilalegal/test-legal-server/archive/v1.0.zip
[download ChromeDriver]: https://sites.google.com/a/chromium.org/chromedriver/downloads

