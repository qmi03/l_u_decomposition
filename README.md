# Phân tích LU và Giải Hệ Phương Trình Tuyến Tính

Chương trình này thực hiện phân tích LU (LU Decomposition) sử dụng phương pháp Doolittle với partial pivoting, và giải hệ phương trình tuyến tính dạng **Ax = b**.

## Thuật toán

### Phân tích LU với Partial Pivoting

Cho ma trận vuông A, ta phân tích thành:
```

PA = LU

````
Trong đó:
- **P**: Ma trận hoán vị (permutation matrix)
- **L**: Ma trận tam giác dưới (lower triangular) với đường chéo toàn 1
- **U**: Ma trận tam giác trên (upper triangular)

### Giải hệ phương trình Ax = b

1. Phân tích A thành PA = LU
2. Biến đổi: Ax = b ⟹ PAx = Pb ⟹ LUx = Pb
3. Đặt y = Ux, giải Ly = Pb tìm y (forward substitution)
4. Giải Ux = y tìm x (backward substitution)


## Cài đặt

### Cách 1: Sử dụng Python và pip (đơn giản nhất)

#### Bước 1: Kiểm tra Python
Đảm bảo bạn đã cài Python 3.12 trở lên:
```bash
python --version
# hoặc
python3 --version
````

Nếu chưa có, tải Python tại: <https://www.python.org/downloads/>

#### Bước 2: Tạo môi trường ảo (virtual environment)

```bash
# Tạo môi trường ảo
python -m venv .venv

# Kích hoạt môi trường ảo
# Trên Linux/Mac:
source .venv/bin/activate

# Trên Windows:
.venv\Scripts\activate
```

#### Bước 3: Cài đặt thư viện

```bash
pip install -r requirements.txt
```

#### Bước 4: Chạy chương trình

```bash
python main.py
```

### Cách 2: Sử dụng uv (nhanh hơn)

Nếu bạn đã cài `uv`:

```bash
uv sync
uv run python main.py
```

### Cách 3: Sử dụng Nix (cho người dùng NixOS)

```bash
nix develop
uv sync
uv run python main.py
```

## Cách sử dụng

### Thay đổi dữ liệu đầu vào

Chương trình đọc ma trận A và vector b từ thư mục `input/`:

#### 1. Chỉnh sửa ma trận A (`input/A`)

File này chứa ma trận vuông A, mỗi hàng cách nhau bởi dấu xuống dòng, mỗi phần tử cách nhau bởi dấu phẩy.

**Ví dụ ma trận 4x4:**

```
7,3,-1,2
3,8,1,-4
-1,1,4,-1
2,-4,-1,6
```

#### 2. Chỉnh sửa vector b (`input/b`)

File này chứa vector cột b, mỗi phần tử trên một dòng.

**Ví dụ vector 4 phần tử:**

```
7
3
-1
2
```

**Lưu ý:** Ma trận A phải là ma trận vuông (nxn) và vector b phải có n phần tử.

### Ví dụ đầy đủ

Giải hệ phương trình:

```
7x₁  + 3x₂  - x₃  + 2x₄ = 7
3x₁  + 8x₂  + x₃  - 4x₄ = 3
-x₁  + x₂   + 4x₃ - x₄  = -1
2x₁  - 4x₂  - x₃  + 6x₄ = 2
```

**Ma trận A** (input/A):

```
7,3,-1,2
3,8,1,-4
-1,1,4,-1
2,-4,-1,6
```

**Vector b** (input/b):

```
7
3
-1
2
```

Chạy chương trình sẽ cho kết quả x.

## Cấu trúc project

```
├── README.md              # File này
├── main.py                # File chính để chạy chương trình
├── requirements.txt       # Danh sách thư viện cần thiết
├── pyproject.toml         # Cấu hình project (cho uv)
├── input/
│   ├── A                  # File chứa ma trận A
│   └── b                  # File chứa vector b
└── l_u/                   # Package chứa thuật toán
    ├── __init__.py
    └── l_u.py             # Các hàm phân tích LU
```

## Kết quả đầu ra

Chương trình sẽ in ra:

1. Ma trận A và vector b
2. Ma trận P, L, U từ phân tích LU
3. Kiểm nghiệm: PA = LU
4. Nghiệm x của hệ phương trình
5. Kiểm tra: Ax = b

## Tham khảo

- [LU Decomposition in Python and Numpy](https://www.quantstart.com/articles/LU-Decomposition-in-Python-and-NumPy/)
- [NumPy Documentation](https://numpy.org/doc/)
