def compute(int n):
    cdef double total_sum = 0.0
    cdef long i

    for i in range(n):
        total_sum += i * 1.01

    return total_sum