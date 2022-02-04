import requests
from bs4 import BeautifulSoup
import re


headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}

# url that will be gathered
url = 'https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/acoes-e-programas/covid-19/noticias-covid-19'


site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
last_page = \
    soup.find('a', {'href':'https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/acoes-e-programas/covid-19/noticias-covid-19?b_start:int=150'})\
        .get_text()


# last page of the pagination
num_last_page = int(last_page)

# results per page of pagination
number_per_page = 30

# loop to take each value from the given url
for i in range(1, num_last_page * number_per_page):

    # site url page with the navigation
    # this sites shows 30 results per page of navigation, so
    # I need to implemente the loop that take the last page of pagination
    # and multiply by the number of results per page
    url_page = f'https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/acoes-e-programas/covid-19/noticias-covid-19?b_start:int={i}'

    site = requests.get(url_page, headers=headers)

    # parsing the page content
    soup = BeautifulSoup(site.content, 'html.parser')
    # List of new that will be gathered
    actions = soup.find_all('div', {'class': 'tileContent'})

    with open('scrapper_covid_gov_BR.csv', 'a', newline='', encoding='UTF-8') as file:
        for article in actions:
            # take the title of the new
            title = article.find('a', {'title': 'collective.nitf.content'}).get_text().strip()
            # take the link of the new
            link = article.find('a', {'class': 'summary url'}, {'href': True})
            # make the link a list
            listed_link = list(str(link))
            # delete the text before the "http"
            del listed_link[:29]
            # transform back the modified list into string to use regex
            stred_link = ''.join(listed_link)
            # regex the string to exclude everything after the link itself
            final_link = stred_link[0:stred_link.index('"')]
            # gather date request
            date = soup.find('span', {'class': 'summary-view-icon'}).get_text()
            # print(date)

        # Prepare each line of the CSV file
        line = date + ';' + title + ';' + final_link + '\n'
        # print(line)
        file.write(line)
    # print(url_page)


