# This file is Oscillator1.py. It illustrates a simple feedback oscillator mechanism.
# It was written during 2023 and is described in the paper "Design Patterns of Biological Cells"
# by Steven S. Andrews, H. Steven Wiley, and Herbert M. Sauro, which was submitted to BioEssays
# in October, 2023. This file is in the public domain.
# In this toy model, A, B, and C are oscillating species, each of which negatively affects
# the concentration of the following species. No units are used or assumed.

import tellurium as te
import matplotlib.pyplot as plt

# Model is a repressilator, in which each node represses the next one

model1 = te.loada('''

J1: -> A ; kA
J2: A -> ; kCa * C * A / (V + A)
J3: -> B ; kB
J4: B -> ; kAb * A * B / (V + B)
J5: -> C ; kC
J6: C -> ; kBc * B * C / (V + C)

A = 1
B = 1
C = 1

kA = 2
kB = 1
kC = 1
kCa = 1
kAb = 1
kBc = 1
V = 1

''')



sim = model1.simulate(0, 50, 500, selections=['time', 'A', 'B', 'C'])

print(sim)

t = sim['time']

A = sim['A']
B = sim['B']
C = sim['C']

fig, ax1 = plt.subplots()

ax1.plot(t, A, c='red', linewidth=2.5)
ax1.plot(t, B, c='green', linewidth=2.5)
ax1.plot(t, C, c='blue', linewidth=2.5)

ax1.set_ylabel('Concentration',size=16)
ax1.set_xlabel('Time',size=16)
ax1.tick_params(axis='both', which='major', labelsize=16)

ax1.legend(['A', 'B', 'C'])
plt.show()
#plt.savefig("Oscillator1",bbox_inches='tight')


