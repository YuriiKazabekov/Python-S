word = 'Found name:'  # String variable
ids = {'name':"Alice", 'age':27}  # Dict with user data

def intersection(word,name,*args,age=None): 
    print(word, name) # word and name neccessary arguments
    print('Age:',age) # age argument at the end of function arguments set
    print(args)       # collecting any arguments into one tuple

intersection(word, **ids)  # call function with word and ids data unpack
intersection(word, ids['name'], *list(range(10)))# call function with word and ids data and some list unpack
