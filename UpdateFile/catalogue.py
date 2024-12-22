"""

Ricardo Veras
Student #: 250692934
CompSci-1026A Assignment 4 (catalogue file)

This file contains class CountryCatalogue that will take in a file and utilize class Country from file country.py
It will use Country to make objects and then add those objects to a dictionary of CountryCatalogue

It contains functions to set values for population, area and continent.
It also has a function to check if a country is in the dictionary and a function to add a country if not in the dictionary.

This file also has a function that utilizes Country's __repr__ function to print objects within the dictionary

"""


from country import Country


class CountryCatalogue:
    def __init__(self, countryFile):
        self._file = open(countryFile, 'r')
        self._countryCat = {}
        for line in self._file:                                             # sets values to each country and adds them to self._countryCat
            line = line.strip().split('|')
            self._countryCat[line[0]] = Country(line[0], line[1], line[2], line[3])
            self._name = line[0]
            self._continent = line[1]
            self._pop = line[2]
            self._area = line[3]
            self._countryCat[line[0]] = Country(line[0], line[1], line[2], line[3])

    def setPopulationOfCountry(self, value):                                # value will be the updated population value
        self._pop = value

    def setAreaOfCountry(self, value):
        self._area = value

    def setContinentOfCountry(self, value):
        self._continent = value

    def findCountry(self, country):
        if country in self._countryCat:
            return self._countryCat[country]

    def addCountry(self, countryName, pop, area, cont):
        if countryName not in self._countryCat:
            self._countryCat[countryName] = Country(countryName, pop, area, cont)   # sets new Country object to countryCat
            return True
        else:
            return False

    def printCountryCatalogue(self):
        for country in self._countryCat:
            print(Country.__repr__(self._countryCat[country]))

    def saveCountryCatalogue(self, fname):
        try:
            newfile = open(fname, 'w')
            count = 0
            for i in sorted(self._countryCat):
                count += 1
                newfile.write(self._countryCat[i]._name + '|' + self._countryCat[i]._continent + '|' + self._countryCat[i]._pop + '|' + self._countryCat[i]._area + '\n')
            newfile.close()
            return count                    # returns number of lines written to the new file
        except:
            return -1

    def __repr__(self):
        return str(self._countryCat)
