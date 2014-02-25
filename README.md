Looseleaf, a simple viewer of Markdown document collections
===========================================================

*GTK+3 Frontend*

## Description

(Description)

## Features

* No proprietary formats or lock-in; Documents are just plain text files
* Uses Markdown for comfortable reading

## Requirements

One-line dependency installation for Debian/Ubuntu:

    sudo apt-get install python3-gi gir1.2-webkit-3.0

* [Python 3](https://www.python.org)
* [PyGI](https://wiki.gnome.org/action/show/Projects/PyGObject)
* GObject WebKit bindings

## Setup

Virtualenv creation:

    looseleaf-gtk$ virtualenv venv --system-site-packages

## Usage

Looseleaf is launched by simply pointing the executable at a directory where
your files live (or will live):

    $ looseleaf ~/Notes

If the specified directory doesn't already exist, it will be created
automatically as soon as you create your first file.

You can also avoid specifying the same directory each time you launch the
software by setting the LOOSELEAF_HOME environment variable:

    export LOOSELEAF_HOME="~/Notes"

