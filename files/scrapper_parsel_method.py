from parsel import Selector
import requests

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}

# url that will be gathered
url = 'https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/acoes-e-programas/covid-19/noticias-covid-19'

html_content = requests.get(url, headers=headers).text
print(html_content)
