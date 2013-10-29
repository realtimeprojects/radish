# Windows installation Guide

**Author:** Claudio Klinglerer <ck@realtime-projects.com><br />
**License:** GPL<br />

## About this document

In order to use radish on your Windows system, you find here a quick
installation guide on how to get radish running on it.

There may are additional ways in how to get radish running on windows. We
welcome any feedback!

## Step by Step

1. Download Cygwin installer from http://www.cygwin.com
2. Run Cygwin installer
3. Install the following packages. Make sure, you also install
   the recommended additional packages from the next tab.
   1. Git
   2. Python
   3. gcc
   4. python-lxml
   5. libxml2-devel
   6. python-setuptools
   7. python-libxslt
   8. libxslt-devel
   9. vim (not required)
4. Run the cygwin terminal :-)))
5. Clone radish from https://github.com/timofurrer/radish.git under your home directory

        git clone https://github.com/timofurrer/radish.git ~/radish

6. Follow the instructions at "Manual installation from source" from the [README.md](https://github.com/timofurrer/radish#installation_source).

If everything went fine, you should now be able to use radish:

        cd ~/radish/testfiles
        radish features/*

