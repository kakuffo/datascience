import requests

print('Beginning file download with requests')

url = 'https://www2.census.gov/census_2010/01-Redistricting_File--PL_94-171/Alaska/ak2010.pl.zip'
r = requests.get(url)

with open('/Users/kwameakuffo/Alaska.zip', 'wb') as f:
    f.write(r.content)


# Retrieve HTTP meta-data
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
