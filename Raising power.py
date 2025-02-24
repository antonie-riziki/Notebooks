def raising_number (base_num, pow_num):
    outcome = 1 #sets the value to 1 so that looping stops at the pow_number
    for index in range(pow_num):
        outcome = outcome * base_num
    #outcome = pow(base_num, pow_num)
    return outcome

answer = raising_number(2,8)
print(answer)


