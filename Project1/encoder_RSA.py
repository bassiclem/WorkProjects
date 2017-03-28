def encoder_RSA(L,E,N):
    P = len(L)
    S = [0x0]*P
    i = 0
    while i < P:

        L_i = int(L[i],16)
        S[i] = hex(((L_i)**E)%N)
        i += 1
    print( "S vaut {}".format(S))
    print( "S vaut {}".format(type(S[0])))

    return S

