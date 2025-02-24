""" Permutation """

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#alphabet = "ABCDE"
for first in alphabet:
    for second in alphabet:
        if first != second:
            for third in alphabet:
                print(first + second + third)
            
