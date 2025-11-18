import numpy as np

import l_u


def main():
    A = np.loadtxt("input/A", delimiter=",", dtype=float)
    b = np.loadtxt("input/b", delimiter=",", dtype=float)

    print("Ma trận A:")
    print(A)
    print("\nVector b:")
    print(b)
    print("\n" + "=" * 50)

    # Giải hệ Ax = b
    x, P, L, U = l_u.solve_linear_system(A, b)

    print("\nKết quả phân tích LU:")
    print("\nP (Permutation matrix):")
    print(P)
    print("\nL (Lower triangular):")
    print(L)
    print("\nU (Upper triangular):")
    print(U)

    # Kiểm nghiệm
    print("\n" + "=" * 50)
    print("Kiểm nghiệm phân tích LU:")
    print("\nPA:")
    print(np.dot(P, A))
    print("\nLU:")
    print(np.dot(L, U))

    if np.allclose(np.dot(P, A), np.dot(L, U)):
        print("\n✓ LU Decomposition verified: PA = LU")
    else:
        print("\n✗ LU Decomposition failed")

    # In kết quả giải hệ
    print("\n" + "=" * 50)
    print("Nghiệm hệ A @ x = b:")
    print("\nx =")
    print(x)

    # Kiểm tra kết quả nghiệm
    print("\n" + "=" * 50)
    print("Kiểm tra nghiệm")
    print("\nAx:")
    print(np.dot(A, x))
    print("\nb:")
    print(b)

    if np.allclose(np.dot(A, x), b):
        print("\n✓ Nghiệm đúng: A @ x = b")
    else:
        print("\n✗ Giải hệ sai")


if __name__ == "__main__":
    main()
