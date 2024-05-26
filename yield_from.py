def chain(iterables):
    for iterable in iterables:
        for v in iterable:
            yield v

iterables = ('python', 'test')

print(list(chain(iterables)))

def chain(iterables):
    for iterable in iterables:
        yield from (v for v in iterable)

t = list(chain(iterables))
print(t)