# UNFINISHED PROJECT

Ongoing project developed to interact with [this habit tracker](https://docs.google.com/spreadsheets/d/1DajqsoW14-qOIwudflfm8z3iszPKc0n9gU3hxN1Ma6o/edit#gid=0) through CMD or IDE.

---

The features will be to:
- Add up to 6 habits to keep track of;
- Edit existing habits;
- Mark and unmark habits as done;
- Check the monthly repetitions of a habit.

More features might be added as progress is made.


The design of this habit tracker is heavily based on [Gracia Kleijnen](https://graciakleijnen.medium.com/) 's template.

## Usage

### Make a copy of the habit tracker
Open the habit tracker (you can do this by [clicking here](https://docs.google.com/spreadsheets/d/1DajqsoW14-qOIwudflfm8z3iszPKc0n9gU3hxN1Ma6o/edit#gid=0)) and select the option `Make a copy` on the `File` menu. 

### Create credentials in Google API Console

1. Log in on [Google Cloud API](https://console.cloud.google.com/home/);
2. Create a project. You can name it however you like and keep the `Location` as "no organization";
3. Search for Google Sheets API and enable it
4. Search for Google Drive API and enable it
5. Click on `create credentials` on the top right corner and choose the options:
    - `Which API are you using?` Google Drive API
    - `Where will you be calling the API from?` Web server (e. g. node js, Tomcat)
    - `What data will you be accessing?` Application data
    - `Are you planning to use this API with App Engine or Compute Engine?` No

    What Credentials do I need?
    - `Service account name:` Any name you want
    - `Role:` Project > Editor
    - `Key type:` JSON
6. Save the `.json` file in the python project folder;
7. On your IDE, open the `.json` file and copy the `"client_email"`;
8. Open the habit tracker and share it with the e-mail you just copied as `Editor`;


### Set up 

1. Open the Command Prompt and type `pip install gspread oauth2client` to install the needed modules.
2. Rename the `.json` file to `credentials.json`


-----

To be continued
