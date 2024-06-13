#!/bin/bash

SCRIPTDIR=$(dirname "$0")

. $SCRIPTDIR/../env/bin/activate
python $SCRIPTDIR/manage.py runserver 0.0.0.0:8000