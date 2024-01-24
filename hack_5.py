"""
text: "fooziman" output => "f00z1m@n"
"""

def fn_hack_5():
    result = "fooziman"
    res = ""
    for c in result:
        if c.islower():
            if c == "o":
                res += "0"
            elif c == "i":
                res += "1"
            elif c == "a":
                res += "@"
            else:
                res += c.lower()   
    #...
    return res

P = fn_hack_5()
print (P)



