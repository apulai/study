def minimumConcat(source, target):
    # Put your code here
    #map = new Map();

    # We will generate all substrings
    # These will placed in a dictionary like word:length
    # We will always take out words from the dictionary and try to delete 1 letter from it at each postion
    # if the new word is not in the dict yet we will add it
    # we are finished once no new additions made


    dict = {source:len(source)}
    couldaddnewword = True
    while couldaddnewword== True:
        couldaddnewword=False
        # list(dict)
        # if we are not using this form we will get a dictionary changed during iteration
        for word in list(dict):
            for i in range(len(word)):
                newword = word[:i]+word[i+1:]
                if newword not in dict:
                    dict[newword]=len(newword)
                    couldaddnewword = True

    dict.pop('')
    print(dict)

    replacements=0
    for i in sorted(dict.items(), key=lambda x: (-x[1],x[0])):
        #print(i,i[0])
        db=0
        while i[0] in target:
            newtarget=target.replace(i[0]," ",1)
            replacements += 1
            db += 1
            target=newtarget
            print("{} x {} {}->{} ".format(db, i[0], target, newtarget))
        #print(target)

    #remove all spaces
    target=target.replace(" ","")
    if( len(target) > 0):
        return -1
    else:
        return replacements

#source = input()
#target = input()
#source="abcd"
#target="abcbdabcdd"
source="mafla"
target="almafaalmafaalmafaalmaalmafafafa"
rv=minimumConcat(source, target)
if rv!=-1:
    print("To create {} from {} we will need {} substrings of {}".format(target,source,rv,source))
else:
    print("It is not possible to create {} from {}".format(target,source))
print("")

source="axc"
target="ahbgdc"
rv=minimumConcat(source, target)
if rv!=-1:
    print("To create {} from {} we will need {} substrings of {}".format(target,source,rv,source))
else:
    print("It is not possible to create {} from {}".format(target,source))
print("")

source="abc"
target="abcabcabc"
#expect true
rv=minimumConcat(source, target)
if rv!=-1:
    print("To create {} from {} we will need {} substrings of {}".format(target,source,rv,source))
else:
    print("It is not possible to create {} from {}".format(target,source))
print("")

source="acb"
target="ahbgdc"
#expect true
rv=minimumConcat(source, target)
if rv!=-1:
    print("To create {} from {} we will need {} substrings of {}".format(target,source,rv,source))
else:
    print("It is not possible to create {} from {}".format(target,source))
print("")


