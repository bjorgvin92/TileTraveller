#ætla búa til fylki með strengjum sem prentar út leiðbeiningar tengdum þeim reit sem á við
#eining mun ég gera fylki fyrir þau input entry sem eru valid fyrir þann reit sem á við
#nota loopu til að fara yfir þá stafi sem eru í því fylki sem á við þann reit sem er á
#loopan fer í gegnum hvern staf og athugar hvort það samræmist inputtinu sem ég mun uppercase-a.
#síðan þar sem eg mun merkja reitina 1-9 þá mun ég hreyfa reitina með reikning.
#+3 er upp -3 er niður +1 er hægri -1 er vinstri.
#ef location = 9. þá er leikurinn búinn

s = ["","You can travel: (E)ast or (S)outh.", "You can travel: (E)ast or (W)est.", "You can travel:  (S)outh or (W)est.", "You can travel: (N)orth or (E)ast or (S)outh.", "You can travel: (S)outh or (W)est.", "You can travel: (N)orth or (S)outh.", "You can travel: (N)orth.", "You can travel: (N)orth."]
#^ leiðbeiningar hvers reit, bætti við tómu staki í byrjun svo ég þurfi ekki að pæla eins mikið í hvað á við hvaða reit
location = 7  #byrjunarreitur
c = ["", "ES", "EW", "WS", "NSE", "WS", "NS", "N", "N"]
#^ Leyfileg skref hvers reits, sama fyrirkomulag og í instruction strengnum.

while location < 9:  #sleppur úr loopuni þegar þú nærð reit 9 = WIN
    print(s[location]) #prentar út leiðbeiningar reitsins sem þú ert staddur í   
    command = str(input("Direction: "))
    command = command.upper() #til að hafa bara gera ráð fyrir uppercase
    for i, item in enumerate(c[location]): #rullar yfir þá stafi í stakinu í fylkinu númer reitsins sem þu ert staðsettur
        if command == item:
            if command == 'W':
                location = location - 1  # -1 = vinstri
                break
            if command == 'E':
                location = location + 1 # +1 = hægri
                break
            if command == 'N':
                location = location - 3 #-3 er upp
                break
            if command == 'S':
                location = location + 3 #+3 er niður
                break
        if i+1 == len(c[location]):   #þetta er loka keyrsla loopunar. Ef ekkert skilyrði er mætt þá er inputtið rangt.
            print("Not a valid direction!")
print("Victory!") #Þú slapst úr loopuni = WIN

#https://github.com/bjorgvin92/TileTraveller
    
        
