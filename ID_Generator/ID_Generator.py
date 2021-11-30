import string
import random
def id_generator( ):
    size = int(input())
    chars=string.ascii_letters + string.digits
    unique = ''.join(random.choice(chars) for _ in range(size))
    return unique


print(id_generator())