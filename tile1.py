#ætla búa til fylki með strengjum sem prentar út leiðbeiningar tengdum þeim reit sem á við
#eining mun ég gera fylki fyrir þau input entry sem eru valid fyrir þann reit sem á við
#nota loopu til að fara yfir þá stafi sem eru í því fylki sem á við þann reit sem er á
#loopan fer í gegnum hvern staf og athugar hvort það samræmist inputtinu sem ég mun uppercase-a.
#síðan þar sem eg mun merkja reitina 1-9 þá mun ég hreyfa reitina með reikning.
#+3 er upp -3 er niður +1 er hægri -1 er vinstri.
#ef location = 9. þá er leikurinn búinn

s = ["","You can travel: (E)ast or (S)outh.", "You can travel: (E)ast or (W)est.", "You can travel:  (S)outh or (W)est.", "You can travel: (N)orth or (E)ast or (S)outh.", "You can travel: (S)outh or (W)est.", "You can travel: (N)orth or (S)outh.", "You can travel: (N)orth.", "You can travel: (N)orth."]
location = 7
c = ["", "ES", "EW", "WS", "NSE", "WS", "NS", "N", "N"]

while location < 9:
    print(s[location])    
    command = str(input("Direction: "))
    command = command.upper()
    for i, item in enumerate(c[location]):
        if command == item:
            if command == 'W':
                location = location - 1
                break
            if command == 'E':
                location = location + 1
                break
            if command == 'N':
                location = location - 3
                break
            if command == 'S':
                location = location + 3
                break
        if i+1 == len(c[location]):
            print("Not a valid direction!")
print("Victory!")


    
        
