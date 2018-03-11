# Which Sandwich

## Setting Up the Virtual Environment

1. Check that you have Python 3.x installed with `python --version`.
2. Create a virtual environment using `mkvirtualenv which_sandwich`.
3. Make sure that the virtual environment is activated (use `workon which_sandwich` if in doubt) and run `pip install -r requirements.txt`.

We're using Python 3.x and Django 2.0.2 for this project.

## Populating a Local Database File

The database file is not committed to GitHub.

1. Run `python manage.py migrate` to build the database schema from the models.
2. Create an admin profile with `python manage.py createsuperuser`.
3. Run the population script with `python populate_whichsandwich.py`.

To reset everything to a clean database just delete the db.sqlite3 file and perform the above steps again.

#### The Population Script
* Randomly generates sandwiches from given ingredients.
* Fake users are predefined but more can be added easily if you wish.
* Comments are also predefined but are randomly assigned to sandwiches and commenters.
* User favourites are randomly selected.
* Can be run multiple times to generate more sandwiches.

## Document Previews

#### Wireframes

* [Home](https://www.draw.io/#Uhttps%3A%2F%2Fraw.githubusercontent.com%2F2268563%2Fwhich-sandwich%2Fmaster%2Fspecification%2Fspecification%2Fwireframes%2Fhome.xml)

* [Make Sandwich](https://www.draw.io/#Uhttps%3A%2F%2Fraw.githubusercontent.com%2F2268563%2Fwhich-sandwich%2Fmaster%2Fspecification%2Fwireframes%2Fmake_sandwich.xml)

* [Sign In](https://www.draw.io/#Uhttps%3A%2F%2Fraw.githubusercontent.com%2F2268563%2Fwhich-sandwich%2Fmaster%2Fspecification%2Fwireframes%2Fsign_in.xml)

* [Sign Up](https://www.draw.io/#Uhttps%3A%2F%2Fraw.githubusercontent.com%2F2268563%2Fwhich-sandwich%2Fmaster%2Fspecification%2Fwireframes%2Fsign_up.xml)

* [My Account](https://www.draw.io/#Uhttps%3A%2F%2Fraw.githubusercontent.com%2F2268563%2Fwhich-sandwich%2Fmaster%2Fspecification%2Fwireframes%2Fmy_account.xml)

* [Template](https://www.draw.io/#Uhttps%3A%2F%2Fraw.githubusercontent.com%2F2268563%2Fwhich-sandwich%2Fmaster%2Fspecification%2Fwireframes%2Ftemplate.xml)

#### The Rest

* [ER Diagram](https://www.draw.io/#Uhttps%3A%2F%2Fraw.githubusercontent.com%2F2268563%2Fwhich-sandwich%2Fmaster%2Fspecification%2FER%2520Diagram.xml)

* [System Architecture Diagram](https://www.draw.io/#Uhttps%3A%2F%2Fraw.githubusercontent.com%2F2268563%2Fwhich-sandwich%2Fmaster%2Fspecification%2Fsystem_architecture_diagram.xml)

* [Site Map](https://www.draw.io/#Uhttps%3A%2F%2Fraw.githubusercontent.com%2F2268563%2Fwhich-sandwich%2Fmaster%2Fspecification%2Fsite_map.xml)

* [User Personas](https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fgithub.com%2F2268563%2Fwhich-sandwich%2Fblob%2Fmaster%2Fspecification%2Fuser%2520personas.docx%3Fraw%3Dtrue)
