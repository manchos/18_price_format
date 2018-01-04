
def format_price(price):
    if isinstance(price, str):
        price = price.replace(',', '.')
    if is_validate_price(price):
        str_price = str(float(price))
        before_dot, after_dot = str_price.split('.')
        return '{}{}'.format(get_format_before_dot_str(before_dot), get_after_dot_str(after_dot))


def get_format_before_dot_str(before_dot_str, digits_amount_in_part=3):
    length = len(before_dot_str)
    if length > digits_amount_in_part:
        parts = len(before_dot_str) // digits_amount_in_part
        parts_list = list(range(parts + 1))
        for part in parts_list:
            parts_list[parts] = before_dot_str[length - digits_amount_in_part:length]
            parts = parts - 1
            if parts != 0:
                length = length - digits_amount_in_part
        parts_list[0] = before_dot_str[:length]
        return ' '.join(parts_list)
    else:
        return before_dot_str


def get_after_dot_str(str_after_dot):
    if int(str_after_dot) == 0:
        return ''
    return '.{}'.format(str_after_dot)


def is_validate_price(price):
    try:
        float(price)
    except (ValueError, TypeError):
        return False
    return True


if __name__ == '__main__':
    price = input('Enter the price to process: ')
    try:
        formatted_price = format_price(price)
    except ValueError as error:
        print(error)
    else:
        print(formatted_price)
