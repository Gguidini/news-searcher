# News Searcher

News Searcher is a simple system that collects news articles from the internet, ranks them and generates part of the news clipping produced by the team in Sala de Situação.

This project was created for them ([Sala de Situação](https://fs.unb.br/saladesituacao/)), taylored for their needs.
If you are going to work in it, as a developer, then this **manual will guide you in the system structure and components**. All python files are (hopefully) well commented, for your convenience. 

You're welcome. Good luck.

# System Overview

### Normal Operation Sequence
The operation sequence is as follows:

1. Select **sources** and **terms** to search;
2. Select best news to move to clipping. News are ranked based on user-defined score for each search term selected, and displayed in decreasing order of score. When selecting a news article the user is also supposed to sleect the region for that article.
3. Download clipping docx file generated. News articles will also have been moved to the [News Database](https://github.com/luisfbgs/BD-Sala-de-Situacao), created by another group.
   
Each of these operations has a dedicated view. There's also an extra view for the settings.

### Deploy Structure
The system was requested to be deployed using Docker. The structure uses Django as the webframework, Gunicorn to communicate with Django and serve files, and Nginx to receive requests from the internet and serve static files.

The docker-compose file creates 2 containers: one for Django+Gunicorn, another for Nginx. They are connected by a bridge network.

# System File Structure - Overview
Below is an overview of the more important files and folders in the system. Less important ones are left out. A more in-depth overview of the core system's structure is given further on.

System's structure layout follows Django layout - obviously. If you're not familiarized with it, [read the docs](https://www.djangoproject.com/).

```
news-searcher/
|
|-- news-app/   # Root of the Django application
|       |
|       |-- docs/     # Manuals and documentation on the system
|       |-- interface/   # App inside Django that actually does all the magic
|       |       |
|       |       |-- src/    # System core functionality. View details below.
|       |       |-- templates/  # templates for system's views
|       |       |-- tests/  # tests for CORE code only
|       |       |-- views.py  # definition of system's views behavior
|       |-- media/  # stores generated Clipping, temporarily
|       |-- news_searcher/  # Django settings
|       |       |
|       |       |-- settings.py  # system-wide configurations
|       |       |-- urls.py      # url patterns
|       |--manage.py  # Controls Django app
|-- nginx/  # Nginx configuration
|       |-- nginx.conf
|
|-- docker-compose.yml  # Definition of docker-compose. Sets up containers
|-- Dockerfile  # Build file for the news searcher container. Not nginx.
|-- requirements.txt  # System python requirements
```

As a developer, you mainly need to concern yourself with from `news-app/` folder down. The rest is just configuration and deployment.

# System Core - Overview
The core functionality of the system is defined in `news-searcher/news-app/interface/src`. Let's take a closer look in that now.

```
src/
|
|-- assets/  # Pictures and templates used in clipping generation
|-- bins/    # configuratio varaiables pickle files
|-- config.py  # Configuration variables and functions
|-- data_output.py  # Clipping generation and DB connection
|-- models.py   # definition of News class
|-- news_handler.py   # Connection to NewsAPI
|-- scor-_handler.py  # Handles ranking process
```