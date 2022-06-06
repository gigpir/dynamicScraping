# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Scraper import Scraper

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def getPagesList(fname):
    with open(fname, "r") as f:
        return f.readlines()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    pages = getPagesList("trip_advisor_links.txt")
    for p in pages:
        print(p)
        scraper = Scraper(startingLink=p).scrapeTripAdvisorReviewPage()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
