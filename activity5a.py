def main():
    print(getTitle())

    names = ['mary', 'mary', 'bill', 'sam', 'maria', 'kahn', 'bill', 'barry', 'george', 'hank', 'belinda', 'maria',
             'karthik']

    sortedNames = sortList(names)
    print("Initial List of Names:\n" + sortedNames)

    final = removeDuplicates(sortedNames)


def getTitle():
    return "Activity 5 List Deduplicator Function"


def sortList(names):

    sortedNames = names.sort()
    return sortedNames


def removeDuplicates(names):

    final = []

    for x in names:
        for y in final:
            if x


    return final