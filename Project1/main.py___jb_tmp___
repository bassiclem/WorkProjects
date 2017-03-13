from market import *
from encoder_RSA import *
from donnees import *
from word2hexa import *

D = Donnees(1111011000110010)
M = Market()
MM = word2hexa(M.Produit)
print(MM)
MMenc = encoder_RSA(MM,6,15)
print("MMenc", MMenc)
DD = D.sequencage(4,4,4,4,4)
DDenc = encoder_RSA(DD,6,15)
print("DDenc",DDenc)
