from selectolax.parser import HTMLParser
import re
import json

# Get the HTML content
def get_html(baseurl):
    #headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
    #resp = httpx.get(baseurl, headers=headers)
    #print(resp.text)
    html = HTMLParser(baseurl)
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
        with open('data.json', 'a') as f:
            json.dump(item, f)
            f.write('\n')
            f.close()

# Crawler function
def crawlerStart(baseurl):
    html = get_html(baseurl)
    parse_page(html)




if __name__ == "__main__":
    crawlerStart()