# write python code to read csv file from URL and print it out

# import urllib, json
import wget, csv
import random


def main():
    print("Hello World!")
    # open csv file from URL and read it into a list
    # print out the list
    # url = "http://maps.googleapis.com/maps/api/geocode/json?address=googleplex&sensor=false"

    # response = urllib.urlopen(url)
    URL = "https://gist.githubusercontent.com/amitkarpe/ae5520f53d0d12d0202fd3a8d24e2e2d/raw/8b57d246142c61563d94b43532258917d31bf424/defi.csv"
    portfolio = "/tmp/portfolio/defi"+str(random.randint(1,100000))+".csv"
    response = wget.download(URL, portfolio)
    print ("\n Portfolio File Name ==>", portfolio)
    file = open(portfolio)
    # Open csv file from URL and read it into a list
    csvreader = csv.reader(file)
    header = []
    header = next(csvreader)
    rows = []
    for row in csvreader:
        rows.append(row)
    file.close()
    print (header)
    print (rows)

if __name__ == "__main__":
    main()