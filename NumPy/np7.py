import numpy as np
from numpy.polynomial import Chebyshev
from numpy.polynomial import Polynomial


def g(x):
    z = (x - 1) * 5
    y = np.sin(z ** 2) + np.sin(z) ** 2
    return y


def main():
    n = 100
    x = Chebyshev.basis(n).roots()
    xd = np.linspace(-1, 1, 1000)

    c1 = Chebyshev.fit(x, g(x), n - 1, domain=[-1, 1])
    c2 = Polynomial.fit(x, g(x), n, domain=[-1, 1])
    print("---不同差值方法的最大误差---")
    print("多项式差值的最大误差：", np.max(abs(g(xd) - c2(xd))))
    print("Chebyshev差值的最大误差：", np.max(abs(g(xd) - c1(xd))))


if __name__ == "__main__":
    main()
