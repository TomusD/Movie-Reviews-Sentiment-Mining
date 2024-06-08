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
    movies = html.css("div.lister-item-content")
    #print(movies)

    for movie in movies:
        item = {
            "review": extractor(movie, "div.content"),
            "rating": extractor(movie, "span.rating-other-user-rating")
        }
        item["review"] = item["review"].replace("\n", " ")
        item["review"] = ' '.join(item["review"].split())
        item["rating"] = item["rating"].replace("\n", " ")
        item["rating"] = ' '.join(item["rating"].split())
        remove_string = "found this helpful. Was this review helpful? Sign in to vote. Permalink"
        item["review"] = item["review"].replace(remove_string, "")
        item["review"] = re.sub(r"\s*\d+\s*out\s*of\s*\d+\s*$", "", item["review"])
        item["review"] = item["review"].replace("\"", "")
        #print(item)
        with open('data_not.json', 'a') as f:
            json.dump(item, f)
            f.write('\n')
            f.close()


def main():
    html = get_html(baseurl)
    parse_page(html)


if __name__ == "__main__":

    key = 100000
    while key < 999999 :

        baseurl = f"https://www.imdb.com/title/tt0{str(key)}/reviews/?ref_=tt_ov_rt"
        main()
        key += 1
        print("Done: " , key)