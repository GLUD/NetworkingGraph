#!/bin/bash
echo "Listen PORT: $PORT"
/usr/bin/python3 manage.py runserver 0.0.0.0:$PORT
