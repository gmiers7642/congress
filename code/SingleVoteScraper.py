from bs4 import BeautifulSoup

html = file('/Users/glenn/Zipfian/project/congress/data/view-source_clerk.house.gov_evs_2016_roll520.xml', 'r')
soup = BeautifulSoup(html, "lxml")
rv = soup.findAll("legislator")

attrs = ['name-id', 'party', 'role', 'sort-field', 'state', 'unaccented-name']
output = []

for record in rv:
    l = []
    for attr in attrs:
        l.append(record[attr])
    output.append(l)

print output
