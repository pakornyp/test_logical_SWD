def convert_number_to_thai_fcn(input_number):
    try:
        number_int = int(input_number)
        number_str = str(number_int)
    except ValueError:
        print("input must be a number (0 to 9999999)")
        return

    if number_str == "0":
        thai_text = "ศูนย์"
        print(thai_text)
        return
    else:
        count_digit = len(number_str)
        if count_digit > 7:
            print("input must not be lower than 10000000 (<10M)")
            return
        thai_pattern = ["", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"]
        digit_pattern = ["", "สิบ", "ร้อย", "พัน", "หมื่น", "แสน", "ล้าน", "สิบล้าน"]
        except_pattern = ["", "เอ็ด", "ยี่"]
        thai_text = ""
        for digit in range(count_digit):
            index = count_digit - digit - 1
            value = int(number_str[index])
            if value != 0:
                if value == 2 and digit == 1:
                    thai_text = except_pattern[value] + digit_pattern[digit] + thai_text
                elif value == 1 and digit == 0 and count_digit != 1:
                    thai_text = except_pattern[value] + digit_pattern[digit] + thai_text
                elif value == 1 and digit == 1:
                    thai_text = digit_pattern[digit] + thai_text
                else:
                    thai_text = thai_pattern[value] + digit_pattern[digit] + thai_text
    return thai_text
