import random

def getCoeff():
    coeff=[]
    i = 1
    while i <= 21:
        coeff.append(i)
        i=i+1
    return random.choice(coeff)

def getConst():
    const=[]
    i = 1
    while i <= 21:
        if i!=11:
            const.append(-11+i)
        i=i+1
    return random.choice(const)

def getMathExpr(a,b):
    if b<0:
        c = ''
    else:
        c = '+'
    if a!=1 :
        result = ('('+str(a)+"x"+c+str(b)+')')
    else:
        result = ('('+"x"+c+str(b)+')')
    return result
n=3
fname="expr.html"
with open(fname, "w") as myfile:
                myfile.write("<head>\n<title>Question</title>\n</head>")
                myfile.write("<body>")
                myfile.write("<p>Express the following expressions as difference of two squares</p>")
                myfile.write("<ol>")
                for i in range(n):
                    u1 = 1
                    u2 = 2
                    v1 = 1
                    v2 = 2
                    while ((u1+u2)%2!=0 or (v1+v2)%2!=0):
                        u1 = getCoeff()
                        v1 = getConst()
                        u2 = getCoeff()
                        v2 = getConst()
                    myfile.write("<p>"+str(i+1)+'. '+getMathExpr(u1,v1)+getMathExpr(u2,v2)+"</p>")
                myfile.write("</ol>")
                myfile.write("<p>Simplify the following expressions</p>")
                myfile.write("<ol>")
                for i in range(n):
                    x = getMathExpr(getCoeff(),getConst())
                    y = getMathExpr(getCoeff(),getConst())
                    if i%2==0:
                        sign = '-'
                    else:
                        sign = '+'
                    myfile.write("<p>"+str(i+1)+'. '+x+"<sup>2</sup>"+sign+"2"+x+y+'+'+y+"<sup>2</sup>"+"</p>")
                myfile.write("</ol>")
                myfile.write("<p>Multiply the following expressions using the appropriate formulae</p>")
                myfile.write("<ol>")
                for i in range(n):
                    coeff = getCoeff()
                    const_1 = getConst()
                    const_2 = getConst()
                    if i%2==0:
                        myfile.write("<p>"+str(i+1)+'. '+getMathExpr(coeff,const_1)+getMathExpr(coeff,const_2)+"</p>")
                    else:
                        myfile.write("<p>"+str(i+1)+'. '+getMathExpr(coeff,const_1)+getMathExpr(coeff,-const_1)+"</p>")
                myfile.write("</ol>")
                myfile.write("</body>")