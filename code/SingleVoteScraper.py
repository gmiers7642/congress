from bs4 import BeautifulSoup

html = file('/Users/glenn/Zipfian/project/congress/data/view-source_clerk.house.gov_evs_2016_roll520.xml', 'r')
soup = BeautifulSoup(html, "lxml")

def get_legislator_table(o_file):
    legislator_attrs = ['name-id', 'party', 'role', 'sort-field', 'state', 'unaccented-name']
    data = scrape_attrs(soup, "legislator", legislator_attrs)
    file_output(data, o_file)

def scrape_attrs(soup, tag_name, attrs):
    output = []
    rv = soup.findAll(tag_name)

    for record in rv:
        l = ','.join([record[attr] for attr in attrs])
        output.append(l)
    return output

def file_output(data, filename):
    with open(filename, 'w') as f:
        #print data
        for d in data:
            f.write(d + "\n")

if __name__ == '__main__':
    get_legislator_table('../data/legislators_house_114th_2nd.txt')
