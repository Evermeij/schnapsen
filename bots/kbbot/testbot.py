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

PC2D = Boolean('pc2D')
PC2H = Boolean('pc2H')
PC2S = Boolean('pc2S')
PC3D = Boolean('pc3D')
PC3H = Boolean('pc3D')
PC3S = Boolean('pc3D')
PC4D = Boolean('pc4D')
PC4H = Boolean('pc4H')
PC4S = Boolean('pc4S')

PC7C = Boolean('pc7C')
PC7H = Boolean('pc7H')
PC7S = Boolean('pc7S')
PC8C = Boolean('pc8C')
PC8H = Boolean('pc8H')
PC8S = Boolean('pc8S')
PC9C = Boolean('pc9C')
PC9H = Boolean('pc9H')
PC9S = Boolean('pc9S')

PC12C = Boolean('pc12C')
PC12D = Boolean('pc12D')
PC12S = Boolean('pc12S')
PC13C = Boolean('pc13C')
PC13D = Boolean('pc13D')
PC13S = Boolean('pc13S')
PC14C = Boolean('pc14C')
PC14D = Boolean('pc14D')
PC14S = Boolean('pc14S')

PC17C = Boolean('pc17C')
PC17D = Boolean('pc17D')
PC17H = Boolean('pc17H')
PC18C = Boolean('pc18C')
PC18D = Boolean('pc18D')
PC18H = Boolean('pc18H')
PC19C = Boolean('pc19C')
PC19D = Boolean('pc19D')
PC19H = Boolean('pc19H')

########################################
WT34CC = Boolean('wt34CC')
WT24CC = Boolean('wt24CC')
WT14CC = Boolean('wt14CC')
WT04CC = Boolean('wt04CC')
WT23CC = Boolean('wt23CC')
WT13CC = Boolean('wt13CC')
WT03CC = Boolean('wt03CC')
WT12CC = Boolean('wt12CC')
WT02CC = Boolean('wt02CC')
WT01CC = Boolean('wt01CC')

WT34DD = Boolean('wt34DD')
WT24DD = Boolean('wt24DD')
WT14DD = Boolean('wt14DD')
WT04DD = Boolean('wt04DD')
WT23DD = Boolean('wt23DD')
WT13DD = Boolean('wt13DD')
WT03DD = Boolean('wt03DD')
WT12DD = Boolean('wt12DD')
WT02DD = Boolean('wt02DD')
WT01DD = Boolean('wt01DD')

WT34HH = Boolean('wt34HH')
WT24HH = Boolean('wt24HH')
WT14HH = Boolean('wt14HH')
WT04HH = Boolean('wt04HH')
WT23HH = Boolean('wt23HH')
WT13HH = Boolean('wt13HH')
WT03HH = Boolean('wt03HH')
WT12HH = Boolean('wt12HH')
WT02HH = Boolean('wt02HH')
WT01HH = Boolean('wt01HH')

WT34SS = Boolean('wt34SS')
WT24SS = Boolean('wt24SS')
WT14SS = Boolean('wt14SS')
WT04SS = Boolean('wt04SS')
WT23SS = Boolean('wt23SS')
WT13SS = Boolean('wt13SS')
WT03SS = Boolean('wt03SS')
WT12SS = Boolean('wt12SS')
WT02SS = Boolean('wt02SS')
WT01SS = Boolean('wt01SS')

WTTCC = Boolean('wttCC')
WTTDD = Boolean('wttDD')
WTTHH = Boolean('wttHH')
WTTSS = Boolean('wttSS')



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
kb.add_clause(PC2D)
kb.add_clause(PC2H)
kb.add_clause(PC2S)
kb.add_clause(PC3D)
kb.add_clause(PC3H)
kb.add_clause(PC3S)
kb.add_clause(PC4D)
kb.add_clause(PC4H)
kb.add_clause(PC4S)
kb.add_clause(PC7C)
kb.add_clause(PC7H)
kb.add_clause(PC7S)
kb.add_clause(PC8C)
kb.add_clause(PC8H)
kb.add_clause(PC8S)
kb.add_clause(PC9C)
kb.add_clause(PC9H)
kb.add_clause(PC9S)
kb.add_clause(PC12C)
kb.add_clause(PC12D)
kb.add_clause(PC12S)
kb.add_clause(PC13C)
kb.add_clause(PC13D)
kb.add_clause(PC13S)
kb.add_clause(PC14C)
kb.add_clause(PC14D)
kb.add_clause(PC14S)
kb.add_clause(PC17C)
kb.add_clause(PC17D)
kb.add_clause(PC17H)
kb.add_clause(PC18C)
kb.add_clause(PC18D)
kb.add_clause(PC18H)
kb.add_clause(PC19C)
kb.add_clause(PC19D)
kb.add_clause(PC19H)

kb.add_clause(WT34CC)
kb.add_clause(WT24CC)
kb.add_clause(WT14CC)
kb.add_clause(WT04CC)
kb.add_clause(WT23CC)
kb.add_clause(WT13CC)
kb.add_clause(WT03CC)
kb.add_clause(WT12CC)
kb.add_clause(WT02CC)
kb.add_clause(WT01CC)

kb.add_clause(WT34DD)
kb.add_clause(WT24DD)
kb.add_clause(WT14DD)
kb.add_clause(WT04DD)
kb.add_clause(WT23DD)
kb.add_clause(WT13DD)
kb.add_clause(WT03DD)
kb.add_clause(WT12DD)
kb.add_clause(WT02DD)
kb.add_clause(WT01DD)

kb.add_clause(WT34HH)
kb.add_clause(WT24HH)
kb.add_clause(WT14HH)
kb.add_clause(WT04HH)
kb.add_clause(WT23HH)
kb.add_clause(WT13HH)
kb.add_clause(WT03HH)
kb.add_clause(WT12HH)
kb.add_clause(WT02HH)
kb.add_clause(WT01HH)

kb.add_clause(WT34SS)
kb.add_clause(WT24SS)
kb.add_clause(WT14SS)
kb.add_clause(WT04SS)
kb.add_clause(WT23SS)
kb.add_clause(WT13SS)
kb.add_clause(WT03SS)
kb.add_clause(WT12SS)
kb.add_clause(WT02SS)
kb.add_clause(WT01SS)



# Print all models of the knowledge base
for model in kb.models():
    print model

# Print out whether the KB is satisfiable (if there are no models, it is not satisfiable)
print kb.satisfiable()