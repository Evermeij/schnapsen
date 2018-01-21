import kb, sys
from kb import KB, Boolean, Integer, Constant

# Define our propositional symbols
# J1 is true if the card with index 1 is a jack, etc
# You need to initialise all variables that you need for you strategies and game knowledge.
# Add those variables here.. The following list is complete for the Play Jack strategy.
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

M23 = Boolean('m23')
M78 = Boolean('m78')
M1213 = Boolean('m1213')
M1718 = Boolean('m1718')

TE4 = Boolean('te4')
TE9 = Boolean('te9')
TE14 = Boolean('te14')
TE19 = Boolean('te19')

PC6 = Boolean('pc6')
PC0 = Boolean('pc0')
PC2 = Boolean('pc2')
PC3 = Boolean('pc3')
PC4 = Boolean('pc4')
PC7 = Boolean('pc7')
PC8 = Boolean('pc8')
PC9 = Boolean('pc9')
PC12 = Boolean('pc12')
PC13 = Boolean('pc13')
PC14 = Boolean('pc14')
PC17 = Boolean('pc17')
PC18 = Boolean('pc18')
PC19 = Boolean('pc19')

TC = Boolean('TC')
TD = Boolean('TD')
TH = Boolean('TH')
TS = Boolean('TS')

# Create a new knowledge base
kb = KB()

# GENERAL INFORMATION ABOUT THE CARDS
# This adds information which cards are Jacks
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

# DEFINITION OF THE STRATEGY
# Add clauses (This list is sufficient for this strategy)
# PJ is the strategy to play jacks first, so all we need to model is all x PJ(x) <-> J(x),
# In other words that the PJ strategy should play a card when it is a jack
kb.add_clause(~M23, K2, K7, K12, K17)
kb.add_clause(~M23, K2, K7, K12, Q18)
kb.add_clause(~M23, K2, K7, Q13, K17)
kb.add_clause(~M23, K2, K7, Q13, Q18)
kb.add_clause(~M23, K2, Q8, K12, K17)
kb.add_clause(~M23, K2, Q8, K12, Q18)
kb.add_clause(~M23, K2, Q8, Q13, K17)
kb.add_clause(~M23, K2, Q8, Q13, Q18)
kb.add_clause(~M23, Q3, K7, K12, K17)
kb.add_clause(~M23, Q3, K7, K12, Q18)
kb.add_clause(~M23, Q3, K7, Q13, K17)
kb.add_clause(~M23, Q3, Q8, K12, K17)
kb.add_clause(~M23, Q3, K7, Q13, Q18)
kb.add_clause(~M23, Q3, Q8, K12, Q18)
kb.add_clause(~M23, Q3, Q8, Q13, K17)
kb.add_clause(~M23, Q3, Q8, Q13, Q18)
kb.add_clause(M23, ~K2, ~Q3)
kb.add_clause(M23, ~K7, ~Q8)
kb.add_clause(M23, ~K12, ~Q13)
kb.add_clause(M23, ~K17, ~Q18)

kb.add_clause(~M78, K2, K7, K12, K17)
kb.add_clause(~M78, K2, K7, K12, Q18)
kb.add_clause(~M78, K2, K7, Q13, K17)
kb.add_clause(~M78, K2, K7, Q13, Q18)
kb.add_clause(~M78, K2, Q8, K12, K17)
kb.add_clause(~M78, K2, Q8, K12, Q18)
kb.add_clause(~M78, K2, Q8, Q13, K17)
kb.add_clause(~M78, K2, Q8, Q13, Q18)
kb.add_clause(~M78, Q3, K7, K12, K17)
kb.add_clause(~M78, Q3, K7, K12, Q18)
kb.add_clause(~M78, Q3, K7, Q13, K17)
kb.add_clause(~M78, Q3, Q8, K12, K17)
kb.add_clause(~M78, Q3, K7, Q13, Q18)
kb.add_clause(~M78, Q3, Q8, K12, Q18)
kb.add_clause(~M78, Q3, Q8, Q13, K17)
kb.add_clause(~M78, Q3, Q8, Q13, Q18)
kb.add_clause(M78, ~K2, ~Q3)
kb.add_clause(M78, ~K7, ~Q8)
kb.add_clause(M78, ~K12, ~Q13)
kb.add_clause(M78, ~K17, ~Q18)

kb.add_clause(~M1213, K2, K7, K12, K17)
kb.add_clause(~M1213, K2, K7, K12, Q18)
kb.add_clause(~M1213, K2, K7, Q13, K17)
kb.add_clause(~M1213, K2, K7, Q13, Q18)
kb.add_clause(~M1213, K2, Q8, K12, K17)
kb.add_clause(~M1213, K2, Q8, K12, Q18)
kb.add_clause(~M1213, K2, Q8, Q13, K17)
kb.add_clause(~M1213, K2, Q8, Q13, Q18)
kb.add_clause(~M1213, Q3, K7, K12, K17)
kb.add_clause(~M1213, Q3, K7, K12, Q18)
kb.add_clause(~M1213, Q3, K7, Q13, K17)
kb.add_clause(~M1213, Q3, Q8, K12, K17)
kb.add_clause(~M1213, Q3, K7, Q13, Q18)
kb.add_clause(~M1213, Q3, Q8, K12, Q18)
kb.add_clause(~M1213, Q3, Q8, Q13, K17)
kb.add_clause(~M1213, Q3, Q8, Q13, Q18)
kb.add_clause(M1213, ~K2, ~Q3)
kb.add_clause(M1213, ~K7, ~Q8)
kb.add_clause(M1213, ~K12, ~Q13)
kb.add_clause(M1213, ~K17, ~Q18)

kb.add_clause(~M1718, K2, K7, K12, K17)
kb.add_clause(~M1718, K2, K7, K12, Q18)
kb.add_clause(~M1718, K2, K7, Q13, K17)
kb.add_clause(~M1718, K2, K7, Q13, Q18)
kb.add_clause(~M1718, K2, Q8, K12, K17)
kb.add_clause(~M1718, K2, Q8, K12, Q18)
kb.add_clause(~M1718, K2, Q8, Q13, K17)
kb.add_clause(~M1718, K2, Q8, Q13, Q18)
kb.add_clause(~M1718, Q3, K7, K12, K17)
kb.add_clause(~M1718, Q3, K7, K12, Q18)
kb.add_clause(~M1718, Q3, K7, Q13, K17)
kb.add_clause(~M1718, Q3, Q8, K12, K17)
kb.add_clause(~M1718, Q3, K7, Q13, Q18)
kb.add_clause(~M1718, Q3, Q8, K12, Q18)
kb.add_clause(~M1718, Q3, Q8, Q13, K17)
kb.add_clause(~M1718, Q3, Q8, Q13, Q18)
kb.add_clause(M1718, ~K2, ~Q3)
kb.add_clause(M1718, ~K7, ~Q8)
kb.add_clause(M1718, ~K12, ~Q13)
kb.add_clause(M1718, ~K17, ~Q18)

###########################################################
kb.add_clause(TE4)
kb.add_clause(TE9)
kb.add_clause(TE14)
kb.add_clause(TE19)

###########################################################
kb.add_clause(~PC2, J2, Q2, K2)
kb.add_clause(~TC, ~PC2)
kb.add_clause(TC, ~J2, PC2)
kb.add_clause(TC, ~Q2, PC2)
kb.add_clause(TC, ~K2, PC2)

kb.add_clause(~PC3, J3, Q3, K3)
kb.add_clause(~TC, ~PC3)
kb.add_clause(TC, ~J3, PC3)
kb.add_clause(TC, ~Q3, PC3)
kb.add_clause(TC, ~K3, PC3)

kb.add_clause(~PC4, J4, Q4, K4)
kb.add_clause(~TC, ~PC4)
kb.add_clause(TC, ~J4, PC4)
kb.add_clause(TC, ~Q4, PC4)
kb.add_clause(TC, ~K4, PC4)

kb.add_clause(~PC7, J7, Q7, K7)
kb.add_clause(~TD, ~PC7)
kb.add_clause(TD, ~J7, PC7)
kb.add_clause(TD, ~Q7, PC7)
kb.add_clause(TD, ~K7, PC7)

kb.add_clause(~PC8, J8, Q8, K8)
kb.add_clause(~TD, ~PC8)
kb.add_clause(TD, ~J8, PC8)
kb.add_clause(TD, ~Q8, PC8)
kb.add_clause(TD, ~K8, PC8)

kb.add_clause(~PC9, J9, Q9, K9)
kb.add_clause(~TD, ~PC9)
kb.add_clause(TD, ~J9, PC9)
kb.add_clause(TD, ~Q9, PC9)
kb.add_clause(TD, ~K9, PC9)

kb.add_clause(~PC12, J12, Q12, K12)
kb.add_clause(~TH, ~PC12)
kb.add_clause(TH, ~J12, PC12)
kb.add_clause(TH, ~Q12, PC12)
kb.add_clause(TH, ~K12, PC12)

kb.add_clause(~PC13, J13, Q13, K13)
kb.add_clause(~TH, ~PC13)
kb.add_clause(TH, ~J13, PC13)
kb.add_clause(TH, ~Q13, PC13)
kb.add_clause(TH, ~K13, PC13)

kb.add_clause(~PC14, J14, Q14, K14)
kb.add_clause(~TH, ~PC14)
kb.add_clause(TH, ~J14, PC14)
kb.add_clause(TH, ~Q14, PC14)
kb.add_clause(TH, ~K14, PC14)

kb.add_clause(~PC17, J17, Q17, K17)
kb.add_clause(~TS, ~PC17)
kb.add_clause(TS, ~J17, PC17)
kb.add_clause(TS, ~Q17, PC17)
kb.add_clause(TS, ~K17, PC17)

kb.add_clause(~PC18, J18, Q18, K18)
kb.add_clause(~TS, ~PC18)
kb.add_clause(TS, ~J18, PC18)
kb.add_clause(TS, ~Q18, PC18)
kb.add_clause(TS, ~K18, PC18)

kb.add_clause(~PC19, J19, Q19, K19)
kb.add_clause(~TS, ~PC19)
kb.add_clause(TS, ~J19, PC19)
kb.add_clause(TS, ~Q19, PC19)
kb.add_clause(TS, ~K19, PC19)


# Print all models of the knowledge base
for model in kb.models():
    print model

# Print out whether the KB is satisfiable (if there are no models, it is not satisfiable)
print kb.satisfiable()