from selenium import webdriver 
import time
import crawler2
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

    key = 1
    while key < 500000:
        driver.get(f"https://www.themoviedb.org/movie/{str(key)}/reviews?language=en-US")

        print("Bot 3: ")
        print("~" * 50)    
        time.sleep(8)
        crawler2.crawler2Start(driver.page_source)
        key += 1
        print("Done: " , driver.title) 
        print("\n") 

    driver.quit()
    
    
if __name__ == "__main__":
    loadBot()