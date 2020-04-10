import wave_checker.scrape_titles as sc

def contents(soup):
    table_contents = soup.find_all("table", class_="tabulka")
    mix_models = table_contents[0]
    mix_models_contents = get_contents(mix_models)
    # coger tabla "class_=tabulka" y buscar los tr. Dentro de cada tr buscar tds

def get_contents(table):
    dict_content = {}
    trs = table.find_all("tr")
    for i, tr in enumerate(trs):
        content = []
        tds = tr.find_all("td")
        if i in [0, 1, 3, 6, 7, 9, 13]:
            for td in tds:
                text = td.text
                if text.strip() == "":
                    text = None
                content.append(text)

        elif i in [2, 4, 10, 12, 14]:
            continue
        elif i == 11:
            for td in tds:
                div_list = []
                divs = td.find_all("div")
                for div in divs:
                    text = div.text
                    if text.strip() == "":
                        text = None
                    div_list.append(text)
                content.append(div_list)
        elif i in [5, 8]:
            for td in tds:
                try:
                    span = td.find_all("span")[0]
                    title = span['title']
                except IndexError:
                    title = None
                content.append(title)

        dict_content[i]=content
    print(dict_content)
