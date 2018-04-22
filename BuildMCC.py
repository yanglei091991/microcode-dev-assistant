fp = open("config.xml", "w")

result = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MCCTree>\n"
fp.writelines(result)
#M
result = "<M>\n"
fp.writelines(result)

#MR0ToM R0.M['s|I++|S++']->M[t]{@('C|!C')}
m = ["s", "I++", "S++"]
c = ["", "@(C)", "@(!C)"]

result = "<MR0ToM>"

for i in m:
    for k in c:
	s = "R0.M[%s]->M[t]%s;" % (i, k)
	result += s
result = result[: -1]
result += "</MR0ToM>\n"
fp.writelines(result)
	    
#MR0ToMACC R0.M['s|I++|S++']->'IALU.T|IMAC.T|FALU.T|FMAC.T't(I'0|1|2'){@('C|!C')}
m = ["s", "I++", "S++"]
r = ["IALU", "IMAC", "FALU", "FMAC"]
n = ["I0", "I1", "I2"]
c = ["", "@(C)", "@(!C)"]

result = "<MR0ToMACC>"

for i in m:
    for j in r:
	for h in n:
	    for x in c:
		s = "R0.M[%s]->%s.Tt(%s)%s;" % (i, j, h, x)
		result += s	
result = result[: -1]
result += "</MR0ToMACC>\n"
fp.writelines(result)
		    
#MR0ToSHU R0.M['s|I++|S++']->'SHU0.T|SHU1.T't{@('C|!C')}
m = ["s", "I++", "S++"]
r = ["SHU0", "SHU1"]
c = ["", "@(C)", "@(!C)"]

result = "<MR0ToSHU>"

for i in m:
    for j in r:
	for x in c:
	    s = "R0.M[%s]->%s.Tt%s;" % (i, j, x)
	    result += s	
result = result[: -1]
result += "</MR0ToSHU>\n"
fp.writelines(result)

#MR1ToSHU R1.M['s|I++|S++']->'SHU0.T|SHU1.T't{@('C|!C')}
m = ["s", "I++", "S++"]
r = ["SHU0", "SHU1"]
c = ["", "@(C)", "@(!C)"]

result = "<MR1ToSHU>"

for i in m:
    for j in r:
	for x in c:
	    s = "R1.M[%s]->%s.Tt%s;" % (i, j, x)
	    result += s	
result = result[: -1]
result += "</MR1ToSHU>\n"
fp.writelines(result)

#MR1ToMACC R1.M['s|I++|S++']->'IALU.T|IMAC.T|FALU.T|FMAC.T't(I'0|1|2'){@('C|!C')}
m = ["s", "I++", "S++"]
r = ["IALU", "IMAC", "FALU", "FMAC"]
n = ["I0", "I1", "I2"]
c = ["", "@(C)", "@(!C)"]

result = "<MR1ToMACC>"

for i in m:
    for j in r:
	for h in n:
	    for x in c:
		s = "R1.M[%s]->%s.Tt(%s)%s;" % (i, j, h, x)
		result += s	
result = result[: -1]
result += "</MR1ToMACC>\n"
fp.writelines(result)

#MR2ToMACC R2.M[s]->'IALU.T|IMAC.T|FALU.T|FMAC.T't(I'0|1|2'){@('C|!C')}
r = ["IALU", "IMAC", "FALU", "FMAC"]
n = ["I0", "I1", "I2"]
c = ["", "@(C)", "@(!C)"]

result = "<MR2ToMACC>"

for j in r:
    for h in n:
	for x in c:
	    s = "R2.M[s]->%s.Tt(%s)%s;" % (j, h, x)
	    result += s	  
result = result[: -1]
result += "</MR2ToMACC>\n"
fp.writelines(result)

#MR2WToMACC R2.M[s](W'F1|F2|F3|X1|X2|X3|X4')->'IALU.T|IMAC.T|FALU.T|FMAC.T't(I'0|1|2') {@('C|!C')}
w = ["F1", "F2", "F3", "X1", "X2", "X3", "X4"]
r = ["IALU", "IMAC", "FALU", "FMAC"]
n = ["I0", "I1", "I2"]
c = ["", "@(C)", "@(!C)"]

result = "<MR2WToMACC>"

for y in w:
    for j in r:
	for h in n:
	    for x in c:
		s = "R2.M[s](W%s)->%s.Tt(%s)%s;" % (y, j, h, x)
		result += s	 
result = result[: -1]
result += "</MR2WToMACC>\n"
fp.writelines(result)

#MR3ToBIU {R3.}M[s]-> BIU'0|1|2'{@('C|!C')}
r = ["", "R3."]
b = range(0, 3)
c = ["", "@(C)", "@(!C)"]

result = "<MR3ToBIU>"

for i in r:
    for k in b:
	for h in c:
	    s = "%sM[s]->BIU%s%s;"%(i, k, h)
	    result += s
result = result[: -1]
result += "</MR3ToBIU>\n"
fp.writelines(result)

#MR3ToBIUKG {R3.}M[s]-> BIU'0|1|2'(KG){@('C|!C')}
r = ["", "R3."]
b = range(0, 3)
c = ["", "@(C)", "@(!C)"]

result = "<MR3ToBIUKG>"

for i in r:
    for k in b:
	for h in c:
	    s = "%sM[s]->BIU%s(KG)%s;"%(i, k, h)
	    result += s
result = result[: -1]
result += "</MR3ToBIUKG>\n"
fp.writelines(result)

#END M
result = "</M>\n"
fp.writelines(result)

#SHU
result = "<SHU>\n"
fp.writelines(result)

#SHUIndTToBIU SHU'0|1'.T'm|SQ|BB|BH|BW|BD' IND T'm|SQ|BB|BH|BW|BD'{(TB =+ imm3)}-> BIU'0|1|2'{@('C|!C')}
a = range(0, 2)
b = ["m", "SQ", "BB", "BH", "BW", "BD"]
c = ["m", "SQ", "BB", "BH", "BW", "BD"]
d = ["", "(TB =+ imm3)"]
e = range(0, 3)
f = ["", "@(C)", "@(!C)"]

result = "<SHUIndTToBIU>"

for i in a:
    for j in b:
	for k in c:
	    for h in d:
		for l in e:
		    for m in f:
		        s = "SHU%s.T%s IND T%s%s->BIU%s%s;"%(i, j, k, h, l, m) 
		        result += s
result = result[: -1]
result += "</SHUIndTToBIU>\n"
fp.writelines(result)

#SHUIndTToM SHU'0|1'.T'm|SQ|BB|BH|BW|BD' IND T'm|SQ|BB|BH|BW|BD'{(TB =+ imm3)}-> M[t] {@('C|!C')}
a = range(0, 2)
b = ["m", "SQ", "BB", "BH", "BW", "BD"]
c = ["m", "SQ", "BB", "BH", "BW", "BD"]
d = ["", "(TB =+ imm3)"]
f = ["", "@(C)", "@(!C)"]

result = "<SHUIndTToM>"

for i in a:
    for j in b:
	for k in c:
	    for h in d:
		for m in f:
		    s = "SHU%s.T%s IND T%s%s->M[t]%s;"%(i, j, k, h, m) 
		    result += s
result = result[: -1]
result += "</SHUIndTToM>\n"
fp.writelines(result)

#SHUIndTToMACC SHU'0|1'.T'm|SQ|BB|BH|BW|BD' IND T'm|SQ|BB|BH|BW|BD'{(TB =+ imm3)}->'IALU.T|IMAC.T|FALU.T|FMAC.T't(I'0|1|2') {@('C|!C')}
a = range(0, 2)
b = ["m", "SQ", "BB", "BH", "BW", "BD"]
c = ["m", "SQ", "BB", "BH", "BW", "BD"]
d = ["", "(TB =+ imm3)"]
e = ["IALU", "IMAC", "FALU", "FMAC"]
g = ["I0", "I1", "I2"]
h = ["", "@(C)", "@(!C)"]

result = "<SHUIndTToMACC>"

for i in a:
    for j in b:
	for k in c:
	    for o in d:
		for l in e:
		    for n in g:
			for p in h:
		            s = "SHU%s.T%s IND T%s%s->%s.Tt(%s)%s;"%(i, j, k, o, l, n, p) 
		            result += s
result = result[: -1]
result += "</SHUIndTToMACC>\n"
fp.writelines(result)

#SHUIndTToSHU SHU0.T'm|SQ|BB|BH|BW|BD' IND T'm|SQ|BB|BH|BW|BD'{(TB =+ imm3)} -> SHU0.Tt{@('C|!C')}
#	      SHU1.T'm|SQ|BB|BH|BW|BD' IND T'm|SQ|BB|BH|BW|BD'{(TB =+ imm3)} -> SHU1.Tt{@('C|!C')}
b = ["m", "SQ", "BB", "BH", "BW", "BD"]
c = ["m", "SQ", "BB", "BH", "BW", "BD"]
d = ["", "(TB =+ imm3)"]
h = ["", "@(C)", "@(!C)"]

result = "<SHUIndTToSHU>"

for j in b:
    for k in c:
	for o in d:
	    for p in h:
		s = "SHU0.T%s IND T%s%s->SHU0.Tt%s;"%(j, k, o, p) 
		result += s
for j in b:
    for k in c:
	for o in d:
	    for p in h:
		s = "SHU1.T%s IND T%s%s->SHU1.Tt%s;"%(j, k, o, p) 
		result += s
result = result[: -1]
result += "</SHUIndTToSHU>\n"
fp.writelines(result)

#SHUIndTBToBIU SHU'0|1'.T'm|SQ|BB|BH|BW|BD' IND TB{(TB += imm3)}-> BIU'0|1|2'{@('C|!C')}
a = range(0, 2)
b = ["m", "SQ", "BB", "BH", "BW", "BD"]
d = ["", "(TB =+ imm3)"]
e = range(0, 3)
h = ["", "@(C)", "@(!C)"]

result = "<SHUIndTBToBIU>"

for i in a:
    for j in b:
	for o in d:
	    for l in e:
		for p in h:
		    s = "SHU%s.T%s IND TB%s->BIU%s%s;"%(i, j, o, l, p) 
		    result += s
result = result[: -1]
result += "</SHUIndTBToBIU>\n"
fp.writelines(result)

#SHUIndTBToM SHU'0|1'.T'm|SQ|BB|BH|BW|BD' IND TB{(TB += imm3)}-> M[t] {@('C|!C')}
a = range(0, 2)
b = ["m", "SQ", "BB", "BH", "BW", "BD"]
d = ["", "(TB =+ imm3)"]
h = ["", "@(C)", "@(!C)"]

result = "<SHUIndTBToM>"

for i in a:
    for j in b:
	for o in d:
	    for p in h:
		s = "SHU%s.T%s IND TB%s->M[t]%s;"%(i, j, o, p) 
		result += s
result = result[: -1]
result += "</SHUIndTBToM>\n"
fp.writelines(result)

#SHUIndTBToMACC SHU'0|1'.T'm|SQ|BB|BH|BW|BD' IND TB{(TB += imm3)} ->'IALU.T|IMAC.T|FALU.T|FMAC.T't(I'0|1|2') {@('C|!C')}
a = range(0, 2)
b = ["m", "SQ", "BB", "BH", "BW", "BD"]
d = ["", "(TB =+ imm3)"]
e = ["IALU", "IMAC", "FALU", "FMAC"]
g = ["I0", "I1", "I2"]
h = ["", "@(C)", "@(!C)"]

result = "<SHUIndTBToMACC>"

for i in a:
    for j in b:
	for o in d:
	    for l in e:
		for x in g:
	            for p in h:
		        s = "SHU%s.T%s IND TB%s->%s.Tt(%s)%s;"%(i, j, o, l, x, p) 
		        result += s
result = result[: -1]
result += "</SHUIndTBToMACC>\n"
fp.writelines(result)

#SHUIndTBToSHU SHU0.T'm|SQ|BB|BH|BW|BD' IND TB{(TB += imm3)} -> SHU0.Tt{@('C|!C')}
#   	       SHU1.T'm|SQ|BB|BH|BW|BD' IND TB{(TB += imm3)} -> SHU1.Tt{@('C|!C')}
b = ["m", "SQ", "BB", "BH", "BW", "BD"]
d = ["", "(TB =+ imm3)"]
h = ["", "@(C)", "@(!C)"]

result = "<SHUIndTBToSHU>"

for j in b:
    for o in d:
	for p in h:
	    s = "SHU0.T%s IND TB%s->SHU0.Tt%s;"%(j, o, p) 
	    result += s
for j in b:
    for o in d:
	for p in h:
	    s = "SHU1.T%s IND TB%s->SHU1.Tt%s;"%(j, o, p) 
	    result += s
result = result[: -1]
result += "</SHUIndTBToSHU>\n"
fp.writelines(result)

#SHUCombToBIU SHU'0|1'.COMB(T'm|SQ|BB|BH|BW|BD', T'm|SQ|BB|BH|BW|BD'){({'B|H|L'},{TC})}-> BIU'0|1|2'{@('C|!C')}
a = range(0, 2)
b = ["m", "SQ", "BB", "BH", "BW", "BD"]
c = ["m", "SQ", "BB", "BH", "BW", "BD"]
d = ["", "(B)", "(H)", "(L)", "(TC)", "(B,TC)", "(H,TC)", "(L,TC)"]
e = range(0, 3)
h = ["", "@(C)", "@(!C)"]

result = "<SHUCombToBIU>"

for i in a:
    for j in b:
        for k in c:
	    for o in d:
	        for l in e:
		    for p in h:
		        s = "SHU%s.COMB(T%s IND T%s)%s->BIU%s%s;"%(i, j, k, o, l, p) 
		        result += s
result = result[: -1]
result += "</SHUCombToBIU>\n"
fp.writelines(result)

#SHUCombToM SHU'0|1'.COMB(T'm|SQ|BB|BH|BW|BD', T'm|SQ|BB|BH|BW|BD'){({'B|H|L'},{TC})}-> M[t] {@('C|!C')}
a = range(0, 2)
b = ["m", "SQ", "BB", "BH", "BW", "BD"]
c = ["m", "SQ", "BB", "BH", "BW", "BD"]
d = ["", "(B)", "(H)", "(L)", "(TC)", "(B,TC)", "(H,TC)", "(L,TC)"]
h = ["", "@(C)", "@(!C)"]

result = "<SHUCombToM>"

for i in a:
    for j in b:
        for k in c:
	    for o in d:
		for p in h:
		    s = "SHU%s.COMB(T%s IND T%s)%s->M[t]%s;"%(i, j, k, o, p) 
		    result += s
result = result[: -1]
result += "</SHUCombToM>\n"
fp.writelines(result)

#SHUCombToMACC SHU'0|1'.COMB(T'm|SQ|BB|BH|BW|BD', T'm|SQ|BB|BH|BW|BD'){({'B|H|L'},{TC})}->'IALU.T|IMAC.T|FALU.T|FMAC.T't(I'0|1|2') {@('C|!C')}
a = range(0, 2)
b = ["m", "SQ", "BB", "BH", "BW", "BD"]
c = ["m", "SQ", "BB", "BH", "BW", "BD"]
d = ["", "(B)", "(H)", "(L)", "(TC)", "(B,TC)", "(H,TC)", "(L,TC)"]
e = ["IALU", "IMAC", "FALU", "FMAC"]
f = ["I0", "I1", "I2"]
h = ["", "@(C)", "@(!C)"]

result = "<SHUCombToMACC>"

for i in a:
    for j in b:
        for k in c:
	    for o in d:
	        for l in e:
		    for x in f:
		        for p in h:
		            s = "SHU%s.COMB(T%s IND T%s)%s->%s.Tt(%s)%s;"%(i, j, k, o, l, x, p) 
		            result += s
result = result[: -1]
result += "</SHUCombToMACC>\n"
fp.writelines(result)

#SHUCombToSHU SHU0.COMB(T'm|SQ|BB|BH|BW|BD', T'm|SQ|BB|BH|BW|BD'){({'B|H|L'},{TC})} ->SHU0.Tt{@('C|!C')}
#             SHU1.COMB(T'm|SQ|BB|BH|BW|BD', T'm|SQ|BB|BH|BW|BD'){({'B|H|L'},{TC})} ->SHU1.Tt{@('C|!C')}
b = ["m", "SQ", "BB", "BH", "BW", "BD"]
c = ["m", "SQ", "BB", "BH", "BW", "BD"]
d = ["", "(B)", "(H)", "(L)", "(TC)", "(B,TC)", "(H,TC)", "(L,TC)"]
h = ["", "@(C)", "@(!C)"]

result = "<SHUCombToSHU>"

for j in b:
    for k in c:
	for o in d:
	    for p in h:
	        s = "SHU0.COMB(T%s IND T%s)%s->SHU0.Tt%s;"%(j, k, o, p) 
		result += s
for j in b:
    for k in c:
	for o in d:
	    for p in h:
	        s = "SHU1.COMB(T%s IND T%s)%s->SHU1.Tt%s;"%(j, k, o, p) 
		result += s
result = result[: -1]
result += "</SHUCombToSHU>\n"
fp.writelines(result)

#END SHU
result = "</SHU>\n"
fp.writelines(result)

#BIU
result = "<BIU>\n"
fp.writelines(result)

#BIULdToM BIU'0|1|2'.DM{({A++}, {K++}, {M}, {BR})}->M['t|I++']{@('C|!C')}
a = range(0, 3)
b = ["", "(A++)", "(K++)", "(M)", "(BR)", "(A++,K++)", "(A++,M)", "(A++,BR)", "(K++,M)", "(K++,BR)", "(M,BR)", "(A++,K++,M)", "(A++,K++,BR)", "(A++,M,BR)", "(K++,M,BR)", "(A++,K++,M,BR)"]
c = ["t", "I++"]
d = ["", "@(C)", "@(!C)"]

result = "<BIULdToM>"
    
for i in a:
    for j in b:
	for k in c:
	    for h in d:
		s = "BIU%s.DM%s->M[%s]%s;" % (i, j, k, h)
		result += s
result = result[: -1]
result += "</BIULdToM>\n"
fp.writelines(result)

#BIULdToMACC BIU'0|1|2'.DM{({A++}, {K++}, {M}, {BR})}->'IALU.T|IMAC.T|FALU.T|FMAC.T't(I'0|1|2'){@('C|!C')}
a = range(0, 3)
b = ["", "(A++)", "(K++)", "(M)", "(BR)", "(A++,K++)", "(A++,M)", "(A++,BR)", "(K++,M)", "(K++,BR)", "(M,BR)", "(A++,K++,M)", "(A++,K++,BR)", "(A++,M,BR)", "(K++,M,BR)", "(A++,K++,M,BR)"]
c = ["IALU", "IMAC", "FALU", "FMAC"]
d = ["I0", "I1", "I2"]
e = ["", "@(C)", "@(!C)"]

result = "<BIULdToMACC>"
    
for i in a:
    for j in b:
	for k in c:
	    for h in d:
		for l in e:
		    s = "BIU%s.DM%s->%s.Tt(%s)%s;" % (i, j, k, h, l)
		    result += s
result = result[: -1]
result += "</BIULdToMACC>\n"
fp.writelines(result)

#BIULdToSHU BIU'0|1|2'.DM{({A++}, {K++}, {M}, {BR})}->'SHU0.Tt|SHU1.Tt'{@('C|!C')}
a = range(0, 3)
b = ["", "(A++)", "(K++)", "(M)", "(BR)", "(A++,K++)", "(A++,M)", "(A++,BR)", "(K++,M)", "(K++,BR)", "(M,BR)", "(A++,K++,M)", "(A++,K++,BR)", "(A++,M,BR)", "(K++,M,BR)", "(A++,K++,M,BR)"]
c = range(0, 2)
d = ["", "@(C)", "@(!C)"]

result = "<BIULdToSHU>"
    
for i in a:
    for j in b:
	for k in c:
	    for h in d:
		s = "BIU%s.DM%s->SHU%s.Tt%s;" % (i, j, k, h)
		result += s
result = result[: -1]
result += "</BIULdToSHU>\n"
fp.writelines(result)

#BIUSt BIU'0|1|2'-> DM {({A++}, {K++}, {M}, {BR},{I})}{@('C|!C')}
a = range(0, 3)
b = ["", "(A++)", "(K++)", "(M)", "(BR)", "(I)", "(A++,K++)", "(A++,M)", "(A++,BR)", "(A++,I)", "(K++,M)", "(K++,BR)", "(K++,I)", "(M,BR)", "(M,I)", "(A++,K++,M)", "(A++,K++,BR)", "(A++,K++,I)", "(A++,M,BR)", "(A++,M,I)", "(A++,BR,I)", "(K++,M,BR)", "(K++,M,I)", "(M,BR,I)", "(A++,K++,M,BR)"]
c = ["", "@(C)", "@(!C)"]

result = "<BIUSt>"
    
for i in a:
    for j in b:
	for k in c:
	    s = "BIU%s->DM%s%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</BIUSt>\n"
fp.writelines(result)

#BIUKG BIU'0|1|2'(KG) ->M['t|I++']{@('C|!C')}
a = range(0, 3)
b = ["t", "I++"]
c = ["", "@(C)", "@(!C)"]

result = "<BIUKG>"

for i in a:
    for j in b:
	for k in c:
	    s = "BIU%s(KG)->M[%s]%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</BIUKG>\n"
fp.writelines(result)

#END BIU
result = "</BIU>\n"
fp.writelines(result)

#IALU
result = "<IALU>\n"
fp.writelines(result)

#IALUMergeToBIU MERGE(Tm, Tn, Tp) {'B|H'}-> BIU'0|1|2'{@('C|!C')}
a = ["", "B", "H"]
b = range(0, 3)
c = ["", "@(C)", "@(!C)"]

result = "<IALUMergeToBIU>"

for i in a:
    for j in b:
	for k in c:
	    s = "MERGE(Tm,Tn,Tp)%s->BIU%s%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALUMergeToBIU>\n"
fp.writelines(result)

#IALUMergeToM MERGE(Tm, Tn, Tp) {'B|H'}-> M[t]{@('C|!C')}
a = ["", "B", "H"]
b = ["", "@(C)", "@(!C)"]

result = "<IALUMergeToM>"

for i in a:
    for j in b:
	s = "MERGE(Tm,Tn,Tp)%s->M[t]%s;" % (i, j)
	result += s
result = result[: -1]
result += "</IALUMergeToM>\n"
fp.writelines(result)

#IALUMergeToMACC MERGE(Tm, Tn, Tp) {'B|H'}->'IALU.T|IMAC.T|FALU.T|'t{@('C|!C')}
a = ["", "B", "H"]
b = ["IALU", "IMAC", "FALU"]
c = ["", "@(C)", "@(!C)"]

result = "<IALUMergeToMACC>"

for i in a:
    for j in b:
	for k in c:
	    s = "MERGE(Tm,Tn,Tp)%s->%s.Tt%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALUMergeToMACC>\n"
fp.writelines(result)

#IALUMergeToSHU MERGE(Tm, Tn, Tp) {'B|H'}->'SHU0.T|SHU1.T't{@('C|!C')}
a = ["", "B", "H"]
b = range(0, 2)
c = ["", "@(C)", "@(!C)"]

result = "<IALUMergeToSHU>"

for i in a:
    for j in b:
	for k in c:
	    s = "MERGE(Tm,Tn,Tp)%s->SHU%s.Tt%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALUMergeToSHU>\n"
fp.writelines(result)

#IALUAddToBIU Tm + Tn{({U}, {T}, {'B|H'})}-> BIU'0|1|2'{@('C|!C')}
a = ["", "(U)", "(T)", "(B)", "(H)", "(U,T)", "(U,B)", "(U,H)", "(T,B)", "(T,H)", "(U,T,B)", "(U,T,H)"]
b = range(0, 3)
c = ["", "@(C)", "@(!C)"]

result = "<IALUAddToBIU>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm+Tn%s->BIU%s%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALUAddToBIU>\n"
fp.writelines(result)

#IALUAddToM Tm + Tn{({U}, {T}, {'B|H'})}-> M[t]{@('C|!C')}
a = ["", "(U)", "(T)", "(B)", "(H)", "(U,T)", "(U,B)", "(U,H)", "(T,B)", "(T,H)", "(U,T,B)", "(U,T,H)"]
b = ["", "@(C)", "@(!C)"]

result = "<IALUAddToM>"

for i in a:
    for j in b:
	s = "Tm+Tn%s->M[t]%s;" % (i, j)
	result += s
result = result[: -1]
result += "</IALUAddToM>\n"
fp.writelines(result)

#IALUAddToMACC Tm + Tn{({U}, {T}, {'B|H'})}->'IALU.T|IMAC.T|FALU.T|'t{@('C|!C')}
a = ["", "(U)", "(T)", "(B)", "(H)", "(U,T)", "(U,B)", "(U,H)", "(T,B)", "(T,H)", "(U,T,B)", "(U,T,H)"]
b = ["IALU", "IMAC", "FALU"]
c = ["", "@(C)", "@(!C)"]

result = "<IALUAddToMACC>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm+Tn%s->%s.Tt%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALUAddToMACC>\n"
fp.writelines(result)

#IALUAddToSHU Tm + Tn{({U}, {T}, {'B|H'})}->'SHU0.T|SHU1.T't{@('C|!C')}
a = ["", "(U)", "(T)", "(B)", "(H)", "(U,T)", "(U,B)", "(U,H)", "(T,B)", "(T,H)", "(U,T,B)", "(U,T,H)"]
b = range(0, 2)
c = ["", "@(C)", "@(!C)"]

result = "<IALUAddToSHU>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm+Tn%s->SHU%s.Tt%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALUAddToSHU>\n"
fp.writelines(result)

#IALUSubToBIU Tm - Tn{({U}, {T}, {'B|H'})}-> BIU'0|1|2'{@('C|!C')}
a = ["", "(U)", "(T)", "(B)", "(H)", "(U,T)", "(U,B)", "(U,H)", "(T,B)", "(T,H)", "(U,T,B)", "(U,T,H)"]
b = range(0, 3)
c = ["", "@(C)", "@(!C)"]

result = "<IALUSubToBIU>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm-Tn%s->BIU%s%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALUSubToBIU>\n"
fp.writelines(result)

#IALUSubToM Tm - Tn{({U}, {T}, {'B|H'})}-> M[t]{@('C|!C')}
a = ["", "(U)", "(T)", "(B)", "(H)", "(U,T)", "(U,B)", "(U,H)", "(T,B)", "(T,H)", "(U,T,B)", "(U,T,H)"]
b = ["", "@(C)", "@(!C)"]

result = "<IALUSubToM>"

for i in a:
    for j in b:
	s = "Tm-Tn%s->M[t]%s;" % (i, j)
	result += s
result = result[: -1]
result += "</IALUSubToM>\n"
fp.writelines(result)

#IALUSubToMACC Tm - Tn{({U}, {T}, {'B|H'})}->'IALU.T|IMAC.T|FALU.T|'t{@('C|!C')}
a = ["", "(U)", "(T)", "(B)", "(H)", "(U,T)", "(U,B)", "(U,H)", "(T,B)", "(T,H)", "(U,T,B)", "(U,T,H)"]
b = ["IALU", "IMAC", "FALU"]
c = ["", "@(C)", "@(!C)"]

result = "<IALUSubToMACC>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm-Tn%s->%s.Tt%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALUSubToMACC>\n"
fp.writelines(result)

#IALUSubToSHU Tm - Tn{({U}, {T}, {'B|H'})}->'SHU0.T|SHU1.T't{@('C|!C')}
a = ["", "(U)", "(T)", "(B)", "(H)", "(U,T)", "(U,B)", "(U,H)", "(T,B)", "(T,H)", "(U,T,B)", "(U,T,H)"]
b = range(0, 2)
c = ["", "@(C)", "@(!C)"]

result = "<IALUSubToSHU>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm-Tn%s->SHU%s.Tt%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALUSubToSHU>\n"
fp.writelines(result)

#IALUAndToBIU Tm& Tn -> BIU'0|1|2'{@('C|!C')}
b = range(0, 3)
c = ["", "@(C)", "@(!C)"]

result = "<IALUAndToBIU>"

for j in b:
    for k in c:
	s = "Tm&amp;Tn->BIU%s%s;" % (j, k)
	result += s
result = result[: -1]
result += "</IALUAndToBIU>\n"
fp.writelines(result)

#IALUAndToM Tm& Tn -> M[t]{@('C|!C')}
b = ["", "@(C)", "@(!C)"]

result = "<IALUAndToM>"

for j in b:
    s = "Tm&amp;Tn->M[t]%s;" % (j)
    result += s
result = result[: -1]
result += "</IALUAndToM>\n"
fp.writelines(result)

#IALUAndToMACC Tm& Tn ->'IALU.T|IMAC.T|FALU.T|'t{@('C|!C')}
b = ["IALU", "IMAC", "FALU"]
c = ["", "@(C)", "@(!C)"]

result = "<IALUAndToMACC>"

for j in b:
    for k in c:
	s = "Tm&amp;Tn->%s.Tt%s;" % (j, k)
	result += s
result = result[: -1]
result += "</IALUAndToMACC>\n"
fp.writelines(result)

#IALUAndToSHU Tm& Tn ->'SHU0.T|SHU1.T't{@('C|!C')}
b = range(0, 2)
c = ["", "@(C)", "@(!C)"]

result = "<IALUAndToSHU>"

for j in b:
    for k in c:
	s = "Tm&amp;Tn->SHU%s.Tt%s;" % (j, k)
	result += s
result = result[: -1]
result += "</IALUAndToSHU>\n"
fp.writelines(result)

#IALUOrToBIU Tm | Tn -> BIU'0|1|2'{@('C|!C')}
b = range(0, 3)
c = ["", "@(C)", "@(!C)"]

result = "<IALUOrToBIU>"

for j in b:
    for k in c:
	s = "Tm|Tn->BIU%s%s;" % (j, k)
	result += s
result = result[: -1]
result += "</IALUOrToBIU>\n"
fp.writelines(result)

#IALUOrToM Tm | Tn -> M[t]{@('C|!C')}
b = ["", "@(C)", "@(!C)"]

result = "<IALUOrToM>"

for j in b:
    s = "Tm|Tn->M[t]%s;" % (j)
    result += s
result = result[: -1]
result += "</IALUOrToM>\n"
fp.writelines(result)

#IALUOrToMACC Tm | Tn ->'IALU.T|IMAC.T|FALU.T|'t{@('C|!C')}
b = ["IALU", "IMAC", "FALU"]
c = ["", "@(C)", "@(!C)"]

result = "<IALUOrToMACC>"

for j in b:
    for k in c:
	s = "Tm|Tn->%s.Tt%s;" % (j, k)
	result += s
result = result[: -1]
result += "</IALUOrToMACC>\n"
fp.writelines(result)

#IALUOrToSHU Tm | Tn ->'SHU0.T|SHU1.T't{@('C|!C')}
b = range(0, 2)
c = ["", "@(C)", "@(!C)"]

result = "<IALUOrToSHU>"

for j in b:
    for k in c:
	s = "Tm|Tn->SHU%s.Tt%s;" % (j, k)
	result += s
result = result[: -1]
result += "</IALUOrToSHU>\n"
fp.writelines(result)

#IALUXorToBIU Tm ^ Tn -> BIU'0|1|2'{@('C|!C')}
b = range(0, 3)
c = ["", "@(C)", "@(!C)"]

result = "<IALUXorToBIU>"

for j in b:
    for k in c:
	s = "Tm^Tn->BIU%s%s;" % (j, k)
	result += s
result = result[: -1]
result += "</IALUXorToBIU>\n"
fp.writelines(result)

#IALUXorToM Tm ^ Tn -> M[t]{@('C|!C')}
b = ["", "@(C)", "@(!C)"]

result = "<IALUXorToM>"

for j in b:
    s = "Tm^Tn->M[t]%s;" % (j)
    result += s
result = result[: -1]
result += "</IALUXorToM>\n"
fp.writelines(result)

#IALUXorToMACC Tm ^ Tn ->'IALU.T|IMAC.T|FALU.T|'t{@('C|!C')}
b = ["IALU", "IMAC", "FALU"]
c = ["", "@(C)", "@(!C)"]

result = "<IALUXorToMACC>"

for j in b:
    for k in c:
	s = "Tm^Tn->%s.Tt%s;" % (j, k)
	result += s
result = result[: -1]
result += "</IALUXorToMACC>\n"
fp.writelines(result)

#IALUXorToSHU Tm ^ Tn ->'SHU0.T|SHU1.T't{@('C|!C')}
b = range(0, 2)
c = ["", "@(C)", "@(!C)"]

result = "<IALUXorToSHU>"

for j in b:
    for k in c:
	s = "Tm^Tn->SHU%s.Tt%s;" % (j, k)
	result += s
result = result[: -1]
result += "</IALUXorToSHU>\n"
fp.writelines(result)

#IALUEquToBIU Tm == Tn{('B|H')}-> BIU'0|1|2'{@('C|!C')}
a = ["", "(B)", "(H)"]
b = range(0, 3)
c = ["", "@(C)", "@(!C)"]

result = "<IALUEquToBIU>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm==Tn%s->BIU%s%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALUEquToBIU>\n"
fp.writelines(result)

#IALUEquToM Tm == Tn{('B|H')}-> M[t]{@('C|!C')}
a = ["", "(B)", "(H)"]
b = ["", "@(C)", "@(!C)"]

result = "<IALUEquToM>"

for i in a:
    for j in b:
	s = "Tm==Tn%s->M[t]%s;" % (i, j)
	result += s
result = result[: -1]
result += "</IALUEquToM>\n"
fp.writelines(result)

#IALUEquToMACC Tm == Tn{('B|H')}->'IALU.T|IMAC.T|FALU.T't{@('C|!C')}
a = ["", "(B)", "(H)"]
b = ["IALU", "IMAC", "FALU"]
c = ["", "@(C)", "@(!C)"]

result = "<IALUEquToMACC>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm==Tn%s->%s.Tt%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALUEquToMACC>\n"
fp.writelines(result)

#IALUEquToSHU Tm == Tn{('B|H')}->'SHU0.T|SHU1.T't{@('C|!C')}
a = ["", "(B)", "(H)"]
b = range(0, 2)
c = ["", "@(C)", "@(!C)"]

result = "<IALUEquToSHU>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm==Tn%s->SHU%s.Tt%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALUEquToSHU>\n"
fp.writelines(result)

#IALUNeqToBIU Tm != Tn{('B|H')}-> BIU'0|1|2'{@('C|!C')}
a = ["", "(B)", "(H)"]
b = range(0, 3)
c = ["", "@(C)", "@(!C)"]

result = "<IALUNeqToBIU>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm!=Tn%s->BIU%s%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALUNeqToBIU>\n"
fp.writelines(result)

#IALUNeqToM Tm != Tn{('B|H')}-> M[t]{@('C|!C')}
a = ["", "(B)", "(H)"]
b = ["", "@(C)", "@(!C)"]

result = "<IALUNeqToM>"

for i in a:
    for j in b:
	s = "Tm!=Tn%s->M[t]%s;" % (i, j)
	result += s
result = result[: -1]
result += "</IALUNeqToM>\n"
fp.writelines(result)

#IALUNeqToMACC Tm != Tn{('B|H')}->'IALU.T|IMAC.T|FALU.T't{@('C|!C')}
a = ["", "(B)", "(H)"]
b = ["IALU", "IMAC", "FALU"]
c = ["", "@(C)", "@(!C)"]

result = "<IALUNeqToMACC>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm!=Tn%s->%s.Tt%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALUNeqToMACC>\n"
fp.writelines(result)

#IALUNeqToSHU Tm != Tn{('B|H')}->'SHU0.T|SHU1.T't{@('C|!C')}
a = ["", "(B)", "(H)"]
b = range(0, 2)
c = ["", "@(C)", "@(!C)"]

result = "<IALUNeqToSHU>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm!=Tn%s->SHU%s.Tt%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALUNeqToSHU>\n"
fp.writelines(result)

#IALULtToBIU Tm> Tn{({U}, {'B|H'})}-> BIU'0|1|2'{@('C|!C')}
a = ["", "(U)", "(B)", "(H)", "(U,B)", "(U,H)"]
b = range(0, 3)
c = ["", "@(C)", "@(!C)"]

result = "<IALULtToBIU>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm&gt;Tn%s->BIU%s%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALULtToBIU>\n"
fp.writelines(result)

#IALULtToM Tm> Tn{({U}, {'B|H'})}-> M[t]{@('C|!C')}
a = ["", "(U)", "(B)", "(H)", "(U,B)", "(U,H)"]
b = ["", "@(C)", "@(!C)"]

result = "<IALULtToM>"

for i in a:
    for j in b:
	s = "Tm&gt;Tn%s->M[t]%s;" % (i, j)
	result += s
result = result[: -1]
result += "</IALULtToM>\n"
fp.writelines(result)

#IALULtToMACC Tm> Tn{({U}, {'B|H'})}->'IALU.T|IMAC.T|FALU.T't{@('C|!C')}
a = ["", "(U)", "(B)", "(H)", "(U,B)", "(U,H)"]
b = ["IALU", "IMAC", "FALU"]
c = ["", "@(C)", "@(!C)"]

result = "<IALULtToMACC>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm&gt;Tn%s->%s.Tt%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALULtToMACC>\n"
fp.writelines(result)

#IALULtToSHU Tm> Tn{({U}, {'B|H'})}->'SHU0.T|SHU1.T't{@('C|!C')}
a = ["", "(U)", "(B)", "(H)", "(U,B)", "(U,H)"]
b = range(0, 2)
c = ["", "@(C)", "@(!C)"]

result = "<IALULtToSHU>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm&gt;Tn%s->SHU%s.Tt%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALULtToSHU>\n"
fp.writelines(result)

#IALUNstToBIU Tm>= Tn{({U}, {'B|H'})}-> BIU'0|1|2'{@('C|!C')}
a = ["", "(U)", "(B)", "(H)", "(U,B)", "(U,H)"]
b = range(0, 3)
c = ["", "@(C)", "@(!C)"]

result = "<IALUNstToBIU>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm&gt;=Tn%s->BIU%s%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALUNstToBIU>\n"
fp.writelines(result)

#IALUNstToM Tm>= Tn{({U}, {'B|H'})}-> M[t]{@('C|!C')}
a = ["", "(U)", "(B)", "(H)", "(U,B)", "(U,H)"]
b = ["", "@(C)", "@(!C)"]

result = "<IALUNstToM>"

for i in a:
    for j in b:
	s = "Tm&gt;=Tn%s->M[t]%s;" % (i, j)
	result += s
result = result[: -1]
result += "</IALUNstToM>\n"
fp.writelines(result)

#IALUNstToMACC Tm>= Tn{({U}, {'B|H'})}->'IALU.T|IMAC.T|FALU.T't{@('C|!C')}
a = ["", "(U)", "(B)", "(H)", "(U,B)", "(U,H)"]
b = ["IALU", "IMAC", "FALU"]
c = ["", "@(C)", "@(!C)"]

result = "<IALUNstToMACC>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm&gt;=Tn%s->%s.Tt%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALUNstToMACC>\n"
fp.writelines(result)

#IALUNstToSHU Tm>= Tn{({U}, {'B|H'})}->'SHU0.T|SHU1.T't{@('C|!C')}
a = ["", "(U)", "(B)", "(H)", "(U,B)", "(U,H)"]
b = range(0, 2)
c = ["", "@(C)", "@(!C)"]

result = "<IALUNstToSHU>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm&gt;=Tn%s->SHU%s.Tt%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALUNstToSHU>\n"
fp.writelines(result)

#IALUStToBIU Tm< Tn{({U}, {'B|H'})}-> BIU'0|1|2'{@('C|!C')}
a = ["", "(U)", "(B)", "(H)", "(U,B)", "(U,H)"]
b = range(0, 3)
c = ["", "@(C)", "@(!C)"]

result = "<IALUStToBIU>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm&lt;Tn%s->BIU%s%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALUStToBIU>\n"
fp.writelines(result)

#IALUStToM Tm< Tn{({U}, {'B|H'})}-> M[t]{@('C|!C')}
a = ["", "(U)", "(B)", "(H)", "(U,B)", "(U,H)"]
b = ["", "@(C)", "@(!C)"]

result = "<IALUStToM>"

for i in a:
    for j in b:
	s = "Tm&lt;Tn%s->M[t]%s;" % (i, j)
	result += s
result = result[: -1]
result += "</IALUStToM>\n"
fp.writelines(result)

#IALUStToMACC Tm< Tn{({U}, {'B|H'})}->'IALU.T|IMAC.T|FALU.T't{@('C|!C')}
a = ["", "(U)", "(B)", "(H)", "(U,B)", "(U,H)"]
b = ["IALU", "IMAC", "FALU"]
c = ["", "@(C)", "@(!C)"]

result = "<IALUStToMACC>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm&lt;Tn%s->%s.Tt%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALUStToMACC>\n"
fp.writelines(result)

#IALUStToSHU Tm< Tn{({U}, {'B|H'})}->'SHU0.T|SHU1.T't{@('C|!C')}
a = ["", "(U)", "(B)", "(H)", "(U,B)", "(U,H)"]
b = range(0, 2)
c = ["", "@(C)", "@(!C)"]

result = "<IALUStToSHU>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm&lt;Tn%s->SHU%s.Tt%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALUStToSHU>\n"
fp.writelines(result)

#IALUNltToBIU Tm<= Tn{({U}, {'B|H'})}-> BIU'0|1|2'{@('C|!C')}
a = ["", "(U)", "(B)", "(H)", "(U,B)", "(U,H)"]
b = range(0, 3)
c = ["", "@(C)", "@(!C)"]

result = "<IALUNltToBIU>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm&lt;Tn%s->BIU%s%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALUNltToBIU>\n"
fp.writelines(result)

#IALUNltToM Tm<= Tn{({U}, {'B|H'})}-> M[t]{@('C|!C')}
a = ["", "(U)", "(B)", "(H)", "(U,B)", "(U,H)"]
b = ["", "@(C)", "@(!C)"]

result = "<IALUNltToM>"

for i in a:
    for j in b:
	s = "Tm&lt;=Tn%s->M[t]%s;" % (i, j)
	result += s
result = result[: -1]
result += "</IALUNltToM>\n"
fp.writelines(result)

#IALUNltToMACC Tm<= Tn{({U}, {'B|H'})}->'IALU.T|IMAC.T|FALU.T't{@('C|!C')}
a = ["", "(U)", "(B)", "(H)", "(U,B)", "(U,H)"]
b = ["IALU", "IMAC", "FALU"]
c = ["", "@(C)", "@(!C)"]

result = "<IALUNltToMACC>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm&lt;=Tn%s->%s.Tt%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALUNltToMACC>\n"
fp.writelines(result)

#IALUNltToSHU Tm<= Tn{({U}, {'B|H'})}->'SHU0.T|SHU1.T't{@('C|!C')}
a = ["", "(U)", "(B)", "(H)", "(U,B)", "(U,H)"]
b = range(0, 2)
c = ["", "@(C)", "@(!C)"]

result = "<IALUNltToSHU>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm&lt;=Tn%s->SHU%s.Tt%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALUNltToSHU>\n"
fp.writelines(result)

#IALULshToBIU Tm<< Tn{({'B|H'})}-> BIU'0|1|2'{@('C|!C')}
a = ["", "(B)", "(H)"]
b = range(0, 3)
c = ["", "@(C)", "@(!C)"]

result = "<IALULshToBIU>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm&lt;&lt;Tn%s->BIU%s%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALULshToBIU>\n"
fp.writelines(result)

#IALULshToM Tm<< Tn{({'B|H'})}-> M[t]{@('C|!C')}
a = ["", "(B)", "(H)"]
b = ["", "@(C)", "@(!C)"]

result = "<IALULshToM>"

for i in a:
    for j in b:
	s = "Tm&lt;&lt;Tn%s->M[t]%s;" % (i, j)
	result += s
result = result[: -1]
result += "</IALULshToM>\n"
fp.writelines(result)

#IALULshToMACC Tm<< Tn{({'B|H'})}->'IALU.T|IMAC.T|FALU.T't{@('C|!C')}
a = ["", "(B)", "(H)"]
b = ["IALU", "IMAC", "FALU"]
c = ["", "@(C)", "@(!C)"]

result = "<IALULshToMACC>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm&lt;&lt;Tn%s->%s.Tt%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALULshToMACC>\n"
fp.writelines(result)

#IALULshToSHU Tm<< Tn{({'B|H'})}->'SHU0.T|SHU1.T't{@('C|!C')}
a = ["", "(B)", "(H)"]
b = range(0, 2)
c = ["", "@(C)", "@(!C)"]

result = "<IALULshToSHU>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm&lt;&lt;Tn%s->SHU%s.Tt%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALULshToSHU>\n"
fp.writelines(result)

#IALURshToBIU Tm>> Tn{({U}, {'B|H'})}-> BIU'0|1|2'{@('C|!C')}
a = ["", "(U)", "(B)", "(H)", "(U,B)", "(U,H)"]
b = range(0, 3)
c = ["", "@(C)", "@(!C)"]

result = "<IALURshToBIU>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm&gt;&gt;Tn%s->BIU%s%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALURshToBIU>\n"
fp.writelines(result)

#IALURshToM Tm>> Tn{({U}, {'B|H'})}-> M[t]{@('C|!C')}
a = ["", "(U)", "(B)", "(H)", "(U,B)", "(U,H)"]
b = ["", "@(C)", "@(!C)"]

result = "<IALURshToM>"

for i in a:
    for j in b:
	s = "Tm&gt;&gt;Tn%s->M[t]%s;" % (i, j)
	result += s
result = result[: -1]
result += "</IALURshToM>\n"
fp.writelines(result)

#IALURshToMACC Tm>> Tn{({U}, {'B|H'})}->'IALU.T|IMAC.T|FALU.T't{@('C|!C')}
a = ["", "(U)", "(B)", "(H)", "(U,B)", "(U,H)"]
b = ["IALU", "IMAC", "FALU"]
c = ["", "@(C)", "@(!C)"]

result = "<IALURshToMACC>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm&gt;&gt;Tn%s->%s.Tt%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALURshToMACC>\n"
fp.writelines(result)

#IALURshToSHU Tm>> Tn{({U}, {'B|H'})}->'SHU0.T|SHU1.T't{@('C|!C')}
a = ["", "(U)", "(B)", "(H)", "(U,B)", "(U,H)"]
b = range(0, 2)
c = ["", "@(C)", "@(!C)"]

result = "<IALURshToSHU>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm&gt;&gt;Tn%s->SHU%s.Tt%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALURshToSHU>\n"
fp.writelines(result)

#IALUMaxToBIU MAX(Tm, Tn){({U}, {'B|H'})}-> BIU'0|1|2'{@('C|!C')}
a = ["", "(U)", "(B)", "(H)", "(U,B)", "(U,H)"]
b = range(0, 3)
c = ["", "@(C)", "@(!C)"]

result = "<IALUMaxToBIU>"

for i in a:
    for j in b:
	for k in c:
	    s = "MAX(Tm,Tn)%s->BIU%s%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALUMaxToBIU>\n"
fp.writelines(result)

#IALUMaxToM MAX(Tm, Tn){({U}, {'B|H'})}-> M[t]{@('C|!C')}
a = ["", "(U)", "(B)", "(H)", "(U,B)", "(U,H)"]
b = ["", "@(C)", "@(!C)"]

result = "<IALUMaxToM>"

for i in a:
    for j in b:
	s = "MAX(Tm,Tn)%s->M[t]%s;" % (i, j)
	result += s
result = result[: -1]
result += "</IALUMaxToM>\n"
fp.writelines(result)

#IALUMaxToMACC MAX(Tm, Tn){({U}, {'B|H'})}->'IALU.T|IMAC.T|FALU.T't{@('C|!C')}
a = ["", "(U)", "(B)", "(H)", "(U,B)", "(U,H)"]
b = ["IALU", "IMAC", "FALU"]
c = ["", "@(C)", "@(!C)"]

result = "<IALUMaxToMACC>"

for i in a:
    for j in b:
	for k in c:
	    s = "MAX(Tm,Tn)%s->%s.Tt%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALUMaxToMACC>\n"
fp.writelines(result)

#IALUMaxToSHU MAX(Tm, Tn){({U}, {'B|H'})}->'SHU0.T|SHU1.T't{@('C|!C')}
a = ["", "(U)", "(B)", "(H)", "(U,B)", "(U,H)"]
b = range(0, 2)
c = ["", "@(C)", "@(!C)"]

result = "<IALUMaxToSHU>"

for i in a:
    for j in b:
	for k in c:
	    s = "MAX(Tm,Tn)%s->SHU%s.Tt%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALUMaxToSHU>\n"
fp.writelines(result)

#IALUMinToBIU MIN(Tm, Tn){({U}, {'B|H'})}-> BIU'0|1|2'{@('C|!C')}
a = ["", "(U)", "(B)", "(H)", "(U,B)", "(U,H)"]
b = range(0, 3)
c = ["", "@(C)", "@(!C)"]

result = "<IALUMinToBIU>"

for i in a:
    for j in b:
	for k in c:
	    s = "MIN(Tm,Tn)%s->BIU%s%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALUMinToBIU>\n"
fp.writelines(result)

#IALUMinToM MIN(Tm, Tn){({U}, {'B|H'})}-> M[t]{@('C|!C')}
a = ["", "(U)", "(B)", "(H)", "(U,B)", "(U,H)"]
b = ["", "@(C)", "@(!C)"]

result = "<IALUMinToM>"

for i in a:
    for j in b:
	s = "MIN(Tm,Tn)%s->M[t]%s;" % (i, j)
	result += s
result = result[: -1]
result += "</IALUMinToM>\n"
fp.writelines(result)

#IALUMinToMACC MIN(Tm, Tn){({U}, {'B|H'})}->'IALU.T|IMAC.T|FALU.T't{@('C|!C')}
a = ["", "(U)", "(B)", "(H)", "(U,B)", "(U,H)"]
b = ["IALU", "IMAC", "FALU"]
c = ["", "@(C)", "@(!C)"]

result = "<IALUMinToMACC>"

for i in a:
    for j in b:
	for k in c:
	    s = "MIN(Tm,Tn)%s->%s.Tt%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALUMinToMACC>\n"
fp.writelines(result)

#IALUMinToSHU MIN(Tm, Tn){({U}, {'B|H'})}->'SHU0.T|SHU1.T't{@('C|!C')}
a = ["", "(U)", "(B)", "(H)", "(U,B)", "(U,H)"]
b = range(0, 2)
c = ["", "@(C)", "@(!C)"]

result = "<IALUMinToSHU>"

for i in a:
    for j in b:
	for k in c:
	    s = "MIN(Tm,Tn)%s->SHU%s.Tt%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALUMinToSHU>\n"
fp.writelines(result)

#IALUAbsToBIU ABS(Tm, Tn){({U}, {'B|H'})}-> BIU'0|1|2'{@('C|!C')}
a = ["", "(U)", "(B)", "(H)", "(U,B)", "(U,H)"]
b = range(0, 3)
c = ["", "@(C)", "@(!C)"]

result = "<IALUAbsToBIU>"

for i in a:
    for j in b:
	for k in c:
	    s = "ABS(Tm,Tn)%s->BIU%s%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALUAbsToBIU>\n"
fp.writelines(result)

#IALUAbsToM ABS(Tm, Tn){({U}, {'B|H'})}-> M[t]{@('C|!C')}
a = ["", "(U)", "(B)", "(H)", "(U,B)", "(U,H)"]
b = ["", "@(C)", "@(!C)"]

result = "<IALUAbsToM>"

for i in a:
    for j in b:
	s = "ABS(Tm,Tn)%s->M[t]%s;" % (i, j)
	result += s
result = result[: -1]
result += "</IALUAbsToM>\n"
fp.writelines(result)

#IALUAbsToMACC ABS(Tm, Tn){({U}, {'B|H'})}->'IALU.T|IMAC.T|FALU.T't{@('C|!C')}
a = ["", "(U)", "(B)", "(H)", "(U,B)", "(U,H)"]
b = ["IALU", "IMAC", "FALU"]
c = ["", "@(C)", "@(!C)"]

result = "<IALUAbsToMACC>"

for i in a:
    for j in b:
	for k in c:
	    s = "ABS(Tm,Tn)%s->%s.Tt%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALUAbsToMACC>\n"
fp.writelines(result)

#IALUAbsToSHU ABS(Tm, Tn){({U}, {'B|H'})}->'SHU0.T|SHU1.T't{@('C|!C')}
a = ["", "(U)", "(B)", "(H)", "(U,B)", "(U,H)"]
b = range(0, 2)
c = ["", "@(C)", "@(!C)"]

result = "<IALUAbsToSHU>"

for i in a:
    for j in b:
	for k in c:
	    s = "ABS(Tm,Tn)%s->SHU%s.Tt%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALUAbsToSHU>\n"
fp.writelines(result)

#IALURshiToBIU Tm>>imm5{({U}, {'B|H'})}-> BIU'0|1|2'{@('C|!C')}
a = ["", "(U)", "(B)", "(H)", "(U,B)", "(U,H)"]
b = range(0, 3)
c = ["", "@(C)", "@(!C)"]

result = "<IALURshiToBIU>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm&gt;&gt;imm5(Tm, Tn)%s->BIU%s%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALURshiToBIU>\n"
fp.writelines(result)

#IALURshiToM Tm>>imm5{({U}, {'B|H'})}-> M[t]{@('C|!C')}
a = ["", "(U)", "(B)", "(H)", "(U,B)", "(U,H)"]
b = ["", "@(C)", "@(!C)"]

result = "<IALURshiToM>"

for i in a:
    for j in b:
	s = "Tm&gt;&gt;imm5%s->M[t]%s;" % (i, j)
	result += s
result = result[: -1]
result += "</IALURshiToM>\n"
fp.writelines(result)

#IALURshiToMACC Tm>>imm5{({U}, {'B|H'})}->'IALU.T|IMAC.T|FALU.T't{@('C|!C')}
a = ["", "(U)", "(B)", "(H)", "(U,B)", "(U,H)"]
b = ["IALU", "IMAC", "FALU"]
c = ["", "@(C)", "@(!C)"]

result = "<IALURshiToMACC>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm&gt;&gt;imm5%s->%s.Tt%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALURshiToMACC>\n"
fp.writelines(result)

#IALURshiToSHU Tm>>imm5{({U}, {'B|H'})}->'SHU0.T|SHU1.T't{@('C|!C')}
a = ["", "(U)", "(B)", "(H)", "(U,B)", "(U,H)"]
b = range(0, 2)
c = ["", "@(C)", "@(!C)"]

result = "<IALURshiToSHU>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm&gt;&gt;imm5%s->SHU%s.Tt%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALURshiToSHU>\n"
fp.writelines(result)

#IALULshiToBIU Tm<<imm5{('B|H')}-> BIU'0|1|2'{@('C|!C')}
a = ["", "(B)", "(H)"]
b = range(0, 3)
c = ["", "@(C)", "@(!C)"]

result = "<IALULshiToBIU>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm&lt;&lt;imm5(Tm, Tn)%s->BIU%s%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALULshiToBIU>\n"
fp.writelines(result)

#IALULshiToM Tm<<imm5{('B|H')}-> M[t]{@('C|!C')}
a = ["", "(B)", "(H)"]
b = ["", "@(C)", "@(!C)"]

result = "<IALULshiToM>"

for i in a:
    for j in b:
	s = "Tm&lt;&lt;imm5%s->M[t]%s;" % (i, j)
	result += s
result = result[: -1]
result += "</IALULshiToM>\n"
fp.writelines(result)

#IALULshiToMACC Tm<<imm5{('B|H')}->'IALU.T|IMAC.T|FALU.T't{@('C|!C')}
a = ["", "(B)", "(H)"]
b = ["IALU", "IMAC", "FALU"]
c = ["", "@(C)", "@(!C)"]

result = "<IALULshiToMACC>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm&lt;&lt;imm5%s->%s.Tt%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALULshiToMACC>\n"
fp.writelines(result)

#IALULshiToSHU Tm<<imm5{('B|H')}->'SHU0.T|SHU1.T't{@('C|!C')}
a = ["", "(B)", "(H)"]
b = range(0, 2)
c = ["", "@(C)", "@(!C)"]

result = "<IALULshiToSHU>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm&lt;&lt;imm5%s->SHU%s.Tt%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALULshiToSHU>\n"
fp.writelines(result)

#IALUNotToBIU NOT Tm -> BIU'0|1|2'{@('C|!C')}
a = range(0, 2)
b = ["", "@(C)", "@(!C)"]

result = "<IALUNotToBIU>"

for i in a:
    for j in b:
	s = "NOT Tm->BIU%s%s;" % (i, j)
	result += s
result = result[: -1]
result += "</IALUNotToBIU>\n"
fp.writelines(result)

#IALUNotToM NOT Tm -> M[t]{@('C|!C')}
a = ["", "@(C)", "@(!C)"]

result = "<IALUNotToM>"

for i in a:
    s = "NOT Tm->M[t]%s;" % (i)
    result += s
result = result[: -1]
result += "</IALUNotToM>\n"
fp.writelines(result)

#IALUNotToMACC NOT Tm ->'IALU.T|IMAC.T|FALU.T't{@('C|!C')}
a = ["IALU", "IMAC", "FALU"]
b = ["", "@(C)", "@(!C)"]

result = "<IALUNotToMACC>"

for i in a:
    for j in b:
	s = "NOT Tm->%s.Tt%s;" % (i, j)
	result += s
result = result[: -1]
result += "</IALUNotToMACC>\n"
fp.writelines(result)

#IALUNotToSHU NOT Tm ->'SHU0.T|SHU1.T't{@('C|!C')}
a = range(0, 2)
b = ["", "@(C)", "@(!C)"]

result = "<IALUNotToSHU>"

for i in a:
    for j in b:
	s = "NOT Tm->SHU%s.Tt%s;" % (i, j)
	result += s
result = result[: -1]
result += "</IALUNotToSHU>\n"
fp.writelines(result)

#IALURmaxToBIU RMAX Tm({U}, B)-> BIU'0|1|2'{@('C|!C')}
a = ["(B)", "(U,B)"]
b = range(0, 3)
c = ["", "@(C)", "@(!C)"]

result = "<IALURmaxToBIU>"

for i in a:
    for j in b:
	for k in c:
	    s = "RMAX Tm%s->BIU%s%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALURmaxToBIU>\n"
fp.writelines(result)

#IALURmaxToM RMAX Tm({U}, B)-> M[t]{@('C|!C')}
a = ["(B)", "(U,B)"]
b = ["", "@(C)", "@(!C)"]

result = "<IALURmaxToM>"

for i in a:
    for j in b:
	s = "RMAX Tm%s->M[t]%s;" % (i, j)
	result += s
result = result[: -1]
result += "</IALURmaxToM>\n"
fp.writelines(result)

#IALURmaxToMACC RMAX Tm({U}, B)->'IALU.T|IMAC.T|FALU.T't{@('C|!C')}
a = ["(B)", "(U,B)"]
b = ["IALU", "IMAC", "FALU"]
c = ["", "@(C)", "@(!C)"]

result = "<IALURmaxToMACC>"

for i in a:
    for j in b:
	for k in c:
	    s = "RMAX Tm%s->%s.Tt%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALURmaxToMACC>\n"
fp.writelines(result)

#IALURmaxToSHU RMAX Tm({U}, B)->'SHU0.T|SHU1.T't{@('C|!C')}
a = ["(B)", "(U,B)"]
b = range(0, 2)
c = ["", "@(C)", "@(!C)"]

result = "<IALURmaxToSHU>"

for i in a:
    for j in b:
	for k in c:
	    s = "RMAX Tm%s->SHU%s.Tt%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALURmaxToSHU>\n"
fp.writelines(result)

#IALURminToBIU RMIN Tm({U}, B)-> BIU'0|1|2'{@('C|!C')}
a = ["(B)", "(U,B)"]
b = range(0, 3)
c = ["", "@(C)", "@(!C)"]

result = "<IALURminToBIU>"

for i in a:
    for j in b:
	for k in c:
	    s = "RMIN Tm%s->BIU%s%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALURminToBIU>\n"
fp.writelines(result)

#IALURminToM RMIN Tm({U}, B)-> M[t]{@('C|!C')}
a = ["(B)", "(U,B)"]
b = ["", "@(C)", "@(!C)"]

result = "<IALURminToM>"

for i in a:
    for j in b:
	s = "RMIN Tm%s->M[t]%s;" % (i, j)
	result += s
result = result[: -1]
result += "</IALURminToM>\n"
fp.writelines(result)

#IALURminToMACC RMIN Tm({U}, B)->'IALU.T|IMAC.T|FALU.T't{@('C|!C')}
a = ["(B)", "(U,B)"]
b = ["IALU", "IMAC", "FALU"]
c = ["", "@(C)", "@(!C)"]

result = "<IALURminToMACC>"

for i in a:
    for j in b:
	for k in c:
	    s = "RMIN Tm%s->%s.Tt%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALURminToMACC>\n"
fp.writelines(result)

#IALURminToSHU RMIN Tm({U}, B)->'SHU0.T|SHU1.T't{@('C|!C')}
a = ["(B)", "(U,B)"]
b = range(0, 2)
c = ["", "@(C)", "@(!C)"]

result = "<IALURminToSHU>"

for i in a:
    for j in b:
	for k in c:
	    s = "RMIN Tm%s->SHU%s.Tt%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALURminToSHU>\n"
fp.writelines(result)

#IALUExpdToBIU EXPD Tm({U}, 'B|H') ->BIU'0|1|2'{@('C|!C')}{@('C|!C')}
a = ["(B)", "(H)", "(U,B)", "(U,H)"]
b = range(0, 3)
c = ["", "@(C)", "@(!C)"]

result = "<IALUExpdToBIU>"

for i in a:
    for j in b:
	for k in c:
	    s = "EXPD Tm%s->BIU%s%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALUExpdToBIU>\n"
fp.writelines(result)

#IALUExpdToM EXPD Tm({U}, 'B|H') ->M[t]{@('C|!C')}
a = ["(B)", "(H)", "(U,B)", "(U,H)"]
b = ["", "@(C)", "@(!C)"]

result = "<IALUExpdToM>"

for i in a:
    for j in b:
	s = "EXPD Tm%s->M[t]%s;" % (i, j)
	result += s
result = result[: -1]
result += "</IALUExpdToM>\n"
fp.writelines(result)

#IALUExpdToMACC EXPD Tm({U}, 'B|H') ->'IALU.T|IMAC.T|FALU.T't{@('C|!C')}
a = ["(B)", "(H)", "(U,B)", "(U,H)"]
b = ["IALU", "IMAC", "FALU"]
c = ["", "@(C)", "@(!C)"]

result = "<IALUExpdToMACC>"

for i in a:
    for j in b:
	for k in c:
	    s = "EXPD Tm%s->%s.Tt%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALUExpdToMACC>\n"
fp.writelines(result)

#IALUExpdToSHU EXPD Tm({U}, 'B|H') ->'SHU0.T|SHU1.T't{@('C|!C')}
a = ["(B)", "(H)", "(U,B)", "(U,H)"]
b = range(0, 2)
c = ["", "@(C)", "@(!C)"]

result = "<IALUExpdToSHU>"

for i in a:
    for j in b:
	for k in c:
	    s = "EXPD Tm%s->SHU%s.Tt%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALUExpdToSHU>\n"
fp.writelines(result)

#IALUCprsToBIU CPRS (Tm, Tn){({U}, {H})}-> BIU'0|1|2'{@('C|!C')}
a = ["", "(H)", "(U)", "(U,H)"]
b = range(0, 3)
c = ["", "@(C)", "@(!C)"]

result = "<IALUCprsToBIU>"

for i in a:
    for j in b:
	for k in c:
	    s = "CPRS (Tm, Tn)%s->BIU%s%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALUCprsToBIU>\n"
fp.writelines(result)

#IALUCprsToM CPRS (Tm, Tn){({U}, {H})}-> M[t]{@('C|!C')}
a = ["", "(H)", "(U)", "(U,H)"]
b = ["", "@(C)", "@(!C)"]

result = "<IALUCprsToM>"

for i in a:
    for j in b:
	s = "CPRS (Tm, Tn)%s->M[t]%s;" % (i, j)
	result += s
result = result[: -1]
result += "</IALUCprsToM>\n"
fp.writelines(result)

#IALUCprsToMACC CPRS (Tm, Tn){({U}, {H})}->'IALU.T|IMAC.T|FALU.T't{@('C|!C')}
a = ["", "(H)", "(U)", "(U,H)"]
b = ["IALU", "IMAC", "FALU"]
c = ["", "@(C)", "@(!C)"]

result = "<IALUCprsToMACC>"

for i in a:
    for j in b:
	for k in c:
	    s = "CPRS (Tm, Tn)%s->%s.Tt%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALUCprsToMACC>\n"
fp.writelines(result)

#IALUCprsToSHU CPRS (Tm, Tn){({U}, {H})}->'SHU0.T|SHU1.T't{@('C|!C')}
a = ["", "(H)", "(U)", "(U,H)"]
b = range(0, 2)
c = ["", "@(C)", "@(!C)"]

result = "<IALUCprsToSHU>"

for i in a:
    for j in b:
	for k in c:
	    s = "CPRS (Tm, Tn)%s->SHU%s.Tt%s;" % (i, j, k)
	    result += s
result = result[: -1]
result += "</IALUCprsToSHU>\n"
fp.writelines(result)

#IALUDivs Tm DIVS Tn{(U)}-> DIVR{@('C|!C')}
a = ["", "(U)"]
b = ["", "@(C)", "@(!C)"]

result = "<IALUDivs>"

for i in a:
    for j in b:
	s = "Tm DIVS Tn%s->DIVR%s;" % (i, j)
	result += s
result = result[: -1]
result += "</IALUDivs>\n"
fp.writelines(result)

#IALUMdivr MDIVR-> DIVR{@('C|!C')}
a = ["", "@(C)", "@(!C)"]

result = "<IALUMdivr>"

for i in a:
    s = "MDIVR->DIVR%s;" % (i)
    result += s
result = result[: -1]
result += "</IALUMdivr>\n"
fp.writelines(result)

#IALUMdivq MDIVQ-> DIVR{@('C|!C')}
a = ["", "@(C)", "@(!C)"]

result = "<IALUMdivq>"

for i in a:
    s = "MDIVQ->DIVR%s;" % (i)
    result += s
result = result[: -1]
result += "</IALUMdivq>\n"
fp.writelines(result)

#IALUDivq DIVQ-> DIVR{@('C|!C')}
a = ["", "@(C)", "@(!C)"]

result = "<IALUDivq>"

for i in a:
    s = "DIVQ->DIVR%s;" % (i)
    result += s
result = result[: -1]
result += "</IALUDivq>\n"
fp.writelines(result)

#IALUDivrToBIU DIVR -> BIU'0|1|2'{@('C|!C')}
a = range(0, 3)
b = ["", "@(C)", "@(!C)"]

result = "<IALUDivrToBIU>"

for i in a:
    for j in b:
        s = "DIVR->BIU%s%s;" % (i, j)
        result += s
result = result[: -1]
result += "</IALUDivrToBIU>\n"
fp.writelines(result)

#IALUDivrToM DIVR -> M[t]{@('C|!C')}
a = ["", "@(C)", "@(!C)"]

result = "<IALUDivrToM>"

for i in a:
    s = "DIVR->M[t]%s;" % (i)
    result += s
result = result[: -1]
result += "</IALUDivrToM>\n"
fp.writelines(result)

#IALUDivrToMACC DIVR ->'IALU.T|IMAC.T|FALU.T't{@('C|!C')}
a = ["IALU", "IMAC", "FALU"]
b = ["", "@(C)", "@(!C)"]

result = "<IALUDivrToMACC>"

for i in a:
    for j in b:
        s = "DIVR->%s.Tt%s;" % (i, j)
        result += s
result = result[: -1]
result += "</IALUDivrToMACC>\n"
fp.writelines(result)

#IALUDivrToSHU DIVR ->'SHU0.T|SHU1.T't{@('C|!C')}
a = range(0, 2)
b = ["", "@(C)", "@(!C)"]

result = "<IALUDivrToSHU>"

for i in a:
    for j in b:
        s = "DIVR->SHU%s.Tt%s;" % (i, j)
        result += s
result = result[: -1]
result += "</IALUDivrToSHU>\n"
fp.writelines(result)

#IALULtToCond Tm> Tn{({U}, {'B|H'})}-> Cond{@('C|!C')}
a = ["", "(U)", "(B)", "(H)", "(U,B)", "(U,H)"]
b = ["", "@(C)", "@(!C)"]

result = "<IALULtToCond>"

for i in a:
    for j in b:
        s = "Tm&gt;Tn%s->Cond%s;" % (i, j)
        result += s
result = result[: -1]
result += "</IALULtToCond>\n"
fp.writelines(result)

#IALUNstToCond Tm>= Tn{({U}, {'B|H'})}-> Cond{@('C|!C')}
a = ["", "(U)", "(B)", "(H)", "(U,B)", "(U,H)"]
b = ["", "@(C)", "@(!C)"]

result = "<IALUNstToCond>"

for i in a:
    for j in b:
        s = "Tm&gt;=Tn%s->Cond%s;" % (i, j)
        result += s
result = result[: -1]
result += "</IALUNstToCond>\n"
fp.writelines(result)

#IALUStToCond Tm< Tn{({U}, {'B|H'})}-> Cond{@('C|!C')}
a = ["", "(U)", "(B)", "(H)", "(U,B)", "(U,H)"]
b = ["", "@(C)", "@(!C)"]

result = "<IALUStToCond>"

for i in a:
    for j in b:
        s = "Tm&lt;Tn%s->Cond%s;" % (i, j)
        result += s
result = result[: -1]
result += "</IALUStToCond>\n"
fp.writelines(result)

#IALUNltToCond Tm<= Tn{({U}, {'B|H'})}-> Cond{@('C|!C')}
a = ["", "(U)", "(B)", "(H)", "(U,B)", "(U,H)"]
b = ["", "@(C)", "@(!C)"]

result = "<IALUNltToCond>"

for i in a:
    for j in b:
        s = "Tm&lt;=Tn%s->Cond%s;" % (i, j)
        result += s
result = result[: -1]
result += "</IALUNltToCond>\n"
fp.writelines(result)

#IALUEquToCond Tm == Tn{'B|H'}-> Cond{@('C|!C')}
a = ["", "B", "H"]
b = ["", "@(C)", "@(!C)"]

result = "<IALUEquToCond>"

for i in a:
    for j in b:
        s = "Tm==Tn%s->Cond%s;" % (i, j)
        result += s
result = result[: -1]
result += "</IALUEquToCond>\n"
fp.writelines(result)

#IALUNeqToCond Tm != Tn{'B|H'}-> Cond{@('C|!C')}
a = ["", "B", "H"]
b = ["", "@(C)", "@(!C)"]

result = "<IALUNeqToCond>"

for i in a:
    for j in b:
        s = "Tm!=Tn%s->Cond%s;" % (i, j)
        result += s
result = result[: -1]
result += "</IALUNeqToCond>\n"
fp.writelines(result)

#END IALU
result = "</IALU>\n"
fp.writelines(result)

#FALU
result = "<FALU>\n"
fp.writelines(result)

#FALUAddToBIU Tm + Tn({T}, 'S|D')-> BIU'0|1|2'{@('C|!C')}
a = ["S", "D", "T,S", "T,D"]
b = range(0, 3)
c = ["", "@(C)", "@(!C)"]

result = "<FALUAddToBIU>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm+Tn(%s)->BIU%s%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FALUAddToBIU>\n"
fp.writelines(result)

#FALUAddToM Tm + Tn({T}, 'S|D')-> M[t]{@('C|!C')}
a = ["S", "D", "T,S", "T,D"]
b = ["", "@(C)", "@(!C)"]

result = "<FALUAddToM>"

for i in a:
    for j in b:
	s = "Tm+Tn(%s)->M[t]%s;" % (i, j)
        result += s
result = result[: -1]
result += "</FALUAddToM>\n"
fp.writelines(result)

#FALUAddToMACC Tm + Tn({T}, 'S|D')->'IALU.T|IMAC.T|FALU.T|FMAC.T't{@('C|!C')}
a = ["S", "D", "T,S", "T,D"]
b = ["IALU", "IMAC", "FALU", "FMAC"]
c = ["", "@(C)", "@(!C)"]

result = "<FALUAddToMACC>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm+Tn(%s)->%s.Tt%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FALUAddToMACC>\n"
fp.writelines(result)

#FALUAddToSHU Tm + Tn({T}, 'S|D')->'SHU0.T|SHU1.T't{@('C|!C')}
a = ["S", "D", "T,S", "T,D"]
b = range(0, 2)
c = ["", "@(C)", "@(!C)"]

result = "<FALUAddToSHU>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm+Tn(%s)->SHU%s.Tt%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FALUAddToSHU>\n"
fp.writelines(result)

#FALUSubToBIU Tm - Tn({T}, 'S|D')-> BIU'0|1|2'{@('C|!C')}
a = ["S", "D", "T,S", "T,D"]
b = range(0, 3)
c = ["", "@(C)", "@(!C)"]

result = "<FALUSubToBIU>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm-Tn(%s)->BIU%s%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FALUSubToBIU>\n"
fp.writelines(result)

#FALUSubToM Tm - Tn({T}, 'S|D')-> M[t]{@('C|!C')}
a = ["S", "D", "T,S", "T,D"]
b = ["", "@(C)", "@(!C)"]

result = "<FALUSubToM>"

for i in a:
    for j in b:
	s = "Tm-Tn(%s)->M[t]%s;" % (i, j)
        result += s
result = result[: -1]
result += "</FALUSubToM>\n"
fp.writelines(result)

#FALUSubToMACC Tm - Tn({T}, 'S|D')->'IALU.T|IMAC.T|FALU.T|FMAC.T't{@('C|!C')}
a = ["S", "D", "T,S", "T,D"]
b = ["IALU", "IMAC", "FALU", "FMAC"]
c = ["", "@(C)", "@(!C)"]

result = "<FALUSubToMACC>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm-Tn(%s)->%s.Tt%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FALUSubToMACC>\n"
fp.writelines(result)

#FALUSubToSHU Tm - Tn({T}, 'S|D')->'SHU0.T|SHU1.T't{@('C|!C')}
a = ["S", "D", "T,S", "T,D"]
b = range(0, 2)
c = ["", "@(C)", "@(!C)"]

result = "<FALUSubToSHU>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm-Tn(%s)->SHU%s.Tt%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FALUSubToSHU>\n"
fp.writelines(result)

#FALUAddSubToBIU Tm +- Tn(S)-> BIU'0|1|2'{@('C|!C')}
a = range(0, 3)
b = ["", "@(C)", "@(!C)"]

result = "<FALUAddSubToBIU>"

for i in a:
    for j in b:
	s = "Tm+-Tn(S)->BIU%s%s;" % (i, j)
        result += s
result = result[: -1]
result += "</FALUAddSubToBIU>\n"
fp.writelines(result)

#FALUAddSubToM Tm +- Tn(S)-> M[t]{@('C|!C')}
b = ["", "@(C)", "@(!C)"]

result = "<FALUAddSubToM>"

for i in b:
    s = "Tm+-Tn(S)->M[t]%s;" % (i)
    result += s
result = result[: -1]
result += "</FALUAddSubToM>\n"
fp.writelines(result)

#FALUAddSubToMACC Tm +- Tn(S)->'IALU.T|IMAC.T|FALU.T|FMAC.T't{@('C|!C')}
a = ["IALU", "IMAC", "FALU", "FMAC"]
b = ["", "@(C)", "@(!C)"]

result = "<FALUAddSubToMACC>"

for i in a:
    for j in b:
	s = "Tm+-Tn(S)->%s.Tt%s;" % (i, j)
        result += s
result = result[: -1]
result += "</FALUAddSubToMACC>\n"
fp.writelines(result)

#FALUAddSubToSHU Tm +- Tn(S)->'SHU0.T|SHU1.T't{@('C|!C')}
a = range(0, 2)
b = ["", "@(C)", "@(!C)"]

result = "<FALUAddSubToSHU>"

for i in a:
    for j in b:
	s = "Tm+-Tn(S)->SHU%s.Tt%s;" % (i, j)
        result += s
result = result[: -1]
result += "</FALUAddSubToSHU>\n"
fp.writelines(result)

#FALUEquToBIU Tm == Tn('S|D')->BIU'0|1|2'{@('C|!C')}
a = ["S", "D"]
b = range(0, 3)
c = ["", "@(C)", "@(!C)"]

result = "<FALUEquToBIU>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm==Tn(%s)->BIU%s%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FALUEquToBIU>\n"
fp.writelines(result)

#FALUEquToM Tm == Tn('S|D')-> M[t]{@('C|!C')}
a = ["S", "D"]
b = ["", "@(C)", "@(!C)"]

result = "<FALUEquToM>"

for i in a:
    for j in b:
	s = "Tm==Tn(%s)->M[t]%s;" % (i, j)
        result += s
result = result[: -1]
result += "</FALUEquToM>\n"
fp.writelines(result)

#FALUEquToMACC Tm == Tn('S|D')->'IALU.T|IMAC.T|FALU.T|FMAC.T't{@('C|!C')}
a = ["S", "D"]
b = ["IALU", "IMAC", "FALU", "FMAC"]
c = ["", "@(C)", "@(!C)"]

result = "<FALUEquToMACC>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm==Tn(%s)->%s.Tt%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FALUEquToMACC>\n"
fp.writelines(result)

#FALUEquToSHU Tm == Tn('S|D')->'SHU0.T|SHU1.T't{@('C|!C')}
a = ["S", "D"]
b = range(0, 2)
c = ["", "@(C)", "@(!C)"]

result = "<FALUEquToSHU>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm==Tn(%s)->SHU%s.Tt%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FALUEquToSHU>\n"
fp.writelines(result)

#FALUNeqToBIU Tm != Tn('S|D')-> BIU'0|1|2'{@('C|!C')}
a = ["S", "D"]
b = range(0, 3)
c = ["", "@(C)", "@(!C)"]

result = "<FALUNeqToBIU>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm!=Tn(%s)->BIU%s%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FALUNeqToBIU>\n"
fp.writelines(result)

#FALUNeqToM Tm != Tn('S|D')-> M[t]{@('C|!C')}
a = ["S", "D"]
b = ["", "@(C)", "@(!C)"]

result = "<FALUNeqToM>"

for i in a:
    for j in b:
	s = "Tm!=Tn(%s)->M[t]%s;" % (i, j)
        result += s
result = result[: -1]
result += "</FALUNeqToM>\n"
fp.writelines(result)

#FALUNeqToMACC Tm != Tn('S|D')->'IALU.T|IMAC.T|FALU.T|FMAC.T't{@('C|!C')}
a = ["S", "D"]
b = ["IALU", "IMAC", "FALU", "FMAC"]
c = ["", "@(C)", "@(!C)"]

result = "<FALUNeqToMACC>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm!=Tn(%s)->%s.Tt%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FALUNeqToMACC>\n"
fp.writelines(result)

#FALUNeqToSHU Tm != Tn('S|D')->'SHU0.T|SHU1.T't{@('C|!C')}
a = ["S", "D"]
b = range(0, 2)
c = ["", "@(C)", "@(!C)"]

result = "<FALUNeqToSHU>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm!=Tn(%s)->SHU%s.Tt%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FALUNeqToSHU>\n"
fp.writelines(result)

#FALULtToBIU Tm> Tn('S|D')-> BIU'0|1|2'{@('C|!C')}
a = ["S", "D"]
b = range(0, 3)
c = ["", "@(C)", "@(!C)"]

result = "<FALULtToBIU>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm&gt;Tn(%s)->BIU%s%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FALULtToBIU>\n"
fp.writelines(result)

#FALULtToM Tm> Tn('S|D')-> M[t]{@('C|!C')}
a = ["S", "D"]
b = ["", "@(C)", "@(!C)"]

result = "<FALULtToM>"

for i in a:
    for j in b:
	s = "Tm&gt;Tn(%s)->M[t]%s;" % (i, j)
        result += s
result = result[: -1]
result += "</FALULtToM>\n"
fp.writelines(result)

#FALULtToMACC Tm> Tn('S|D')->'IALU.T|IMAC.T|FALU.T|FMAC.T't{@('C|!C')}
a = ["S", "D"]
b = ["IALU", "IMAC", "FALU", "FMAC"]
c = ["", "@(C)", "@(!C)"]

result = "<FALULtToMACC>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm&gt;Tn(%s)->%s.Tt%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FALULtToMACC>\n"
fp.writelines(result)

#FALULtToSHU Tm> Tn('S|D')->'SHU0.T|SHU1.T't{@('C|!C')}
a = ["S", "D"]
b = range(0, 2)
c = ["", "@(C)", "@(!C)"]

result = "<FALULtToSHU>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm&gt;Tn(%s)->SHU%s.Tt%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FALULtToSHU>\n"
fp.writelines(result)

#FALUNstToBIU Tm>= Tn('S|D')-> BIU'0|1|2'{@('C|!C')}
a = ["S", "D"]
b = range(0, 3)
c = ["", "@(C)", "@(!C)"]

result = "<FALUNstToBIU>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm&gt;=Tn(%s)->BIU%s%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FALUNstToBIU>\n"
fp.writelines(result)

#FALUNstToM Tm>= Tn('S|D')-> M[t]{@('C|!C')}
a = ["S", "D"]
b = ["", "@(C)", "@(!C)"]

result = "<FALUNstToM>"

for i in a:
    for j in b:
	s = "Tm&gt;=Tn(%s)->M[t]%s;" % (i, j)
        result += s
result = result[: -1]
result += "</FALUNstToM>\n"
fp.writelines(result)

#FALUNstToMACC Tm>= Tn('S|D')->'IALU.T|IMAC.T|FALU.T|FMAC.T't{@('C|!C')}
a = ["S", "D"]
b = ["IALU", "IMAC", "FALU", "FMAC"]
c = ["", "@(C)", "@(!C)"]

result = "<FALUNstToMACC>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm&gt;=Tn(%s)->%s.Tt%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FALUNstToMACC>\n"
fp.writelines(result)

#FALUNstToSHU Tm>= Tn('S|D')->'SHU0.T|SHU1.T't{@('C|!C')}
a = ["S", "D"]
b = range(0, 2)
c = ["", "@(C)", "@(!C)"]

result = "<FALUNstToSHU>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm&gt;=Tn(%s)->SHU%s.Tt%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FALUNstToSHU>\n"
fp.writelines(result)

#FALUStToBIU Tm< Tn('S|D')-> BIU'0|1|2'{@('C|!C')}
a = ["S", "D"]
b = range(0, 3)
c = ["", "@(C)", "@(!C)"]

result = "<FALUStToBIU>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm&lt;Tn(%s)->BIU%s%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FALUStToBIU>\n"
fp.writelines(result)

#FALUStToM Tm< Tn('S|D')-> M[t]{@('C|!C')}
a = ["S", "D"]
b = ["", "@(C)", "@(!C)"]

result = "<FALUStToM>"

for i in a:
    for j in b:
	s = "Tm&lt;Tn(%s)->M[t]%s;" % (i, j)
        result += s
result = result[: -1]
result += "</FALUStToM>\n"
fp.writelines(result)

#FALUStToMACC Tm< Tn('S|D')->'IALU.T|IMAC.T|FALU.T|FMAC.T't{@('C|!C')}
a = ["S", "D"]
b = ["IALU", "IMAC", "FALU", "FMAC"]
c = ["", "@(C)", "@(!C)"]

result = "<FALUStToMACC>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm&lt;Tn(%s)->%s.Tt%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FALUStToMACC>\n"
fp.writelines(result)

#FALUStToSHU Tm< Tn('S|D')->'SHU0.T|SHU1.T't{@('C|!C')}
a = ["S", "D"]
b = range(0, 2)
c = ["", "@(C)", "@(!C)"]

result = "<FALUStToSHU>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm&lt;Tn(%s)->SHU%s.Tt%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FALUStToSHU>\n"
fp.writelines(result)

#FALUNltToBIU Tm<= Tn('S|D')-> BIU'0|1|2'{@('C|!C')}
a = ["S", "D"]
b = range(0, 3)
c = ["", "@(C)", "@(!C)"]

result = "<FALUNltToBIU>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm&lt;=Tn(%s)->BIU%s%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FALUNltToBIU>\n"
fp.writelines(result)

#FALUNltToM Tm<= Tn('S|D')-> M[t]{@('C|!C')}
a = ["S", "D"]
b = ["", "@(C)", "@(!C)"]

result = "<FALUNltToM>"

for i in a:
    for j in b:
	s = "Tm&lt;=Tn(%s)->M[t]%s;" % (i, j)
        result += s
result = result[: -1]
result += "</FALUNltToM>\n"
fp.writelines(result)

#FALUNltToMACC Tm<= Tn('S|D')->'IALU.T|IMAC.T|FALU.T|FMAC.T't{@('C|!C')}
a = ["S", "D"]
b = ["IALU", "IMAC", "FALU", "FMAC"]
c = ["", "@(C)", "@(!C)"]

result = "<FALUNltToMACC>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm&lt;=Tn(%s)->%s.Tt%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FALUNltToMACC>\n"
fp.writelines(result)

#FALUNltToSHU Tm<= Tn('S|D')->'SHU0.T|SHU1.T't{@('C|!C')}
a = ["S", "D"]
b = range(0, 2)
c = ["", "@(C)", "@(!C)"]

result = "<FALUNltToSHU>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm&lt;=Tn(%s)->SHU%s.Tt%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FALUNltToSHU>\n"
fp.writelines(result)

#FALUAbsToBIU ABS Tm('S|D') -> BIU'0|1|2'{@('C|!C')}
a = ["S", "D"]
b = range(0, 3)
c = ["", "@(C)", "@(!C)"]

result = "<FALUAbsToBIU>"

for i in a:
    for j in b:
	for k in c:
	    s = "ABS Tm(%s)->BIU%s%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FALUAbsToBIU>\n"
fp.writelines(result)

#FALUAbsToM ABS Tm('S|D') -> M[t]{@('C|!C')}
a = ["S", "D"]
b = ["", "@(C)", "@(!C)"]

result = "<FALUAbsToM>"

for i in a:
    for j in b:
	s = "ABS Tm(%s)->M[t]%s;" % (i, j)
        result += s
result = result[: -1]
result += "</FALUAbsToM>\n"
fp.writelines(result)

#FALUAbsToMACC ABS Tm('S|D') ->'IALU.T|IMAC.T|FALU.T|FMAC.T't{@('C|!C')}
a = ["S", "D"]
b = ["IALU", "IMAC", "FALU", "FMAC"]
c = ["", "@(C)", "@(!C)"]

result = "<FALUAbsToMACC>"

for i in a:
    for j in b:
	for k in c:
	    s = "ABS Tm(%s)->%s.Tt%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FALUAbsToMACC>\n"
fp.writelines(result)

#FALUAbsToSHU ABS Tm('S|D') ->'SHU0.T|SHU1.T't{@('C|!C')}
a = ["S", "D"]
b = range(0, 2)
c = ["", "@(C)", "@(!C)"]

result = "<FALUAbsToSHU>"

for i in a:
    for j in b:
	for k in c:
	    s = "ABS Tm(%s)->SHU%s.Tt%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FALUAbsToSHU>\n"
fp.writelines(result)

#FALURecipToBIU RECIP Tm('S|D') -> BIU'0|1|2'{@('C|!C')}
a = ["S", "D"]
b = range(0, 3)
c = ["", "@(C)", "@(!C)"]

result = "<FALURecipToBIU>"

for i in a:
    for j in b:
	for k in c:
	    s = "RECIP Tm(%s)->BIU%s%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FALURecipToBIU>\n"
fp.writelines(result)

#FALURecipToM RECIP Tm('S|D') -> M[t]{@('C|!C')}
a = ["S", "D"]
b = ["", "@(C)", "@(!C)"]

result = "<FALURecipToM>"

for i in a:
    for j in b:
	s = "RECIP Tm(%s)->M[t]%s;" % (i, j)
        result += s
result = result[: -1]
result += "</FALURecipToM>\n"
fp.writelines(result)

#FALURecipToMACC RECIP Tm('S|D') ->'IALU.T|IMAC.T|FALU.T|FMAC.T't{@('C|!C')}
a = ["S", "D"]
b = ["IALU", "IMAC", "FALU", "FMAC"]
c = ["", "@(C)", "@(!C)"]

result = "<FALURecipToMACC>"

for i in a:
    for j in b:
	for k in c:
	    s = "RECIP Tm(%s)->%s.Tt%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FALURecipToMACC>\n"
fp.writelines(result)

#FALURecipToSHU RECIP Tm('S|D') ->'SHU0.T|SHU1.T't{@('C|!C')}
a = ["S", "D"]
b = range(0, 2)
c = ["", "@(C)", "@(!C)"]

result = "<FALURecipToSHU>"

for i in a:
    for j in b:
	for k in c:
	    s = "RECIP Tm(%s)->SHU%s.Tt%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FALURecipToSHU>\n"
fp.writelines(result)

#FALURsqrtToBIU RSQRT Tm('S|D') -> BIU'0|1|2'{@('C|!C')}
a = ["S", "D"]
b = range(0, 3)
c = ["", "@(C)", "@(!C)"]

result = "<FALURsqrtToBIU>"

for i in a:
    for j in b:
	for k in c:
	    s = "RSQRT Tm(%s)->BIU%s%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FALURsqrtToBIU>\n"
fp.writelines(result)

#FALURsqrtToM RSQRT Tm('S|D') -> M[t]{@('C|!C')}
a = ["S", "D"]
b = ["", "@(C)", "@(!C)"]

result = "<FALURsqrtToM>"

for i in a:
    for j in b:
	s = "RSQRT Tm(%s)->M[t]%s;" % (i, j)
        result += s
result = result[: -1]
result += "</FALURsqrtToM>\n"
fp.writelines(result)

#FALURsqrtToMACC RSQRT Tm('S|D') ->'IALU.T|IMAC.T|FALU.T|FMAC.T't{@('C|!C')}
a = ["S", "D"]
b = ["IALU", "IMAC", "FALU", "FMAC"]
c = ["", "@(C)", "@(!C)"]

result = "<FALURsqrtToMACC>"

for i in a:
    for j in b:
	for k in c:
	    s = "RSQRT Tm(%s)->%s.Tt%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FALURsqrtToMACC>\n"
fp.writelines(result)

#FALURsqrtToSHU RSQRT Tm('S|D') ->'SHU0.T|SHU1.T't{@('C|!C')}
a = ["S", "D"]
b = range(0, 2)
c = ["", "@(C)", "@(!C)"]

result = "<FALURsqrtToSHU>"

for i in a:
    for j in b:
	for k in c:
	    s = "RSQRT Tm(%s)->SHU%s.Tt%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FALURsqrtToSHU>\n"
fp.writelines(result)

#FALUToSingleToBIU SINGLE Tm{({T}, {'U|D'})}-> BIU'0|1|2'{@('C|!C')}
a = ["", "(T)", "(U)", "(D)", "(T,U)", "(T,D)"]
b = range(0, 3)
c = ["", "@(C)", "@(!C)"]

result = "<FALUToSingleToBIU>"

for i in a:
    for j in b:
	for k in c:
	    s = "SINGLE Tm%s->BIU%s%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FALUToSingleToBIU>\n"
fp.writelines(result)

#FALUToSingleToM SINGLE Tm{({T}, {'U|D'})}-> M[t]{@('C|!C')}
a = ["", "(T)", "(U)", "(D)", "(T,U)", "(T,D)"]
b = ["", "@(C)", "@(!C)"]

result = "<FALUToSingleToM>"

for i in a:
    for j in b:
	s = "SINGLE Tm%s->M[t]%s;" % (i, j)
        result += s
result = result[: -1]
result += "</FALUToSingleToM>\n"
fp.writelines(result)

#FALUToSingleToMACC SINGLE Tm{({T}, {'U|D'})}->'IALU.T|IMAC.T|FALU.T|FMAC.T't{@('C|!C')}
a = ["", "(T)", "(U)", "(D)", "(T,U)", "(T,D)"]
b = ["IALU", "IMAC", "FALU", "FMAC"]
c = ["", "@(C)", "@(!C)"]

result = "<FALUToSingleToMACC>"

for i in a:
    for j in b:
	for k in c:
	    s = "SINGLE Tm%s->%s.Tt%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FALUToSingleToMACC>\n"
fp.writelines(result)

#FALUToSingleToSHU SINGLE Tm{({T}, {'U|D'})}->'SHU0.T|SHU1.T't{@('C|!C')}
a = ["", "(T)", "(U)", "(D)", "(T,U)", "(T,D)"]
b = range(0, 2)
c = ["", "@(C)", "@(!C)"]

result = "<FALUToSingleToSHU>"

for i in a:
    for j in b:
	for k in c:
	    s = "SINGLE Tm%s->SHU%s.Tt%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FALUToSingleToSHU>\n"
fp.writelines(result)

#FALUToDoubleToBIU DOUBLE Tm{({T}, {'U|S'})}-> BIU'0|1|2'{@('C|!C')}
a = ["", "(T)", "(U)", "(S)", "(T,U)", "(T,S)"]
b = range(0, 3)
c = ["", "@(C)", "@(!C)"]

result = "<FALUToDoubleToBIU>"

for i in a:
    for j in b:
	for k in c:
	    s = "DOUBLE Tm%s->BIU%s%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FALUToDoubleToBIU>\n"
fp.writelines(result)

#FALUToDoubleToM DOUBLE Tm{({T}, {'U|S'})}-> M[t]{@('C|!C')}
a = ["", "(T)", "(U)", "(S)", "(T,U)", "(T,S)"]
b = ["", "@(C)", "@(!C)"]

result = "<FALUToDoubleToM>"

for i in a:
    for j in b:
	s = "DOUBLE Tm%s->M[t]%s;" % (i, j)
        result += s
result = result[: -1]
result += "</FALUToDoubleToM>\n"
fp.writelines(result)

#FALUToDoubleToMACC DOUBLE Tm{({T}, {'U|S'})}->'IALU.T|IMAC.T|FALU.T|FMAC.T't{@('C|!C')}
a = ["", "(T)", "(U)", "(S)", "(T,U)", "(T,S)"]
b = ["IALU", "IMAC", "FALU", "FMAC"]
c = ["", "@(C)", "@(!C)"]

result = "<FALUToDoubleToMACC>"

for i in a:
    for j in b:
	for k in c:
	    s = "DOUBLE Tm%s->%s.Tt%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FALUToDoubleToMACC>\n"
fp.writelines(result)

#FALUToDoubleToSHU DOUBLE Tm{({T}, {'U|S'})}->'SHU0.T|SHU1.T't{@('C|!C')}
a = ["", "(T)", "(U)", "(S)", "(T,U)", "(T,S)"]
b = range(0, 2)
c = ["", "@(C)", "@(!C)"]

result = "<FALUToDoubleToSHU>"

for i in a:
    for j in b:
	for k in c:
	    s = "DOUBLE Tm%s->SHU%s.Tt%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FALUToDoubleToSHU>\n"
fp.writelines(result)

#FALUToIntToBIU INT Tm({T}, 'S|D')-> BIU'0|1|2'{@('C|!C')}
a = ["(S)", "(D)", "(T,S)", "(T,D)"]
b = range(0, 3)
c = ["", "@(C)", "@(!C)"]

result = "<FALUToIntToBIU>"

for i in a:
    for j in b:
	for k in c:
	    s = "INT Tm%s->BIU%s%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FALUToIntToBIU>\n"
fp.writelines(result)

#FALUToIntToM INT Tm({T}, 'S|D')-> M[t]{@('C|!C')}
a = ["(S)", "(D)", "(T,S)", "(T,D)"]
b = ["", "@(C)", "@(!C)"]

result = "<FALUToIntToM>"

for i in a:
    for j in b:
	s = "INT Tm%s->M[t]%s;" % (i, j)
        result += s
result = result[: -1]
result += "</FALUToIntToM>\n"
fp.writelines(result)

#FALUToIntToMACC INT Tm({T}, 'S|D')->'IALU.T|IMAC.T|FALU.T|FMAC.T't{@('C|!C')}
a = ["(S)", "(D)", "(T,S)", "(T,D)"]
b = ["IALU", "IMAC", "FALU", "FMAC"]
c = ["", "@(C)", "@(!C)"]

result = "<FALUToIntToMACC>"

for i in a:
    for j in b:
	for k in c:
	    s = "INT Tm%s->%s.Tt%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FALUToIntToMACC>\n"
fp.writelines(result)

#FALUToIntToSHU INT Tm({T}, 'S|D')->'SHU0.T|SHU1.T't{@('C|!C')}
a = ["(S)", "(D)", "(T,S)", "(T,D)"]
b = range(0, 2)
c = ["", "@(C)", "@(!C)"]

result = "<FALUToIntToSHU>"

for i in a:
    for j in b:
	for k in c:
	    s = "INT Tm%s->SHU%s.Tt%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FALUToIntToSHU>\n"
fp.writelines(result)

#FALUToUintToBIU UINT Tm({T}, 'S|D')-> BIU'0|1|2'{@('C|!C')}
a = ["(S)", "(D)", "(T,S)", "(T,D)"]
b = range(0, 3)
c = ["", "@(C)", "@(!C)"]

result = "<FALUToUintToBIU>"

for i in a:
    for j in b:
	for k in c:
	    s = "UINT Tm%s->BIU%s%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FALUToUintToBIU>\n"
fp.writelines(result)

#FALUToUintToM UINT Tm({T}, 'S|D')-> M[t]{@('C|!C')}
a = ["(S)", "(D)", "(T,S)", "(T,D)"]
b = ["", "@(C)", "@(!C)"]

result = "<FALUToUintToM>"

for i in a:
    for j in b:
	s = "UINT Tm%s->M[t]%s;" % (i, j)
        result += s
result = result[: -1]
result += "</FALUToUintToM>\n"
fp.writelines(result)

#FALUToUintToMACC UINT Tm({T}, 'S|D')->'IALU.T|IMAC.T|FALU.T|FMAC.T't{@('C|!C')}
a = ["(S)", "(D)", "(T,S)", "(T,D)"]
b = ["IALU", "IMAC", "FALU", "FMAC"]
c = ["", "@(C)", "@(!C)"]

result = "<FALUToUintToMACC>"

for i in a:
    for j in b:
	for k in c:
	    s = "UINT Tm%s->%s.Tt%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FALUToUintToMACC>\n"
fp.writelines(result)

#FALUToUintToSHU UINT Tm({T}, 'S|D')->'SHU0.T|SHU1.T't{@('C|!C')}
a = ["(S)", "(D)", "(T,S)", "(T,D)"]
b = range(0, 2)
c = ["", "@(C)", "@(!C)"]

result = "<FALUToUintToSHU>"

for i in a:
    for j in b:
	for k in c:
	    s = "UINT Tm%s->SHU%s.Tt%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FALUToUintToSHU>\n"
fp.writelines(result)

#FALUMaxToBIU MAX(Tm,Tn)('S|D')->BIU'0|1|2'{@('C|!C')}
a = ["S", "D"]
b = range(0, 3)
c = ["", "@(C)", "@(!C)"]

result = "<FALUMaxToBIU>"

for i in a:
    for j in b:
	for k in c:
	    s = "MAX(Tm,Tn)(%s)->BIU%s%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FALUMaxToBIU>\n"
fp.writelines(result)

#FALUMaxToM MAX(Tm,Tn)('S|D')-> M[t]{@('C|!C')}
a = ["S", "D"]
b = ["", "@(C)", "@(!C)"]

result = "<FALUMaxToM>"

for i in a:
    for j in b:
	s = "MAX(Tm,Tn)(%s)->M[t]%s;" % (i, j)
        result += s
result = result[: -1]
result += "</FALUMaxToM>\n"
fp.writelines(result)

#FALUMaxToMACC MAX(Tm,Tn)('S|D') ->'IALU.T|IMAC.T|FALU.T|FMAC.T't{@('C|!C')}
a = ["S", "D"]
b = ["IALU", "IMAC", "FALU", "FMAC"]
c = ["", "@(C)", "@(!C)"]

result = "<FALUMaxToMACC>"

for i in a:
    for j in b:
	for k in c:
	    s = "MAX(Tm,Tn)(%s)->%s.Tt%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FALUMaxToMACC>\n"
fp.writelines(result)

#FALUMaxToSHU MAX(Tm,Tn)('S|D') ->'SHU0.T|SHU1.T't{@('C|!C')}
a = ["S", "D"]
b = range(0, 2)
c = ["", "@(C)", "@(!C)"]

result = "<FALUMaxToSHU>"

for i in a:
    for j in b:
	for k in c:
	    s = "MAX(Tm,Tn)(%s)->SHU%s.Tt%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FALUMaxToSHU>\n"
fp.writelines(result)

#FALUMinToBIU MIN(Tm,Tn)('S|D') ->BIU'0|1|2'{@('C|!C')}
a = ["S", "D"]
b = range(0, 3)
c = ["", "@(C)", "@(!C)"]

result = "<FALUMinToBIU>"

for i in a:
    for j in b:
	for k in c:
	    s = "MIN(Tm,Tn)(%s)->BIU%s%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FALUMinToBIU>\n"
fp.writelines(result)

#FALUMinToM MIN(Tm,Tn)('S|D') -> M[t]{@('C|!C')}
a = ["S", "D"]
b = ["", "@(C)", "@(!C)"]

result = "<FALUMinToM>"

for i in a:
    for j in b:
	s = "MIN(Tm,Tn)(%s)->M[t]%s;" % (i, j)
        result += s
result = result[: -1]
result += "</FALUMinToM>\n"
fp.writelines(result)

#FALUMinToMACC MIN(Tm,Tn)('S|D') ->'IALU.T|IMAC.T|FALU.T|FMAC.T't{@('C|!C')}
a = ["S", "D"]
b = ["IALU", "IMAC", "FALU", "FMAC"]
c = ["", "@(C)", "@(!C)"]

result = "<FALUMinToMACC>"

for i in a:
    for j in b:
	for k in c:
	    s = "MIN(Tm,Tn)(%s)->%s.Tt%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FALUMinToMACC>\n"
fp.writelines(result)

#FALUMinToSHU MIN(Tm,Tn)('S|D') ->'SHU0.T|SHU1.T't{@('C|!C')}
a = ["S", "D"]
b = range(0, 2)
c = ["", "@(C)", "@(!C)"]

result = "<FALUMinToSHU>"

for i in a:
    for j in b:
	for k in c:
	    s = "MIN(Tm,Tn)(%s)->SHU%s.Tt%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FALUMinToSHU>\n"
fp.writelines(result)

#END FALU
result = "</FALU>\n"
fp.writelines(result)

#IMAC
result = "<IMAC>\n"
fp.writelines(result)

#IMACMulTToBIU Tm* Tn({U}, T, {I}, {'B|H'})-> BIU'0|1|2'{@('C|!C')} 
a = ["T", "T,I", "T,B", "T,H", "T,U", "T,U,I", "T,U,B", "T,U,H", "T,I,B", "T,I,H", "T,U,I,B", "T,U,I,H"]
b = range(0, 3)
c = ["", "@(C)", "@(!C)"]

result = "<IMACMulTToBIU>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm*Tn(%s)->BIU%s%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</IMACMulTToBIU>\n"
fp.writelines(result)

#IMACMulTToM Tm* Tn({U}, T, {I}, {'B|H'})->M[t]{@('C|!C')}
a = ["T", "T,I", "T,B", "T,H", "T,U", "T,U,I", "T,U,B", "T,U,H", "T,I,B", "T,I,H", "T,U,I,B", "T,U,I,H"]
b = ["", "@(C)", "@(!C)"]

result = "<IMACMulTToM>"

for i in a:
    for j in b:
	s = "Tm*Tn(%s)->M[t]%s;" % (i, j)
        result += s
result = result[: -1]
result += "</IMACMulTToM>\n"
fp.writelines(result)

#IMACMulTToMACC Tm* Tn({U}, T, {I}, {'B|H'})->'IALU.T|IMAC.T|FALU.T't{@('C|!C')}
a = ["T", "T,I", "T,B", "T,H", "T,U", "T,U,I", "T,U,B", "T,U,H", "T,I,B", "T,I,H", "T,U,I,B", "T,U,I,H"]
b = ["IALU", "IMAC", "FALU"]
c = ["", "@(C)", "@(!C)"]

result = "<IMACMulTToMACC>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm*Tn(%s)->%s.Tt%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</IMACMulTToMACC>\n"
fp.writelines(result)

#IMACMulTToSHU Tm* Tn({U}, T, {I}, {'B|H'})->'SHU0.Tt|SHU1.Tt'{@('C|!C')}
a = ["T", "T,I", "T,B", "T,H", "T,U", "T,U,I", "T,U,B", "T,U,H", "T,I,B", "T,I,H", "T,U,I,B", "T,U,I,H"]
b = range(0, 2)
c = ["", "@(C)", "@(!C)"]

result = "<IMACMulTToSHU>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm*Tn(%s)->SHU%s.Tt%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</IMACMulTToSHU>\n"
fp.writelines(result)

#IMACMulToBIU Tm* Tn({U}, {I}, 'B|H')-> BIU'0|1|2'{@('C|!C')}
a = ["B", "H", "U,B", "U,H", "I,B", "I,H", "U,I,B", "U,I,H"]
b = range(0, 3)
c = ["", "@(C)", "@(!C)"]

result = "<IMACMulToBIU>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm*Tn(%s)->BIU%s%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</IMACMulToBIU>\n"
fp.writelines(result)

#IMACMulToM Tm* Tn({U}, {I}, 'B|H')->M[t]{@('C|!C')}
a = ["B", "H", "U,B", "U,H", "I,B", "I,H", "U,I,B", "U,I,H"]
b = ["", "@(C)", "@(!C)"]

result = "<IMACMulToM>"

for i in a:
    for j in b:
	s = "Tm*Tn(%s)->M[t]%s;" % (i, j)
        result += s
result = result[: -1]
result += "</IMACMulToM>\n"
fp.writelines(result)

#IMACMulToMACC Tm* Tn({U}, {I}, 'B|H')->'IALU.T|IMAC.T|FALU.T't{@('C|!C')}
a = ["B", "H", "U,B", "U,H", "I,B", "I,H", "U,I,B", "U,I,H"]
b = ["IALU", "IMAC", "FALU"]
c = ["", "@(C)", "@(!C)"]

result = "<IMACMulToMACC>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm*Tn(%s)->%s.Tt%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</IMACMulToMACC>\n"
fp.writelines(result)

#IMACMulToSHU Tm* Tn({U}, {I}, 'B|H')->'SHU0.Tt|SHU1.Tt'{@('C|!C')}
a = ["B", "H", "U,B", "U,H", "I,B", "I,H", "U,I,B", "U,I,H"]
b = range(0, 2)
c = ["", "@(C)", "@(!C)"]

result = "<IMACMulToSHU>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm*Tn(%s)->SHU%s.Tt%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</IMACMulToSHU>\n"
fp.writelines(result)

#IMACMASToBIU Tp +- Tm* Tn(H)-> BIU'0|1|2'{@('C|!C')}
a = range(0, 3)
b = ["", "@(C)", "@(!C)"]

result = "<IMACMASToBIU>"

for i in a:
    for j in b:
	s = "Tp+-Tm*Tn(H)->BIU%s%s;" % (i, j)
        result += s
result = result[: -1]
result += "</IMACMASToBIU>\n"
fp.writelines(result)

#IMACMASToM Tp +- Tm* Tn(H)-> M[t]{@('C|!C')}
a = ["", "@(C)", "@(!C)"]

result = "<IMACMASToM>"

for i in a:
    s = "Tp+-Tm*Tn(H)->M[t]%s;" % (i)
    result += s
result = result[: -1]
result += "</IMACMASToM>\n"
fp.writelines(result)

#IMACMASToMACC Tp +- Tm* Tn(H)->'IALU.T|IMAC.T|FALU.T't{@('C|!C')}
a = ["IALU", "IMAC", "FALU"]
b = ["", "@(C)", "@(!C)"]

result = "<IMACMASToMACC>"

for i in a:
    for j in b:
	s = "Tp+-Tm*Tn(H)->%s.Tt%s;" % (i, j)
        result += s
result = result[: -1]
result += "</IMACMASToMACC>\n"
fp.writelines(result)

#IMACMASToSHU Tp +- Tm* Tn(H)->'SHU0.Tt|SHU1.Tt'{@('C|!C')}
a = range(0, 2)
b = ["", "@(C)", "@(!C)"]

result = "<IMACMASToSHU>"

for i in a:
    for j in b:
	s = "Tp+-Tm*Tn(H)->SHU%s.Tt%s;" % (i, j)
        result += s
result = result[: -1]
result += "</IMACMASToSHU>\n"
fp.writelines(result)

#IMACMA MR <- Tp + Tm* Tn{({U}, {'B|H'})}{@('C|!C')}
a = ["", "(U)", "(B)", "(H)", "(U,B)", "(U,H)"]
b = ["", "@(C)", "@(!C)"]

result = "<IMACMA>"

for i in a:
    for j in b:
	s = "MR&lt;-Tp+Tm*Tn%s%s;" % (i, j)
        result += s
result = result[: -1]
result += "</IMACMA>\n"
fp.writelines(result)

#IMACMaC MR += Tm* Tn{({U}, {CR}, {'B|H'})}{@('C|!C')}
a = ["", "(U)", "(CR)", "(B)", "(H)", "(U,CR)", "(U,B)", "(U,H)", "(CR,B)", "(CR,H)", "(U,CR,B)", "(U,CR,H)"]
b = ["", "@(C)", "@(!C)"]

result = "<IMACMaC>"

for i in a:
    for j in b:
	s = "MR+=Tm*Tn%s%s;" % (i, j)
        result += s
result = result[: -1]
result += "</IMACMaC>\n"
fp.writelines(result)

#IMACMaCToBIU MR += Tm* Tn{({U}, {CR}, {'B|H'})}-> BIU'0|1|2'{@('C|!C')}
a = ["", "(U)", "(CR)", "(B)", "(H)", "(U,CR)", "(U,B)", "(U,H)", "(CR,B)", "(CR,H)", "(U,CR,B)", "(U,CR,H)"]
b = range(0, 3)
c = ["", "@(C)", "@(!C)"]

result = "<IMACMaCToBIU>"

for i in a:
    for j in b:
	for k in c:
	    s = "MR+=Tm*Tn%s->BIU%s%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</IMACMaCToBIU>\n"
fp.writelines(result)

#IMACMaCToM MR += Tm* Tn{({U}, {CR}, {'B|H'})}-> M[t]{@('C|!C')}
a = ["", "(U)", "(CR)", "(B)", "(H)", "(U,CR)", "(U,B)", "(U,H)", "(CR,B)", "(CR,H)", "(U,CR,B)", "(U,CR,H)"]
b = ["", "@(C)", "@(!C)"]

result = "<IMACMaCToM>"

for i in a:
    for j in b:
	s = "MR+=Tm*Tn%s->M[t]%s;" % (i, j)
        result += s
result = result[: -1]
result += "</IMACMaCToM>\n"
fp.writelines(result)

#IMACMaCToMACC MR += Tm* Tn{({U}, {CR}, {'B|H'})}->'IALU.T|IMAC.T|FALU.T't{@('C|!C')}
a = ["", "(U)", "(CR)", "(B)", "(H)", "(U,CR)", "(U,B)", "(U,H)", "(CR,B)", "(CR,H)", "(U,CR,B)", "(U,CR,H)"]
b = ["IALU", "IMAC", "FALU"]
c = ["", "@(C)", "@(!C)"]

result = "<IMACMaCToMACC>"

for i in a:
    for j in b:
	for k in c:
	    s = "MR+=Tm*Tn%s->%s.Tt%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</IMACMaCToMACC>\n"
fp.writelines(result)

#IMACMaCToSHU MR += Tm* Tn{({U}, {CR}, {'B|H'})}->'SHU0.Tt|SHU1.Tt'{@('C|!C')}
a = ["", "(U)", "(CR)", "(B)", "(H)", "(U,CR)", "(U,B)", "(U,H)", "(CR,B)", "(CR,H)", "(U,CR,B)", "(U,CR,H)"]
b = ["SHU0", "SHU1"]
c = ["", "@(C)", "@(!C)"]

result = "<IMACMaCToSHU>"

for i in a:
    for j in b:
	for k in c:
	    s = "MR+=Tm*Tn%s->%s.Tt%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</IMACMaCToSHU>\n"
fp.writelines(result)

#IMACMaCLToBIU MR += Tm* Tn{({U}, L, {CR}, {'B|H'})}-> BIU'0|1|2'{@('C|!C')}
a = ["", "L", "(L,U)", "(L,CR)", "(L,B)", "(L,H)", "(L,U,CR)", "(L,U,B)", "(L,U,H)", "(L,CR,B)", "(L,CR,H)", "(L,U,CR,B)", "(L,U,CR,H)"]
b = range(0, 3)
c = ["", "@(C)", "@(!C)"]

result = "<IMACMaCLToBIU>"

for i in a:
    for j in b:
	for k in c:
	    s = "MR+=Tm*Tn%s->BIU%s%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</IMACMaCLToBIU>\n"
fp.writelines(result)

#IMACMaCLToM MR += Tm* Tn{({U}, L, {CR}, {'B|H'})}-> M[t]{@('C|!C')}
a = ["", "L", "(L,U)", "(L,CR)", "(L,B)", "(L,H)", "(L,U,CR)", "(L,U,B)", "(L,U,H)", "(L,CR,B)", "(L,CR,H)", "(L,U,CR,B)", "(L,U,CR,H)"]
b = ["", "@(C)", "@(!C)"]

result = "<IMACMaCLToM>"

for i in a:
    for j in b:
	s = "MR+=Tm*Tn%s->M[t]%s;" % (i, j)
        result += s
result = result[: -1]
result += "</IMACMaCLToM>\n"
fp.writelines(result)

#IMACMaCLToMACC MR += Tm* Tn{({U}, L, {CR}, {'B|H'})}->'IALU.T|IMAC.T|FALU.T't{@('C|!C')}
a = ["", "L", "(L,U)", "(L,CR)", "(L,B)", "(L,H)", "(L,U,CR)", "(L,U,B)", "(L,U,H)", "(L,CR,B)", "(L,CR,H)", "(L,U,CR,B)", "(L,U,CR,H)"]
b = ["IALU", "IMAC", "FALU"]
c = ["", "@(C)", "@(!C)"]

result = "<IMACMaCLToMACC>"

for i in a:
    for j in b:
	for k in c:
	    s = "MR+=Tm*Tn%s->%s.Tt%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</IMACMaCLToMACC>\n"
fp.writelines(result)

#IMACMaCLToSHU MR += Tm* Tn{({U}, L, {CR}, {'B|H'})}->'SHU0.Tt|SHU1.Tt'{@('C|!C')}
a = ["", "L", "(L,U)", "(L,CR)", "(L,B)", "(L,H)", "(L,U,CR)", "(L,U,B)", "(L,U,H)", "(L,CR,B)", "(L,CR,H)", "(L,U,CR,B)", "(L,U,CR,H)"]
b = ["SHU0", "SHU1"]
c = ["", "@(C)", "@(!C)"]

result = "<IMACMaCLToSHU>"

for i in a:
    for j in b:
	for k in c:
	    s = "MR+=Tm*Tn%s->%s.Tt%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</IMACMaCLToSHU>\n"
fp.writelines(result)

#IMACAcc MR += Tm{({U}, {CR}, {'B|H'})}{@('C|!C')}
a = ["", "(U)", "(CR)", "(B)", "(H)", "(U,CR)", "(U,B)", "(U,H)", "(CR,B)", "(CR,H)", "(U,CR,B)", "(U,CR,H)"]
b = ["", "@(C)", "@(!C)"]

result = "<IMACAcc>"

for i in a:
    for j in b:
	s = "MR+=Tm%s%s;" % (i, j)
        result += s
result = result[: -1]
result += "</IMACAcc>\n"
fp.writelines(result)

#IMACAccToBIU MR += Tm{({U}, {CR}, {'B|H'})}-> BIU'0|1|2'{@('C|!C')}
a = ["", "(U)", "(CR)", "(B)", "(H)", "(U,CR)", "(U,B)", "(U,H)", "(CR,B)", "(CR,H)", "(U,CR,B)", "(U,CR,H)"]
b = range(0, 3)
c = ["", "@(C)", "@(!C)"]

result = "<IMACAccToBIU>"

for i in a:
    for j in b:
	for k in c:
	    s = "MR+=Tm%s->BIU%s%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</IMACAccToBIU>\n"
fp.writelines(result)

#IMACAccToM MR += Tm{({U}, {CR}, {'B|H'})}-> M[t]{@('C|!C')}
a = ["", "(U)", "(CR)", "(B)", "(H)", "(U,CR)", "(U,B)", "(U,H)", "(CR,B)", "(CR,H)", "(U,CR,B)", "(U,CR,H)"]
b = ["", "@(C)", "@(!C)"]

result = "<IMACAccToM>"

for i in a:
    for j in b:
	s = "MR+=Tm%s->M[t]%s;" % (i, j)
        result += s
result = result[: -1]
result += "</IMACAccToM>\n"
fp.writelines(result)

#IMACAccToMACC MR += Tm{({U}, {CR}, {'B|H'})}->'IALU.T|IMAC.T|FALU.T't{@('C|!C')}
a = ["", "(U)", "(CR)", "(B)", "(H)", "(U,CR)", "(U,B)", "(U,H)", "(CR,B)", "(CR,H)", "(U,CR,B)", "(U,CR,H)"]
b = ["IALU", "IMAC", "FALU"]
c = ["", "@(C)", "@(!C)"]

result = "<IMACAccToMACC>"

for i in a:
    for j in b:
	for k in c:
	    s = "MR+=Tm%s->%s.Tt%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</IMACAccToMACC>\n"
fp.writelines(result)

#IMACAccToSHU MR += Tm{({U}, {CR}, {'B|H'})}->'SHU0.Tt|SHU1.Tt'{@('C|!C')}
a = ["", "(U)", "(CR)", "(B)", "(H)", "(U,CR)", "(U,B)", "(U,H)", "(CR,B)", "(CR,H)", "(U,CR,B)", "(U,CR,H)"]
b = ["SHU0", "SHU1"]
c = ["", "@(C)", "@(!C)"]

result = "<IMACAccToSHU>"

for i in a:
    for j in b:
	for k in c:
	    s = "MR+=Tm%s->%s.Tt%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</IMACAccToSHU>\n"
fp.writelines(result)

#END IMAC
result = "</IMAC>\n"
fp.writelines(result)

#FMAC
result = "<FMAC>\n"
fp.writelines(result)

#FMACMulToBIU Tm* Tn({T}, 'S|D')->BIU'0|1|2'{@('C|!C')}
a = ["S", "D", "T,S", "T,D"]
b = range(0, 3)
c = ["", "@(C)", "@(!C)"]

result = "<FMACMulToBIU>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm*Tn(%s)->BIU%s%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FMACMulToBIU>\n"
fp.writelines(result)

#FMACMulToM Tm* Tn({T}, 'S|D')->M[t]{@('C|!C')}
a = ["S", "D", "T,S", "T,D"]
b = ["", "@(C)", "@(!C)"]

result = "<FMACMulToM>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm*Tn(%s)->M[t]%s;" % (i, j)
            result += s
result = result[: -1]
result += "</FMACMulToM>\n"
fp.writelines(result)

#FMACMulToMACC Tm* Tn({T}, 'S|D')->'FMAC.T|FALU.T't{@('C|!C')}
a = ["S", "D", "T,S", "T,D"]
b = ["FMAC", "FALU"]
c = ["", "@(C)", "@(!C)"]

result = "<FMACMulToMACC>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm*Tn(%s)->%s.Tt%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FMACMulToMACC>\n"
fp.writelines(result)

#FMACMulToSHU Tm* Tn({T}, 'S|D')->'SHU0.Tt|SHU1.Tt'{@('C|!C')}
a = ["S", "D", "T,S", "T,D"]
b = ["SHU0", "SHU1"]
c = ["", "@(C)", "@(!C)"]

result = "<FMACMulToSHU>"

for i in a:
    for j in b:
	for k in c:
	    s = "Tm*Tn(%s)->%s.Tt%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FMACMulToSHU>\n"
fp.writelines(result)

#FMACCmulToBIU Tm** Tn(S)-> BIU'0|1|2'{@('C|!C')}
a = range(0, 3)
b = ["", "@(C)", "@(!C)"]

result = "<FMACCmulToBIU>"

for i in a:
    for j in b:
	s = "Tm**Tn(S)->BIU%s%s;" % (i, j)
        result += s
result = result[: -1]
result += "</FMACCmulToBIU>\n"
fp.writelines(result)

#FMACCmulToM Tm** Tn(S)-> M[t]{@('C|!C')}
a = ["", "@(C)", "@(!C)"]

result = "<FMACCmulToM>"

for i in a:
    s = "Tm**Tn(S)->M[t]%s;" % (i)
    result += s
result = result[: -1]
result += "</FMACCmulToM>\n"
fp.writelines(result)

#FMACCmulToMACC Tm** Tn(S)->'FMAC.T|FALU.T't{@('C|!C')}
a = ["FMAC", "FALU"]
b = ["", "@(C)", "@(!C)"]

result = "<FMACCmulToMACC>"

for i in a:
    for j in b:
	s = "Tm**Tn(S)->%s.Tt%s;" % (i, j)
        result += s
result = result[: -1]
result += "</FMACCmulToMACC>\n"
fp.writelines(result)

#FMACCmulToSHU Tm** Tn(S)->'SHU0.Tt|SHU1.Tt'{@('C|!C')}
a = ["SHU0", "SHU1"]
b = ["", "@(C)", "@(!C)"]

result = "<FMACCmulToSHU>"

for i in a:
    for j in b:
	s = "Tm**Tn(S)->%s.Tt%s;" % (i, j)
        result += s
result = result[: -1]
result += "</FMACCmulToSHU>\n"
fp.writelines(result)

#FMACMA MR<-Tp + Tm* Tn('S|D'){@('C|!C')}
a = ["(S)", "(D)"]
b = ["", "@(C)", "@(!C)"]

result = "<FMACMA>"

for i in a:
    for j in b:
	s = "MR&lt;-Tp+Tm*Tn%s%s;" % (i, j)
        result += s
result = result[: -1]
result += "</FMACMA>\n"
fp.writelines(result)

#FMACMaC MR += Tm* Tn({CR}, 'S|D'){@('C|!C')}
a = ["S", "D", "CR,S", "CR,D"]
b = ["", "@(C)", "@(!C)"]

result = "<FMACMaC>"

for i in a:
    for j in b:
	s = "MR+=Tm*Tn(%s)%s;" % (i, j)
        result += s
result = result[: -1]
result += "</FMACMaC>\n"
fp.writelines(result)

#FMACMaCToBIU MR += Tm* Tn({CR}, 'S|D')-> BIU'0|1|2'{@('C|!C')}
a = ["S", "D", "CR,S", "CR,D"]
b = range(0, 3)
c = ["", "@(C)", "@(!C)"]

result = "<FMACMaCToBIU>"

for i in a:
    for j in b:
	for k in c:
	    s = "MR+=Tm*Tn(%s)->BIU%s%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FMACMaCToBIU>\n"
fp.writelines(result)

#FMACMaCToM MR += Tm* Tn({CR}, 'S|D')-> M[t]{@('C|!C')}
a = ["S", "D", "CR,S", "CR,D"]
b = ["", "@(C)", "@(!C)"]

result = "<FMACMaCToM>"

for i in a:
    for j in b:
	for k in c:
	    s = "MR+=Tm*Tn(%s)->M[t]%s;" % (i, j)
            result += s
result = result[: -1]
result += "</FMACMaCToM>\n"
fp.writelines(result)

#FMACMaCToMACC MR += Tm* Tn({CR}, 'S|D')->'FMAC.T|FALU.T't{@('C|!C')}
a = ["S", "D", "CR,S", "CR,D"]
b = ["FMAC", "FALU"]
c = ["", "@(C)", "@(!C)"]

result = "<FMACMaCToMACC>"

for i in a:
    for j in b:
	for k in c:
	    s = "MR+=Tm*Tn(%s)->%s.Tt%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FMACMaCToMACC>\n"
fp.writelines(result)

#FMACMaCToSHU MR += Tm* Tn({CR}, 'S|D')->'SHU0.Tt|SHU1.Tt'{@('C|!C')}
a = ["S", "D", "CR,S", "CR,D"]
b = ["SHU0", "SHU1"]
c = ["", "@(C)", "@(!C)"]

result = "<FMACMaCToSHU>"

for i in a:
    for j in b:
	for k in c:
	    s = "MR+=Tm*Tn(%s)->%s.Tt%s;" % (i, j, k)
            result += s
result = result[: -1]
result += "</FMACMaCToSHU>\n"
fp.writelines(result)

#END FMAC
result = "</FMAC>\n"
fp.writelines(result)

#MSEQ
result = "<MSEQ>\n"
fp.writelines(result)

#RepeatImm REPEAT @(imm10)
result = "<RepeatImm>REPEAT @(imm10)</RepeatImm>\n"
fp.writelines(result)

#RepeatKI REPEAT @(KIm{-imm4})
result = "<RepeatKI>REPEAT @(KIm);REPEAT @(KIm-imm4)</RepeatKI>\n"
fp.writelines(result)

#LpTo LPTO 'label|imm10' @(KIm{-imm4})
a = ["label", "imm10"]
b = ["", "-imm4"]

result = "<LpTo>"

for i in a:
    for j in b:
	s = "LPTO %s @(KIm%s);" % (i, j)
	result += s
result = result[: -1]
result += "</LpTo>\n"
fp.writelines(result)

#MPUSTOP MPUSTOP
result = "<MPUSTOP>MPUSTOP</MPUSTOP>\n"
fp.writelines(result)

#END MSEQ
result = "</MSEQ>\n"
fp.writelines(result)

result = "</MCCTree>\n"
fp.writelines(result)

fp.close()
