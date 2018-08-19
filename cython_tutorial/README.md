# Compile as cyhton 
- save the `*.py` file as `*.pyx`
- create a `setup.py` file - refer to example
- run `python setup.py build_ext --inplace`
- Now this will create the compiled file where you can actually import

# Run peformance test
- to begin with, we can modify the `*.pyx` file
- check the example for the actual modification, basically you can use `cpdef` for the function, and for each variable, declare with data type
- run `python setup.py build_ext --inplace` again to re-compile
- then we can run the performance test by using the timeit module, see code example

# Run Cython to see html
- run for example,  `cython -a example_cy.pyx` and it will generate an html that tells you the interaction with python
