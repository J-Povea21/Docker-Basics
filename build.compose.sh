#!/bin/bash

echo 'Building images...'

sudo docker compose build &&

echo 'Images built. Now running containers...'

sudo docker compose up -d &&

echo 'Containers running. The process has finished.'