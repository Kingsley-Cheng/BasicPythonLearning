from scipy import sparse

A_dok = sparse.dok_matrix([[3, 0, 8, 0], [0, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]])
A_lil = sparse.lil_matrix([[3, 0, 8, 0], [0, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]])
A_coo = sparse.coo_matrix([[3, 0, 8, 0], [0, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]])

print("dok_matrix:\n", A_dok)
print("lil_matrix:\n", A_lil)
print("coo_matrix:\n", A_coo)
