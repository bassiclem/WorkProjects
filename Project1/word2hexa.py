def word2hexa(WORD):

    i = 0
    k = 0
    l = 0
    for character in WORD.lower():
        i += 1
    e = ["a"] * i
    e_hexa = [0x0] * i
    for character in WORD.lower():
        e[k] = character
        k += 1
    while l < i:
        e_hexa[l] = hex(ord(e[l]))
        l += 1

    return e_hexa