
# TEST_NEWS

A simple python backend service "News blog with nested comments".

Tested on Ubuntu 20.04 and</br>
Python==3.8.10       </br>
Django==4.0.4        </br>
django_environ==0.8.1</br>
django_mptt==0.13.4  </br>
environ==1.0         </br>
requests==2.27.1     </br>
pip==22.0.4          </br>
# CONTENTS:
[Description](#description) </br>
[Deploy](#deploy)           </br>
[Test](#test)               </br>

## Description <a name="description"></a>
**The system have API methods that provide:**
- ✓ Adding an article.
- ✓ Adding a comment to an article.
- ✓ Adding a comment in response to another comment (any nesting is possible).
- × Retrieve all comments on an article up to 3 levels of nesting. <br>
  ✓ Retrieve all comments on an article up to 20 levels of nesting.

- ✓ Retrieve all nested comments for a level 3 comment.
- × A tree structure can be recreated from the comment API response.  
  ✓ A tree structure is recreated from the comment API response. Via html, css, js.

**Non-functional properties:**
- ✓ Using Django ORM.
- ✓ Following the principles of REST.
- ✓ The number of queries to the database doesn't directly depend on the number of comments, nesting level.
- ✓ Solution in the form of a repository on Github.
- ✓ README.md, which shows how to build and run the project. 
- ✓ Specify dependencies in requirements.txt.
- ✓ Using the latest versions of python and Django.

**Additionally:**
- × Using PostgreSQL.
- ✓ docker-compose to run api and database.
- × Swagger or other API documentation.



## Getting Started <a name="deploy"></a>
These instructions will get you a copy of the project up and running on your local machine. There are **two** ways to run a project.

1. run without Docker
2. run with Docker 

### Build Without Docker

#### Git

Clone the repository
```
git clone https:github.com/Alexander671/test_news
```

Navigate into the `test_news` directory
```
cd test_news/test_news
```

#### .env file

For correct work you need to create .env file in ~/PROJECT_DIR/test_news/test_news/.env
with the following content:

```
nano .env 
```

```
SECRET_KEY = <your_secret_key>
DEBUG = <True/False>
ALLOWED_HOSTS = <list_hosts>

```

#### Dependencies

Install, using `pip`:

```
pip install -r requirements.txt
```


#### Usage
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

### Build Using Docker

#### Git

Clone the repository
```
git clone https:github.com/Alexander671/test_news
```

Navigate into the `test_news` directory
```
cd test_news/test_news
```

#### .env file

For correct work you need to create .env file in ~/PROJECT_DIR/test_news/test_news/.env
with the following content:

```
nano .env 
```

```
SECRET_KEY = <your_secret_key>
DEBUG = <True/False>
ALLOWED_HOSTS = <list_hosts>

```

#### Usage

1. Build the image

`docker build .`

2. Сompiling the image with the team

`docker-compose build`

3. Run container:

`docker-compose up -d`

## Some examples and test <a name="test"></a>

Some edge-cases examples are available on the `examples` folder. 

## Authors

* **Alexander Matveev** - *Initial work* - [Alexander671](https://github.com/Alexander671)

