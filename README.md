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

Install flask and other dependencies:

```
PS > python -m pip install -r requirements.txt
```

**Linux**

```
$ python3 -m pip install -r requirements.txt
```

## Run

### Windows

```
PS > cd .\web\
PS > $env:FLASK_APP = "app"
PS > $env:FLASK_DEBUG = "true"
PS > python -m flask run
```

## Solution

<details>

<summary>Spoilers</summary>

Via login function:
- Looking closely at the requests when submitting a password shows a POST to `/verify-login` that gives a 302 status code, redirecting to `/secret` which then 302s back to the index page
- When a password is submitted, a `status` cookie is added - it has a value of `hanhgubevfrq` - checking this in a ROT13 decoder, it reads `unauthorized`
- If we change this to `authorized` by deleting the first two letters of the encoded version, we can navigate directly to `/secret`

Via password reset (**TODO**):
- The page has minified javascript that can be prettified
- It shows that when the 'Forgot Password' button is clicked, the security question pops up
- The security question is compared server-side via Ajax - the form is submitted with `new_password=&security_question=answer` - this shows the user the request format
- If the question answer is correct, the new password field appears and a new password can be posted to the same endpoint
- However, the user can simply send `new_password=new&security_question=` and the flask app will behave based on which parameter is set

</details>