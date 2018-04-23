#!/bin/bash
echo "Listen in Heroku's PORT: $PORT"
/usr/bin/python3 manage.py runserver 0.0.0.0:$PORT
