from numbers import Number


def person(name,**data):
    print(name)
    print(data)

    for i,j in data.items():
        print(i,j)
person('Varun',age=22,city="New York",Country="USA",Number='7337291592')
