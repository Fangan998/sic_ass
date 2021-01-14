def _hex_(add):
    a = add
    
    return a

    
from pass_one import optab,LOCCTR,start,sym
length = hex(int(LOCCTR,16) - int(start,16))

objpgm = open('objectProgram.txt','w')
inter =open('intermediate.txt','r')
systab = open('symbolTab.txt','r')

l = []
addrlist = []

for i in inter.readlines():
    
    list_1 = i.strip().split()
    add = list_1[0][2:]
    if add !='-':
        addrlist.append(add)
    label=list_1[1]
    opcode = list_1[2]
    if len(list_1) == 4:
        operand = list_1[3]

    if (list_1[2]== "START" ):
        objpgm.write(i)
    elif (list_1[2]=='END'):
        objpgm.write(i)
    else:
        objpgm.write(i)

  
objpgm.close()
inter.close()
systab.close()
