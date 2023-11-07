#MENU DRIVEN PROGRAM
while True:
    print((10*('*')),'I N D E X',(10*('*')))
#table of content
    QWE=('1.Create a Copy of Dictionary\n2.Removing or Adding Values in Dictionary\n3.Merging of 2 dictionary\n4.Keys, Values and Length of dictionary')
    print(QWE.upper())
    print('5.Viewing Values of Fields\n6.Sum of Values in Dictionary')
#index input
    I=(int(input('  Enter the Topic You Want to Continue With: ')))
#program 1
    if I==1:
        print('1. Create a Copy of Dictionary')
        DIC={}
        a=int(input('Enter Number Of Fields Wanted:  '))
        for x in range(0,a):
            o=(input('Enter Key:  '))
            p=(input('Enter Value:  '))
            DIC[o]=p
        print('Original Dictionary',DIC)
        PICK=DIC.copy()
        print('Duplicate Dictionary Is:',PICK)
#program 2
    elif I==2:
        print('2. Removing or Adding Values in Dictionary')
        DIC={}
        a=int(input('Enter The Number Of field Needed: '))
        for x in range(0,a):
            n=input('Enter KEY:')
            p=input('Enter Value:')
            DIC[n]=p
            print('>>Press 1 to ADD \n >>Press 2 to UPDATE\n>>Press 3 To DELETE' )
        f=int(input('Enter Your Choice: '))
        if f== 1:
                e=input('Enter KEY: ')
                d=input('Enter VALUE: ')
                DIC=[e]=d
                print('Value Added')
                print('Updated Dictionary',DIC)
        
        if f== 2:
            v=input('Enter The Key To Be Updated: ')
            c=input('Enter The New Value: ')
            DIC[v]=c
            print('Key is updated with new value')
            print('Updated Dictionary',DIC)
        if f==3:
            e=input('Enter KEY to be Deleted')
            DIC.pop(e)
            print('Updated Dictionary',DIC)
#program 3
    elif I==3:
        print('3.Merging of 2 dictionary')
        f1=int(input('Enter The Number of Fields Required in First Dictionary: '))
        DIC1={}
        for x in range (0,f1):
            O=input('Enter Key : ')
            P=input('Enter Value: ')
            DIC1[O]=P
        DIC2={}
        f2=int(input('Enter The Number of Fields Required in First Dictionary: '))
        for y in range (0,f2):
            for x in range (0,f2):
                L=input('Enter Key : ')
                K=input('Enter Value: ')
                DIC2[L]=K
        DICT={}
        for x in (DIC1,DIC2):
            DICT.update(x)
        print(DICT)
#program 4
    elif I==4:
        print('4.Keys, Values and Length of dictionary')
        DIC={}
        j=int(input('Enter The Number Of Fields Required: '))
        for x in range (0,j):
            z=input('Enter Key : ')
            t=input('Enter Value: ')
            DIC[z.upper]=t.upper
        print(DIC)
        a=str(input('Enter The KEY Name: '))
        print(DIC[a])
        print(DIC.keys())
        print(DIC.values)
        print(len(DIC))
#program 5
    elif I==5:
        print('5.Viewing Values of Fields')
        a=int(input('Enter The Number of Fields Required: '))
        DIC={}
        for i in range(0,a):
            n=input("Enter Key: ")
            s=input("Enter Value: ")
            o=n.upper()
            DIC[o]=s
        print(DIC)
        z=int(input('Enter The Number Of Fields You need Values For:  '))
        if z>len[DIC]:
            print('Only ',len[DIC],'Values Present')
        elif z<=len[DIC] :
            for r in range(1,z) :
                b=str(input('Enter The Key: '))
                c=b.upper
                print('Value of Field=',DIC[c])
#program 6
    elif I==6:
        print('6.Sum of Values in Dictionary')
        l=[]
        DIC={}
        a=int(input('Enter The Number Of field Needed: '))
        for x in range(0,a):
            n=int(input('Enter KEY:'))
            p=int(input('Enter Value:'))
            l.append(p)
            DIC[n]=p
        print('Sum=',sum(l))
#incorrect value condition for dumbasses
    else:
        print('Value Of Of Index Range')
        print('     Press any Key to Restart')
        opi=input()