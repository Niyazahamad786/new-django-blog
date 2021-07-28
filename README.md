### Django Blog
A blog where user can create a post,delete,update etc ,which is visible to users in the blog.

Clone This Project (Make Sure You Have Git Installed)
```
https://github.com/Niyazahamad786/new-django-blog.git
```
Install Dependencies 

```
pip install -r requirements.txt
```

Set Database (Make Sure you are in directory same as manage.py)
```
python manage.py makemigrations
python manage.py migrate
```
Create SuperUser 
```
python manage.py createsuperuser
```

To run the project in local host
```
python manage.py runserver
Open a browser to http://127.0.0.1:8000/admin/ to open the admin site
Create a few test objects of each type.
Open tab to http://127.0.0.1:8000 to see the main site, with your new objects.
```
The application is deployed in Heroku
```
https://django-blog6.herokuapp.com
```
Clone the Docker image of the application
'''
docker pull niyazahamad195/django-blog
'''
#### That's it! Happy Coding!
