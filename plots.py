# EN3330 Assignment 03 - plots
# problem: min x^2  s.t.  x >= 1,   L(mu, x) = x^2 + mu*(1 - x)

import numpy as np
import matplotlib.pyplot as plt


def L(mu, x):
    return x**2 + mu * (1 - x)


def d(mu):
    return mu - mu**2 / 4


# Q1 (a)
x = np.linspace(-1, 3, 200)
plt.figure()
for k in [0, 1, 2, 3]:
    plt.plot(x, L(k, x), label="mu = " + str(k))
    plt.plot(k / 2, L(k, k / 2), "ko")
plt.axvline(1, color="gray", linestyle="--", label="x = 1")
plt.xlabel("x")
plt.ylabel("L(mu, x)")
plt.title("L(mu, x) for different mu")
plt.legend()
plt.grid()
plt.savefig("q1a.png", dpi=200)

# Q1 (b)
mu = np.linspace(0, 5, 200)
plt.figure()
plt.plot(mu, d(mu), label="d(mu)")
plt.plot(2, d(2), "ro", label="mu* = 2, d* = 1")
plt.xlabel("mu")
plt.ylabel("d(mu)")
plt.title("Dual function")
plt.legend()
plt.grid()
plt.savefig("q1b.png", dpi=200)

# Q1 (c)
plt.figure()
for k in [0, 2, 5, 10]:
    plt.plot(x, L(k, x), "--", label="L(" + str(k) + ", x)")
xf = x[x >= 1]
plt.plot(xf, xf**2, "k", linewidth=3, label="g(x)")
plt.axvspan(-1, 1, color="red", alpha=0.1, label="infeasible (g = inf)")
plt.ylim(-2, 15)
plt.xlabel("x")
plt.title("Primal function g(x)")
plt.legend()
plt.grid()
plt.savefig("q1c.png", dpi=200)

# Q2 (a)(iv)
fig, ax = plt.subplots(1, 2, figsize=(9, 3.5))
m = np.linspace(0, 5, 100)
ax[0].plot(m, L(m, 1))
ax[0].plot(2, 1, "ro")
ax[0].set_ylim(0, 2)
ax[0].set_xlabel("mu")
ax[0].set_title("L(mu, x*)")
ax[0].grid()
ax[1].plot(x, L(2, x))
ax[1].plot(1, 1, "ro")
ax[1].set_xlabel("x")
ax[1].set_title("L(mu*, x)")
ax[1].grid()
plt.tight_layout()
plt.savefig("q2a.png", dpi=200)

# Q3 (b)
plt.figure()
for xv in [0, 1, 2]:
    plt.plot(mu, L(mu, xv), label="x = " + str(xv))
env = np.minimum(np.minimum(L(mu, 0), L(mu, 1)), L(mu, 2))
plt.plot(mu, env, "k", linewidth=3, label="lower envelope")
plt.plot(mu, d(mu), "r--", label="d(mu)")
plt.xlabel("mu")
plt.title("L(mu, x) as lines in mu")
plt.legend()
plt.grid()
plt.savefig("q3b.png", dpi=200)
