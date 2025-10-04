def convert_temperature(temp, unit):
    if unit == 'C':
        f = (temp * 9/5) + 32
        k = temp + 273.15
        return {'F': f, 'K': k}
    elif unit == 'F':
        c = (temp - 32) * 5/9
        k = c + 273.15
        return {'C': c, 'K': k}
    elif unit == 'K':
        c = temp - 273.15
        f = (c * 9/5) + 32
        return {'C', 'F': f}
    else:
        return 'Unsupported unit'

def main():
    data = [
        (100, 'C'),
        (32, 'F'),
        (300, 'K'),
        (40, 'X')
    ]
    for temp, unit in data:
        result = convert_temperature(temp, unit)
        print(f'Input: {temp}°{unit} -> Output: {result}')


if name == "main":
    main()
