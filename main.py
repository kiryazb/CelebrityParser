from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from datetime import datetime
import json
import csv
import multiprocessing

options = webdriver.ChromeOptions()
options.add_argument('--headless')

categor = []
urls = []


def download(url):
    s = Service("C:\\PythonProjects\\3st_kwork\\chromedriver\\chromedriver.exe")
    driver = webdriver.Chrome(service=s,
                              options=options)
    driver.get(url=url)
    a = driver.page_source
    driver.close()
    driver.quit()
    return a


def get_full_info(list):
    url = list[0]
    categor = list[1]
    soup = BeautifulSoup(download(url), "lxml")
    all_class = soup.find_all(class_="card card-full hover-a mb-module mb-md-5")
    for i in all_class:
        try:
            flg = False
            url_page = ("https://www.peoples.ru" + i.find_all("a")[2].get("href"))
            soup = BeautifulSoup(download(url_page), "lxml")
            name = soup.find_all("h2")[0].text
            table = soup.find("p").find_all("a")
            try:
                int(table[1].text)
                birthday = table[0].text + "." + table[1].text
            except:
                birthday = table[0].text
            birthplace = soup.find_all("br")[0].find_next().text
            try:
                int(birthplace[0])
                death = birthplace
                birthplace = "Отсутсвует"
                flg = True
            except:
                birthplace = soup.find_all("br")[0].find_next().text
            if not (flg):
                test = soup.find_all("br")[1]
                death = test.find_next().text + "." + test.find_next().find_next().text
                try:
                    int(death[-1])
                    death = test.find_next().text + "." + test.find_next().find_next().text
                except:
                    try:
                        int(death[-1])
                        death = test.find_next().text
                    except:
                        death = "Отсутствует"
            first = categor.split(" ")[1]
            second = categor.split(" ")[3]
            list = [first, second, name, birthday, birthplace, death]
            with open("tv.csv", "a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(list)
        except:
            pass


if __name__ == "__main__":
    urls = ["https://www.peoples.ru/tv/"]
    categors = [" Телевидение Личности "]
    for i in range(len(urls)):
        try:
            url = urls[i]
            categor = categors[i]
            soup = BeautifulSoup(download(url), "lxml")
            coun = int(soup.find(class_="pagination justify-content-center").text.split(" ")[6].replace(",", ""))
            count_page = 28
            if coun > 27:
                coun = 27
            print(coun)
            while coun > 0:
                start = datetime.now()
                if coun == 1:
                    url = url + f"?page={count_page}"
                    get_full_info([url, categor])
                    print(url, "Записано, reset")
                    break
                if coun == 2:
                    hrefs = [[url + f"?page={count_page}", categor], [url + f"?page={count_page + 1}", categor]]
                    with multiprocessing.Pool(len(hrefs)) as pool:
                        pool.map(get_full_info, hrefs)
                    print(hrefs[0][0], hrefs[1][0])
                    print("Записано, reset")
                if coun == 3:
                    hrefs = [[url + f"?page={count_page}", categor], [url + f"?page={count_page + 1}", categor],
                             [url + f"?page={count_page + 2}", categor]]
                    with multiprocessing.Pool(len(hrefs)) as pool:
                        pool.map(get_full_info, hrefs)
                    print(hrefs[0][0], hrefs[1][0], hrefs[2][0])
                    print("Записано, reset")
                if coun == 4:
                    hrefs = [[url + f"?page={count_page}", categor], [url + f"?page={count_page + 1}", categor],
                             [url + f"?page={count_page + 2}", categor], [url + f"?page={count_page + 3}", categor]]
                    with multiprocessing.Pool(len(hrefs)) as pool:
                        pool.map(get_full_info, hrefs)
                    print(hrefs[0][0], hrefs[1][0], hrefs[2][0], hrefs[3][0])
                    print("Записано, reset")
                if coun == 5:
                    hrefs = [[url + f"?page={count_page}", categor], [url + f"?page={count_page + 1}", categor],
                             [url + f"?page={count_page + 2}", categor], [url + f"?page={count_page + 3}", categor],
                             [url + f"?page={count_page + 4}", categor]]
                    with multiprocessing.Pool(len(hrefs)) as pool:
                        pool.map(get_full_info, hrefs)
                    print(hrefs[0][0], hrefs[1][0], hrefs[2][0], hrefs[3][0], hrefs[4][0])
                    print("Записано, reset")
                if coun == 6:
                    hrefs = [[url + f"?page={count_page}", categor], [url + f"?page={count_page + 1}", categor],
                             [url + f"?page={count_page + 2}", categor], [url + f"?page={count_page + 3}", categor],
                             [url + f"?page={count_page + 4}", categor], [url + f"?page={count_page + 5}", categor]]
                    with multiprocessing.Pool(len(hrefs)) as pool:
                        pool.map(get_full_info, hrefs)
                    print(hrefs[0][0], hrefs[1][0], hrefs[2][0], hrefs[3][0], hrefs[4][0], hrefs[5][0])
                    print("Записано, reset")
                if coun == 7:
                    hrefs = [[url + f"?page={count_page}", categor], [url + f"?page={count_page + 1}", categor],
                             [url + f"?page={count_page + 2}", categor], [url + f"?page={count_page + 3}", categor],
                             [url + f"?page={count_page + 4}", categor], [url + f"?page={count_page + 5}", categor],
                             [url + f"?page={count_page + 6}", categor]]
                    with multiprocessing.Pool(len(hrefs)) as pool:
                        pool.map(get_full_info, hrefs)
                    print(hrefs[0][0], hrefs[1][0], hrefs[2][0], hrefs[3][0], hrefs[4][0], hrefs[5][0], hrefs[6][0])
                    print("Записано, reset")
                if coun == 8:
                    hrefs = [[url + f"?page={count_page}", categor], [url + f"?page={count_page + 1}", categor],
                             [url + f"?page={count_page + 2}", categor], [url + f"?page={count_page + 3}", categor],
                             [url + f"?page={count_page + 4}", categor], [url + f"?page={count_page + 5}", categor],
                             [url + f"?page={count_page + 6}", categor], [url + f"?page={count_page + 7}", categor]]
                    with multiprocessing.Pool(len(hrefs)) as pool:
                        pool.map(get_full_info, hrefs)
                    print(hrefs[7][0])
                    print("Записано, reset")
                if coun >= 9:
                    hrefs = [[url + f"?page={count_page}", categor], [url + f"?page={count_page + 1}", categor],
                             [url + f"?page={count_page + 2}", categor], [url + f"?page={count_page + 3}", categor],
                             [url + f"?page={count_page + 4}", categor], [url + f"?page={count_page + 5}", categor],
                             [url + f"?page={count_page + 6}", categor], [url + f"?page={count_page + 7}", categor],
                             [url + f"?page={count_page + 8}", categor]]
                    with multiprocessing.Pool(len(hrefs)) as pool:
                        pool.map(get_full_info, hrefs)
                    print(hrefs[8][0])
                    print("Записано, reset")
                print(datetime.now() - start)
                count_page += 9
                coun -= 9
        except:
            pass
