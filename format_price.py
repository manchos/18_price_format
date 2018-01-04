
def format_price(price):
    if isinstance(price, str):
        price = price.replace(',', '.')
    if price_validate(price):
        str_price = str(float(price))
        before_dot, after_dot = str_price.split('.')
        return '{}{}'.format(get_before_dot_str(before_dot), get_str_after_dot(after_dot))


def get_before_dot_str(str_before_dot):
    length = len(str_before_dot)
    if length > 3:
        parts = len(str_before_dot) // 3
        parts_list = list(range(0, parts+1))
        for i in parts_list:
            parts_list[parts] = str_before_dot[length-3:length]
            parts = parts-1
            if parts != 0:
                length = length-3
        parts_list[0] = str_before_dot[:length]
        return ' '.join(parts_list)
    else:
        return str_before_dot


def get_str_after_dot(str_after_dot):
    if int(str_after_dot) == 0:
        return ''
    return '.{}'.format(str_after_dot)


def price_validate(price):
    try:
        float(price)
    except (ValueError, TypeError):
        return False
    return True


if __name__ == '__main__':
    price = input('Enter the price to process (e.g. "3245.000000"): ')
    try:
        formatted_price = format_price(price)
    except ValueError as error:
        print(error)
    else:
        print(formatted_price)