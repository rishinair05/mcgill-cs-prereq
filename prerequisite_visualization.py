import pickle
import pandas as pd
from pyvis.network import Network

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

with open('./CS_Courses.pkl', 'rb') as df_file:
    df = pickle.load(df_file)

null_value = df.loc[1]['prerequisites']

no_prereq = [0, 2, 3, 6]

for i in range(len(df.index)):
    if df.loc[i]['prerequisites'] == null_value:
        no_prereq.append(i)

df2 = df.drop(index=no_prereq)
df2.reset_index(drop=True, inplace=True)

net = Network(height="750px", width="100%", bgcolor="#222222", font_color="white", directed=True, select_menu=True, cdn_resources='remote')

course_names = []
for i in range(len(df2)):
    if i == 15:
        net.add_node("COMP 361D1", label="COMP 361D1")
        course_names.append("COMP 361D1")
    elif i == 16:
        net.add_node("COMP 361D2", label="COMP 361D2")
        course_names.append("COMP 361D2") 
    elif i == 23:
        net.add_node("COMP 402D1", label="COMP 402D1")
        course_names.append("COMP 402D1")
    elif i == 24:
        net.add_node("COMP 402D2", label="COMP 402D2")
        course_names.append("COMP 402D2")
    elif i == 66:
        net.add_node("COMP 601D2", label="COMP 601D2")
        course_names.append("COMP 601D2")
    elif i == 67:
        net.add_node("COMP 601N2", label="COMP 601N2")
        course_names.append("COMP 601N2")
    elif i == 69:
        net.add_node("COMP 616D2", label="COMP 616D2")
        course_names.append("COMP 616D2")
    elif i == 70:
        net.add_node("COMP 616N2", label="COMP 616N2")
        course_names.append("COMP 616N2")
    elif i == 71:
        net.add_node("COMP 700D2", label="COMP 700D2")
        course_names.append("COMP 700D2")
    else:
        net.add_node(df2.loc[i]['course code'][:8], label=df2.loc[i]['course code'][:8])
        course_names.append(df2.loc[i]['course code'][:8])



course_names.append("COMP 202")
course_names.append("MATH 235")
course_names.append("MATH 240")
course_names.append("MATH 318")
course_names.append("COMP 230")
course_names.append("PHIL 210")
course_names.append("COMP 273")
course_names.append("COMP 208")
course_names.append("MATH 222")
course_names.append("MATH 223")
course_names.append("MATH 362")
course_names.append("COMP 361D1")
course_names.append("BIOL 200")
course_names.append("15 Computer Science credits.")
course_names.append("9 credits of COMP courses and 9 credits of BIOL courses.")
course_names.append("ECSE 427")
course_names.append("ECSE 321",)
course_names.append("MATH 323",)
course_names.append("MATH 203")
course_names.append("BIOL 309",)
course_names.append("ECSE 305",)
course_names.append("ECSE 205",)
course_names.append("MATH 350",)
course_names.append("MATH 454",)
course_names.append("MATH 487")
course_names.append("MATH 462")
course_names.append("MATH 324")
course_names.append("ECSE 551",)
course_names.append("BIOL 202",)
course_names.append("BIOL 302",)
course_names.append("MATH 417",)
course_names.append("COMP 601D1",)
course_names.append("COMP 601N1",)
course_names.append("COMP 435",)
course_names.append("COMP 616D1",)
course_names.append("COMP 616N1",)
course_names.append("")
course_names.append("COMP 526")
course_names.append("ECSE 526",)
course_names.append("COMP 700D1")

net.add_node("COMP 202", "COMP 202") #82
net.add_node("MATH 235", "MATH 235", color='red') #83
net.add_node("MATH 240", "MATH 240", color='red') #84
net.add_node("MATH 318", "MATH 318", color='red') #85
net.add_node("COMP 230", "COMP 230") #86
net.add_node("PHIL 210", "PHIL 210", color='yellow') #87
net.add_node("COMP 273", "COMP 273") #88
net.add_node("COMP 208", "COMP 208") #89
net.add_node("MATH 222", "MATH 222", color='red') #90
net.add_node("MATH 223", "MATH 223", color='red') #91
net.add_node("MATH 362", "MATH 362", color='red') #92
net.add_node("COMP 361D1", "COMP 361D1") #93
net.add_node("BIOL 200", "BIOL 200", color='blue') #94
net.add_node("15 Computer Science credits.", "15 Computer Science credits.", color='black') #95
net.add_node("9 credits of COMP courses and 9 credits of BIOL courses.", "9 credits of COMP courses and 9 credits of BIOL courses.", color='black') #96
net.add_node("ECSE 427", "ECSE 427", color='green') #97
net.add_node("ECSE 321", "ECSE 321", color='green') #98
net.add_node("MATH 323", "MATH 323", color='red') #99
net.add_node("MATH 203", "MATH 203", color='red') #100
net.add_node("BIOL 309", "BIOL 309", color='blue') #101
net.add_node("ECSE 305", "ECSE 305", color='green') #102
net.add_node("ECSE 205", "ECSE 205", color='green') #103
net.add_node("MATH 350", "MATH 350", color='red') #104
net.add_node("MATH 454", "MATH 454", color='red') #105
net.add_node("MATH 487", "MATH 487", color='red') #106
net.add_node("MATH 462", "MATH 462", color='red') #107
net.add_node("MATH 324", "MATH 324", color='red') #108
net.add_node("ECSE 551", "ECSE 551", color='green') #109
net.add_node("BIOL 202", "BIOL 202", color='blue') #110
net.add_node("BIOL 302", "BIOL 302", color='blue') #111
net.add_node("MATH 417", "MATH 417", color='red') #112
net.add_node("COMP 601D1", "COMP 601D1") #113
net.add_node("COMP 601N1", "COMP 601N1") #114
net.add_node("COMP 435", "COMP 435") #115
net.add_node("COMP 616D1", "COMP 616D1") #116
net.add_node("COMP 616N1", "COMP 616N1") #117
#118 is blank
net.add_node("COMP 526", "COMP 526") #119
net.add_node("ECSE 526", "ECSE 526", color='green') #120
net.add_node("COMP 700D1", "COMP 700D1") #121


net.add_edge(course_names[1], course_names[0], color='yellow')
net.add_edge(course_names[82], course_names[0], color='yellow')
net.add_edge(course_names[82], course_names[1], color='white')
net.add_edge(course_names[1], course_names[2], color='white')
net.add_edge(course_names[83], course_names[2], color='yellow')
net.add_edge(course_names[84], course_names[2], color='yellow')
net.add_edge(course_names[1], course_names[3], color='white')
net.add_edge(course_names[83], course_names[3], color='yellow')
net.add_edge(course_names[84], course_names[3], color='yellow')
net.add_edge(course_names[1], course_names[4], color='white')
net.add_edge(course_names[83], course_names[4], color='yellow')
net.add_edge(course_names[84], course_names[4], color='yellow')
net.add_edge(course_names[85], course_names[4], color='yellow')
net.add_edge(course_names[86], course_names[4], color='yellow')
net.add_edge(course_names[87], course_names[4], color='yellow')
net.add_edge(course_names[0], course_names[5], color='white')
net.add_edge(course_names[1], course_names[5], color='white')
net.add_edge(course_names[0], course_names[6], color='white')
net.add_edge(course_names[88], course_names[7], color='white')
net.add_edge(course_names[88], course_names[8], color='white')
net.add_edge(course_names[0], course_names[9], color='white')
net.add_edge(course_names[1], course_names[10], color='white')
net.add_edge(course_names[0], course_names[10], color='yellow')
net.add_edge(course_names[89], course_names[10], color='yellow')
net.add_edge(course_names[2], course_names[11], color='white')
net.add_edge(course_names[1], course_names[12], color='white')
net.add_edge(course_names[84], course_names[12], color='white')
net.add_edge(course_names[90], course_names[13], color='white')
net.add_edge(course_names[91], course_names[13], color='white')
net.add_edge(course_names[82], course_names[13], color='yellow')
net.add_edge(course_names[89], course_names[13], color='yellow')
net.add_edge(course_names[1], course_names[13], color='yellow')
net.add_edge(course_names[2], course_names[14], color='yellow')
net.add_edge(course_names[3], course_names[14], color='yellow')
net.add_edge(course_names[83], course_names[14], color='blue')
net.add_edge(course_names[84], course_names[14], color='blue')
net.add_edge(course_names[92], course_names[14], color='blue')
net.add_edge(course_names[0], course_names[15], color='white')
net.add_edge(course_names[1], course_names[15], color='white')
net.add_edge(course_names[93], course_names[16], color='white')
net.add_edge(course_names[3], course_names[17], color='white')
net.add_edge(course_names[94], course_names[18], color='white')
net.add_edge(course_names[0], course_names[19], color='white')
net.add_edge(course_names[1], course_names[19], color='white')
net.add_edge(course_names[95], course_names[20], color='white')
net.add_edge(course_names[2], course_names[21], color='white')
net.add_edge(course_names[96], course_names[21], color='white')
net.add_edge(course_names[96], course_names[22], color='white')
net.add_edge(course_names[96], course_names[23], color='white')
net.add_edge(course_names[96], course_names[24], color='white')
net.add_edge(course_names[2], course_names[25], color='white')
net.add_edge(course_names[4], course_names[25], color='white')
net.add_edge(course_names[8], course_names[25], color='yellow')
net.add_edge(course_names[97], course_names[25], color='yellow')
net.add_edge(course_names[2], course_names[26], color='white')
net.add_edge(course_names[91], course_names[26], color='white')
net.add_edge(course_names[98], course_names[26], color='yellow')
net.add_edge(course_names[0], course_names[26], color='yellow')
net.add_edge(course_names[0], course_names[27], color='white')
net.add_edge(course_names[2], course_names[27], color='white')
net.add_edge(course_names[4], course_names[27], color='white')
net.add_edge(course_names[0], course_names[28], color='yellow')
net.add_edge(course_names[98], course_names[28], color='yellow')
net.add_edge(course_names[99], course_names[28], color='white')
net.add_edge(course_names[2], course_names[28], color='white')
net.add_edge(course_names[1], course_names[29], color='white')
net.add_edge(course_names[84], course_names[29], color='white')
net.add_edge(course_names[2], course_names[30], color='white')
net.add_edge(course_names[90], course_names[30], color='white')
net.add_edge(course_names[91], course_names[30], color='white')
net.add_edge(course_names[99], course_names[30], color='white')
net.add_edge(course_names[2], course_names[31], color='white')
net.add_edge(course_names[99], course_names[31], color='white')
net.add_edge(course_names[100], course_names[31], color='yellow')
net.add_edge(course_names[101], course_names[31], color='yellow')
net.add_edge(course_names[8], course_names[32], color='white')
net.add_edge(course_names[2], course_names[32], color='white')
net.add_edge(course_names[91], course_names[33], color='white')
net.add_edge(course_names[99], course_names[33], color='white')
net.add_edge(course_names[0], course_names[33], color='white')
net.add_edge(course_names[1], course_names[33], color='white')
net.add_edge(course_names[88], course_names[34], color='white')
net.add_edge(course_names[4], course_names[34], color='white')
net.add_edge(course_names[2], course_names[35], color='white')
net.add_edge(course_names[91], course_names[35], color='white')
net.add_edge(course_names[5], course_names[35], color='yellow')
net.add_edge(course_names[16], course_names[35], color='yellow')
net.add_edge(course_names[4], course_names[36], color='white')
net.add_edge(course_names[11], course_names[36], color='white')
net.add_edge(course_names[2], course_names[37], color='white')
net.add_edge(course_names[11], course_names[37], color='white')
net.add_edge(course_names[4], course_names[38], color='white')
net.add_edge(course_names[5], course_names[39], color='white')
net.add_edge(course_names[11], course_names[40], color='white')
net.add_edge(course_names[98], course_names[41], color='yellow')
net.add_edge(course_names[5], course_names[41], color='yellow')
net.add_edge(course_names[16], course_names[41], color='yellow')
net.add_edge(course_names[8], course_names[42], color='yellow')
net.add_edge(course_names[97], course_names[42], color='yellow')
net.add_edge(course_names[14], course_names[43], color='yellow')
net.add_edge(course_names[13], course_names[43], color='yellow')
net.add_edge(course_names[14], course_names[44], color='yellow')
net.add_edge(course_names[17], course_names[44], color='yellow')
net.add_edge(course_names[99], course_names[44], color='white')
net.add_edge(course_names[90], course_names[45], color='white')
net.add_edge(course_names[91], course_names[45], color='white')
net.add_edge(course_names[99], course_names[45], color='white')
net.add_edge(course_names[99], course_names[46], color='yellow')
net.add_edge(course_names[102], course_names[46], color='yellow')
net.add_edge(course_names[2], course_names[46], color='blue')
net.add_edge(course_names[3], course_names[46], color='blue')
net.add_edge(course_names[99], course_names[47], color='yellow')
net.add_edge(course_names[103], course_names[47], color='yellow')
net.add_edge(course_names[102], course_names[47], color='yellow')
net.add_edge(course_names[104], course_names[48], color='yellow')
net.add_edge(course_names[17], course_names[48], color='yellow')
net.add_edge(course_names[17], course_names[49], color='yellow')
net.add_edge(course_names[104], course_names[49], color='yellow')
net.add_edge(course_names[105], course_names[49], color='yellow')
net.add_edge(course_names[106], course_names[49], color='yellow')
net.add_edge(course_names[17], course_names[50], color='yellow')
net.add_edge(course_names[104], course_names[50], color='yellow')
net.add_edge(course_names[5], course_names[51], color='white')
net.add_edge(course_names[90], course_names[52], color='white')
net.add_edge(course_names[91], course_names[52], color='white')
net.add_edge(course_names[0], course_names[52], color='white')
net.add_edge(course_names[1], course_names[52], color='white')
net.add_edge(course_names[2], course_names[53], color='white')
net.add_edge(course_names[90], course_names[53], color='white')
net.add_edge(course_names[91], course_names[53], color='white')
net.add_edge(course_names[90], course_names[54], color='white')
net.add_edge(course_names[91], course_names[54], color='white')
net.add_edge(course_names[0], course_names[54], color='white')
net.add_edge(course_names[1], course_names[54], color='white')
net.add_edge(course_names[2], course_names[55], color='white')
net.add_edge(course_names[99], course_names[55], color='yellow')
net.add_edge(course_names[100], course_names[55], color='yellow')
net.add_edge(course_names[101], course_names[55], color='yellow')
net.add_edge(course_names[107], course_names[56], color='yellow')
net.add_edge(course_names[30], course_names[56], color='yellow')
net.add_edge(course_names[47], course_names[56], color='red')
net.add_edge(course_names[90], course_names[56], color='red')
net.add_edge(course_names[91], course_names[56], color='red')
net.add_edge(course_names[108], course_names[56], color='red')
net.add_edge(course_names[109], course_names[56], color='yellow')
net.add_edge(course_names[31], course_names[57], color='white')
net.add_edge(course_names[110], course_names[58], color='yellow')
net.add_edge(course_names[111], course_names[58], color='yellow')
net.add_edge(course_names[108], course_names[58], color='white')
net.add_edge(course_names[30], course_names[58], color='blue')
net.add_edge(course_names[47], course_names[58], color='blue')
net.add_edge(course_names[14], course_names[59], color='white')
net.add_edge(course_names[91], course_names[59], color='white')
net.add_edge(course_names[59], course_names[60], color='yellow')
net.add_edge(course_names[112], course_names[60], color='yellow')
net.add_edge(course_names[5], course_names[62], color='white')
net.add_edge(course_names[28], course_names[62], color='yellow')
net.add_edge(course_names[47], course_names[62], color='yellow')
net.add_edge(course_names[2], course_names[63], color='white')
net.add_edge(course_names[99], course_names[63], color='white')
net.add_edge(course_names[108], course_names[63], color='white')
net.add_edge(course_names[113], course_names[66], color='white')
net.add_edge(course_names[114], course_names[67], color='white')
net.add_edge(course_names[27], course_names[68], color='white')
net.add_edge(course_names[115], course_names[68], color='yellow')
net.add_edge(course_names[42], course_names[68], color='yellow')
net.add_edge(course_names[32], course_names[68], color='yellow')
net.add_edge(course_names[116], course_names[69], color='white')
net.add_edge(course_names[117], course_names[70], color='white')
net.add_edge(course_names[2], course_names[72], color='white')
net.add_edge(course_names[4], course_names[72], color='white')
net.add_edge(course_names[99], course_names[73], color='white')
net.add_edge(course_names[108], course_names[73], color='white')
net.add_edge(course_names[13], course_names[73], color='white')
net.add_edge(course_names[44], course_names[74], color='white')
net.add_edge(course_names[44], course_names[75], color='white')
net.add_edge(course_names[28], course_names[76], color='yellow')
net.add_edge(course_names[119], course_names[76], color='yellow')
net.add_edge(course_names[120], course_names[76], color='yellow')
net.add_edge(course_names[14], course_names[76], color='blue')
net.add_edge(course_names[99], course_names[76], color='blue')
net.add_edge(course_names[102], course_names[76], color='blue')
net.add_edge(course_names[90], course_names[77], color='white')
net.add_edge(course_names[91], course_names[77], color='white')
net.add_edge(course_names[14], course_names[77], color='white')
net.add_edge(course_names[30], course_names[77], color='yellow')
net.add_edge(course_names[47], course_names[77], color='yellow')
net.add_edge(course_names[8], course_names[78], color='white')
net.add_edge(course_names[25], course_names[79], color='white')
net.add_edge(course_names[31], course_names[80], color='white')
net.add_edge(course_names[121], course_names[81], color='white')

net.show('prerequisites_new_id.html')
print(course_names)