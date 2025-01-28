def find_smallest(x, y, z):
    if x < y:
        if x < z :
            return x
    if y < z:
        return y
    return z

result = find_smallest(50, 43, 100)
print("the smallest number out of three: ", result)

def find_smallest(x, y, z):
    if x<y and x<z:
        return x
    elif y<x and y<z:
        return y
    elif z<x and z<y:
        return z

result = find_smallest(30, 23, 60)
print("the smallest number out of three: ", result)


def custom_sheep_call(vowel, count):
    #print B
    print("B", end = "")
    #for loop that runs count times
    for i in range(count):
        #print vowel
        print(vowel, end = "")
        
print(custom_sheep_call("E", 10))
#call it

def sum_even_number(max_num):
    #add variable
    Ahhhhh = 0
    for i in range(1, max_num):
        #check if even (%2==0)
        if i%2==0:
            Ahhhhh +=i
            #add to variable
    return Ahhhhh 
        
#call it
print(" ", sum_even_number(8))