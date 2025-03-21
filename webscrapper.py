from bs4 import BeautifulSoup
import requests
import sys


def main():
    url = "https://pt.wikipedia.org/wiki/Lista_de_deputados_federais_do_Brasil_da_57.%C2%AA_legislatura"

    # get html content from url
    url_open =  page_content(url)

    # scrape the names
    congresspeople = scrape_congresspeople(url_open)
    
    # remove from the words that represents a profission (Col., Doutor(a), etc)
    congresspeople = clean_names(congresspeople)
    
    # create dictionary that counts first name most popular in congresspeople
    names_score = count_names(congresspeople)
    
    # display the socres by name to the user
    display_scores(names_score)


def page_content(url):
    '''Fetch content from a webpage'''
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        sys.exit("Failed to retrieve content form the url")


def scrape_congresspeople(url_open):
    '''
    Scrape names from the tables of Wikipedia page
    First, parse the HTML content
    Extract the names from tables with class "wikitable"
    From all tables, put names in a set
    Return set
    '''
    # parse HTML content
    soup = BeautifulSoup(url_open, 'html.parser')

    # find tables with the class wikitable
    tables = soup.find_all('table', {'class': 'wikitable'})

    # ignore the first 3 tables from wikipedia
    tables = tables[3:]

    # from all tables, extract names
    congress_names = set()
    for table in tables:
        names = parse_names_from_table(table)
        congress_names.update(names)

    return congress_names


def parse_names_from_table(table):
    '''
    Extract names from a table
    '''
    names = []
    rows  = table.find_all('tr')[1:]  # skip the header from the table
    for row in rows:
        # make a list with all td from row
        cells = row.find_all('td')
        # if number of tds > 1, than
        if len(cells) >= 2:
            # name of congresspeople is in the second <td>
            name_cell = cells[1]
            name = name_cell.text.strip()
            # ignore empty strings and dates
            if name and not any(char.isdigit() for char in name):
                names.append(name)
    return names


def clean_names(dirty_set):
    '''
    Remove from each name in set words that are related to
    profissions like Doutor(a), Col., Delegada(o), etc
    '''
    jobs = [
        "Col.", "Cap.", "Dr.", "Enfermeira", "Enfermeiro",
        "Delegado", "Delegada", "Coronel", "Professor", "Professora",
        "Prof.", "Doutor", "Doutora", "Del.", "Pastor", "Pastora", "General",
        "Tenente", "Sargento",  "Capitão", "Pr.", "Dra.", "Cab.",
        "Pastor Sargento", "Cabo"
    ]
    # create an ampty set, lopp trough each name in dirty_set
    clean_set = set()
    for name in dirty_set:
        # if first worn in name os a job, remove it
        parts = name.split()
        if parts[0] in jobs:
            clean_name = " ".join(parts[1:]).strip()
        else:
            clean_name = name.strip()
        clean_set.add(clean_name)
    
    return clean_set


def count_names(names_set):
    '''
    Count number of congresspeople with the same first name
    Return a dictionary with name as key and count as value
    '''
    names_count = {}
    for full_names in names_set:
        # betting that the first substring is the first name
        first_name = full_names.split()[0]
        # if first name is already a key, add one. If note, create the key
        if first_name in names_count:
            names_count[first_name] += 1
        else:
            names_count[first_name] = 1
    
    return names_count


def display_scores(names_score):
    '''
    Sort the dictionary in descending order,
    than print it
    '''
    # convert each key-value pair as tuple, than sort them
    sorted_names = sorted(
        names_score.items(), # convert the dict to list of tuples
        key=lambda item : item[1], # second element as parameter to sort
        reverse=True # sort by descending order
    )
    for name, count in sorted_names:
        print(f"{name}: {count}")



if __name__ == "__main__":
    main()