![github workflow](https://github.com/pritesh-ranjan/Help-Desk-Search-Engine/actions/workflows/python-app.yml/badge.svg)


![image] (./helpdesk/search/static/search/logo.png)
# Help-Desk-Search-Engine

A web application based on Python-Django and Elasticsearch

## Prequisites:

1. Python3.8
2. Requirements via requirements.txt
   
   `
    pip install -r requirements.txt   
`
   
All python packages like django, etc are installed in this step.
   
3. Elasticsearch 

https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html
   
Note: Elasticsearch also needs Java installed.
Please make sure Elasticsearch is running in localhost port 9200

## Run
` python manage.py runserver`

We can access the web application in the URL below (if it is running in localhost other wise please use appropriate url):

http://127.0.0.1:8000/

Features:
1. User can sign up and login
2. Data gets autogenerated when the user accesses the home url
for the first time.
   
3. User can search the Elastisearch by providing the appropriate query in the searchbar

4. To use the API, user needs to add api after the base url
So to login we need to do POST request to (assuming that script is running in local host)
   http://127.0.0.1:8000/api/login
   
5. To signup, we need to do POST request to 
   http://127.0.0.1:8000/api/signup
   
6. To search a specific query via the API:
We can do a get request. For example:
   http://127.0.0.1:8000/api/search/?query=computer
   
7. We can run tests from the following command
`
python manage.py test search   
`
