# file for manipulating/editing data_james and data_anna

import sys, json, jsonhandling, os


# conditions for adding other rewards for certain values of folge
def checkConditionsAndManipulate_Anna():
    global data_anna

    # annas conditions
    if data_anna['folge'] == 0:
        print('Anna: Deine Folge wurde zurückgesetzt. Streng dich was an!')
    elif data_anna['folge'] == 1:
        print('Anna hat 1 Schnapszahl in Folge. Nichts passiert. Viel Glück für die nächste!')
    elif data_anna['folge'] == 2:
        print('Die Folge beträgt 2! Du erhältst eine Freikarte')
        data_anna['freikarten'] += 1
    elif data_anna['folge'] == 3:
        print('Es sind nun ganze drei Schnapszahlen hintereinander. \nDu kriegst einen YouTube-Gutschein!')
        data_anna['youtube'] += 1
    elif data_anna['folge'] == 4:
        print('Langsam langsam... Du hast eine Viererfolge! \nDu kriegst den Einmal-Aufstehen-Gutschein.')
        data_anna['einmal_aufstehen'] += 1
    elif data_anna['folge'] == 5:
        print('Das gibt eine wohlverdiente Massage. Du hast eine Fünferfolge erreicht!')
        data_anna['massage'] += 1
    elif data_anna['folge'] == 6:
        print('Wieso bist du eigentlich plötzlich so gut?! Du hast 6 in Folge! \nDas gibt einen Sklavengutschein.')
        data_anna['sklave'] +=1
    elif data_anna['folge'] == 7:
        print('Du hast scheinbar eine Siebenerfolge. Aber ich glaube du schummelst... \nDu kriegst einen Striptease, uh lala ;)')
        data_anna['striptease'] += 1
    elif data_anna['folge'] == 8:
        print('Wow! Scheinbar hast du die Folge einmal erfüllt. \nEigentlich dachte ich nicht, dass es so weit kommen würde. \nHerzlichen Glückwunsch. \nDeine Folge wird jetzt allerdings auf 0 zurückgesetzt. Auf ein Neues! \nDu kriegst den ultimativen Preis: Du darfst meine Hasssache machen!')
        data_anna['hasssache'] += 1
        data_anna['folge'] = 0
    else:
        print('Ein Fehler ist wohl unterlaufen. Konsultiere James um ihn zu beheben. \nAchtung merke dir, was passiert ist.')
        # data_anna['folge'] = 0


    # We manipulated the data. Now we need to add it to the json files again.
    # turn it into json 
    json_anna = json.dumps(data_anna, indent=2)

    # add it to their file
    with open("data_anna.json", "w") as file_anna:
        file_anna.write(json_anna)



def checkConditionsAndManipulate_James():
    global data_james

    # james conditions
    if data_james['folge'] == 0:
        print('James: Deine Folge wurde zurückgesetzt. Streng dich was an!')
    elif data_james['folge'] == 1:
        print('James hat 1 Schnapszahl in Folge. Nichts passiert. Viel Glück für die nächste!')
    elif data_james['folge'] == 2:
        print('Die Folge beträgt 2! Du erhältst eine Freikarte')
        data_james['freikarten'] += 1
    elif data_james['folge'] == 3:
        print('Es sind nun ganze drei Schnapszahlen hintereinander. \nDu kriegst einen YouTube-Gutschein!')
        data_james['youtube'] += 1
    elif data_james['folge'] == 4:
        print('Langsam langsam... Du hast eine Viererfolge! \nDu kriegst den Einmal-Aufstehen-Gutschein.')
        data_james['einmal_aufstehen'] += 1
    elif data_james['folge'] == 5:
        print('Das gibt eine wohlverdiente Massage. Du hast eine Fünferfolge erreicht!')
        data_james['massage'] += 1
    elif data_james['folge'] == 6:
        print('Wieso bist du eigentlich plötzlich so gut?! Du hast 6 in Folge! \nDas gibt einen Sklavengutschein.')
        data_james['sklave'] +=1
    elif data_james['folge'] == 7:
        print('Du hast scheinbar eine Siebenerfolge. Aber ich glaube du schummelst... \nDu kriegst einen Striptease, uh lala ;)')
        data_james['striptease'] += 1
    elif data_james['folge'] == 8:
        print('Wow! Scheinbar hast du die Folge einmal erfüllt. \nEigentlich dachte ich nicht, dass es so weit kommen würde. \nHerzlichen Glückwunsch. \nDeine Folge wird jetzt allerdings auf 0 zurückgesetzt. Auf ein Neues! \nDu kriegst den ultimativen Preis: Du darfst meine Hasssache machen!')
        data_james['hasssache'] += 0
        data_james['folge'] = 0
    else:
        print('Ein Fehler ist wohl unterlaufen. Konsultiere James um ihn zu beheben. \nAchtung merke dir, was passiert ist.')
        # data_james['folge'] = 0


    # We manipulated the data. Now we need to add it to the json files again.
    # turn it into json 
    json_james = json.dumps(data_james, indent=2)

    # add it to their file
    with open("data_james.json", "w") as file_james:
        file_james.write(json_james)








######### ACTUAL START OF CODE #########


# getting all users specifications
opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]


with open("data_anna.json", "r") as f_a: # open  annas json file
    data_anna = json.load(f_a) # read it
    

with open("data_james.json", "r") as f_j: # open  james json file
    data_james = json.load(f_j) # read it



# checking for user command specification
if "-r" in opts: # resetting all data
   jsonhandling.reset() 
elif "-j" in opts: # adding one schnapszahl to james
    print('adding one to streak of james')
    data_james['folge'] += 1
    data_anna['folge'] = 0
    checkConditionsAndManipulate_James()
    checkConditionsAndManipulate_Anna()

elif "-rj" in opts: # removing one schnapszahl from james
    print('removing one Schnapszahl from james')
    data_james['folge'] -= 1
    checkConditionsAndManipulate_James()    

elif "-a" in opts: # adding one schnapszahl to anna
    print('adding one to streak of anna')
    data_anna['folge'] += 1
    data_james['folge'] = 0
    checkConditionsAndManip;ulate_Anna()
    checkConditionsAndManipulate_James()

elif "-ra" in opts: # removing one schnapszahl from anna
    print('removing one Schnapszahl from anna')
    data_anna['folge'] -= 1
    checkConditionsAndManipulate_Anna()

elif "-az" in opts: # setting annas folge to zero
    print('setting annas folge to zero')
    data_anna['folge'] = 0
    checkConditionsAndManipulate_Anna()

elif "-jz" in opts: # setting james folge to zero
    print('setting james folge to zero')
    data_james['folge'] = 0
    checkConditionsAndManipulate_James()

elif "-z" in opts: # setting all streaks to zero
    print('setting all streaks to zero')
    data_anna['folge'] = 0
    data_james['folge'] = 0
    checkConditionsAndManipulate_Anna()
    checkConditionsAndManipulate_James()

elif "-aj" in opts or "-ja" in opts: # adding one to streak in both data sets
    print('adding one to streak of james and anna')
    data_anna['folge'] += 1
    data_james['folge'] += 1
    checkConditionsAndManipulate_James()
    checkConditionsAndManipulate_Anna()


# adding changed to github
#os.system('git add * && git commit -q -m "S.o got a Schnapszahl." && git push -q')
#print('Pushed succesfully :)')
