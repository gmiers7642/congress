from bs4 import BeautifulSoup
import requests

#html = file('/Users/glenn/Zipfian/project/congress/data/view-source_clerk.house.gov_evs_2016_roll520.xml', 'r')

def get_legislator_table(soup, o_file):
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

def pull_page(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")
    return soup

def file_output(data, filename):
    with open(filename, 'w') as f:
        #print data
        for d in data:
            f.write(d + "\n")

if __name__ == '__main__':
    soup = pull_page('http://clerk.house.gov/evs/2016/roll520.xml')
    get_legislator_table(soup, '../data/legislators_house_114th_2nd.txt')
