<h1> Web 3 Project </h1>

Done by:
    - Maruf Abdirimov
    - Miguel Boekhold
    
    
<h2> Description of the project:</h2>

...

<h2> Installation of the project</h2>

<h3> Clonning the project</h3>

You need git for that, so make sure to install it if you did not.

You can install it following instructions on official git <a href="https://git-scm.com/downloads">page</a>

Command:
    git clone https://git.fhict.nl/I378188/web3.git

<h3>For Windows OS : </h3>

Installing python:

    1. Follow instructions on page this <a href="https://realpython.com/installing-python/">page</a>

    2. Important! Make sure python is added to path variable.

Installing pip:

    1. pip should be going with python package, if its version is 2.7.* or 3.6.*. You can check if you have pip by writting

    2. In case it is not you can find installation instruction on this <a href="https://pip.pypa.io/en/stable/installing/">page</a>

Installing package via pip:

    1. Open console(Press "Windows+R", write cmd and press "Enter"  || Press "Windows", write cmd and choose cmd in search results).

    2. Go to cloned directory(.../directory_to_which_you_cloned/web3/)

    3. Write that command:
        pip install -r package.txt

<h2> Description of <i> web3_project </i> folder: </h2>

<h3>For MAC/Linux OS : </h3>

Installing python:

    1. Follow instructions on page this <a href="https://realpython.com/installing-python/">page</a>

    2. Important! Make sure python is added to path variable. Also, python needs to be version 3.6.* or higher.

Installing pip:
    1. pip should be going with python package, if its version is 2.7.* or 3.6.*. You can check if you have pip by writting

    2. In case it is not you can find installation instruction on this <a href="https://pip.pypa.io/en/stable/installing/">page</a>

Installing package via pip:

    1. Open console

    2. Go to cloned directory(.../directory_to_which_you_cloned/web3/)
    
    3. Write that command:
        pip install -r package.txt
        
<h2> Description of <i> web3_project </i> folder: </h2>


<h2> <b>manage.py</b>:</h2>
A command-line utility that lets us interact with Django project in various ways. You can read all the details about manage.py in django-admin and manage.py.

<h2> Folder <b>web3_project</b></h2> is a container for the project. Contains:

<h3>-<b>directory</b></h3>
<p> This is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. mysite.urls).</p>
<h3>-<b>__init__.py</b>:</h3>
An empty file that tells Python that this directory should be considered a Python package. If you’re a Python beginner, read more about packages in the official Python docs.
<h3>-<b>settings.py</b>:</h3>
Settings/configuration for this Django project. Django settings will tell you all about how settings work.
<h3>-<b>urls.py</b>:</h3>
The URL declarations for this Django project; a “table of contents” of the Django-powered site. You can read more about URLs in URL dispatcher.
<h3>-<b>wsgi.py</b>:</h3>
An entry-point for WSGI-compatible web servers to serve the project.
<h2> To run the site </h2>

<p> To run the site, you need to start up the server. File <b>manage.py</b> already has a command that can allow you to do it</p>
First open cmd (analog on other OS) in the folder <b>web3_project</b> and write this code: 

<i>python manage.py runserver</i> 

Prerequisite is to have python installed globally
<p>Site can be found on this url: </p>
http://127.0.0.1:8000/ 

<h2>In case port or/and IP are already taken/cannot be used</h2>
<p>Use this command "<i>python manage.py runserver ip:port</i>" but in place of ip and port use those that you need.</p>
In case you need to change only port "<i>python manage.py runserver port</i>" ip part can be skipped 