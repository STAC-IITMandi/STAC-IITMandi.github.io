Steps:-
1. Before running server, you need to go migrate the models. 
For that run , `python manage.py  makemigrations`
2. Then, make migrations `python manage.py migrate`
3. Now models are created now you can runserver, `python manage.py runserver`
4. To goto admin page, just enter `/admin` in the localhost.
5. Then login as a superuser and now can add/edit/delete the details in the models.
6. All users created in the models are stored in a file `db.sqlite3` present in the root of the app.
So you need to store the db database as it is ignored in `.gitignore`.

Note: If while logging to admin you need to create a superuser. 
To create superuser, `python manage.py createsuperuser`. In the end while hosting , superuser can be created for later use.
