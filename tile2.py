#ætla búa til fylki með strengjum sem prentar út leiðbeiningar tengdum þeim reit sem á við
#eining mun ég gera fylki fyrir þau input entry sem eru valid fyrir þann reit sem á við
#nota loopu til að fara yfir þá stafi sem eru í því fylki sem á við þann reit sem er á
#loopan fer í gegnum hvern staf og athugar hvort það samræmist inputtinu sem ég mun uppercase-a.
#síðan þar sem eg mun merkja reitina 1-9 þá mun ég hreyfa reitina með reikning.
#+3 er upp -3 er niður +1 er hægri -1 er vinstri.
#ef location = 9. þá er leikurinn búinn

def valid_answer(command): #fall sem sleppur ekki svari í gegn sem er ekki gilt.
    while True:
        for i, item in enumerate(c[location]):
                if command == item:
                    return command
                        
                if i+1 == len(c[location]):
                    print("Not a valid direction!")
        command = str(input("Direction: "))
        command = command.upper()

def relocate(command, location): #fall sem breytir um stöðu location eftir inntaki
    if command == 'N':
        location = location - 3
        return location
    if command == 'S':
        location = location + 3
        return location
    if command == 'W':
        location = location - 1
        return location
    if command == 'E':
        location = location + 1
        return location



s = ["","(E)ast or (S)outh.", "(E)ast or (W)est.", "(S)outh or (W)est.", "(N)orth or (E)ast or (S)outh.", "(S)outh or (W)est.", "(N)orth or (S)outh.", "(N)orth.", "(N)orth."]
#^ leiðbeiningar hvers reit, bætti við tómu staki í byrjun svo ég þurfi ekki að pæla eins mikið í hvað á við hvaða reit
location = 7  #byrjunarreitur
c = ["", "ES", "EW", "WS", "NSE", "WS", "NS", "N", "N"]
#^ Leyfileg skref hvers reits, sama fyrirkomulag og í instruction strengnum.







while location < 9: #hættir þegar loka reit er náð(nr9)
    print("You can travel: "+s[location])   #leiðbeiningar um mögulega leiðir tengd þeim reit sem þú ert á
    command = str(input("Direction: ")) #input
    command = command.upper() #breytir inputti i uppercase
    command = valid_answer(command) #sér til þess að svarið er gilt sem gefið var ef ekki þá krefst það annað svar.
    location = relocate(command, location) #breyir um staðsetningu
print("Victory!") #tilkynning um að þú vannst

#https://github.com/bjorgvin92/TileTraveller
    
        
