from kb import KB, Boolean, Integer

# Initialise all variables that you need for you strategies and game knowledge.
# First all possible cards:
J0 = Boolean('j0')
J1 = Boolean('j1')
J2 = Boolean('j2')
J3 = Boolean('j3')
J4 = Boolean('j4')
J5 = Boolean('j5')
J6 = Boolean('j6')
J7 = Boolean('j7')
J8 = Boolean('j8')
J9 = Boolean('j9')
J10 = Boolean('j10')
J11 = Boolean('j11')
J12 = Boolean('j12')
J13 = Boolean('j13')
J14 = Boolean('j14')
J15 = Boolean('j15')
J16 = Boolean('j16')
J17 = Boolean('j17')
J18 = Boolean('j18')
J19 = Boolean('j19')

Q0 = Boolean('q0')
Q1 = Boolean('q1')
Q2 = Boolean('q2')
Q3 = Boolean('q3')
Q4 = Boolean('q4')
Q5 = Boolean('q5')
Q6 = Boolean('q6')
Q7 = Boolean('q7')
Q8 = Boolean('q8')
Q9 = Boolean('q9')
Q10 = Boolean('q10')
Q11 = Boolean('q11')
Q12 = Boolean('q12')
Q13 = Boolean('q13')
Q14 = Boolean('q14')
Q15 = Boolean('q15')
Q16 = Boolean('q16')
Q17 = Boolean('q17')
Q18 = Boolean('q18')
Q19 = Boolean('q19')

K0 = Boolean('k0')
K1 = Boolean('k1')
K2 = Boolean('k2')
K3 = Boolean('k3')
K4 = Boolean('k4')
K5 = Boolean('k5')
K6 = Boolean('k6')
K7 = Boolean('k7')
K8 = Boolean('k8')
K9 = Boolean('k9')
K10 = Boolean('k10')
K11 = Boolean('k11')
K12 = Boolean('k12')
K13 = Boolean('k13')
K14 = Boolean('k14')
K15 = Boolean('k15')
K16 = Boolean('k16')
K17 = Boolean('k17')
K18 = Boolean('k18')
K19 = Boolean('k19')

T0 = Boolean('t0')
T1 = Boolean('t1')
T2 = Boolean('t2')
T3 = Boolean('t3')
T4 = Boolean('t4')
T5 = Boolean('t5')
T6 = Boolean('t6')
T7 = Boolean('t7')
T8 = Boolean('t8')
T9 = Boolean('t9')
T10 = Boolean('t10')
T11 = Boolean('t11')
T12 = Boolean('t12')
T13 = Boolean('t13')
T14 = Boolean('t14')
T15 = Boolean('t15')
T16 = Boolean('t16')
T17 = Boolean('t17')
T18 = Boolean('t18')
T19 = Boolean('t19')

A0 = Boolean('a0')
A1 = Boolean('a1')
A2 = Boolean('a2')
A3 = Boolean('a3')
A4 = Boolean('a4')
A5 = Boolean('a5')
A6 = Boolean('a6')
A7 = Boolean('a7')
A8 = Boolean('a8')
A9 = Boolean('a9')
A10 = Boolean('a10')
A11 = Boolean('a11')
A12 = Boolean('a12')
A13 = Boolean('a13')
A14 = Boolean('a14')
A15 = Boolean('a15')
A16 = Boolean('a16')
A17 = Boolean('a17')
A18 = Boolean('a18')
A19 = Boolean('a19')





def general_information(kb):
    # GENERAL INFORMATION ABOUT THE CARDS
    kb.add_clause(J4)
    kb.add_clause(J9)
    kb.add_clause(J14)
    kb.add_clause(J19)

    kb.add_clause(Q3)
    kb.add_clause(Q8)
    kb.add_clause(Q13)
    kb.add_clause(Q18)

    kb.add_clause(K2)
    kb.add_clause(K7)
    kb.add_clause(K12)
    kb.add_clause(K17)

    kb.add_clause(T1)
    kb.add_clause(T6)
    kb.add_clause(T11)
    kb.add_clause(T16)

    kb.add_clause(A0)
    kb.add_clause(A5)
    kb.add_clause(A10)
    kb.add_clause(A15)


def strategy_knowledge(kb):
    kb.add_clause()