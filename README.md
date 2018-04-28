# What is Bootini Star?

If you miss CCP's discontinued EVE Gate application, Bootini Star--abbreviated
as 'BS' from here on out--may be for you. BS is written in Python and uses the
EVE Swagger Interface, Flask and more to allow EVE players to handle their
evemail et al in a web browser.

# What do I need?

You can either run BS yourself if you meet the requirements listed below, or
find somebody who already runs a BS installation like I do, in which case you
only need a web browser. This text is meant for people who want to run their own
instance of BS and/or help with the development.

# How do I run my own instance?

## Requirements

1. An active EVE Online player account (Alpha or Omega).
* A registered application with [CCP Games](https://developers.eveonline.com).
* Python 3.4 or later (3.6 is recommended).
* [pip](https://pypi.python.org/pypi/pip)
* [bash](https://www.gnu.org/software/bash/) or similar.

## Setting up a fresh environment

Clone using Git:

```shell
cd /your/projects
git clone https://github.com/rseichter/bootini-star.git
```

Create and activate a fresh virtual Python environment:

```shell
cd bootini-star
python3.6 -m venv venv
source venv/bin/activate
```

Install BS and required packages. Note that I use a PostgreSQL database for
local development, and the necessary package is therefore listed in the
requirements file.

```shell
pip install -e .
pip install -r requirements.txt
# For developers
pip install -r requirements-testing.txt
which flask
```

The last command should return ```/your/projects/bootini-star/venv/bin/flask```.

Next, you need to configure BS according to your local needs using environment
variables. See the ```config.py``` module for a list of environment variables
to use.

```shell
cd /your/projects/bootini-star
# Activate the virtual Python environment
source venv/bin/activate
# Flask basics
export FLASK_APP='bootini_star'
export FLASK_ENV='development'
# Allow HTTP callbacks during local development
export OAUTHLIB_INSECURE_TRANSPORT=1
# Change the following three lines!
export SECRET_KEY='Choose something random here'
export ESI_CLIENT_ID='Your ESI client ID'
export ESI_SECRET_KEY='Your ESI secret key'
# Change to whatever DB you use
SQLALCHEMY_DATABASE_URI='postgresql://postgres:@localhost/bs'
```
Once the settings are to your satisfaction,
initialise the database:

```shell
flask db upgrade
```

This will create the necessary DB tables.

## Why is there no complete default configuration?

Every BS installation requires individual settings for application ID,
application secret and OAuth2 callback URL which are available only after
registering an application at [CCP's developer
site](https://developers.eveonline.com). That is something I cannot do for you,
because for some weird reason I don't seem to have access to your EVE online
accounts.

## Running the application

Make sure to set up your environment properly for each development session, as
described above. You might want to add these commands to a shell script. With the correct environment, all that's left to do is this:

```shell
# Set up environment first!
flask run
```

After Flask startup is complete, you should be able to open the application via
[http://127.0.0.1:5000](http://127.0.0.1:5000) in your web browser, if you have
kept Flask's default server and port settings.
