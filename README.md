# Honours

## Built By [Dennis](https://github.com/oodennis20/)

## Description
This is a web application that allows different developers to post their projects and peers can review the same by grading the projects in terms of userbility, design and content.


## User Stories
These are the behaviours/features that the application implements for use by a user.

Users would like to:
* View all projects submitted by any user.
* Click on links to visit a live site.
* Search for users.
* Must be signed up to vote
* See averages for the three grading criterias
* Grade Projects.


## Admin Abilities
These are the behaviours/features that the application implements for use by the admin.

Admin should:
* Sign in to the application
* Add, Edit and Delete projects
* Delete projects
* Manage the application.


## [Specifications](Specs.md)

## SetUp / Installation Requirements
### Prerequisites
* python3.6
* pip
* virtualenv
* Requirements.txt

### Cloning
* In your terminal:

        $ git clone https://github.com/oodennis20/Honours
        $ cd Awards

## Running the Application
* Creating the virtual environment

        $ python3.6 -m venv --without-pip virtual
        $ source virtual/bin/activate
        $ curl https://bootstrap.pypa.io/get-pip.py | python

* Installing Django and other Modules

        $ see Requirements.txt

* To run the application, in your terminal:

        $ python3.6 manage.py runserver

## Testing the Application
* To run the tests for the class files:

        $ python3.6 manage.py test projects

## Technologies Used
* Python3.6
* Django  framework and postgresql database

## [License](License.txt)


