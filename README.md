# Real Estate Django Web App


## Django 2.x Cheat Sheet

### Creating a virtual environment

We need to create a virtual env for our app to run in: [More Here](https://docs.python.org/3/library/venv.html)
Run this command in whatever folder you want to create your venv folder

```
python -m venv ./venv
```
### Activate the virtualenv

```
# Linux
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

### Create your project

## Web App Features
FRONTEND PAGES

    • Home
    • About
    • Listings
    • Single Listing
    • Search
    • Register
    • Login
    • Dashboard (Inquiries)
    
DESIGN SPECIFICATION

    • Use Any Logo (Frontend and admin)
    • Branding colors – blue(#10284e) green(#30caa0)
    • Mobile Friendly
    • Social media icons & contact info
    • Doesn’t have to be too fancy but must be clean
 
FUNCTIONALITY SPECS

    • Manage listings, realtors, contact inquiries and website users via admin
    • Role based users (staff and non-staff)
    • Display listings in app with pagination
    • Ability to set listings to unpublished
    • Search listings by keyword, city, state, bedrooms and price (Homepage & search page)
    • List realtors on about page with “seller of the month” (Control via admin)
    • Listing page should have fields listed below
    • Listing page should have 5 images with lightbox
    • Lightbox should scroll through images
    • Listing page should have a form to submit inquiry for that property listing
    • Form info should go to database and notify realtor(s) with an email
    • Frontend register/login to track inquiries
    • Both unregistered and registered users can submit form. If registered, can only submit one per listing
    
LISTING PAGE FIELDS

    • Title
    • Address, city, state, zip
    • Price
    • Bedrooms
    • Bathrooms
    • Square Feet
    • Lot Size
    • Garage
    • Listing Date
    • Realtor – Name & Image
    • Main image and 5 other images

  
