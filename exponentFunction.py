def exponent(base_number, power_number):
    result = 1
    for index in range(power_number):
        result = result*base_number
    return result


print(exponent(3, 3))
