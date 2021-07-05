# An entry-level flask template for designing web applications.
Hello my dear friends :)  <br><br>
A design pattern is a collection and organization of project files for the initial deployment of a [**Flask**](https://pypi.org/project/Flask/) application in a virtual developer environment.  <br><br>
At the design stage of the template, the top priority was to eliminate _circular imports_. To some extent, we managed to do this. In places of the program, where even cyclic dependencies appeared during import, they were bypassed in other ways, which will be described below.  <br><br>
The project has implemented two **blueprints** for a general example, as well as a starter example of **models** for adding _**migrations** to the database_. The **configuration** file is output as a separate file.  <br><br><br>
## Brief description of the project files:
<ul>
<li>main.py : -start file for launching Flask application</li>
<li>app.py : -application factory </li>
<li>config.default.py : -application configuration file (for correct application work, rename to config.py)</li>
<li>models.py : -database table model description file</li>
<li>admin : -application admin panel blueprint. connected but not ready yet (empty folder)</li>
<li>frontend : -blueprint frontend application</li>
<li>migrations : -migrations folder automatically generated during database migration. can be used or can be deleted after importing the project (with migration commands, you will have a personal migration folder automatically generated)</li>
<li>requirements.txt : -installed dependencies file in Python virtual environment</li>
</ul> 
<br> 

### Application launch instructions:
! When describing the application instructions, I assume that you have the [**Python**](https://www.python.org) programming language installed and you know how to work with a **virtual environment**.

1. Setting up a virtual environment, I used [virtualenv](https://pypi.org/project/virtualenv/). You can use any, it does not affect the project.
2. Create a folder for deploying the project and go to this folder.
3. We activate the virtual environment.
4. Updating pip: **python -m pip install --upgrade pip**
5.     Clone the repository: git clone https://github.com/haossten/Python-Flask-experiment.git
6. Install the dependencies from the requirements.txt file: **python -m pip install -r requirements.txt**
7.     Rename the config.default.py file to config.py and make settings for the SQLALCHEMY_DATABASE_URI field database username, database user password, host where the database is located and the name of the database. Drivers for MySQL and PostgreSQL databases were installed from the dependency file. By default, the PostgreSQL field is active. If you want to use MySQL then comment out the PostgreSQL field and uncomment the MySQL field in the config.py file. Also, don't forget to fill in the database field with your database access data.
8.     Run database migration to create tables in the database, which are described in the models.py file. Initializing migrations: flask db init. Generating migrations: flask db migrate. Apply migrations to write to the database: flask db upgrade. After these steps, tables should be created in your database, written in the models.py file.
9.     After all the steps you have passed, you can launch the application. Press run in your ide editor with active tab in the ide of main.py file.

        PS: Alternative ways to run main.py file:

        using powershell:
        $env:FLASK_APP = "main"
        $env:FLASK_ENV = "development"
        flask run

        usinf cmd:
        set FLASK_APP=main
        set FLASK_ENV=development
        flask run

        using bash:
        export FLASK_APP=main
        export FLASK_ENV=development
        flask run



### An example of writing to the database through the interface in the browser:

1. Enter the address http://127.0.0.1:5000 in the browser.
2. On the page, click on the Add a note link
3. Enter text in the Title and Body fields. After entering, press the Enter button. Now click on the Home page link to return to the previous page and you will see the output of the added record from the database.

### Note: The application may be improved and changed in the future. Watch for the release of the commits.

Thanks for attention!:)