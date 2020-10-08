## How to Contribute

1.  Fork this repository to your github account.
2.  Clone the forked repository using `git clone https://github.com/<github-username>/STAC-IITMandi.github.io.git`

3.  You can have the project running in a virtual environment or otherwise. Virtual environment is a preferred option.

    **Steps to set up a virtual environment for this project**

    1. Create a virtual environment using `python3 -m venv venv`
    2. Activate virtual environment -

        **On Linux** `source venv/bin/activate`

        **On Windows** `venv\Scripts\activate`

    3. Install required modules using `pip3 install -r requirements.txt`.

4.  Store your secrets by adding them at the end of `venv/bin/activate`. They will be set whenever you run the virtual environment.

    ```bash
    export SECRET_KEY=''
    export DB_NAME=''
    ```
    To learn how to generate a secret key click [here](https://stackoverflow.com/questions/41298963/is-there-a-function-for-generating-settings-secret-key-in-django).

5.  Change directory to src using `cd src`.
6.  Run the server on your machine using `python manage.py runserver` and then open [localhost:8000](http://localhost:8000) in your browser.
7.  Switch to a new branch before making changes `git checkout -b NewBranchName`.
8.  Make the changes in the repo.
9.  Stage the changes using `git add path/to/changed-files` ( avoid using `git add .` ).
10. Commit your changes using `git commit -m "Appropriate Commit Message"`.
11. Push your changes using `git push origin NewBranchName`.
12. Create a pull request.
13. Mention someone to review it.
14. Celebrate your contribution rocket :rocket:
