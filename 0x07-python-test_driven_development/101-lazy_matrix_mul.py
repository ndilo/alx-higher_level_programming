import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices m_a and m_b using NumPy.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        numpy.ndarray: The result of multiplying m_a and m_b.

    Raises:
        ValueError: If the matrices cannot be multiplied due to invalid dimensions.

    """
    np_a = np.array(m_a)
    np_b = np.array(m_b)

    try:
        result = np.matmul(np_a, np_b)
    except ValueError as e:
        raise ValueError("m_a and m_b can't be multiplied") from e

    return result
