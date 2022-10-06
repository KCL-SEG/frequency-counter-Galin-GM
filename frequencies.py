"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):

    stringItems = [];

    for i in items:
        stringItems.append(str(i));

    frequencies = {}
    alreadyChecked = [];
    repetitions = 0;

    for i in stringItems:

        if not(i in alreadyChecked):
            repetitions = stringItems.count(i);
            alreadyChecked.append(i);
            frequencies[i] = repetitions;

    print(frequencies);
    # Your code goes here
    return frequencies


#frequencies(["a","c","a","d", 4, 4, '4']);
