# This file is Antithetic.py. It illustrates the antithetic integral feedback control mechanism.
# It was written during 2023 and is described in the paper "Design Patterns of Biological Cells"
# by Steven S. Andrews, H. Steven Wiley, and Herbert M. Sauro, which was submitted to BioEssays
# in October, 2023. This file is in the public domain.
# In this toy model, X is the input, Y is the output, and A and B are antithetic control species.
# No units are used or assumed.

import tellurium as te
import matplotlib.pyplot as plt


model = te.loada('''

ext X

J1: X -> Y; kY * X * A
J2: Y -> ; ky * Y
J3: -> B; kB * Y
J4: -> A; kA
J5: A -> ; kab * A * B
J6: B -> ; kab * A * B

X = 1
Y = 1
A = 1
B = 1

kY = 1
ky = 1
kA = 1
kB = 1
kab = 1

at (time > 0): X = 3

''')


sim = model.simulate(-2, 10, 500, selections=['time', 'X', 'Y', 'A', 'B'])

print(sim)

t = sim['time']
Y0 = []
for _ in t:
    Y0.append(1)


t = sim['time']

X = sim['X']
Y = sim['Y']
A = sim['A']
B = sim['B']

fig, ax1 = plt.subplots()

ax1.plot(t, X, c='green', linewidth=2.5)
ax1.plot(t, Y, c='blue', linewidth=2.5)
ax1.plot(t, A, c='red', linewidth=2.5)
ax1.plot(t, B, c='purple', linewidth=2.5)
ax1.plot(t, Y0, linestyle='dashed', c='blue', linewidth=2.5)

ax1.set_ylabel('Concentration',size=16)
ax1.set_xlabel('Time',size=16)
ax1.tick_params(axis='both', which='major', labelsize=16)

ax1.legend(['X', 'Y', 'A', 'B'])
plt.show()
#plt.savefig("Antithetic",bbox_inches='tight')

