# Azure DevOps Extension Task Example

## Overview

This repository is for me to see how to build, test, package and publish an
Azure DevOps Extension.

The `shovel/shovel.py` holds the actual tasks that are performed to build and
publish the ADO Extension. The Tasks being created are stored in `tasks/`. This
is useful for making an Extension with multiple tasks.

## Requirements

* NodeJS + TypeScript
    * Windows: [nvm-windows](https://github.com/coreybutler/nvm-windows)
    * Linux/MacOS: [nvm-sh](https://github.com/nvm-sh/nvm)
* Python 3 + pip (For the shovel task runner)

## Setup

Install the Python 3 dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r python-3-requirements.txt
```

Then build the package.

```bash
shovel build
```

This will `cd tasks/buildAndReleaseTask/` then execute `./node_modules/.bin/tsc`
via `npm`'s s script functionality.

## Usage

Package the ADO Extension

```bash
shovel package
```

This will execute the `tfx` CLI client to package the ADO Extension.

## References

* [Microsoft Azure DevOps: Create Custom Agent Task](https://docs.microsoft.com/en-us/azure/devops/extend/develop/add-build-task?view=azure-devops)
* [Microsoft Azure DevOps: azure-pipelines-task-lib Reference](https://github.com/microsoft/azure-pipelines-task-lib/blob/master/node/docs/azure-pipelines-task-lib.md)
* [Microsoft Azure DevOps: Custom Task Folder Structures](https://docs.microsoft.com/en-us/azure/devops/extend/develop/integrate-build-task?view=azure-devops)
* [Microsoft Azure DevOps: vss-extension.json Schema](https://docs.microsoft.com/en-us/azure/devops/extend/develop/manifest?view=azure-devops)
* [Microsoft Azure DevOps: Create Custom Server Task](https://github.com/Microsoft/azure-pipelines-tasks/blob/master/docs/authoring/servertaskauthoring.md)
