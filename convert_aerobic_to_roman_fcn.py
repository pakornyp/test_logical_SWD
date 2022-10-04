def convert_aerobic_to_roman_fcn(input_number):
    try:
        number_int = int(input_number)
        number_str = str(number_int)
    except ValueError:
        print("input must be a number between 1 and 1000")
        return

    if number_int <= 0 or number_int > 1000:
        print("input must be a number between 1 and 1000")
        return

    aerobic_reference = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                         10, 20, 30, 40, 50, 60, 70, 80, 90,
                         100, 200, 300, 400, 500, 600, 700, 800, 900,
                         1000]
    roman_reference = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX",
                       "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "CX",
                       "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM",
                       "M"]
    roman_number = ""
    value_1000 = number_int // 1000
    if value_1000 != 0:
        roman_number = roman_number + roman_reference[aerobic_reference.index(value_1000*1000)]
        number_int = number_int - (1000*value_1000)
    value_100 = number_int // 100
    if value_100 != 0:
        roman_number = roman_number + roman_reference[aerobic_reference.index(value_100*100)]
        number_int = number_int - (100*value_100)
    value_10 = number_int // 10
    if value_10 != 0:
        roman_number = roman_number + roman_reference[aerobic_reference.index(value_10*10)]
        number_int = number_int - (10*value_10)
    if number_int != 0:
        roman_number = roman_number + roman_reference[aerobic_reference.index(number_int)]

    print(roman_number)


convert_aerobic_to_roman_fcn(800)
