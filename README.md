# Setup

You need `make` and `git-lfs` installed. Most Unix like environment come with make
in the box. To install `git-lfs` see below.

## Mac
`brew install git-lfs`

## Ubuntu
```
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
apt install git-lfs
```

## Other
Follow the installation instructions in the official wiki https://github.com/git-lfs/git-lfs/wiki/Installation

## Additional

* `git lfs install` - do users need to do that? I assume yes since git hooks need to be installed
* `make virtualenv` - assuming we will use some packages and train some models

# Data

Initially downloaded by running
`curl -s https://raw.githubusercontent.com/t-davidson/hate-speech-and-offensive-language/master/data/labeled_data.csv --output data/data.csv`
