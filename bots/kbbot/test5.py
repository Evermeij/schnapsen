import kb, sys
from kb import KB, Boolean, Integer, Constant

# Define our symbols
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

PC0 = Boolean('pc0')
PC1 = Boolean('pc1')
PC2 = Boolean('pc2')
PC3 = Boolean('pc3')
PC4 = Boolean('pc4')
PC5 = Boolean('pc5')
PC6 = Boolean('pc6')
PC7 = Boolean('pc7')
PC8 = Boolean('pc8')
PC9 = Boolean('pc9')
PC10 = Boolean('pc10')
PC11 = Boolean('pc11')
PC12 = Boolean('pc12')
PC13 = Boolean('pc13')
PC14 = Boolean('pc14')
PC15 = Boolean('pc15')
PC16 = Boolean('pc16')
PC17 = Boolean('pc17')
PC18 = Boolean('pc18')
PC19 = Boolean('pc19')

# Create a new knowledge base
kb = KB()

# Add the info which cards are Jacks, Queens or Kings
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

#############################################
# Add clauses
#############################################

kb.add_clause(~PC2, J2, Q2, K2)
kb.add_clause(~J2, PC2)
kb.add_clause(~Q2, PC2)
kb.add_clause(~K2, PC2)

kb.add_clause(~PC3, J3, Q3, K3)
kb.add_clause(~J3, PC3)
kb.add_clause(~Q3, PC3)
kb.add_clause(~K3, PC3)

kb.add_clause(~PC4, J4, Q4, K4)
kb.add_clause(~J4, PC4)
kb.add_clause(~Q4, PC4)
kb.add_clause(~K4, PC4)

kb.add_clause(~PC7, J7, Q7, K7)
kb.add_clause(~J7, PC7)
kb.add_clause(~Q7, PC7)
kb.add_clause(~K7, PC7)

kb.add_clause(~PC8, J8, Q8, K8)
kb.add_clause(~J8, PC8)
kb.add_clause(~Q8, PC8)
kb.add_clause(~K8, PC8)

kb.add_clause(~PC9, J9, Q9, K9)
kb.add_clause(~J9, PC9)
kb.add_clause(~Q9, PC9)
kb.add_clause(~K9, PC9)

kb.add_clause(~PC12, J12, Q12, K12)
kb.add_clause(~J12, PC12)
kb.add_clause(~Q12, PC12)
kb.add_clause(~K12, PC12)

kb.add_clause(~PC13, J13, Q13, K13)
kb.add_clause(~J13, PC13)
kb.add_clause(~Q13, PC13)
kb.add_clause(~K13, PC13)

kb.add_clause(~PC14, J14, Q14, K14)
kb.add_clause(~J14, PC14)
kb.add_clause(~Q14, PC14)
kb.add_clause(~K14, PC14)

kb.add_clause(~PC17, J17, Q17, K17)
kb.add_clause(~J17, PC17)
kb.add_clause(~Q17, PC17)
kb.add_clause(~K17, PC17)

kb.add_clause(~PC18, J18, Q18, K18)
kb.add_clause(~J18, PC18)
kb.add_clause(~Q18, PC18)
kb.add_clause(~K18, PC18)

kb.add_clause(~PC19, J19, Q19, K19)
kb.add_clause(~J19, PC19)
kb.add_clause(~Q19, PC19)
kb.add_clause(~K19, PC19)

kb.add_clause(~PC6)

# Print all models of the knowledge base
for model in kb.models():
    print model

# Print out whether the KB is satisfiable (if there are no models, it is not satisfiable)
print kb.satisfiable()
