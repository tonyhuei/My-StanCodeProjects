"""
File: webcrawler.py
Name: Tony
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup
RANK = 200


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #
        tags = soup.find_all("table", {"class": "t-stripe"})[0].tbody.text.split()
        male_number = 0     # 男生人數總和
        female_number = 0   # 女生人數總和
        for i in range(5 * RANK):
            if (i-2) % 5 == 0 or (i-4) % 5 == 0:
                population_number = ""
                for element in tags[i]:
                    if element.isdigit():
                        population_number += element
                if (i-2) % 5 == 0:
                    male_number += int(population_number)
                if (i-4) % 5 == 0:
                    female_number += int(population_number)
        print("Male Number: " + str(male_number))
        print("Female Number: " + str(female_number))


if __name__ == '__main__':
    main()
