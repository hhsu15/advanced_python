import timeit

cy = timeit.timeit('example_cy.test(5000)', setup='import example_cy', number=1000)
py = timeit.timeit('example_py.test(5000)', setup='import example_py', number=1000)

print('cy:',cy)
print('py:',py)
print("Cython is {} x faster!".format(py/cy))
