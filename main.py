import numpy as np

import l_u


def main():
    # Test the implementation
    A = np.array(
        [[7, 3, -1, 2], [3, 8, 1, -4], [-1, 1, 4, -1], [2, -4, -1, 6]], dtype=float
    )

    P, L, U = l_u.l_u_decomposition(A)

    print("A:")
    print(A)
    print("\nP:")
    print(P)
    print("\nL:")
    print(L)
    print("\nU:")
    print(U)

    # Verify that PA = LU
    print("\nVerification - PA:")
    print(np.dot(P, A))
    print("\nVerification - LU:")
    print(np.dot(L, U))


if __name__ == "__main__":
    main()
