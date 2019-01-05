def main():
    print(getTitle())

    names = ['mary', 'mary', 'bill', 'sam', 'maria', 'kahn', 'bill', 'barry', 'george', 'hank', 'belinda', 'maria',
             'karthik']

    sortedNames = sortList(names)
    sortedString = str(sortedNames)
    print("\nInitial List of Names: ")
    print(sortedNames)

    final = removeDuplicates(sortedNames)

    finalString = str(final)
    print("\nList of unique names after running through the de-duplicator program:\n" + finalString)


def getTitle():
    return "Activity 5 List Deduplicator Function"

#comment
def sortList(names):

    names.sort()
    return names


def removeDuplicates(names):

    final = []

    for x in names:
        if x not in final:
            final.append(x)

    return final

main()