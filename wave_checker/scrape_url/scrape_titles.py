

def scrape_titles(soup):
    table_legends = soup.find_all("table", class_="table_legend")
    mix_models = table_legends[0]
    mix_models_titles = get_titles(mix_models)
    swell_table = table_legends[2]
    swell_table_titles = get_titles(swell_table)
    return mix_models_titles, swell_table_titles

def get_titles(table):
    tds = table.find_all("td")
    titles = []
    for td in tds:
        title = td.text
        titles.append(title)
    return titles


