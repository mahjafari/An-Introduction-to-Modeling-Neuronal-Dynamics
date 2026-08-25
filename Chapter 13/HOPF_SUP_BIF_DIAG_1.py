"""
Chapter 13 - The Hopf Bifurcation.

Variant of the supercritical Hopf bifurcation diagram, highlighting the
stable and unstable branches with different line styles.
"""

import numpy as np
import matplotlib.pyplot as plt

I = np.linspace(-1, 0, 101)

plt.figure(figsize=(6, 6))
plt.plot(I, np.sqrt(-I), '--k', linewidth=2)
plt.plot(I, -np.sqrt(-I), '--k', linewidth=2)
plt.plot(-I, np.zeros_like(I), '--k', linewidth=2)
plt.plot(I, np.zeros_like(I), '-k', linewidth=2)


plt.xlabel('$I$')
plt.ylabel('oscillation amplitude')
plt.axis([-1, 1, -1, 1])
plt.axis('square')
plt.show()
