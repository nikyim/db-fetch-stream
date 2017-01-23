#!/bin/bash

option=$1

if [ "$option" == "start" ]
then
    ps aux | grep '[m]ain.py'
    if [ $? -ne 0 ]
    then
        /opt/conda/bin/python /var/db-fetch-stream/main.py
    fi
fi