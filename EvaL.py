def evalexpn(exp):
    s=[]
    i=0
    while i<len(exp):
        if exp[i].isdigit():
            n=int(exp[i])
            i=i+1
            while i<len(exp) and exp[i].isdigit():
                n=n*10+int(exp[i])
                i=i+1
            s.append(n)
        elif exp[i] =="+":
            s.append("+")
            i=i+1
        elif exp[i]=="-":
            s.append("-")
            i=i+1
        elif exp[i]=="*":
            s.append("*")
            i=i+1
        elif exp[i]=="/":
            s.append("/")
            i=i+1
        else:
            i=i+1
    res=s[0]
    for i in range(1,len(s),2):
        if i!=len(s)-1:
            if s[i]=="+":
                res+=s[i+1]
            elif s[i]=="-":
                res-=s[i+1]
            elif s[i]=="*":
                res*=s[i+1]
            elif s[i]=="/":
                res/=s[i+1]
    return res

exp=input("enter the valid expression")
val=evalexpn(exp)
print("the evaluate expression: ",val)
