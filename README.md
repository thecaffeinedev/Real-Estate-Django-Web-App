# Real Estate Django Web App

If you are new to Django, checkout the [Django 2.x Cheat Sheet](https://github.com/TheCaffeineDev/Real-Estate-Django-Web-App/blob/master/django_cheat_sheet.md)

If you want to deploy this Web App In Ubuntu 18.04 Server, Please Follow this [Guide](https://github.com/TheCaffeineDev/Real-Estate-Django-Web-App/blob/master/Django_Deployment_to_Ubuntu_18.04.md) 

## How to run this project (Ubuntu 18.04)

1. **Clone the project**

```sh
git clone https://github.com/TheCaffeineDev/Real-Estate-Django-Web-App.git
```

2.  **Make sure you are in *Real-Estate-Django-Web-App* folder**

   1. Install all dependencies

      ```sh
      pip install -r requirements.txt
      ```

3. **Install PostgreSQL in your Ubuntu 18.04**

   1. Enable PostgreSQL Apt Repository

      ```sh
      sudo apt-get install wget ca-certificates
      
      wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
      
      # Now add the repository to your system.
      
      sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
      ```

   2. Install PostgreSQL on Ubuntu

      ```sh
      sudo apt-get update
      sudo apt-get install postgresql postgresql-contrib
      ```

   3. Connect to PostgreSQL

      ```sh
      sudo su - postgres
      psql
      ```

      Now you are logged in to PostgreSQL database server. To check login info use following command from the database command prompt.

      ```sh
      postgres-# \conninfo
      ```

   4. Create a database

      ```sh
      CREATE DATABASE real_estate;
      ```

   5. Create user 

      ```sh
      CREATE USER pks WITH PASSWORD 'abc123!';
      ```
   
4. **Run Migrations**

```sh
python manage.py makemigrations
python manage.py migrate
```

5. **Run Server**

```sh
python manage.py runserver 
```

And you are good to go. 

## Web App Features
**FRONTEND PAGES**

- [x] 
   Home

- [x]  About
- [x]  Listings
- [x]  Single Listing
- [x]  Search
- [x]  Register
- [x]  Login
- [x]  Dashboard (Inquiries)

**DESIGN SPECIFICATION**

- [x]  Use Any Logo (Frontend and admin)

- [x]  Branding colors – blue(#10284e) green(#30caa0)
- [x]  Mobile Friendly
- [x]  Social media icons & contact info
- [x]  Doesn’t have to be too fancy but must be clean

**FUNCTIONALITY SPECS**

- [x]  Manage listings, realtors, contact inquiries and website users via admin

- [x]  Role based users (staff and non-staff)
- [x]  Display listings in app with pagination
- [x]  Ability to set listings to unpublished
- [x]  Search listings by keyword, city, state, bedrooms and price (Homepage & search page)
- [x]  List realtors on about page with “seller of the month” (Control via admin)
- [x]  Listing page should have fields listed below
- [x]  Listing page should have 5 images with lightbox
- [x]  Lightbox should scroll through images
- [x]  Listing page should have a form to submit inquiry for that property listing
- [x]  Form info should go to database and notify realtor(s) with an email
- [x]  Frontend register/login to track inquiries
- [x]  Both unregistered and registered users can submit form. If registered, can only submit one per listing

**LISTING PAGE FIELDS**

- [x] Title
- [x]  Address, city, state, zip
- [x]  Price
- [x]  Bedrooms
- [x]  Bathrooms
- [x]  Square Feet
- [x]  Lot Size
- [x]  Garage
- [x]  Listing Date
- [x]  Realtor – Name & Image
- [x] Main image and 5 other images

**Backend**
For Database I have used Postgres Database Name: real_estate

Note: Please change those gmail credentials from real_estate folder you will get settings.py inside that file you will see username and password mentioned as place your Username and Password. Also do that same thing from Contacts folder views.py you will see YourEmail mentioned on line number 33.

### Screenshots

- **HOME**

![Home](https://github.com/TheCaffeineDev/Real-Estate-Django-Web-App/blob/master/screenshots/s1.JPG)

- **Listings** 


![Listings](https://github.com/TheCaffeineDev/Real-Estate-Django-Web-App/blob/master/screenshots/s3list.JPG)

- **Registration** 

![Registration](https://github.com/TheCaffeineDev/Real-Estate-Django-Web-App/blob/master/screenshots/s4reg.JPG)

- **Admin Panel - 1**

![Admin](https://github.com/TheCaffeineDev/Real-Estate-Django-Web-App/blob/master/screenshots/s5adm.JPG)

- **Admin Panel - 2**

![Admin](https://github.com/TheCaffeineDev/Real-Estate-Django-Web-App/blob/master/screenshots/s6r.JPG)

- **About**

![About ](https://github.com/TheCaffeineDev/Real-Estate-Django-Web-App/blob/master/screenshots/s2about.JPG)



If you face any problems, please let me know !
