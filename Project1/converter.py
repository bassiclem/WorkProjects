class Donnees:
    def __init__(self, chaine_donnee):
        print (type(chaine_donnee))
        self.chaine = chaine_donnee
        self.chaine_str = str(self.chaine)
        self.origine = ""
        self.length = len(self.chaine_str)

    def sequencage(self, a, b, c):
        chaine_decomposee = [00000000000000000]
        first = Donnees(0000)
        second = Donnees(0000)
        third = Donnees(0000)
        print(first,second,third)
        if a+b+c == self.length:


            first.chaine_str = self.chaine_str[0:a]
            second.chaine_str = self.chaine_str[a:a+b]
            third.chaine_str = self.chaine_str[a+b:a+b+c]

        else:
            print ("pas de decomposition possible")
            first.chaine_str = "0"
            second.chaine_str = "0"
            third.chaine_str = "0"
        chaine_decomposee = [first.chaine_str, second.chaine_str, third.chaine_str]
        chaine_decomposee_hexa = [hex(int(first.chaine_str,2)), hex(int(second.chaine_str,2)), hex(int(third.chaine_str,2))]
        return chaine_decomposee_hexa




