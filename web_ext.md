# Web Module 

## WP1

### Packet Management
* [pipenv](https://realpython.com/pipenv-guide/)

```shell
pip install pipenv
pipenv shell

pipenv install flask pytest
pipenv install -r requirements.txt
pipenv lock

pipenv lock -r > requirements.txt
pipenv lock -r -d > dev-requirements.txt
pipenv graph
cat Pipfile         
pipenv run $CMD
pipenv --venv       # path to the virutal env
pipenv check        # security vulnerabilities and PEP 508 req
```

### HTML
* DeveloperTools (CTRL+SHIFT+I)
    * elements, view source

### HTTP
* [Client-Server architecture](https://docs.google.com/presentation/d/1PUggE2mhGVsbtOd62m82mNX8pl0P5MsmSrFw5G4zBfw/edit#slide=id.p7)
* GET vs. POST
* flask: template_render vs redirect

### REST
* Insomnia
* DeveloperTools / copy as curl
  
### PyCharm
