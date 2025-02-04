import numpy as np

def fibonacci_matrix(n: int) -> int:
    """
    Calcul du n-ième nombre de Fibonacci en utilisant l'expression matricielle de manière récursive.

    :param n: Un entier représentant la position dans la suite de Fibonacci (0-indexé).
    :return: Le n-ième nombre de Fibonacci.
    """
    if n < 0:
        raise ValueError("La position dans la suite de Fibonacci doit être un entier positif.")

    # Matrice de transformation de Fibonacci
    F = np.array([[1, 1], [1, 0]], dtype=object)

    def matrix_power_recursive(matrix, power):
        """
        Calcul récursif de la puissance d'une matrice via l'expression matricielle.

        :param matrix: La matrice de base.
        :param power: L'exposant entier.
        :return: La matrice élevée à la puissance spécifiée.
        """
        if power == 0:
            return np.eye(2, dtype=object)  # Matrice identité de dimension 2x2
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

    # Calcul de F^(n-1) de manière récursive
    result_matrix = matrix_power_recursive(F, n - 1)

    # Le n-ième Fibonacci est dans la première ligne, première colonne de la matrice résultante
    return result_matrix[0, 0]

# Exemple d'utilisation
if __name__ == "__main__":
    n = 10  # Par exemple, le 10e terme
    print(f"Le {n}-ième nombre de Fibonacci est : {fibonacci_matrix(n)}")
