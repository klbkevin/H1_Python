"""
text: "fooziman" output => "Fooziman"
"""

def fn_hack_3():
    result = "fooziman"
    #...
    return result.title()

P= fn_hack_3()
print (P)