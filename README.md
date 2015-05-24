# Dyszka.pl

Description goes here.

## Installation

### 1. Frontend
Go to `frontend` directory and type:

```sh
$ npm install -g
$ grunt
```
All librares should download automatically.

### 2. Backend
Go to `backend` directory and type:

```sh
$ virtualenv -p python2.7 venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```
All dependencies should be installed.

## Running

### Backend
```sh
$ cd backend/
$ source venv/bin/activate
$ python manage.py runserver
```

### Frontend
```sh
$ cd frontend/
$ grunt run_backend
```