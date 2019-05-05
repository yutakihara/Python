#
# Name: Yuta Kihara
# Description of program: Reading data of each country, air quality, and population
#                         from tsv file Analyzing air quality data corresponding with Country

# function that reads in air quality data
# and returns a dictionary of average air quality
#
import csv

def make_avg_pm2_dictionary():
    #
    # your code goes here
    pm2Dict = {}
    countDict = {}

    with open('air_data.tsv', encoding="utf8", errors='ignore') as f:
        reader = csv.DictReader(f,delimiter="\t")
        for row in reader: # reader is a dictionary
            country = row['Country'] # extracting data dic[key] -> value
            pm2Dict.setdefault(country, 0) # set country as key and 0 as value
            countDict.setdefault(country,0) # set country as key and 0 as value for counting
            pm2Dict[country] += float (row['PM2'])
            countDict[country] += 1

        for k in countDict:
            pm2Dict[k] = round((pm2Dict[k] / countDict[k]), 2) # calculating average

    return pm2Dict
#
# function that takes a dictionary of air quality for each country (aqd)
# and returns a dictionary with the population and air quality for each country
# if that country has air quality data
#
def add_cia_population_data(aqd):
    #
    # your code goes here, clean up the data with strip
    #
    popDict = {}
    country = aqd.keys(); # extracting only country data

    with open('cia_population.tsv', encoding="utf8", errors='ignore') as f:
        reader = csv.reader(f,delimiter="\t") # reader is a list
        for row in reader:
            if row[1] in country: # if country is in the list
                popDict[row[1]] = [row[2], aqd[row[1]]] # population : air quality

    return popDict

#
# print out country name, population, and  pm2 values
# that exceed the WHO's threshold (in ug/m3) for 1 year pm2 levels
# that increase long-term mortality risk by 15% from figure 1
# Print the data sorted by the last name of the country
#
def print_exceed_threshold(data,threshold):
    #
    # your code goes here
    #
    ranking = 1
    data = sorted(data.items()) # data becomes list type
    print("Ranking" + "\t" + "Country" + "\t" + "Population" + "\t" + "Air Quality(PM2.5)" + "\n")
    for i in range(len(data)):
        val, list = data[i]
        if (list[1] > threshold):
            print(str(ranking) + ": "+ val + "\t" + list[0] + "\t\t" + str(list[1]) + "\n")
            ranking += 1
#
# call all the functions
#
def main():
    # Build dictionary from air quality file
    avg_pm2 = make_avg_pm2_dictionary()

    # Read in cia population and create a dictionary
    # with population and average pm2 data for each country
    country_data = add_cia_population_data(avg_pm2)

    # print countries with air quality
    # exceeding WHO's guidelines
    print_exceed_threshold(country_data,35)

#
#run the analysis
#
main()
