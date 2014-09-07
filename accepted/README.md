Google Summer of Code data browser
==================================

This is an application that parses the CSV and HTML files containing data about
Google Summer of Code projects.

Running
=======

To get data for years 2009-2014, visit the following URLs:

https://www.google-melange.com/gsoc/projects/list/google/gsoc2009
https://www.google-melange.com/gsoc/projects/list/google/gsoc2010
https://www.google-melange.com/gsoc/projects/list/google/gsoc2011
https://www.google-melange.com/gsoc/projects/list/google/gsoc2012
https://www.google-melange.com/gsoc/projects/list/google/gsoc2013
https://www.google-melange.com/gsoc/projects/list/google/gsoc2014

For each URL, scroll down the list until all the entries are downloaded. Then,
scroll up and click the "CSV Export" button. Save the resulting data in a file
named YEAR.csv, like 2009.csv, 2010.csv and so on.

To get 2005-2008 data, run the following commands:

wget "https://developers.google.com/open-source/soc/2005/" -O 2005.html
wget "https://developers.google.com/open-source/soc/2006/" -O 2006.html
wget "https://developers.google.com/open-source/soc/2007/" -O 2007.html
wget "https://developers.google.com/open-source/soc/2008/" -O 2008.html

Now, run "./manage.py syncdb --noinput" to create the SQLite database schema
and the following, to create admin:admin Django user:

echo "from django.contrib.auth.models import User;
User.objects.create_superuser('admin',
                              'admin@example.com',
                              'admin')" | ./manage.py shell

Once it's done, import the data using "./parse.py" command. To run the server,
call "./manage.py runserver".
