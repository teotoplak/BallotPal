import requests
from bs4 import BeautifulSoup


def crawl_url(url):
    # send a GET request to the website and store the response in a variable
    response = requests.get(url)

    # create a BeautifulSoup object to parse the HTML content of the website
    soup = BeautifulSoup(response.content, 'html.parser')

    # find all paragraphs on the page
    paragraphs = soup.find_all('p')
    # find all lists on the page
    lists = soup.find_all('ul')
    # find all tables on the page
    tables = soup.find_all('table')
    ordered_lists = soup.find_all('ol')

    text_chunks = []

    for p in paragraphs:
        text_chunks.append(p.get_text())
        print(p.get_text() + "\n")

    # loop through the lists and print the list items
    for ul in lists:
        for li in ul.find_all('li'):
            text_chunks.append(li.get_text())
            print(li.get_text() + "\n")

    # loop through the lists and print the list items
    for ol in ordered_lists:
        for li in ol.find_all('li'):
            text_chunks.append(li.get_text())
            print(li.get_text() + "\n")

    # loop through the tables and print the table cells
    for table in tables:
        for row in table.find_all('tr'):
            for cell in row.find_all('td'):
                text_chunks.append(cell.get_text())
                print(cell.get_text() + "\n")

    return text_chunks


if __name__ == '__main__':
    for chunk in crawl_url('https://tarkvalija.eu/erakondade-sotsiaalpoliitika-lubadused-mis-miks-ja-kuidas//'):
        print(f"{chunk}\n")
