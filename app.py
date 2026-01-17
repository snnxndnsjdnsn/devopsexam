import sys
if len(sys.argv)==2:
    text=sys.argv[1]
    print("the text is :",text)
else:
    res=text[::-1]
    print("the reversed string is :",res)