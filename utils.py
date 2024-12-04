def read_txt(path, numbers=True):
    data = []
    if numbers:
        with open(path, "r") as file:
            for line in file:
                numbers = list(map(int, line.split()))
                data.append(numbers)
    else: 
        # will change this, works for day03
        with open(path, "r") as file:
            for line in file:
                data.append(line)
    return data