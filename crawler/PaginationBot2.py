from selenium import webdriver 
from selenium.webdriver.common.by import By
import time
import crawler
#import validProxies

# Random proxy function
"""
def rand_proxy():
    #proxy = random.choice(validProxies.ips)
    #return proxy"
"""


def loadBot():

    # List of proxy implementation
    """
    #proxy = rand_proxy()
    #chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument(f'--proxy-server={proxy}')
    """

    
    #Bot implementation
    driver = webdriver.Chrome()

    time.sleep(1)
    key = 1999999
    while key > 1000000:
        driver.get(f"https://www.imdb.com/title/tt0{str(key)}/reviews/?ref_=tt_ov_rt")

        print("Bot 2: ")
        print("~" * 50)
        try:
            loadMore = driver.find_element(By.ID, "load-more-trigger")
            i = 0
            while i < 4:
                driver.execute_script("arguments[0].click();", loadMore);
                i += 1
                print(f"Done {i} loads")
                time.sleep(3)
        except:
                print("No more reviews to load")
        
        
        time.sleep(8)
        crawler.crawlerStart(driver.page_source)
        key -= 1
        print("Done: " , driver.title) 
        print("\n") 

    driver.quit()
    
    
if __name__ == "__main__":
    loadBot()