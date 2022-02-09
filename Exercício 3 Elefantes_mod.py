def incomodam(n,x=None):
    if x==None:
        x=1
    if type(n)!=int:
        return ""
    else:
        if n==1:
            return x*"incomodam "
        else:
            x=x+1
            n=n-1          
            return incomodam(n,x) 

def elefantes(n,x=None):

    if x==None:
        x=1

    if n<=1:
        h=''
        return h

    if n==2:
        h="Um elefante incomoda muita gente\n" + str(x+1) + " elefantes " + incomodam(x+1) + "muito mais"
        return h
   
    if x==n-1:
        h=str(x)+ " elefantes incomodam muita gente\n" + str(x+1)+ " elefantes " + incomodam(x+1)+ "muito mais"
        return h

    else:
        if x==1:
            h="Um elefante incomoda muita gente\n" + str(x+1) + " elefantes " + incomodam(x+1) + "muito mais\n"
            x=x+1
            return h + str(elefantes(n,x))

        if x>1:
            h=str(x)+ " elefantes incomodam muita gente\n" + str(x+1)+ " elefantes " + incomodam(x+1)+ "muito mais\n"
            x=x+1
            return h + str(elefantes(n,x))

        
