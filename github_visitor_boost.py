from bs4 import BeautifulSoup
import requests
import pandas as pd
from selenium import webdriver

url = 'https://www.airbnb.com/s/Paris--France/homes?refinement_paths%5B%5D=%2Fhomes&checkin=2023-05-10&checkout=2023-05-13&source=structured_search_input_header&search_type=autocomplete_click'
driver_path = 'path/to/chromedriver'

driver = webdriver.Chrome(executable_path=driver_path)
driver.get(url)


html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# Trouver tous les éléments HTML contenant les annonces de logements
listings = soup.find_all('div', class_='_8ssblpx')

# Pour chaque annonce, extraire les informations souhaitées
for listing in listings:
    # Extraire le nom et le lien du logement
    name = listing.find('div', class_='_bzh5lkq').text.strip()
    link = listing.find('a', class_='_mm360j')['href']
    # Extraire le prix et la devise
    price_info = listing.find('div', class_='_1fwiw8gv').text.strip()
    price = int(price_info.split()[0].replace(',', ''))
    currency = price_info.split()[1]
    # Extraire le nombre de chambres et de lits
    bedrooms = listing.find('div', class_='_kqh46o').text.strip().split(' · ')[0]
    beds = listing.find('div', class_='_kqh46o').text.strip().split(' · ')[-1]
    # Extraire le nombre de commentaires et la note de l'hô

print(listings)
# Créer un dictionnaire pour stocker les informations extraites
data = {
    'name': name,
    'link': link,
    'price': price,
    'currency': currency,
    'bedrooms': bedrooms,
    'beds': beds,
    'rating': rating,
    'num_reviews': num_reviews
}


# Trouver le lien vers la page suivante et l'utiliser pour répéter les étapes 3-5 pour
