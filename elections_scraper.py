import requests
from bs4 import BeautifulSoup as BS
import re
import csv
import sys

# separators
def sep1():
    print(70 * "=")
def sep2():
    print(70 * "-")
sep3 = 60 * ">"


def intro():
    sep1()
    print("{0:^70}".format("ELECTIONS SCRAPER"))
    sep1()
    print('''Please, choose one of the  Czech regions on this website:
https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ''')
    sep2()


def select_region():
    region = input('''Link to the selected region:
''')
    region_test = re.search("kraj=[0-9+]+&xnumnuts=[0-9+]", region)
    if region_test:
        sep2()
        return region
    else:
        print("Wrong URL!")
        restart = input('''Do you want to restart this app? Type "y" if yes.
Anything else will terminate this app. Restart? ''')
        if restart == "y":
            select_region()
        else:
            sys.exit("Have a nice day!")


def type_filename():
    name = input("Please, name your csv file where you can later find the result: ")
    name_test = re.search("csv$", name)
    if not name_test:
        print("It's working... please wait")
        name = name + ".csv"
        sep2()
        return name
    else:
        print("Don't add the suffix, please. Try again...")
        type_filename()


def get_data(trs):
    td_list = trs.find_all("td")
    town_code = td_list[0].getText()
    town_name = td_list[1].getText()
    town_link = td_list[0].find("a").get("href")
    src = BS(requests.get("https://volby.cz/pls/ps2017nss/" + town_link).text, "html.parser")
    tables = src.find_all("table")
    cells = tables[0].find_all("td")
    data = {"ID": town_code, "Obec": town_name,
            "Voliči": cells[3].getText(),
            "Obálky": cells[6].getText(),
            "Platné hlasy": cells[7].getText()}
    for t in tables[1:]:
        trs = t.find_all("tr")
        for tr in trs[2:]:
            tds = tr.find_all("td")
            party = tds[1].getText()
            votes = tds[2].getText()
            data[tds[1].getText()] = votes
            data[party] = votes
    return data


def get_town_list(source_code):
    towns = source_code.find_all("div", {"class": "t3"})
    town_list = []
    for t in towns:
        all_rows = t.find_all("tr")
        for row in all_rows[2:]:
            town_list.append(get_data(row))
        return town_list


def write_csv_file(filename, town_list):
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=town_list[0].keys())
        writer.writeheader()
        writer.writerows(town_list)


def main():
    intro()
    region = select_region()
    source_code = BS(requests.get(region).text, "html.parser")
    filename = type_filename()
    town_list = get_town_list(source_code)
    write_csv_file(filename, town_list)
    print(f'''{sep3}
Now you can find the result in {filename}.csv.
{sep3}''')


main()
