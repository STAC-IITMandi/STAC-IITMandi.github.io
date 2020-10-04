## How to Contribute
1. Fork this repository to your github account.
2. Clone the forked repository.
   `git clone https://github.com/<github-username>/STAC-IITMandi.github.io.git`
3. Database Setup
   1. You should have postgresql installed on your system. If not, run
    
        `sudo apt update`

        `sudo apt install postgresql postgresql-contrib`
    2. Create a local postgres database. Keep the credentials handy, you'll need them to link the database to django.
    **Steps to create a postgresql db on your system**
       1. `sudo su - postgres`
       2. `psql`
       3. CREATE DATABASE <db-name>;
       4. CREATE USER <db-username> WITH PASSWORD <db-password>;
       5. ALTER ROLE <DB-USERNAME> SET client_encoding TO 'utf-8';
       6. GRANT ALL PRIVILEGES ON DATABASE <db-name> TO <db-username>;
4. You can have the project running in a virtual environment or otherwise. Virtual environment is a preffered option.

   **Steps to set up a virtual environment for this project**
   1. `python3 -m venv myenv`
   2. Activate the virtual environment
      `source myvenv/bin/activate`
   3. Install required modules
      `pip install -r requirements.txt`
5. Open web_main/settings.py and fill in your postgres credentials
   
       DATABASES = {
         'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': <database-name>,
            'USER': <db-username>,
            'PASSWORD': <db-password>,
            'HOST': 'localhost',
            'PORT': '',
         }
       }

6. Change directory to web_main
   `cd web_main`
7. `python manage.py runserver`

   The application will be running at localhost:8000
8. Make the changes in the repo.
9.  Stage the changes.
    git add path/to/changed-files
10. Commit your changes.
    git commit -m "Appropriate Commit Message"
11. Push your Changes
    git push origin NewBranchName
12. Create a Pull request
13. Mention someone to review it.
14. Celebrate your Contribution rocket