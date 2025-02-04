import numpy as np

def fibonacci_matrix(n: int) -> int:

    if n < 0:
        raise ValueError("On veut un entier posiif")

    # Matrice de base
    F = np.array([[1, 1], [1, 0]], dtype=object)

    def matrix_power_recursive(matrix, power):

        if power == 0:
            return np.eye(2, dtype=object)  # Matrice 2x2
        if power == 1:
            return matrix

        half_power = matrix_power_recursive(matrix, power // 2)
        half_result = np.dot(half_power, half_power)

        if power % 2 == 0:
            return half_result
        else:
            return np.dot(half_result, matrix)

    if n == 0:
        return 0

    # Calcul recursif
    result_matrix = matrix_power_recursive(F, n - 1)

    return result_matrix[0, 0]

# Exemple d'utilisation
if __name__ == "__main__":
    n = 35  # Par exemple, le 10e terme
    print(f"La {n}-ième val de fibo est : {fibonacci_matrix(n)}")
