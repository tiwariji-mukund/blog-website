#i-Blogger

BlogApp Demo
Development 👨‍💻

Note : Make sure you have Python version 3.8+
Environment Setup 🚀

$ git clone https://github.com/tiwariji-mukund/blog-website.git

$ cd django_blog_project/

If virtualenv is not installed (What is virtualenv?):

$ pip install virtualenv

Create a virtual environment

$ virtualenv virt

Activate the environment everytime you open the project

$ source virt/Scripts/activate

Install requirements 🛠

$ pip install -r requirements.txt

Run migrations for Database

$ python manage.py makemigrations

$ python manage.py migrate

Create superuser for Admin Login 🔐

$ python manage.py createsuperuser

Enter your desired username, email and password. Make sure you remember them as you'll need them in future.

eg.

Username: admin

Email: admin@admin.com

Password: HighlyConfidentialPassword

All Set! 🤩

Now you can run the server to see your application up & running 🚀

$ python manage.py runserver

To exit the environment ❎

$ deactivate

Every time you want to open the application in browser, make sure you run:

$ source virt/Scripts/activate

$ python manage.py runserver
