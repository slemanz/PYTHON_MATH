def read_data(filename):
    numbers = []
    with open(filename) as f:
        for line in f:
            numbers.append(float(line))
    
    return numbers

def sum_numbers(numbers):
    s = 0
    for number in numbers:
            s = s + number
    
    return s

def calculate_mean(numbers):
    s = sum(numbers)
    N = len(numbers)
    mean = s/N

    return mean

if __name__ == '__main__':
    data = read_data('data.txt')
    print('Sum of the numbers: {0}'.format(sum_numbers(data)))

    mean = calculate_mean(data)
    print('Mean: {0}'.format(mean))
