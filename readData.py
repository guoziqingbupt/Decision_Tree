import csv


def readData(fileName):
    """
    read the csv data into a dictionary
    :param fileName:
    :return: a dictionary, as form as {TID: [items list]}
    """

    with open(fileName) as csvFile:

        data = []

        dict_reader = csv.DictReader(csvFile)

        for row in dict_reader:
            data.append(row)

    return tuple(data)
