def demande():
    while True:
        try:
            N = int(input(": "))

        except:
            print("erreur entre un nombre : ")
            return demande()
        return N

def verification():
    listeNote=[]
    for i in range(0,3):
        print("entre note ",i+1)
        note = demande()
        while note >20:
            print("erreur le nombre ne depasse pas sur 20")
            print("entre note ", i + 1)
            note = demande()
        listeNote.append(note)
    return listeNote


def moyenne(listNote):
    somme = 0
    for i in listNote:
        somme +=i
    moyenne= somme/len(listNote)
    return moyenne


def mention(Moyenne):
    if Moyenne >= 16 :
        print("Tres bien")
    elif Moyenne >= 14 :
        print(" Bien")
    elif Moyenne >= 12 :
        print(" Assez Bien")
    elif Moyenne >= 10  :
        print(" Passable")
    else :
        print(" insufisant")

notes = verification()
Moyenne =moyenne(notes)
print("la moyenne est : ",Moyenne.__round__(2))
mention(Moyenne)



