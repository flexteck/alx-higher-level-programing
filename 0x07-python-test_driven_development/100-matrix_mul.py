#!/usr/bun/python3
def matrix_mul(m_a, m_b):
    """ A function that multiplies two matices
        
        Args:
            m_a: first matrix
            m_b: second matrix

        Return:
            new matrix
        Raises:
            TypeError: if m_a or m_b is not a list
                       if m_a or m_b is not a list of list

            ValueError: if m_a or m_b is an empty list [] / [[]]

                        if one of the element of the list is not
                        an int or a float

                        if all row are not of the same size
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):                                       raise TypeError("m_b must be a list")

    if not all(isinstance(elem, list) for elem in m_a):
                raise TypeError("m_a must be a list of lists")

    if not all(isinstance(elem, list) for elem in m_b):                         raise TypeError("m_b must be a list of lists")

    if (m_a == [] or m_a == [[]]):
        raise ValueError("m_a can't be empty")

    if (m_b == [] or m_b == [[]]):                                      raise ValueError("m_b can't be empty")

    if not all(isinstance(elem, (int, float)) for row in m_a \
            for elem in row):
        raise TypeError("m_a should contain only integers or floats")

    if not all(isinstance(elem, (int, float)) for row in m_b \
            for elem in row):
        raise TypeError("m_b should contain only integers or floats")

    len_a = len(m_a[0])
    len_b = len(m_a[0])

    for elem in m_a:
        if len(elem) != len_a:
            raise TypeError("each row of m_a must be of the\
                    same size or each row of m_b must be of the same size")

        for elem in m_b:
            if len(elem) != len_b:
                raise TypeError("each row of m_a must be of the same \
                size or each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    m_c = []


    for i in range(len(m_a)):
        mul = []
        for j in range(len(m_b[0])):
            current_sum = 0
            for k in range(len(m_a[0])):
                current_sum += m_a[i][k] * m_b[k][j]
            mul.append(current_sum)
        m_c.append(mul)

    return m_c
