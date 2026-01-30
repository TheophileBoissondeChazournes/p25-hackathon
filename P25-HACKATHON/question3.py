import numpy as np

def dot(a, b):
    return np.dot(a, b)

def norm(v):
    return np.sqrt(dot(v, v))

def grad_conj(A, b, x0=None, tol=1e-8, max_iter=1000):
    n = len(b)
    if x0 is None:
        x = np.zeros(n)
    else:
        x = x0.copy()

    r = b - dot(A,x)
    p = r.copy()
    rs_old = dot(r, r)

    for k in range(max_iter):
        Ap = dot(A,p)
        alpha = rs_old / dot(p, Ap)

        x = x + alpha * p
        r = r - alpha * Ap

        rs_new = dot(r, r)

        if np.sqrt(rs_new) < tol:
            print(f"Convergence atteinte en {k+1} itérations")
            break

        beta = rs_new / rs_old
        p = r + beta * p
        rs_old = rs_new

    return x

A = np.eye(3)
b = np.array([1., 2., 3.])

x = grad_conj(A, b)
print(x)   # attendu : [1, 2, 3]

A = np.array([[2., 0.],
              [0., 3.]])
b = np.array([4., 9.])

x = grad_conj(A, b)
print(x)   # attendu : [2, 3]

