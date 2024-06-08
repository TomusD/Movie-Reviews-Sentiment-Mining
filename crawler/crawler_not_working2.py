from selectolax.parser import HTMLParser
import httpx
import re
import json


def get_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = httpx.get(url, headers=headers)
    html = HTMLParser(response.text)

    return html

# Extractor function to bypass NoneType error
def extractor(html, selector):
    try:
        return html.css_first(selector).text()
    except AttributeError:
        return "None"

# Extract the data
def parse_page(html):
    movies = html.css('div.content')
    #print(movies)

    for movie in movies:
        item = {
            "review": extractor(movie, "div.teaser"),
            "rating": extractor(movie, "div.flex")
        }
        item["review"] = item["review"].replace("\n", " ")
        item["review"] = ' '.join(item["review"].split())
        item["rating"] = item["rating"].replace("\n", " ")
        item["rating"] = ' '.join(item["rating"].split())
        remove_string = "... read the rest."
        item["review"] = item["review"].replace(remove_string, "")
        item["rating"] = re.sub(r"%.*$", "", item["rating"])
        item["review"] = item["review"].replace("\"", "")
        #print(item)
        with open('data_no2.json', 'a') as f:
            json.dump(item, f)
            f.write('\n')
            f.close()


def main():
    html = get_html(baseurl)
    parse_page(html)


if __name__ == "__main__":

    key = 1
    while key < 500000 :

        baseurl = f"https://www.themoviedb.org/movie/{str(key)}/reviews?language=en-US"
        main()
        key += 1
        print("Done: " , key)