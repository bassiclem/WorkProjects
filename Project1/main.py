from market import *
from encoder_RSA import *
from donnees import *
from word2hexa import *

D = Donnees(10011001)
M = Market()
MM = word2hexa(M.Produit)
print(MM)
MMenc = encoder_RSA(MM,6,15)
print("MMenc", MMenc)
DD = D.sequencage(3,3,3,2)
DDenc = encoder_RSA(DD,6,15)
print("DDenc",DDenc)
print ("DD vaut {}".format(DD))
X = encoder_RSA(["0x0","0x1","0x2","0x3","0x4","0x5","0x6","0x7","0x8","0x9","0xa","0xb","0xc","0xd","0xe"],3,18)
print(X)
