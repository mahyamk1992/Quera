
"""
TEXTLANG

Second exercise at Quera.ir website

May 2018

MMK
"""

"""
مسابقه شماره ۲۵ براساس APL

id : 17245

"""

def identify_character_firstline(argument):
    switcher={
        '****' : 'T',
        'oo*o' : 'A',
        '**o*' : 'M',
        '*ooo' : 'or'
    }
    return switcher.get(argument,"nothing")


def identify_character_secondline(argument2):
    switcher={

        'oo' : 'X',
        '*o' : 'N'
    }
    return switcher.get(argument2,"nothing")


contents=[]

num_line=0
while num_line<3:
    line=input()
    num_line+=1
    contents.append(line)
    if num_line==1:
        firstline=line
    elif num_line==2:
        secondline=line



wordc=len(firstline)//5



str=""

if __name__ == "__main__" :
    for i in range(wordc):
             argument=firstline[i*5:i*5+4]
             output=identify_character_firstline(argument)
             if output == 'or':
                 argument2=secondline[i*5:i*5+2]
                 output=identify_character_secondline(argument2)
             str=str+output




print(str)






