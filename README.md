# Breathe

A meditative experience inviting people across the world to take a breath together.

This repo is for the cloud run function which runs on a schedule to update the visitor count on https://breathe.acjensen.com. The frontend is [here](https://github.com/acjensen/breathe).

# Local testing

1. `pip3 install -r requirements.txt`
1. `export GOOGLE_APPLICATION_CREDENTIALS="/path/to/google/app/credentials/my-app-287219-ac93a1b70446.json"`
1. `python3 test.py`
