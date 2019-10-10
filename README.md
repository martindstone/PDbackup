# PDbackup

Backup users, teams, services, schedules and escalation policies as a simple JSON file

## Installation

First, have python 3 installed. Then, clone this repo and cd into it. Then:

    python3 -m venv venv              # create a virtual environment
    . venv/bin/activate               # activate it
    pip install -r requirements.txt   # install dependencies

## Usage

    ./backup.py pd_api_key output_file

    positional arguments:
        pd_api_key   PagerDuty API key
        output_file  Filename to write the backup to
