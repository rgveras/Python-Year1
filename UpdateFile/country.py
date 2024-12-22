"""

Ricardo Veras
Student #: 250692934
CompSci-1026A Assignment 4 (country file)

This file has class Country that sets values of country name, area, population and continent to an object

It contains functions to check the values and to set area, population and continent

It contains a __repr__ function that prints a country and its corresponding values of area, population and continent

"""


class Country:                              # sets values of name, continent, population and area to an object
    def __init__(self, name, continent, pop, area):
        self._name = name
        self._pop = pop
        self._area = area
        self._continent = continent

    def getName(self):
        return self._name

    def getPopulation(self):
        return self._pop

    def getArea(self):
        return self._area

    def getContinent(self):
        return self._continent

    def setPopulation(self, value):         # value will replace the current population with updated value
        self._pop = value

    def setArea(self, value):
        self._area = value

    def setContinent(self, value):
        self._continent = value

    def __repr__(self):
        return "%s (pop: %s, size: %s) in %s" % (self._name, self._pop, self._area, self._continent)
