def arithmetic_arranger(problems, show_answers=False):
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
            else:
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
        #print(pro)
        #print(res)
        final=""
        final+=pro[0].rjust(maxlen)
        final+="\n"
        final+=pro[1]
        final+=pro[2].rjust(maxlen-1)
        final+="\n"
        final+="-"*maxlen
        final+="\n"
        final+=res.rjust(maxlen)
        final+="    "
        print(final)
    return problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')

#this is a problem from freecodecamp
