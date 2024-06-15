def arithmetic_arranger(problems, show_answers=False):
    fr_line=""
    sec_line=""
    dash=""
    r=""
    final=""
    if len(problems) > 5:
        return("Error: Too many problems.")

    l=len(problems)
    p=0
    for i in range (l):
        for s in problems[i]:
            if s.count("*")>=1 or s.count("/")>=1:
                return("Error: Operator must be '+' or '-'.")
            if any(c.isalpha()for c in s)==True:
                return("Error: Numbers must only contain digits.")

            if s=="+" or s=="-":
                p=0
            elif s.isdigit():
                p+=1
            
        if p>4:
            return("Error: Numbers cannot be more than four digits.")      

        pro=problems[i].split(" ")
        if pro[1]=="+":
            res=int(pro[0])+int(pro[2])
        elif pro[1]=="-":
            res=int(pro[0])-int(pro[2])
        res=str(res)
        maxlen=max(len(pro[0]), len(pro[2]))+2

        fr_line+= pro[0].rjust(maxlen)
        fr_line+="    "
        sec_line+=pro[1]
        sec_line+= pro[2].rjust(maxlen-1)
        sec_line+="    "
        dash+="-"*maxlen
        dash+="    "
        r+=res.rjust(maxlen)
        r+="    "

    if show_answers:
        final+=fr_line.rstrip()+"\n"+sec_line.rstrip()+"\n"+dash.rstrip()+"\n"+r.rstrip()
    else:
        final+=fr_line.rstrip()+"\n"+sec_line.rstrip()+"\n"+dash.rstrip()
    return final

print(f'\n{arithmetic_arranger(["1 + 2", "1 - 9380"])}')

#this is a problem from freecodecamp
