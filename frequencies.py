"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    alreadyChecked = [];
    repetitions = 0;

    for i in items:

        if not(i in alreadyChecked):
            repetitions = items.count(i);
            alreadyChecked.append(i);
            frequencies[i] = repetitions;
    

    # Your code goes here
    return frequencies


frequencies(["a","c","a","d"]);
