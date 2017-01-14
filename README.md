
     ,-----.,--.                  ,--. ,---.   ,--.,------.  ,------.
    '  .--./|  | ,---. ,--.,--. ,-|  || o   \  |  ||  .-.  \ |  .---'
    |  |    |  || .-. ||  ||  |' .-. |`..'  |  |  ||  |  \  :|  `--, 
    '  '--'\|  |' '-' ''  ''  '\ `-' | .'  /   |  ||  '--'  /|  `---.
     `-----'`--' `---'  `----'  `---'  `--'    `--'`-------' `------'
    ----------------------------------------------------------------- 

________________________________________________________________________________________________________________________________________

## You can also file course from github repository: https://github.com/limpst/case_study. 

## You need to execute bash command 'mysql-ctl cli' before 'Run Project' to start mysql. 

## Please uncomment below at '/case-study/crud/urls.py'  to see deal CRUD UI, and commend all the others in section '##cashflow CRUD'. 
    url(r'^$', views.deal_list, name='deal_list'),
    url(r'^new$', views.deal_create, name='deal_new'),
    url(r'^edit/(?P<pk>\d+)$', views.deal_update, name='deal_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.deal_delete, name='deal_delete'),

________________________________________________________________________________________________________________________________________

Welcome to your Django project on Cloud9 IDE!

Your Django project is already fully setup. Just click the "Run" button to start
the application. On first run you will be asked to create an admin user. You can
access your application from 'https://case-study-limpst.c9users.io/' and the admin page from 
'https://case-study-limpst.c9users.io/admin'.

## Starting from the Terminal

In case you want to run your Django application from the terminal just run:

1) Run syncdb command to sync models to database and create Django's default superuser and auth system

    $ python manage.py migrate

2) Run Django

    $ python manage.py runserver $IP:$PORT
    
## Configuration

You can configure your Python version and `PYTHONPATH` used in
Cloud9 > Preferences > Project Settings > Language Support.

## Support & Documentation

Django docs can be found at https://www.djangoproject.com/

You may also want to follow the Django tutorial to create your first application:
https://docs.djangoproject.com/en/1.9/intro/tutorial01/

Visit http://docs.c9.io for support, or to learn more about using Cloud9 IDE.
To watch some training videos, visit http://www.youtube.com/user/c9ide
