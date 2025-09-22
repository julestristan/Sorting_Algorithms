import random
def generate_list(size):
    return [random.randint(0, size * 100000) for _ in range(size)]