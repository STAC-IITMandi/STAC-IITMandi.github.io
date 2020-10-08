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
    ```
    To learn how to generate a secret key click [here](https://stackoverflow.com/a/16630719/12350727).
    Remember to restart your virtual environment if you get an error after doing this.

5.  Change directory to src using `cd src`.
6.  Check your changes before running `python manage.py check`.
7.  Run the server on your machine using `python manage.py runserver` and then open [localhost:8000](http://localhost:8000) in your browser.
8.  Switch to a new branch before making changes `git checkout -b NewBranchName`.
9.  Make the changes in the repo.
10. Stage the changes using `git add path/to/changed-files` ( avoid using `git add .` ).
11. Commit your changes using `git commit -m "Appropriate Commit Message"`.
12. Push your changes using `git push origin NewBranchName`.
13. Create a pull request.
14. Mention someone to review it.
15. Celebrate your contribution rocket :rocket:
