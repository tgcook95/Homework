def main():
    print(getTitle())

    names = ['mary', 'mary', 'bill', 'sam', 'maria', 'kahn', 'bill', 'barry', 'george', 'hank', 'belinda', 'maria',
             'karthik']

    sortedNames = sortList(names)
    sortedString = str(sortedNames)
    print("Initial List of Names:\n" + sortedString)

    final = removeDuplicates(sortedNames)

    finalString = str(final)
    print("List of unique names after running through the de-duplicator program:\n" + finalString)


def getTitle():
    return "Activity 5 List Deduplicator Function"

#comment
def sortList(names):

    sortedNames = names.sort()
    return sortedNames


def removeDuplicates(names):

    final = []

    for x in names:
        if x not in final:
            final.append(x)

    return final

main()