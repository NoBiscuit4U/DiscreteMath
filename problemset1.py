
#problem 1
def truth_values(p,q):
    vals=[]

    vals.append(p and q)
    vals.append(p or q)
    vals.append(p ^ q)
    vals.append(not p and q)
    vals.append(p == q)

    return vals

#problem 3
def satisfied_checker(self,statement):
    proposition_num=3

    def value_checker(p,q,r):
        vals={"p":p,"q":q,"r":r}

        return eval(statement,vals)

    for i in range(2**proposition_num):
        p=(i<=4)
        q=(i in [1,2,5,6])
        r=(i%2==0)

        val=value_checker(p,q,r)

        if(val==True):
            return True
        elif(i==2**proposition_num-1):
            return False

#knights_and_knaves
def knights_and_knaves(a_statement_a,a_statement_b,b_statement_b,b_statement_a):
    a_evaluation=""
    b_evaluation=""

    if(a_statement_a=="knight"):
        if(a_statement_b=="knave"):
            a_evaluation="a==(a and not b)"
        elif(a_statement_b=="knight"):
            a_evaluation="a==(a and b)"
        elif(a_statement_b=="blank"):
            a_evaluation="a==a"
    elif(a_statement_a=="knave"):
        if(a_statement_b=="knight"):
            a_evaluation="a==(not a and b)"
        elif(a_statement_b=="knave"):
                        a_evaluation="a==(not a and not b)"
        elif(a_statement_b=="blank"):
            a_evaluation="a==(not a)"
    else:
        if(a_statement_b=="knight"):
            a_evaluation="b==b"
        elif(a_statement_b=="knave"):
            a_evaluation="b==(not b)"

    if(b_statement_b=="knight"):
        if(b_statement_a=="knave"):
            b_evaluation="b==(b and not a)"
        elif(b_statement_a=="knight"):
            b_evaluation="b==(a and b)"
        elif(b_statement_a=="blank"):
            b_evaluation="b==b"
    elif(b_statement_b=="knave"):
        if(b_statement_a=="knight"):
            b_evaluation="b==(not b and a)"
        elif(b_statement_a=="knave"):
            b_evaluation="a==(not b and not a)"
        elif(b_statement_a=="blank"):
            b_evaluation="b==(not b)"
    else:
        if(b_statement_a=="knight"):
            b_evaluation="a==a"
        elif(b_statement_a=="knave"):
            b_evaluation="a==(not a)"

    print("Solution(s) to:")
    print(f"A says A is {a_statement_a} and B is {a_statement_b}")
    print(f"B says B is {b_statement_b} and A is {b_statement_a}")

    for i in range(4):
        a=(i<2)
        b=(i%2==0)

        vals={"a":a,"b":b}

        combined_evaluation=eval(a_evaluation+" and "+b_evaluation,vals) if(a_evaluation!="" and b_evaluation!="") else eval(a_evaluation) if(b_evaluation=="" and a_evaluation!="") else eval(b_evaluation) 

        if(combined_evaluation):
           print({"A":"knight" if a else "knave","B":"knight" if b else "knave"})


knights_and_knaves("knave","knave","blank","blank")
knights_and_knaves("knight","knight","knight","knave")
knights_and_knaves("knave","knave","knight","knave")
knights_and_knaves("knight","knight","knight","blank")