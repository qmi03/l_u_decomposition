import numpy as np


def l_u_decomposition(A):
    """
    Phân tích LU dùng phương pháp Doolittle
    """
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


def forward_substitution(L, b):
    """
    Giải Ly = b tìm y
    L là ma trận tam giác dưới
    Thay số y1 tới yn nên gọi là forward_substitution
    """
    n = len(b)
    y = np.zeros(n)

    for i in range(n):
        y[i] = b[i] - sum(L[i, j] * y[j] for j in range(i))
        y[i] /= L[i, i]

    return y


def backward_substitution(U, y):
    """
    Giải Ux = y tìm x
    U là ma trận tam giác trên
    Thay số xn tới x1 nên gọi là backward_substitution
    """
    n = len(y)
    x = np.zeros(n)

    for i in range(n - 1, -1, -1):
        x[i] = y[i] - sum(U[i, j] * x[j] for j in range(i + 1, n))
        x[i] /= U[i, i]

    return x


def solve_linear_system(A, b):
    """
    Giải hệ A @ x = b bằng phân tích LU/PLU

    Các bước:
    1. Phân tích A thành P, L, U sao cho PA = LU
    2. Ax=b tương đương với PAx = Pb => LUx = Pb
    3. Lấy y sao cho Ux = y, giải Ly = Pb tìm y
    4. Giải Ux = y tìm x
    """
    # Thực hiện phân tích LU lên A
    P, L, U = l_u_decomposition(A)

    # Tính Pb
    Pb = np.dot(P, b)

    # Giải Ly = Pb
    y = forward_substitution(L, Pb)

    # Giải Ux = y
    x = backward_substitution(U, y)

    return x, P, L, U
