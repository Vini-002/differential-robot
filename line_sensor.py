import numpy as np
import matplotlib.pyplot as plt
n = 100
d_m= 2
a_m = np.pi/4
thetas = np.linspace(-a_m, a_m, n, True)
ds = np.linspace(-d_m, d_m, 40, True)

print(f'\n{thetas=}\n')


ax = plt.subplot(111)

for d in ds:
    ys = []
    for theta in thetas:
        y = np.clip(np.tan(theta)*(1 + d/np.sin(theta)), -2, 2)
        ys.append(y)
    
    plt.scatter(thetas, ys, s=1, c=[d]*n, vmin=-d_m, vmax=d_m, cmap='tab20')
plt.colorbar()
ax.axis('equal')
plt.show()