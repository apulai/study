def minimumConcat(source, target):
    # Put your code here
    # map = new Map();

    # We will generate all substrings
    # These will placed in a dictionary like word:length
    # We will always take out words from the dictionary and try to delete 1 letter from it at each postion
    # if the new word is not in the dict yet we will add it
    # we are finished once no new additions made

    def flatten(lis):
        for item in lis:
            if isinstance(item, Iterable) and not isinstance(item, basestring):
                for x in flatten(item):
                    yield x
            else:
                yield item

    dict = {source: len(source)}
    couldaddnewword = True
    while couldaddnewword == True:
        couldaddnewword = False
        # list(dict)
        # if we are not using this form we will get a dictionary changed during iteration
        for word in list(dict):
            for i in range(len(word)):
                newword = word[:i] + word[i + 1:]
                if newword not in dict:
                    dict[newword] = len(newword)
                    couldaddnewword = True

    dict.pop('')
    print("List of substrings (total {}) - substing:substring length".format(len(dict)))
    print(dict)

    replacements = 0

    list1 = [target]
    summary={}

    for i in sorted(dict.items(), key=lambda x: (-x[1], x[0])):
        # print(i,i[0])
        j = 0
        db = 0

        while (j < len(list1)):
            list3 = list(list1)
            item = list1[j]
            list2 = item.split(i[0], 1);
            if (len(list2) > 1 ):
                del list1[j]
                for k in range(len(list2)):
                    if (not list2[k] == ""):
                        list1.insert(j + k, list2[k])
                replacements += 1
                db += 1
                if( i[0] not in summary):
                    summary[i[0]]=1
                else:
                    summary[i[0]]=summary[i[0]]+1
                j=0
                print("{} x {} {}->{} ".format(db, i[0], list3, list1))
            else:
                j = j + 1
        # print(target)
    print("v1: Used substings {} Number of different strings: {} Number of replacements:{}".format(summary, len(summary), replacements))

    if (len(list1) > 0):
        return -1
    else:
        return replacements


# source = input()
# target = input()
# source="abcd"
# target="abcbdabcdd"
source = "mafla"
target = "almafaalmafaalmafaalmaalmafafafa"
rv = minimumConcat(source, target)
if rv != -1:
    print("To create {} from {} we will need {} substrings of {}".format(target, source, rv, source))
else:
    print("It is not possible to create {} from {}".format(target, source))
print("")

source = "axc"
target = "ahbgdc"
rv = minimumConcat(source, target)
if rv != -1:
    print("To create {} from {} we will need {} substrings of {}".format(target, source, rv, source))
else:
    print("It is not possible to create {} from {}".format(target, source))
print("")

source = "abc"
target = "abcabcabc"
# expect true
rv = minimumConcat(source, target)
if rv != -1:
    print("To create {} from {} we will need {} substrings of {}".format(target, source, rv, source))
else:
    print("It is not possible to create {} from {}".format(target, source))
print("")

source = "acb"
target = "ahbgdc"
# expect true
rv = minimumConcat(source, target)
if rv != -1:
    print("To create {} from {} we will need {} substrings of {}".format(target, source, rv, source))
else:
    print("It is not possible to create {} from {}".format(target, source))
print("")


