## How to Contribute  

1. Fork this repository to your github account.  

2. Clone the forked repository.  
   `git clone https://github.com/<github-username>/STAC-IITMandi.github.io.git`  

3. Database Setup  
   1. You should have postgresql installed on your system. If not, run    
    
      **On Linux** -    
        `sudo apt update`  

        `sudo apt install postgresql postgresql-contrib`  

      **On Windows** -     
         Install -     
            1. PostgreSQL - `https://www.postgresql.org/download/windows/`   
                        **( Note :- Remeber Password entered here.)**  
            2. pgAdmin - `https://www.pgadmin.org/download/pgadmin-4-windows/`   
                            
   2. Create a local postgres database. Keep the credentials handy, you'll need them to link the database to django.  
    **Steps to create a postgresql db on your system**  
      **On linux** -  
       1. `sudo su - postgres`  
       2. `psql`  
       3. CREATE DATABASE <db-name>;  
       4. CREATE USER <db-username> WITH PASSWORD <db-password>;  
       5. ALTER ROLE <DB-USERNAME> SET client_encoding TO 'utf-8';  
       6. GRANT ALL PRIVILEGES ON DATABASE <db-name> TO <db-username>;    


      **On windows**:-  
      
        1. Open pgAdmin , by default the user is `postgres`.     
        2. Type your Server Password. (Asked during installation.)    
        3. To create, head on to the Databases Right click and create. By Default owner set to `postgres`. Click 'Save'.  
        4. Database created.  

4. You can have the project running in a virtual environment or otherwise. Virtual environment is a preffered option.  

   **Steps to set up a virtual environment for this project**    
   1. `python3 -m venv venv`  
   2. **On Linux** - Activate the virtual environment  
         `source venv/bin/activate`  

      **On Windows** - Activate the virtual environment  
         `venv\Scripts\activate`  
         
   3. Install required modules  
      `pip install -r requirements.txt`  

5.  Store your secrets by adding them at the end of `venv/bin/activate`. They will be set whenever you run the virtual environment.

        ```bash
        export SECRET_KEY=''
        export DB_NAME=''
        export DB_USER=''
        export DB_PASS=''
        ```
    -----------------------------OR------------------------------------------    
     `(Note:- Below method is preferrable if you are on windows,   but works well for both linux/Windows.)  `
    we can use a external file to store all the senstive data ( like `SECRET_KEY`, DB_PASS, DB_USER).   

    Handling and Accessing sensitive data,   
      To access sensitve data from  a different file: -  

        1. `pip install python-decouple` ( Already added in requirements.txt)   
        2. create `.env` file. (in the root folder where manage.py is present)   
        3. Enter the following in .env file ( fill your sensitive data without string quotes.),  
            SECRET_KEY = 'secretkey'  
            DEBUG = True  
            DB_NAME = 'db-name'  
            DB_USERNAME = 'db-username'  
            DB_PASSWORD = 'password'  
            DB_HOST = 'localhost'  

        4. Now open `settings.py` and import   
                `from decouple import config`   ( By Default, already present.)   

        5. Type, `SECRET_KEY = config("SECRET_KEY")`  
            and `DEBUG = config('DEBUG')`      ( By Default, already present.)  

        6. In DATABASES, Replace this  or just Comment out those already present in `settings.py` file.  

            DATABASES = {   
                'default': {  
                    'ENGINE': 'django.db.backends.postgresql_psycopg2',  
                    'NAME': config('DB_NAME'),  
                    'USER': config('DB_USERNAME'),  
                    'PASSWORD': config('DB_PASSWORD'),  
                    'HOST': config('DB_HOST'),  
                    'PORT': '',  
                }  
            }  

        7. Since, .env file conatins all of sensitive data. Before uploading, add `.env` file to gitignore to prevent sensitve data uploading on
        github.  
            To add, just open `.gitignore`, add `.env`. Save file.   ( By Default, already present.)  


6.  Change directory to src  
    
    `cd src`

7.  First check for errors 
    
    `python manage.py check`    

    Run the server on your machine.   
    
    `python manage.py runserver`   
    
    The application will be running at `localhost:8000`.  

8.  Make the changes in the repo.

9.  Stage the changes.
    
    `git add path/to/changed-files`

10. Commit your changes.
    
    `git commit -m "Appropriate Commit Message"`

11. Push your Changes
    
    `git push origin NewBranchName`

12. Create a Pull request

13. Mention someone to review it.

14. Celebrate your Contribution rocket :rocket: <!-- flag{thankyou!} -->
