def gen_function(n):
    while n:
        print(f'yield: {n}')
        yield n   # the generator resumes where it left off
        n -= 1

gen = gen_function(3)

next(gen)
next(gen)
next(gen)