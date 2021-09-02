# LoginChallenge
CTF Challenge for the 2021 Activity Fair

## Install + Setup

### Install Flask

**Windows**

Install Python:

https://www.python.org/downloads/release/python-397/

Set PATH:
- Start > Edit Environment Variables
- Add Python install directory to both System and Environment variables

Check python installed:

```
PS > python --version
```

Install flask:

```
PS > python -m pip install flask
```

**Linux**

```
$ python3 -m pip install flask
```

## Run

### Windows

```
PS > cd .\web\
PS > $env:FLASK_APP = "app"
PS > python -m flask run
```