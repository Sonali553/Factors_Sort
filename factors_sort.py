def count_factors(num):
    factors = set()
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            factors.add(i)
            factors.add(num // i)
    return len(factors)
def custom_sort(arr):
    return sorted(arr, key=lambda x: (count_factors(x), x))
input1 = [6, 8, 9]
input2 = [2, 4, 7]
print(custom_sort(input1))
print(custom_sort(input2))
