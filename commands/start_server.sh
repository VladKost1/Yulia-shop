#!/bin/bash
echo "start project"
python src/manage.py migrate
python src/manage.py runserver 0:8010