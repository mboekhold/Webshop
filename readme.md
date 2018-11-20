<h1> Web 3 Project </h1>

Done by:
    - Maruf Abdirimov
    - Miguel Boekhold
    
    
<h2> Description of the project:</h2>

...

<h2> Description of <i> web3_project </i> folder: </h2>


<h2> <b>manage.py</b>:</h2>
A command-line utility that lets us interact with Django project in various ways. You can read all the details about manage.py in django-admin and manage.py.

<h2> Folder <b>web3_project</b></h2> is a container for the project. Contains:

<h3>-<b>mysite/directory</b></h3>
<p> This is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. mysite.urls).</p>
<h3>-<b>mysite/__init__.py</b>:</h3>
An empty file that tells Python that this directory should be considered a Python package. If you’re a Python beginner, read more about packages in the official Python docs.
<h3>-<b>mysite/settings.py</b>:</h3>
Settings/configuration for this Django project. Django settings will tell you all about how settings work.
<h3>-<b>mysite/urls.py</b>:</h3>
The URL declarations for this Django project; a “table of contents” of your Django-powered site. You can read more about URLs in URL dispatcher.
<h3>-<b>mysite/wsgi.py</b>:</h3>
An entry-point for WSGI-compatible web servers to serve your project. See How to deploy with WSGI for more details.

<h2> To run the site </h2>

<p> To run the site, you need to start up the server. File <b>manage.py</b> already has a command that can allow you to do it</p>
<p> First open cmd (analog on other OS) in the folder <b>web3_project</b> and write this code: "<i>python manage.py runserver</i>" without quotes . Prerequisite is to have python installed globally</p>
<p>Site can be found on this url: </p>
http://127.0.0.1:8000/ 

<h2>In case port or/and IP are already taken/cannot be used</h2>
<p>Use this command "<i>python manage.py runserver ip:port</i>" but in place of ip and port use those that you need.</p>
In case you need to change only port "<i>python manage.py runserver port</i>" ip part can be skipped 