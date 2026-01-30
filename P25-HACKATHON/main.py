import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('midline.txt', comments='#')
t = data[:,0]
Tmat = data[:,1:]
ntime, nx = Tmat.shape

Lx = 1.0
x = np.linspace(0, Lx, nx)

plt.figure(figsize=(6,6))
plt.title('T(x,t) le long de la ligne y=0.5')
extent = [0, Lx, t[-1], t[0]] 
plt.imshow(Tmat, aspect='auto', extent=extent)
plt.xlabel('x')
plt.ylabel('t')
plt.colorbar(label='T')
plt.tight_layout()
plt.savefig('T_xt_image.png', dpi=200)
print("Saved T_xt_image.png")

times_to_plot = [0.0, 0.1* t[-1], 0.5 * t[-1], t[-1]]

indices = [np.argmin(np.abs(t - tt)) for tt in times_to_plot]

plt.figure(figsize=(8,5))
for idx in indices:
    plt.plot(x, Tmat[idx,:], label=f"t={t[idx]:.3f}s")
plt.legend()
plt.xlabel('x')
plt.ylabel('T')
plt.title('Profils T(x) à différents instants (y=0.5)')
plt.grid(True)
plt.tight_layout()
plt.savefig('T_profiles.png', dpi=200)
print("Saved T_profiles.png")
plt.show()