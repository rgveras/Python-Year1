"""

Ricardo Veras
Student #: 250692934
CompSci-1026A Assignment 4 (processUpdates file)

This file will take a data file and an update file from user input from main.py and check if they exist
If they exist, the data will be processed

Each line in the update file will be checked for validity. If invalid, the line will be written to the badUpdateFile

If the line is valid, it will use the class CountryCatalogue's function addCountry to add it to the object catlog if it is not already there
It will then check if there are update values, and it will update those values in catlog using functions from class CountryCatalogue

It will then use the function saveCountryCatalogue of class CountryCatalogue to save the updated values to the file OUTFILE

It will then exit and return True, catlog if updates were successfully carried out or False, None otherwise

"""


from catalogue import CountryCatalogue


def processUpdates(cntryFileName, updateFileName, badUpdateFile):
    OUTFILE = 'output.txt'
    CONTINENT = ["Africa", "Antarctica", "Arctic", "Asia", "Europe", "North_America", "South_America"]
    catlog = None

    def checkFile(type, fileName):                      # checks if a file exists
        OUTFILE = 'output.txt'
        result = False
        catlog = None
        while not result:
            try:
                result = open(fileName, 'r', encoding='UTF-8')
            except FileNotFoundError:
                user = input('Would you like to quit? "Y"(yes) or "N"(no): ')
                if user == 'N':
                    fileName = input('Please enter a new ' + type + ' file name: ')     # if user chooses not to quit a new file is input
                else:
                    break

        if not result:                                  # If no file was found, this prints update unsuccessful to the update file
            OUTFILE = open(OUTFILE, 'w', encoding='UTF-8')
            OUTFILE.write('Update Unsuccessful\n')
            OUTFILE.close()
            return result, catlog
        else:
            result.close()
            result = True
            return result, fileName                     # returns result=True and an existing fileName

    result1, cntryFile = checkFile('country data', cntryFileName)
    if result1:
        CountryCatalogue(cntryFile)                     # creates an object of class CountryCatalogue using cntryFile

    result2, updateFile = checkFile('country update', updateFileName)

    result = result1 and result2                        # result is set to True if data and update files both exist

    if result:
        updateFileOpen = open(updateFile, 'r', encoding='UTF-8')
        badUpdateFileOpen = open(badUpdateFile, 'w', encoding='UTF-8')
        catlog = CountryCatalogue(cntryFile)

        for line in updateFileOpen:                     # checks if a line is valid or not and updates files accordingly
            valid = True
            if line == '\n':                            # if the line is empty, it skips to the next line
                continue
            line = line.strip()
            lineTerms = line.split(';')
            country = lineTerms[0].strip()              # the country name of the line being read is set to country
            cont = ''
            area = ''
            pop = ''

            if lineTerms[0] == '':                     # if no country name, the line is updated to badUpdateFile and the next line is processed
                badUpdateFileOpen.write(line + '\n')
                continue

            if lineTerms[0][0].islower():               # if the first letter of the name is lowercase, valid is set to False
                valid = False

            if len(lineTerms) > 4:                      # if > 3 semi-colons, there will be more than 4 terms and valid is set to False
                valid = False

            for i in range(1, len(lineTerms)-1):        # if there is a duplicate first letter in any two terms after the name, valid is set to False
                if lineTerms[i].strip()[0] == lineTerms[i+1].strip()[0]:
                    valid = False

            for letter in range(1, len(lineTerms)):
                if lineTerms[letter].strip()[0] == 'P' or lineTerms[letter].strip()[0] == 'A':              # if the first letter of a term after the name is P or A
                    if lineTerms[letter].strip()[0] == 'P':
                        pop = lineTerms[letter].strip(' P=')                                                # population value is set to pop
                    if lineTerms[letter].strip()[0] == 'A':
                        area = lineTerms[letter].strip(' A=')                                               # area value is set
                    for term in lineTerms[letter].strip(' PA=').split(','):     # each term has spaces, "P", "A" and "=" removed and is split into smaller terms by commas
                        if len(term) > 3:                                       # if any smaller term is more than 3 characters, valid set to False
                            valid = False

                if lineTerms[letter].strip()[0] == 'C':
                    cont = lineTerms[letter].strip(' C=')                       # sets continent value
                    if lineTerms[letter].strip(' C=') not in CONTINENT:         # if not a valid continent, valid set to False
                        valid = False

            for name in lineTerms[0].strip().split('_'):                        # if country name is not all letters or underscores, valid is set to False
                if not name.isalpha():
                    valid = False

            if not valid:                   # if any of the above parameters prove the line to be invalid, its line is written to badUpdateFile
                badUpdateFileOpen.write(line + '\n')

            else:                                                               # if the line is valid and there are update values, they are updated in catlog
                catlog.addCountry(country, pop, area, cont)
                if area != '':
                    CountryCatalogue.setAreaOfCountry(catlog._countryCat[country], area)
                if cont != '':
                    CountryCatalogue.setContinentOfCountry(catlog._countryCat[country], cont)
                if pop != '':
                    CountryCatalogue.setPopulationOfCountry(catlog._countryCat[country], pop)

            catlog.saveCountryCatalogue(OUTFILE)                                # catlog's updated values are written to output.txt

        updateFileOpen.close()
        badUpdateFileOpen.close()

    return result, catlog
