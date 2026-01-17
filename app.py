import sys
if len(sys.argv)==2:
    text=sys.argv[1]
    print("the text is :",text)
    res=text[::-1]
    print("the reversed string is :",res)
else:
    print("the defult values can be take")