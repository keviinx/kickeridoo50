#!/bin/bash
# change directory to kickeridoo directory
cd ~/Github/kickeridoo50
# set application.py to FLASK_APP
export FLASK_APP=application.py
# start the flask server
flask run --host=0.0.0.0 &