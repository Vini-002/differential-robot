import matplotlib.pyplot as plt
import numpy as np
from numpy.core.function_base import linspace

def bezier(a, b, c, d):
    t = linspace(0, 1, 20)
    return np.array([(1 - i)**3*a + 3*i*(1 - i)**2*b + 3*i**2*(1 - i)*c + i**3*d for i in t])

#np.random.seed(5)

Num = 5
control = np.around(np.random.rand(2*Num, 2), 1)
#control = np.array([[0.0, 0.0], [0.0, 1.0], [0.5, 1.0], [0.5, 0.5], [1.0, 0.5], [1.0, 0.0]])
#control = np.array([[0.0, 0.0], [0.0, 0.6], [0.81, 0.6], [0.6, 1.2], [1., 1.2], [1., 1.], [1., .46], [1.4, .46], [1.4, 1.], [1.2, 1.], [1.2, 1.54], [1.6, 1.54], [1.6, 1.], [1.6, .0], [1.6, -0.4], [1.6, -0.4], [1., -0.4], [1.2, 0.4], [0.6, 0.4], [0.81, 0.0]])
# control = np.array([[-0.6, 0.0], [-0.6, 0.6], [0.21, 0.6], [0.6, 1.2], [1., 1.2], [1., 1.], [1., .46], [1.4, .46], [1.4, 1.], [1.2, 1.], [1.2, 1.54], [1.6, 1.54], [1.6, 1.], [1.6, .0], [1.6, -0.4], [1.6, -0.4], [1., -0.4], [1.2, 0.4], [0.6, 0.4], [.81, .0], [.0, .0], [0.21, 0.0]])
#control= np.array([[0.0, 0.0, 0.4, 0.6, 0.6, 0.8, 0.8, 0.6], [0.0, 0.4, 0.4, 0.6, 1.0, 1.0, 0.4, 0.0]])
# Num = control.shape[0]//2

points = np.array([(control[i-1] + control[i])/2 for i in range(0, 2*Num, 2)])
print(list(range(Num)))
print(list(range(0, 2*Num - 1, 2)))


beziers3 = np.array([bezier(points[i], control[j], control[(j + 1)], points[(i + 1)%Num]) for i, j in zip(range(Num), range(0, 2*Num - 1, 2))])

beziers = np.reshape(beziers3, (20*Num, 2))
#beziers = np.concatenate((bezier(points[0], control[0], control[1], points[1]), bezier(points[1], control[2], control[3], points[0])))

print(f'{beziers3.shape=}')
print(f'{beziers.shape=}')
print(f'{points=}\n')

control2 = np.array(list(zip(*control)))
#print(f'{control2=}')

points2 = np.array(list(zip(*points)))
print(f'{points2=}')

bezier2 = np.array(list(zip(*beziers)))

""" fig,ax = plt.subplots(figsize=(10,50))
ax.set_aspect(1)
ax.plt.plot(control2[0], control2[1], 'x')
ax.plt.plot(points2[0], points2[1], 'o')
ax.plt.plot(bezier2[0], bezier2[1])
plt.show() """

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(control2[0], control2[1], 'x')
ax.plot(points2[0], points2[1], 'o')
ax.plot(bezier2[0], bezier2[1])
ax.set_aspect(1)
plt.show()