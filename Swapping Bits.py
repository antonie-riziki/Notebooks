Even = 0b10101010
Odd = 0b01010101
def swap_bits(Even, Odd):
    #return (Odd & Even) >> 1 | (Odd & Odd) << 1
    return (Odd) >> 1 | (Even) << 1

#print(swap_bits(Even,Odd))
print(swap_bits(0b10101010, 0b01010101))
print(Even)
print(Odd)
