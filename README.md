# Setup

## Dependencies

You need `make` and `git-lfs` installed. Most Unix like environment come with make
in the box. To install `git-lfs` see below.

### Mac
`brew install git-lfs`

### Ubuntu
```
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
apt install git-lfs
```

### Other
Follow the installation instructions in the official wiki https://github.com/git-lfs/git-lfs/wiki/Installation

## Virtualenv
To create the virtualenv
`make virtualenv`

# Data and models
Data and models are tracked and versioned through `git-lfs`. At the moment `.jsonl`, `.csv` and `.pkl`
files are tracked. You can see a list in `.git-attributes`

You can track additional files by running `git lfs track "*.ext"` with the ext you want.

No need to do anything additional for tracking and version data and models other than following
your git flow. Whenever you run a push or pull command git will sync the data and models separately
and when you checkout, reset etc it will retrieve the version in the same way that retrieves the
version of the source files.

# Repro

For reproducibility we use make and we define helper functions to ease development. Current commands
* preprocess
* train

Those commands create outputs that have dependencies which you define, at the moment the source
and data files. This is simialr to DVC dependencies with the difference that make checks the timestamp
of those files for changes instead of a hash.


# Data source


Initially downloaded by running
`curl -s https://raw.githubusercontent.com/t-davidson/hate-speech-and-offensive-language/master/data/labeled_data.csv --output data/data.csv`
