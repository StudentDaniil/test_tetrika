import requests
from bs4 import BeautifulSoup
import csv


def number_of_animals():
    animal_counts = {}

    def process_page(url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        groups = soup.find_all('div', class_='mw-category-group')
        for group in groups:
            letter = group.find('h3').text.strip()
            items = group.find_all('li')
            count = len(items)
            animal_counts[letter] = animal_counts.get(letter, 0) + count

        next_page_link = soup.find('a', string='Следующая страница')
        if next_page_link:
            next_url = 'https://ru.wikipedia.org' + next_page_link['href']
            process_page(next_url)

    start_url = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
    process_page(start_url)

    with open('beasts.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Буква', 'Количество'])
        for letter in sorted(animal_counts.keys()):
            writer.writerow([letter, animal_counts[letter]])


if __name__ == '__main__':
    number_of_animals()
