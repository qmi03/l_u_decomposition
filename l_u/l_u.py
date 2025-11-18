import numpy as np


def l_u_decomposition(A):
    n = len(A)

    # Khởi tạo ma trận L, U
    L = np.eye(n)
    U = np.zeros((n, n))

    # Tạo ma trận P
    P = pivot_matrix(A)
    PA = np.dot(P, A)

    # Phương pháp Doolittle
    for j in range(n):
        # Uij = Aij - SUM(from k = 1 to i-1) Ukj * Jik
        for i in range(j + 1):
            s1 = sum(U[k, j] * L[i, k] for k in range(i))
            U[i, j] = PA[i, j] - s1

        # Lij = 1/Ujj * (Aij - SUM(k from 1 to j-1) Ukj * Lik
        for i in range(j, n):
            s2 = sum(U[k, j] * L[i, k] for k in range(j))
            L[i, j] = (PA[i, j] - s2) / U[j, j]

    return P, L, U


def pivot_matrix(M):
    m = len(M)
    id_mat = np.eye(m)

    for j in range(m):
        # Tìm phần tử có trị tuyệt đối lớn nhất ở cột j từ hàng j trở đi
        max_value = abs(M[j, j])
        pivot_row = j

        for i in range(j + 1, m):
            if abs(M[i, j]) > max_value:
                max_value = abs(M[i, j])
                pivot_row = i

        # Nếu phần tử có trị tuyệt đối ở hàng khác j thì tráo hàn đó với hàng j
        if j != pivot_row:
            id_mat[j, pivot_row] = id_mat[pivot_row, j]

    return id_mat
