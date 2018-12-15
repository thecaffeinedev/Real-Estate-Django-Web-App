# Django 2.x Cheat Sheet

### Creating a virtual environment

We need to create a virtual env for our app to run in: [More Here](https://docs.python.org/3/library/venv.html)
Run this command in whatever folder you want to create your venv folder

```
python -m venv ./venv
```

### Activate the virtualenv

```
# Mac/Linux
source ./venv/bin/activate

# Windows
venv\Scripts\activate.bat - May need to add full path (c:\users\....venv\Scripts\activate.bat)
```

### Escape from venv

```
deactivate
```

### Check packages installed in that venv

```
pip freeze
```

### Install Django

```
pip install django
```

### Create your project

```
django-admin startproject PROJECTNAME
```

### Run Server (http://127.0.0.1:8000) CTRL+C to stop

```
python manage.py runserver
```

### Create an app
```
python manage.py start app APPNAME
```

### Create migrations
```
python manage.py makemigrations
```

### Run migration
```
python manage.py migrate
```

### Collect Static Files
```
python manage.py collectstatic
```
