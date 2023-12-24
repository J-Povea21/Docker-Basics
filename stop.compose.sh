#!/bin/bash

echo 'Stoping containers...'
sudo docker stop back front &&

echo 'Containers stoped. Removing process started...'

sudo docker rm back front &&

echo 'Containers removed. Removing images started...'

sudo docker rmi -f frontend && sudo docker rmi -f backend &&

echo 'Images removed! Now removing default network...'

sudo docker network rm platzi-project_default &&

echo 'Network removed. The process has finished.'
