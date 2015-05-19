Google Summer of Code data browser
==================================

This is an application that parses the CSV and HTML files containing data about
Google Summer of Code projects.

Running
=======

To get data for years 2009-2014, visit the following URLs:

1. https://www.google-melange.com/gsoc/projects/list/google/gsoc2009
2. https://www.google-melange.com/gsoc/projects/list/google/gsoc2010
3. https://www.google-melange.com/gsoc/projects/list/google/gsoc2011
4. https://www.google-melange.com/gsoc/projects/list/google/gsoc2012
5. https://www.google-melange.com/gsoc/projects/list/google/gsoc2013
6. https://www.google-melange.com/gsoc/projects/list/google/gsoc2014

For each URL, scroll down the list until all the entries are downloaded. Then,
scroll up and click the "CSV Export" button. Save the resulting data in a file
named YEAR.csv, like 2009.csv, 2010.csv and so on.

To get 2005-2008 data, run the following commands:

```
wget "https://developers.google.com/open-source/soc/2005/" -O 2005.html
wget "https://developers.google.com/open-source/soc/2006/" -O 2006.html
wget "https://developers.google.com/open-source/soc/2007/" -O 2007.html
wget "https://developers.google.com/open-source/soc/2008/" -O 2008.html
```

Now, run "./manage.py syncdb --noinput" to create the SQLite database schema
and "./parse.py" to load all the data. To run the server, call:

```
./manage.py runserver
```
