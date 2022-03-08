


def get_loteimg(secuence):
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