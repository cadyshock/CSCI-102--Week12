#Cady Shock
#CSCI 102- E
#Lab 12

def PrintOutput(string):
    print( 'OUTPUT ' + string)
def LoadFile(file):
    f=open(file,'r')
    final=[]
    for i in f:
        final.append(i)
    return final
def UpdateString(st1,st2,x):
    slist=list(st1)
    new=''
    slist[x]=st2
    for i in slist:
        new+=i
    return new
def FindWordCount(lis,string):
    count=0
    for i in lis:
        if i == string:
            count=count+1
    return count





            
    

