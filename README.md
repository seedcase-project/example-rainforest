# Template for Seedcase Python packages

This repository contains a template for setting up new Python package projects in Seedcase. The first step is to create a new repository using this template. This can easily be done by clicking the "Use this template" button on the repository page or by using the GitHub CLI:

``` bash
# NAME is the name to give the new repository
gh repo create NAME --template seedcase-project/template-python-project
```

## Setting things up after cloning

To add Poetry:

``` bash
cd new-project
poetry init
```

Search for `NAME` and `REPO` and replace them with the name of your project and the repository name. Then look for any `TODO` items.

## Setting things up

Use the commands found in [`spaid`](https://github.com/seedcase-project/spaid) repo to run the next setup steps.
