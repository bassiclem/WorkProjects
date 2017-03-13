class Donnees:
    def __init__(self, chaine_donnee):
        print (type(chaine_donnee))
        self.chaine = chaine_donnee
        self.chaine_str = str(self.chaine)
        self.origine = ""
        self.length = len(self.chaine_str)

    def sequencage(self, n, *parameter):
        i = 0
        k = 0
        indice = [0]*(n+1)
        indice[0] = 0
        part = [0]*n
        part_hexa = [0x0]*n
        taille = 0
        while i < n :
            taille += parameter[i]
            i += 1
            indice[i] = indice[i-1]+parameter[i-1]

        if taille == self.length:
            while k < n:
                part[k] = self.chaine_str[indice[k]:indice[k+1]]
                part_hexa[k] = hex(int(part[k],2))
                k += 1
        else:
            print ("pas de decomposition possible")


        return part_hexa




