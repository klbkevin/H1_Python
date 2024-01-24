"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    RR=[]
    text=[]
    result = "fooziman"
    text.append(result.replace("fooziman","F00Z1M@N"))
    RR=list(text[0])
    
    return RR

P = fn_hack_10()
print (P) 