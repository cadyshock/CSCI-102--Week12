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

def ScoreFinder(lis1,lis2,string):
    for i in lis1:
        if i.lower() == string:
            player_number=lis1.index(i)
    try:
        score=lis2[player_number]
        player=lis1[player_number]
        print('OUTPUT %s got a score of %d' % (player,score))
    except:
        print('OUTPUT player not found')

def Union(lis1,lis2):
    for i in lis1:
        for item in lis2:
            if i == item:
                while lis1.count(i) > 0:
                    lis1.remove(i)
    lis3=lis1+lis2
    return lis3

def Intersection(lis1,lis2):
    repeat=[]
    for i in lis1:
        for item in lis2:
            if i == item:
                repeat.append(i)
    return repeat

def NotIn(lis1,lis2):
    for i in lis1:
        print (i)
        for item in lis2:
            print('d',item)
            if i == item:
                while lis2.count(i) > 0:
                    lis2.remove(i)
    return lis2
            
    

