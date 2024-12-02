def read_txt(path):
    data = []
    with open(path, "r") as file:
        for line in file:
            numbers = list(map(int, line.split()))
            data.append(numbers)
    return data