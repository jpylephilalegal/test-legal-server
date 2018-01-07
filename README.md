# test-legal-server

## Prerequisites

This documentation assumes that you are using Windows.  If you are
using another platform, you should be able to figure out what to do
from the instructions below.

You will need an up-to-date version of the [Chrome] web browser.

You need to have Python installed on your computer.  To get Python,
download [Anaconda] (choose the 2.7 version -- this is important).

You will also need Python packages for [Selenium] an [Lettuce].  To
get these, open the **Anaconda Prompt** and run:

```
pip install selenium lettuce lettuce_webdriver
```

Next, you will need to [download ChromeDriver].  You will get a file
called `chromedriver.exe`.  Save this in your home directory (e.g.,
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
lettuce features/casenote.feature
```

The first time you run [Lettuce], you will likely get an error,
because there are some things you need to set up before it will work.

First, you will need to edit the password file, which is a file called
`ls-passwords.yml` in your home directory (e.g.,
`C:\Users\JSmith\ls-passwords.yml`).  Use your favorite text editor to
edit this file.

The contents of the file should be something like:

```
abc.legalserver.org:
  jsmith: xxsecretxx
```

This indicates that on the Legal Server instance at
`https://abc.legalserver.org`, there is a user who logs in as `jsmith`
with the password `xxsecretxx`


[Selenium]: http://selenium-python.readthedocs.io/
[Lettuce]: http://lettuce.it/index.html
[Anaconda]: https://www.anaconda.com/download/#windows
[Chrome]: https://www.google.com/chrome/browser/desktop/index.html
[Notepad++]: https://notepad-plus-plus.org/
[Sublime Text]: https://www.sublimetext.com/
[Jupyter Notebook]: jupyter.org
[Download the Zip file]: https://github.com/jpylephilalegal/test-legal-server/archive/v1.0.zip
[download ChromeDriver]: https://sites.google.com/a/chromium.org/chromedriver/downloads
