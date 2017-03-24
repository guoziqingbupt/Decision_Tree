import math


def classCount(data):
    """
    obtain the number of objects that belongs to each class
    :param data: dataset that contains data objects, is a tuple: (obj_1, ..., obj_n)
    :return: a dictionary, {class_name: number, ...}
    """

    classRecord = {}

    for obj in data:
        classTag = obj["class"]
        if classTag not in classRecord:
            classRecord[classTag] = 1
        else:
            classRecord[classTag] += 1

    return classRecord


def getAttributeList(data):

    attributeList = []

    for key in data[0]:
        if key != "RID" and key != "class":
            attributeList.append(key)

    return attributeList


def info(data):
    """
    calculate the entropy of dataset
    :param data: dataset that contains data objects, is a tuple: (obj_1, ..., obj_n)
    :return: the entropy of dataset
    """

    classRecord = classCount(data)

    n = len(data)
    result = 0
    for classTag in classRecord:
        pi = classRecord[classTag] / n
        result += (-pi * math.log(pi, 2))

    return result


def infoForAttribute(dataSize, attributeValue_subset):
    """
    calculate the expectation of information if we split data with the attribute
    :param dataSize: the number of objects in dataset
    :param attributeValue_subset: a dictionary, as form as {attributeValue_1: subset_1,... }
    :return: the sum of weight x entropy
    """

    result = 0

    for subset in attributeValue_subset.values():

        weight = len(subset) / dataSize
        result += weight * info(subset)

    return result


def dataPartition(data, attribute):
    """
    Partitioning the data according to an attribute
    :param data: dataset that contains data objects, is a tuple: (obj_1, ..., obj_n)
    :param attribute: an attribute
    :return: a dictionary attributeValue_subset, as form as {attributeValue_1: subset_1,... }
    """

    attributeValue_subset = {}

    for obj in data:

        attributeValue = obj[attribute]

        if attributeValue not in attributeValue_subset:
            attributeValue_subset[attributeValue] = [obj]
        else:
            attributeValue_subset[attributeValue].append(obj)

    for key in attributeValue_subset:
        attributeValue_subset[key] = tuple(attributeValue_subset[key])

    return attributeValue_subset


def selectAttribute(data, attributeList):
    """

    :param data:
    :param attributeList:
    :return: the attribute that denotes the split criterion
    """

    attributeValue_subset = dataPartition(data, attributeList[0])
    dataSize = len(data)

    maxGain = info(data) - infoForAttribute(dataSize, attributeValue_subset)
    result = attributeList[0]

    for attribute in attributeList[1:]:

        attributeValue_subset = dataPartition(data, attribute)
        temp = info(data) - infoForAttribute(dataSize, attributeValue_subset)

        if temp > maxGain:
            maxGain = temp
            result = attribute

    return result
