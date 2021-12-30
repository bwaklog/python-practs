# pick max or min value in a list or tuple
def max_min():
    
    # WRITE CODE FROM HERE    
    lt = eval(input("Enter a list or a tuple : "))
    mm = input("Do you want Max(1) or Min(2) :")
    typ = "list" if type(lt) == list else "tuple"
    if mm == "1":
        return print("Maximum value of", typ, "is", max(lt))
    elif mm == 2:
        return print("Maximum value of", typ, "is", min(lt))
    else:
        return print("Invalid Operation")

# swap values in even positions with those in odd positions
def eo_swap():
    
    # WRITE CODE FROM HERE    
    l = list(eval(input("Enter a list with numbers : ")))
    eo = []
    for i in range(0, len(l), +2):
        if i == len(l) - 1:
            eo.append(l[i])
        else:
            eo.extend([l[i+1], l[i]])
    return eo

# search a string for a specific word and return its index
def search():
    
    # WRITE CODE FROM HERE    
    lt = eval(input("Enter a list or tuple : "))
    sr = input("Search element : ")
    indexes = []
    for i in range(len(lt)):
        if str(lt[i]) == sr:
            indexes.append(i)
    return print("The element", sr, "has indexes", indexes)

# print the squares of numbers from 1 to 10
def sqto10():
    
    # WRITE CODE FROM HERE
    return [x**2 for x in range(11)]

# return the first letter of each word in a string
def first_letter():
    # WRITE CODE FROM HERE
    string = input("Enter a string : ").split(' ')
    return [x[0] for x in string]

# Push the duplicate elements in a list to the very end
def punish():
    
    # WRITE CODE FROM HERE
    l = list(eval(input("Enter a list with elements : ")))
    d = {}
    ln = []
    for i in l:
        if i in d:
            d[i].append(i)
        else:
            d[i] = [i]
            ln.append(i)
    for j, value in d.items():
        if len(d[j]) > 1:
            d[j].pop()
            for k in value:
                ln.extend([k])
    return ln

# Return the indexes of the places where two similar lists differ
def differ():
    
    # WRITE CODE FROM HERE
    l1 = list(eval(input("Enter list 1 : ")))
    l2 = list(eval(input("Enter list 2 : ")))

    if len(l1) == len(l2):
        for i in range(0, len(l1), +1):
            if l1[i] != l2[i]:
                print("Differing point index :", i)

# Print name of student getting above 75
def above75(d=dict):
    # WRITE CODE FROM HERE
    
    cl = {'roll':[1, 2, 3, 4, 5], 'name':['Name1', 'Name2', 'Name3', 'Name4', 'Name5'],\
    'marks':[82, 75, 60, 90, 92]}
    for i in range(0, len(d['marks']), +1):
        if d['marks'][i] > 75:
            print(d['name'[i]])

# compare two dictionaries and check if they are similar or not
def chk_d(dict1, dict2):
    
    # WRITE CODE FROM HERE
    d1 = {1: [1, 4, 'Apple', 15.2], 2:"Banana", 3:True, 4:15+2j}
    d2 = {1:"Orange", 2:[[24, 12], 2, [1.0, 2E7]]}
    d3 = {1:"Banana", 2:True, 3:[1, 4, 'Apple', 15.2], 4:15+2j}
    lc = []
    l = []
    for i in dict1:
        l.append(dict1[i]):
        for j in dict2:
            if dict1[i] == dict2[j]:
                lc.append(dict2[j])
        if lc == l:
            return print("The two dictionaries are similar")
        else:
            return print("The two dictionaries are dissimilar")
        
# count the number of times a word occurs in a string
def count_occur():
    
    # WRITE CODE FROM HERE
    s = input("Enter a string : ").lower()
    chk = input("Word count of which word : ").lower()
    return print("The word", chk, "occurs in the string", s.count(chk), "times.")
