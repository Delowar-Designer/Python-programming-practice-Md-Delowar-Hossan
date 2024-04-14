# 3.5 Program 1 Matplotlib Module use and Installe
import matplotlib.pyplot as plt
x = [0, 100]
y = (0, 200)
z = (0, 10000)

fig, axes = plt.subplots(nrows = 1, ncols = 2, figsize = (12,2))

axes[0].plot(x,y, color = 'green', lw = 3)
axes[0].set_xlabel('x')
axes[0].set_ylabel('y')

axes[1].plot(x,z, color = 'blue', lw = 2, ls = '--')
axes[1].set_xlabel('x')
axes[1].set_ylabel('z')
plt.show()
