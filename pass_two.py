def _hex_(add):
    a = hex(int(add,16))
    
    return a

def __w_obj__(i,codenum):
    opd = i
    codenum = codenum
    w_string = f"{i}\t{codenum}\n"
    objpgm.write(w_string) 

from pass_one import optab,LOCCTR,start,sym
length = hex(int(LOCCTR,16) - int(start,16))

objpgm = open('objectProgram.txt','w')
inter =open('intermediate.txt','r')
systab = open('symbolTab.txt','r')

l = []
addrlist = []
tempstr1 = ""
tempstr = ""
operand={}
objpgm.write("sic ass\n")
for i in inter.readlines():
    j = i.strip()
    ls = i.strip().split()
    print(f"ls:{ls}")
    add = ls[0][2:]
    if add !='-':
        addrlist.append(add)
    label=ls[1]
    opcode = ls[2]
    if len(ls) == 4:
        operand = ls[3]

    if (ls[2]== "START" ):
        __w_obj__(i.strip(),"")
        print("i:"+i)
    elif (ls[2]=='END'):
        tempstr = i
        print (tempstr)
    else:
        if ls[2] in optab.keys():
            op = optab[ls[2]]
            if ls[2]=='RSUB':
                op += "0000"
                tempstr1 = op
                print(f"RSUB:{i.strip()} \t{op}")
            elif operand in sym.keys():
                op += sym[operand][2:]
                l.append(op)
                tempstr1 = op
                print(f"IN_SYM_KEY:{i.strip()} \t {op}")

            __w_obj__(j.strip(),tempstr1)

        elif ls[2]=="WORD":
            op = _hex_(operand)
            print("one for op: ",op)
            op1=str(op)
            op1=op1[2:]
            
            if op1 == "4096":
                tempstr1="001000"
                
            elif len(op1)<6:
                for i in range(7-len(op1)):
                    op="0"+op1
                print(f"WORD:i.strip()\t {op}")         
                l.append(op)
                tempstr1=op
            __w_obj__(j,tempstr1)

        elif ls[2]=="BYTE":

            temp =operand[2:len(operand)-1]
            if operand.find("C"):
                l.append(temp)
                tempstr1 = temp
                print(f"X:{i.strip()}\t{temp}")
                
            elif operand.find("X"):
                str1 = ""
                print("C_temp:",temp)
                for i in temp:
                    hexcode = hex(ord(i))
                    tmp = str(hexcode)
                    str1 += tmp[2:]
                l.append(str1)
                tempstr1 = str1
                print(f"C:{i.strip()}\t{str1}")

            __w_obj__(j,tempstr1)     
        else:
            l.append("-")
            print(f"{i.strip()} \t -")
            __w_obj__(j,"-")
        
'''         
j=0
while j<len(l):  
    objpgm.write("\t"+l[j]+"\n")
    j+=1
'''
objpgm.write(tempstr) 
objpgm.close()
inter.close()
systab.close()
