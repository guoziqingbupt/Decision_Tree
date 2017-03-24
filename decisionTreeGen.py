from attributeSelection import *
import copy


class DecisionTreeNode(object):

    def __init__(self):

        # tag is the class name
        self.tag = None

        self.isLeaf = True

        # pointers is a dictionary, {attributeValue: child, ...}
        self.pointers = {}

        # the best attribute that used to split dataset
        self.splitCriterion = None


def isSameClass(data):

    classRecord = classCount(data)
    return len(classRecord) == 1


def majorityVoting(data):

    classRecord = classCount(data)
    return max(classRecord.keys(), key=lambda x: classRecord[x])


def genDecisionTree(data, attributeList):
    """

    :param data: dataset that contains data objects, is a tuple: (obj_1, ..., obj_n)
    :param attributeList: a list that contains all attributes occurred in data
    :return: the root of decision tree
    """

    root = DecisionTreeNode()

    if isSameClass(data):

        root.tag = data[0]["class"]
        return root

    # majority voting
    if len(attributeList) == 0:

        root.tag = majorityVoting(data)
        return root

    # find the split criterion of root
    root.splitCriterion = selectAttribute(data, attributeList)
    root.isLeaf = False

    # Partitioning the data for several blocks
    # attributeValue_subset: a dictionary, {attributeValue: (data_object_1, data_object_2...)},
    # where data_object_i is also a dictionary: {attribute_1: value, attribute_2: value...}
    attributeValue_subset = dataPartition(data, root.splitCriterion)
    attributeList.remove(root.splitCriterion)

    for attributeValue in attributeValue_subset:

        child = DecisionTreeNode()
        subset = attributeValue_subset[attributeValue]

        if len(subset) == 0:
            child.tag = majorityVoting(data)
        else:
            attributeList_ForThisChild = copy.deepcopy(attributeList)
            child = genDecisionTree(subset, attributeList_ForThisChild)

        # pointers: a dictionary, as form as:
        # {"youth": child_1, "middle_aged": child_2, "senior": child_3}
        root.pointers[attributeValue] = child

    return root
