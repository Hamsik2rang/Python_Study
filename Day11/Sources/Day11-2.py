# improve 8*sqrt(n)'s Big-O is bigger than O((logn)^2)

import matplotlib.pyplot as plt
import numpy as np
import math

domain_sqrt = [8 * (i ** (1 / 2)) for i in range(1, 1001)]
domain_log = [math.log(i, 2) ** 2 for i in range(1, 1001)]
domain_n = [i for i in range(1, 1001)]
plt.plot(domain_sqrt, "r--", domain_log, "b--", domain_n, "g--")
plt.xlabel("R = 8*sqrt(2) / B = (log(n))^2 / G = n")
plt.show()