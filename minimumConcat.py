def minimumConcat(source, target):
    # Put your code here
    #map = new Map();
    mydict = {}

    for i in range(len(source)):
        if(mydict(source[i])):
            arr=map(source[i])


    for (let i = 0; i < source.length; i++) {
    if (map.get(source[i])) {
    const arr = map.get(source[i]);
    arr.push(i);
    map.set(source[i], arr);
    } else {
    map.set(source[i], [i]);
    }
    }
    let
    occurrences = 0;
    for (let i = 0; i < target.length; i++) {
        const indexes = map.get(target[i]);
    if (indexes == = void 0)
    return -1;
    occurrences + +;
    let
    max = 0;
    indexes.forEach(index= > {
        let
    j = 0;
    let
    ignore = 0;
    while (source[index + j + ignore] !== void 0) {
    if (target[i + j] != = source[index + j + ignore]) {
    ignore++;
    } else {
    max = Math.max(max, j++);
    }
    }
    });
    i += max;
    }
    return occurrences;




#initial = input()
#goal = input()
initial="xyz"
goal="xytzxz"
minimumConcat(initial, goal)