kroky = [13443,8832,3450,7765,14098]
cvicenia = ["beh","X","plavanie","beh","fitko"]
kalorie = [810,400,590,790,840]

def pridaj_den (kr, cv, kcal):
    kroky.append(kr)
    cvicenia.append(cv)
    kalorie.append(kcal)
    print("Úspešne ste pridali deň!")
    print("-",kr,"krokov")
    print("-",cv)
    print("-",kcal,"kalórií")

def poslednych_5():
    print("Vypisujem poslednývh 5 dní:")
    for i in range(len(kroky)-1,len(kroky)-6,-1):
        print("----------",i+1,"deň","----------")
        print("--> KROKY:",kroky[i])
        print("--> CVIČENIE:",cvicenia[i])
        print("--> KALÓRIE:",kalorie[i])
        print("---------------------------------")
        
def rekord():
    rek = max(kalorie)
    i = kalorie.index(rek)
    print("Váš rekord je:",rek,"kalórií. A v tento deň ste:")
    print("--> spravili",kroky[i],"krokov")
    print("--> cvik:",cvicenia[i])

def profil():
    name=input("Zadajte meno:")
    age=int(input("Zadajte váš vek:"))
    weight=int(input("Zadajte vašu váhu:"))
    height=int(input("Zadajte vašu výšku:"))/100
    bmi= weight/height**2
    print(name,"má BMI:",round(bmi,2))
print("celkový počet krokov:",sum(kroky))
print("Celkový počet spálených kalórií:",sum(kalorie))


##a=0
##for i in cvicenia:
##    if i != "X":
##        print(i)
##        a +=1

print("Celkový počet cvičení:",len(cvicenia)-cvicenia.count("X"))

b=0
for i in kroky:
    if i >= 10000:
        ind = kroky.index(i)
        if cvicenia[ind] != "X" and kalorie[ind] >= 600:
            b +=1


print("Počet aktívnych dní:",b)

def help():
    print("Naša aplikácia ponúka 5 funkcií:")
    print("-->pridaj_den() pridá deň do aplikácie")

##pridaj_den(20000,2,500)
##poslednych_5()
##def rekord()
profil()