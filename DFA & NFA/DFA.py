
f=open("DFA & NFA/DFA_Input.txt")

tranzitii = [[x for x in linie.split()] for linie in f.read().split('\n')]

f.close()


stari_finale = tranzitii[len(tranzitii)-1]
tranzitii.remove(tranzitii[len(tranzitii)-1])
cuvant = input("Cuvant de verificat:").strip(' ')

stare_curenta = tranzitii[0][0]
drum=[stare_curenta]
i=0


while i<len(cuvant):
    for t in tranzitii:
        if t[0]==stare_curenta and cuvant[i]==t[1]:
            stare_curenta=t[2]
            drum.append(stare_curenta)
            i+=1
            break
    continue
if i==len(cuvant) and stare_curenta in stari_finale:
    print("acceptat")
    for i in range(len(drum)-1):
        print(f'{drum[i]} ->',end=' ')
    print(drum[len(drum)-1])
else:
    print("neacceptat")


