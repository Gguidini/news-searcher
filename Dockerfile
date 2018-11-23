FROM python:3.6

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app  

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# copy current dir's content to container's WORKDIR root i.e. all the contents of the web app
COPY news-app/ ./
RUN python manage.py collectstatic --no-input

EXPOSE 8000

# default command to execute    
CMD exec gunicorn news_searcher.wsgi:application --bind 0.0.0.0:8000 --workers 3