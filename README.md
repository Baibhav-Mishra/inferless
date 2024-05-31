# Simple Rest API

It is simple api to perform crud request

## Installation
### Pip Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.txt

```bash
pip install -r requirements.txt
```

### Docker
```bash
cd /MYSQL
docker build .
docker-compose up
```
### Make migrations
```bash
cd /mysite
python manage.py makemigrations
python manage.py migrate
```
## Run Service
```bash
python manage.py runserver
```
