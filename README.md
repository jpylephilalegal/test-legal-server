# test-legal-server

## Prerequisites

This documentation assumes that you are using Windows.  If you are
using another platform, you should be able to figure out what to do
from the instructions below.

You will need an up-to-date version of the [Firefox] web browser.

You need to have Python installed on your computer.  To get Python,
download [Anaconda] (choose the 3.6 version).

You will also need Python packages for [Selenium], [Lettuce], and
[PyYAML].  To get these, open the **Anaconda Prompt** and run:

```
pip install selenium lettuce pyyaml
```

You will also need a text editor.  [Notepad++] and [Sublime Text] are
good ones.

## Installation

Download the Zip file and unpack it into your Documents folder.

## How to run

Open the **Anaconda Prompt** and navigate to `Documents/test-legal-server`:

```
cd Documents\test-legal-server
```

Now you can run [Lettuce]:

```
lettuce features/casenote.feature
```

The first time you run [Lettuce], you will likely get an error,
because there are some things you need to set up.

First, you will need to edit the password file

[Selenium]: http://selenium-python.readthedocs.io/
[Lettuce]: http://lettuce.it/index.html
[Anaconda]: https://www.anaconda.com/download/#windows
[Firefox]: https://www.mozilla.org/en-US/firefox/new/
