from datetime import datetime
import requests
from bs4 import BeautifulSoup
import unicodedata

def row_gen(row):
    sig = lambda x: float(x[0]) if x[1] in ["N","E"] else -float(x[0])
    lat,lon = map(sig,map(lambda x: list(map(lambda y: y.get_text(strip=True),x)),zip(row.select(".tabev1"),row.select(".tabev2"))) )
    row_data = {
        "datetime": datetime.strptime(unicodedata.normalize("NFKD",row.select("a")[-1].text), "%Y-%m-%d %H:%M:%S.%f"),
        "lat":lat,
        "lon":lon,
        "depth":int(row.select_one(".tabev3").get_text(strip=True)),
        "mag":float(row.select_one(".tabev5 ~ .tabev2").get_text(strip=True)),
        "region":row.select_one(".tb_region").get_text(strip=True)
    }
    return row_data
def getdatapoint():
    all_keypoints = []
    


    return keypoint
def get_page(page=1):
    all_earthquakes = []
    url = "https://www.emsc-csem.org/Earthquake/"
    params = {"view":page}
    soup = BeautifulSoup(requests.get(url,params=params).text,"html.parser")
    table = soup.select("#tbody > tr")
    for row in table:
        try:
            all_earthquakes.append(row_gen(row))
        except:
            print(row)
    return all_earthquakes