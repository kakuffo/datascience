# Dataset Extraction Techniques

The first step in the ETL process is to extract data from their sources using effective means to automate the process as best as possible.  What follows are exploration of techniques that will aid extracting data from their sources using Python, and the many modules available.

* urllib.request
* urllib2
* requests
* wget


## urllib

urllib.request is a Python module for fetching URLs (Uniform Resource Locators). It offers a very simple interface, in the form of the urlopen function.

`````python
import urllib.request
print('Census 2010 Redistricting Data Files')
url = 'https://www2.census.gov/census_2010/01-Redistricting_File--PL_94-171/Alaska/ak2010.pl.zip'
urllib.request.urlretrieve(url, '/Users/data/downloads/Alaska.zip')
`````



## urllib2

````
import urllib2

filedata = urllib2.urlopen('https://www2.census.gov/census_2010/01-Redistricting_File--PL_94-171/Alaska/ak2010.pl.zip')
datatowrite = filedata.read()
with open('/Users/data/downloads/Alaska.zip', 'wb') as f:
f.write(datatowrite)

    ````

## requests

## wget
