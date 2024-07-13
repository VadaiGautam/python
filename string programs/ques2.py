''' Python dictionary keys() function is used to return a new view object that contains a list of all the keys in the dictionary. The Python dictionary keys() method returns an object that contains all the keys in a dictionary.'''
def st(str1):
    dict = {}

    for n in str1:
    
        key = dict.keys()   
        # print(key)
        if n in key:
            dict[n] = dict[n]+1
            # print(dict[n])
        else:
            dict[n]=1
            # print(dict[n])
    return dict
print(st('google.com'))




