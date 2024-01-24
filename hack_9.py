"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    res = []
    for number in result:
        res.append(number)
        res.append('@')
    #...
    return res 
P = fn_hack_9()
print (P)