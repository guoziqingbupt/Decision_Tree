from readData import *
from decisionTreeGen import *


def main(fileName):

    data = readData(fileName)

    attributeList = getAttributeList(data)

    return genDecisionTree(data, attributeList)


if __name__ == "__main__":

    root = main("data.csv")
    tempList = [root]

    while len(tempList) != 0:
        node = tempList.pop(0)

        if node.isLeaf:
            print(node.tag)
            print("------------------------")
        else:
            print(node.splitCriterion)
            for attributeValue in node.pointers:
                print(attributeValue)
                tempList.append(node.pointers[attributeValue])
            print("------------------------")
