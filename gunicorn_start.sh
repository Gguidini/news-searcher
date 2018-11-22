#!/bin/bash

NAME="news_searcher"                              #Name of the application (*)
DJANGODIR=/var/www/news-searcher		# Django project directory (*)
SOCKFILE=/var/www/news-searcher/run/gunicorn.sock        # we will communicate using this unix socket (*)
USER=gguidini                                       # the user to run as (*)
GROUP=gguidini                                     # the group to run as (*)
NUM_WORKERS=3                                     # how many worker processes should Gunicorn spawn (*)
DJANGO_SETTINGS_MODULE=news_searcher.settings             # which settings file should Django use (*)
DJANGO_WSGI_MODULE=news_searcher.wsgi                     # WSGI module name (*)

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source venv/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec venv/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user $USER \
  --bind=unix:$SOCKFILE
