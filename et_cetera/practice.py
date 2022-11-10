names = ["marcus", "babe", "fish", "yam"]

for x, y in enumerate(names):
    ...


def noise(*args):
    for name in names:
        yield name

for n in noise(names):
    print(n)