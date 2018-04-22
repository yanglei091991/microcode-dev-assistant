string = "R0.M[s]->M[s]"
textNum = len(string)
for k in range(textNum, 0, -1):
    if string[k - 1] == "s":
        string = string[ : k -1] + "0" + string[k : ]
print string