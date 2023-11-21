# This file is Oscillator2.py. It illustrates a simple relaxation oscillator mechanism.
# It was written during 2023 and is described in the paper "Design Patterns of Biological Cells"
# by Steven S. Andrews, H. Steven Wiley, and Herbert M. Sauro, which was submitted to BioEssays
# in October, 2023. This file is in the public domain.
# In this toy model, A and B are oscillating species, of which A positivey affects itself and B,
# and B negatively affects A. No units are used or assumed.

import tellurium as te
import matplotlib.pyplot as plt

# Model is a relaxation oscillator, in which A amplifies A and B, and B represses A

model1 = te.loada('''

J1: -> A ; k1 * A
J2: A -> ; k2 * B * A / (V+A)
J3: -> B ; k3 * A
J4: B -> ; k4 * B

A = 1
B = 1

k1 = 1.1
k2 = 1
k3 = 1
k4 = 0.5
V = 1

''')



sim = model1.simulate(0, 50, 500, selections=['time', 'A', 'B'])

print(sim)

t = sim['time']

A = sim['A']
B = sim['B']

fig, ax1 = plt.subplots()

ax1.plot(t, A, c='red', linewidth=2.5)
ax1.plot(t, B, c='green', linewidth=2.5)

ax1.set_ylabel('Concentration',size=16)
ax1.set_xlabel('Time',size=16)
ax1.tick_params(axis='both', which='major', labelsize=16)

ax1.legend(['A', 'B'])
plt.show()
#plt.savefig("Oscillator2",bbox_inches='tight')


