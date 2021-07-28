# Help-Desk-Search-Engine

A web application based on Python-Django and Elasticsearch

## Prequisites:

1. Python3.8
2. Requirements via reuquirements.txt
   
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

We can access the web application in the URL below:

http://127.0.0.1:8000/

Features:
1. User can sign up and login
2. Data gets autogenerated when the user accesses the home url
for the first time.
   
3. User can search the Elastisearch by providing the appropriate query in the searchbar

4. To use the api, user needs to add api after the bse url
So to login we need to do POST request to 
   http://127.0.0.1:8000/api/login
   
5. TO search a specific query via the API:
We can do a get request. For example:
   http://127.0.0.1:8000/api/search/?query=computer
   
6. We can run tests from the following command
`
python manage.py test search   
`
