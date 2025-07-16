![django-version](https://img.shields.io/pypi/v/Django?logo=Django&logoColor=green&label=Django)
![pysolr-version](https://img.shields.io/badge/v9.8.1-Solr?logo=apache-solr&label=Apache-Solr&color=blue)
# Polls
A site where you can create, search polls, answer of them. Login and register in the system

## Installation
1. Clone repository:
  ```shell
  $ git clone git@github.com:Kotoninja/Pet-polls-site.git
  $ cd Pet-polls-site
  ```
2. Create and activate virtual environment:
  ```shell
  $ python -m venv venv
  $ venv/scripts/activate # Windows
  $ venv/bin/activate # Linux
  ```
3. Install dependencies:
  ```shell
  $ pip install -r requirements.txt
  ```
4. Create a development database:
  ```shell
  $ python manage.py makemigrations
  $ python manage.py migrate
  ```
5. If everything is alright, start Django server:
  ```shell
  $ python manage.py runserver
  ```

## If Install Solr:
1. Install solr in your system:  
[Getting Started with Haystack](https://django-haystack.readthedocs.io/en/master/tutorial.html#)  
> [!IMPORTANT]
> Be sure to configure schema.xml. [Documentation](https://django-haystack.readthedocs.io/en/master/tutorial.html#reindex)
2. Start Solr:
```shell
$ systemctl start solr #Linux
or
% opt/solr/bin/solr start
```
>[!CAUTION]
> If you got "AttributeError: 'list' object has no attribute 'split' using count() method for a SearchQuerySet" see [Issue #1895](https://github.com/django-haystack/django-haystack/issues/1895) 
