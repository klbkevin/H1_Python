"""
text: "FOOZIMAN" output => "fooziman"
"""

def fn_hack_2():
    result = "FOOZIMAN"
    #...
    return result.swapcase()

P= fn_hack_2()
print(P)