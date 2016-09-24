from bs4 import BeautifulSoup
import requests
import os

html = file('/Users/glenn/Zipfian/project/congress/data/view-source_clerk.house.gov_evs_2016_roll520.xml', 'r')

def scrape_tag_text(soup, tag):
    output = []
    for node in soup.findAll(tag):
        output.append(node.find(text=True) )
    return output

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

def create_vote_file(ip_file, op_file):
    # Create a new text file for vote outputs
    # first, check the file to make sure that doesn't exist yet
    if os.path.isfile(op_file): # fixNote - Add proper path check
        print "File already exists, please choose another."
        return None
    # Split the ip_file on commas, and retireve the first column
    legislator_ids = []
    with open(ip_file, 'r') as i_file:
        for line in i_file:
            legislator_ids.append(line.split(',')[0])
    header = 'issue\t' + "\t".join(legislator_ids)
    with open(op_file, 'w') as o_file:
        o_file.write(header)

def get_single_vote(soup):
    return ','.join(scrape_tag_text(soup, 'vote') )

if __name__ == '__main__':
    soup = pull_page('http://clerk.house.gov/evs/2016/roll520.xml')
    #get_legislator_table(soup, '../data/legislators_house_114th_2nd.txt')
    #ip_file = '/Users/glenn/Zipfian/project/congress/data/legislators_house_114th_2nd.txt'
    #op_file = '/Users/glenn/Zipfian/project/congress/data/votes_house_114th_2nd.txt'
    #create_vote_file(ip_file, op_file)
    print get_single_vote(soup)
