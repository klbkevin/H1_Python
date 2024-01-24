"""
text: "fooziman" output => "foozimaN"
"""

def fn_hack_4():
    result = "fooziman"
    #...
    last_char = result[-1].upper()
    new_string = result[:-1] + last_char
    return new_string
P=fn_hack_4()
print (P)