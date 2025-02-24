is_needy = True
is_single = False

if is_needy and is_single:
    print("Your allowance amounts to 70,000/= ")

elif is_needy and not (is_single):
    print("Your allowance amounts to 40,000/= ")

elif is_single and not (is_needy):
    print("Your allowance amounts to 30,000/= ")

else:
    print("No allowance awarded")


def num(a, b, c):
    if a >= b and a >= c:
        return str(a) + " is the greatest value"

    elif b >= a and b >= c:
        return str(b) + " is the greatest value"

    else:
        return str(c) + " is the greatest value"

a = input()
b = input()
c = input()
print(num(a, b, c))
