def calculeazaDrum(cuvant, stare_curenta, drum, drumuri):
    global stari_finale, tranzitii
    if len(cuvant) == 0:
        if stare_curenta in stari_finale and drum not in drumuri:
            drumuri.append(drum)
        return
    if stare_curenta in tranzitii and cuvant[0] in tranzitii[stare_curenta]:
        stari = tranzitii[stare_curenta][cuvant[0]]
        for s in stari:
            calculeazaDrum(cuvant[1:], s, drum + (s,), drumuri)

f = open('NFA_Input.txt')
stari_finale = set(f.readline().strip().split()) # set cu starile finale
tranzitii = {}   # dictionar de dictionare pentru fiecare stare
s = f.readline()
while s!='':
    tranzitie = s.strip().split()
    if tranzitie[0] not in tranzitii:
        tranzitii[tranzitie[0]] = {}
    if tranzitie[1] not in tranzitii[tranzitie[0]]:
        tranzitii[tranzitie[0]][tranzitie[1]] = [tranzitie[2]]
    else:
        tranzitii[tranzitie[0]][tranzitie[1]].append(tranzitie[2])
    s = f.readline()

f.close()

cuvant = input('Cuvant de verificat: ').strip(' ')

if cuvant == '':
    print('acceptat - cuvant vid')
else:
    drumuri = []
    calculeazaDrum(cuvant, 'q0', ('q0',), drumuri)
    if len(drumuri) == 0:
        print('cuvant neacceptat')
    else:
        for i in range(len(drumuri)):
            print(f'Drumul {i+1}:', end=' ')
            for j in range(len(drumuri[i])-1):
                print(f'{drumuri[i][j]} ->',end=' ')
            print(drumuri[i][len(drumuri[i])-1])

