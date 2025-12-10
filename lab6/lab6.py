from decorator import require_args

@require_args(3)
def test(a, b, c=0):
    return a + b + c

print(test(2,5,7))      # OK

print(test(2,3))            # Недостатньо аргументів
