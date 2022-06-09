from Scraper import Scraper

def getPagesList(fname):
    with open(fname, "r") as f:
        return f.readlines()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    pages = getPagesList("trip_advisor_links.txt")
    for p in pages:
        end = False
        while not end:
            if Scraper(startingLink=p).scrapeTripAdvisorReviewPage():
                end = True
