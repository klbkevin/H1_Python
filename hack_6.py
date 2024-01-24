"""
loop: for [] output => [0,1,2,3,4,5]
"""

def fn_hack_6():
    output = []
    for i in range(6):
        output.append(i)
    #...
    return output  

P = fn_hack_6()
print (P)