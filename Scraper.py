
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from Review import Review
from pandas import pandas
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from tqdm import tqdm

class Scraper():
    def __init__(self, startingLink):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
        self.startingLink = startingLink
    def scrapeTripAdvisorReviewPage(self):
        # Load the HTML page
        self.driver.get(self.startingLink)
        end = False
        firstPage = True
        reviews = []
        sleep(5)
        timeout = 20
        pages = 0
        try:
            element_present = EC.presence_of_element_located((By.ID, "onetrust-reject-all-handler"))
            WebDriverWait(self.driver, timeout).until(element_present)
        except:
            print("Timeout")
            return
        if len(self.driver.find_elements(By.ID, "onetrust-accept-btn-handler")) > 0:
            self.driver.find_element(By.ID, "onetrust-banner-sdk").find_elements(By.ID, "onetrust-accept-btn-handler")[0].click()

        # Get output file name
        titleElem = self.driver.find_elements(By.CLASS_NAME, "WlYyy.cPsXC.GeSzT")
        self.outputFilename = titleElem[0].text.replace(" ", "_") + ".xlsx"

        print(f"Processing page: {self.outputFilename}")


        while(not end):
            print(f"Page {pages}", end="\r")
            try:
                element_present = EC.presence_of_element_located((By.CLASS_NAME, "ffbzW._c"))
                WebDriverWait(self.driver, timeout).until(element_present)
            except:
                print(f"Timeout occurred after {pages} pages")
                self.save(reviews)
                return

            mydivs = self.driver.find_elements(By.CLASS_NAME, "ffbzW._c")
            for div in mydivs:
                date = div.find_elements(By.CLASS_NAME,"eRduX")[0].text if len(div.find_elements(By.CLASS_NAME,"eRduX"))>0 else 'Null'
                date = date.split("•")[0]
                rev = Review(title=div.find_elements(By.CLASS_NAME,"NejBf")[0].text,
                             date=date,
                             text=div.find_elements(By.CLASS_NAME,"NejBf")[1].text)
                reviews.append(rev)
            try:
                element_present = EC.presence_of_element_located((By.CLASS_NAME, "eRhUG"))
                WebDriverWait(self.driver, timeout).until(element_present)
            except:
                print(f"Timeout occurred after {pages} pages")
                self.save(reviews)
                return
            if len(self.driver.find_elements(By.CLASS_NAME, "eRhUG")) == 2:
                self.driver.find_elements(By.CLASS_NAME, "eRhUG")[1].click()
            elif len(self.driver.find_elements(By.CLASS_NAME,"eRhUG")) == 1 and firstPage:
                self.driver.find_elements(By.CLASS_NAME, "eRhUG")[0].click()
                firstPage = False
            else:
                end = True
            pages += 1
            if pages==500:
                end = True
        if pages > 0:
            print(f"Scraped {pages} pages")
            self.save(reviews)

    def save(self, reviews):
        df = pandas.DataFrame.from_records([s.to_dict() for s in reviews])
        df.to_excel(self.outputFilename)