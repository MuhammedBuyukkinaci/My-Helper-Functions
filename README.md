# My-Helper-Functions
This repository is containing functions that I use in Python a lot.

# Important Python Concepts in OOP

1) Inheritance: Using methods and attributes of a parent Class in Child Class

2) Encapsulation: Accessing the attribute of a Class only in itself(private) by defining the attributes starting with double underscore __. Single underscore _ used for defining protected attributes in a class. Protected means accesible with the Class and its subclasses. No underscore for public attributes.

3) Polymorphism: Being available to send different inputs to a method or a function like Python's built-in len function.

4) Method Overriding: Rewriting a method inherited from a parent class in the Child class.

5) Method Overloading: Calling same method with different number of parameters like we did in C#. Two methods can't have the same name in Python. Not possible in Python.

6) property usage in Python classes. property is making a method as an attribute of a Class

7) self is a conventional name in Python classes, not a magical keyword. It could be s or me or whatever we name. 

8) To check if a variable has a numeric type of Float, integer, Decimal etc; use isinstance.

```filename.py
import numbers
isinstance(variable_name,numbers.Number)
```

![property](./images/000.png)

# Python Logging

[Video Link 1](https://www.youtube.com/watch?v=-ARI4Cz-awo)

[Video Link 2](https://www.youtube.com/watch?v=jxmzY9soFXg)

1) Python logging becomes more meaningful when the project gets bigger.

2) Logging levels allow us to specify exactly what we want to log by separating these into 5 different categories.

- DEBUG: Detailed info, typicaly of interest when diagnosing problems.

- INFO: Confirmation that things are going well

- WARNING: An indication that something unexpected happened, or indicative of some problem in the near future("eg, disk space low"). The software is still working as expected.

- ERROR: Due to a more serious problem, the software hasn't been able to perform some function.

- CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

3) The default level for logging is set to Warning. If logging is set to warning, it will show warning, error and critical loggings. If it is info, it will show info,warning, error and critical.

![logging_levels](./images/001.png)

4) Python logging is similar to print statement in terms of functionality. An example code for logging is as follows:

```
import logging
def add(x,y):
    return x + y

a = 10
b = 5

add_result = add(10,5)

logging.debug("{} + {} = {}".format( a, b, add_result ) )

```

5) To change logging level

```
import logging
#logging.DEBUG is different than logging.debug. logging.DEBUG is an integer in the background.
logging.basicConfig(level=logging.DEBUG)
```

6) Log files are great way to capture information because it allows to see our logged information over time in one place.

7) Use log files instead of printing on console.

8) Store your logs in a log file like I did below

```
import logging
logging.basicConfig(filename='test.log',level=logging.DEBUG)
```

9) We can format log lines by specifying in configuration.

```
import logging
# Log in this format: time:loglevel:message
logging.basicConfig(filename='test.log',level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')
```

10) You can take a look at python log attributes from [here](https://docs.python.org/3/library/logging.html#logrecord-attributes).

11) Name like root can be specified in format of logging.basicConfig like below:

```
import logging
# Log in this format: time:loglevel:message
logging.basicConfig(filename='test.log',level=logging.DEBUG,format='%(asctime)s:%(name)s:%(message)s')
```

12) Since we haven't specified a specific logger, we are working with root logger. Working with root logger isn't the best option. If we are importing file01.py from file02.py, logger configuration of file01.py will be valid in file02.py. Logger configuration of file02 will be invalid.

13)  Despite we define a logger using logging.getLogger, we are still configuring using logging.basicConfig()

```file01.py
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='test.log',level=logging.DEBUG,format='%(asctime)s:%(name)s:%(message)s')
logger.info('What will be logged here')

```

14) We can split parameters of logging.basicConfig into different lines. If file01.py run directly, the name is __main__. If we import file01.py from file02.py, the name in lines of log file is file01.

15) We are adding formatting to file handler, not to the logger. Logging level should be attached to logger directly.

16) If we want to keep only errors in log file, we can make this by specifying `file_handler.setLevel(logging.ERROR)`.

```file01.py

# Importing module
import logging
# Creating a logger object
logger = logging.getLogger(__name__)
# Setting logging level in the script as INFO
logger.setLevel(logging.INFO)

# Defining a log formatter
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
# Defining a file handler and its affiliated log file.
file_handler = logging.FileHandler('logfile.log')
# Keep only ERROR logs in the log file
file_handler.setLevel(logging.ERROR)
# Binding formatter to file handler
file_handler.setFormatter(formatter)
# Binding file handler to logger
logger.addHandler(file_handler)

##Use the defined logger below instead of logging module

logger.info("log message here")
#logger.exception("log message here")
```

17) If we want to have a traceback in errors in order to have more infos, use `logger.exception("log message here")` instead of `logger.error("log message here")`

18) If we want to see loggings on consele in the phase of runnning, use stream handler. One logger can have 2 handlers, one of them is file handler and the other one might be stream handler.

```
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('logfile.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

# To show on console
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

# Link handlers to loggers
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# Log messages
logger.info("log message here")

```

19) One of them most used formats is "{asctime} {levelname:<8} {message}" with style = "{"

```
import logging
logging.basicConfig(format = "{asctime} {levelname:<8} {message}",  style = '{' )
```

20) Filemode can be either 'a' or 'w'. 'w' overrides the existing one.

21) If you are using try and except words in Python code, python logging is great to capture what is going on. It gives tracebacks etc.

```
a = 2

b = 0


try:
    mysub = a /b
except Exception as e:
    logging.critical("exception occurred: ",exc_info=True)
    #The above line prints traceback errors

```

21) The standard logging format is `'%(asctime)s - %(levelname)s - %(message)s'`.

22) filemode in logging.basicConfig() is either 'a' (append) or 'w' (write). 'w' deletes the log file and recreates it. 'a' just adds new logs to existing files.

23) We can add process id to logging.basicConfig via '%(process)d' to format attribute.

24) If we want to trace back the error, use one of the lines below based on your desired log level.

```
logging.info("info level: ",exc_info=True)
logging.warning("warning level: ",exc_info=True)
logging.error("error level",exc_info=True)
logging.critical("warning level: ",exc_info=True)
```

25) We can define a configuration file in conf format or yaml format and load it in Python code like below.

```
import logging
import logging.config
logging.config.fileConfig(fname='file.conf', disable_existing_loggers=False)

```

26) We can set filemode either 'a'  (append) or 'w' (write) in logging.FileHandler(mode = 'w').

27) `The difference between different logging options are below:

- logger.error("message here"): will print out only error
- logger.error("message here", stack_info=True, exc_info=True): will print error, traceback and stack.
- logger.error("message here", exc_info=True): will print out error and traceback(same as **logger.exception("message here")**)
- logger.exception(e): will print out error and traceback (same as **logger.error("message here", exc_info=True)** )


28) [graypy](https://github.com/severb/graypy) is a python library to send python logs into Graylog in the format of GELF (Graylog Extended Log Format).

# Python Testing

1) Exploratory testing is a test without a plan.

2) In order to have a complete set of manual tests, what is required is to list all features our application has, different types of input it can accept and the expected results.

3) Testing multiple parts of our application is called **Integration testing**.

4) If you have many test files, create a folder named **tests** and locate your tests there.

5) Testing in Django and Flask is slightly different than unittest.

6) Functional tests follow 3A's principle.

- Arrange: the conditions for the test
- Act: calling some function or method
- Assert: check the condition is True

# Unit Testing

[Video Link](https://www.youtube.com/watch?v=6tNS--WetLI)

1) Good Unit Test will make sure that everything is working as it should.

2) Testing code with print statements isn't easy to automate. It is hard to maintain.

3) Naming convention: If we want to test a module named **calc.py**, testing file should be **test_calc.py**.

4) The methods in Class in testing file should start with **test_**. This is a naming convention. If we want to test add function, method name should be **test_add**.

5) We can obtain unittest assert methods from [here](https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug).

6) To test the code, run the folloing on Terminal

```
python -m unittest test_calc.py
```

7) If we want to run in a way of `python test_calc.py` instead of `python -m unittest test_calc.py` , add the following to the bottom line of **test_calc.py**

```
if __name__ == '__main__':
    unittest.main()
```

8) We should test a couple of edge cases(different scenarios for different inputs) instead of testing one scenario.

9) When we added 3 different `self.assertEqual(result,15)` to test_add method of TestCalc class, we run one test by 3 different checks.

10) If there are 4 tests in our test script and the third one failed, the output is like **. . F .**

11) assertRaises is taking 3 or more parameters like `self.assertRaises(ValueError,calc.divide,10,0)`. The **ValueError** is the error we want to see. **calc.divide** is the method we called. 10 and 0 are parameters we passed into **calc.divide**.  We aren't directly calling via calc.divide(10,0) because it raises a ValueError doesn't check the situation. However, testing exceptions aren't preferred mostly.

12) Testing exceptions via context managers are more preferrable like below

```
with self.assertRaises(ValueError):
    calc.divide(10,0)
```

13) Programmers try to make their code DRY(Don't repeat yourself). If we are using some piece of code in multiple tests, we should use `setUp()` and `tearDown()` method in out test. **setUp** method will run its code before every single test and **tearDown** method will run its code after every test. For instance, we can create a DB in `setUp()` and destroy it in `tearDown()`.

```file.py

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.emp_1 = Employee('Muhammed','Buyukkinaci',5000)
        self.emp_2 = Employee('Ahmet','Yilmaz',4000)

    def tearDown(self):
        pass

    def test_something(self):
        self.assertEqual(self.emp_1.fullname,'Muhammed Buyukkinaci')


```

14) If we want to run a piece of code at the BEGINNING of tests just ONCE, we can use **setUpClass(cls)** method. If we want to run a piece of code at the END of tests just ONCE, we can use **tearDownClass(cls)**. They are classmethods and no need to create an instance from the class. An example usage is to read a table from DB and use it in all test scenarios.

```file.py
class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
    
        print('tearDownClass')

    def test_something1(self):
        print("test_something1")
        self.assertEqual(self.emp_1.fullname,'Muhammed Buyukkinaci')

    def test_something2(self):
        print("test_something2")
        self.assertEqual(self.emp_1.fullname,'Muhammed Buyukkinaci')
    
    def test_something3(self):
        print("test_something3")
        self.assertEqual(self.emp_1.fullname,'Muhammed Buyukkinaci')

    # The output is as follows:

    # setUpClass
    # test_something1
    # test_something2
    # test_something3
    # tearDownClass

```

15) In short, mocking is creating objects that simulate the behavior of real objects in unit testing. The aim of mocking is to isolate and focus on the code, not to focus on extermal resources. Mocking means creating a fake version of an external or internal service that can stand in for the real one.

16) For example, we wrote a function which scrapes data from a website. However, the website was down. Therefore, our tests would fail. This isn't what we want. In this scenario, using mocks in unit testing sound logical.

17) Test should be isolated. Your tests shouldn't rely on other tests or affet other tests. Run each test independently.

18) Test Driven Development is that you write tests before you write the code.

19) Any testing is better than no testing. Even if you write some basic assertions, It is better than nothing.

20) unittest module in Python is originally inspired from Java's JUnit.

# Pytest

[Video Link 1](https://www.youtube.com/watch?v=etosV2IWBF0)

[Video Link 2](https://www.youtube.com/watch?v=fv259R38gqc)

[Blog Post](https://realpython.com/pytest-python-testing/)

1) Test is code that runs to check the validity of other code.

2) Pytest is the basis for a rich ecosystem of testing plugins and extensions.

3) `assert` is the way to do testing in Pytest

4) Ist API is easier than unittest API.

![property](./images/002.png)

5) pytest looks for a file starting with test_. Also, the name of function to be tested should start with test_

6) If there are 2 assertions in one function, it is one test; not 2 tests.

7) The test should be roughly divided into 3 phases: **Arrange**, **Act**, **Assert**. Arrange is setting up anything that needs to go before the action happens.

8) In test driven development, declare something that clearly doesn't exist yet. We want test to drive out what it is I want to make.

9) Functions names in test file must be unique.

10) The reason why we write tests is to validate our code and not to have to go through process of manually checking things over and over again.

11) Assert by themselves without pytest can explode our code if assert is False

12) Using try/except in Python means "I give up, I don't know how to do this. Somebody above me, please handle this".

13) If we want to raise an error and run our test properly, use below

```demo.py
def add(a,b):
    if a==99:
        raise MysteryError()
    return a + b
```

```test_demo.py
def test_error():
    # Waiting the code to fail. The test runs properly in terminal
    with pytest.raises(demo.MysteryError):
        demo.add(99,1)s
```

14) If the first assertion in test method fails, it aborts the rest of the test.

```test_demo.py
def test_sth():
    assert 1 == 1 # running and successful
    assert 2 == 1 # running and fail; the below asserts not run
    assert 3 > 2 # not running
```

15) Pytest has a feature called parametrize to run all asserts even if the above asset fails to run. If we have multiple failures in test, we have multiple error log chunks. It is a useful tool if you want to test your code against a bunch of
scenarios.

16) We can group tests in test files via creating Classes like TestAdd.

17) Fixtures have various capabilities. Each test using fixture must explicitly accept that fixture as an argument.
- Fixtures allow us to set up some import things before each test to runlike unittest's setUp and tearDown methods.Fixtures are for setup/reuse purposes. 
- Fixtures are providing data.
- Fixtures are also similar to unittest's mocking.

18) Create a conftext.py and define a fixture named *my_fixture*. Feed this **my_fixture** in test_fixture of test_demo.py.

```conftest.py
import pytest
@pytest.fixture
def my_fixture():
    return 51
```

```test_demo.py
def test_fixture(my_fixture):
    assert my_fixture ==51
```

19) There is a library called pytest django, which is an extension to Django Framework.

20) capsys is a pretty cool tool to capture system output.

21) Mnkeypatch is a fixture. monkeypatching is a terminology used when you want to dynamically add runtimes, swap out the behavior of a thing.

22) tmpdir is creating a new file and prints results on it and delete it ultimately.

23) Multiple fixtures operate at the same time.

24) Pytest's fixture mechanism is implicit and hard to understand here this idea comes from.

25) To list available fixtures on Terminal

```
pytest --fixtures
```

26) F means test failed and E means there is an unexpected exception.

27) If we have 4 tests in our script and only want to test 2 of these 4, filter them via pytest -k 'test_add'. Usage is `pytest test_demo.py -k 'test_with_param'`.

```test_filter_based_on_name.py
def test_add_tuple():
    #some code here
def test_add_list():
    #some code here
def test_subtract_tuple():
    #some code here
def test_subtract_tuple():
    #some code here
```

28) We can assign marks to our tests and check only these tests via -m parameter on console. A test may have multiple marks. Example: `pytest test_demo.py -k 'test_with_param'`

29) If we write 2 tests and both are using the same data, we can define a fixture via `@pytest.fixture` decorator and pass the fixture via argument into test method.

30) We should move fixtures to a different module(conftest.py) and import fixtures from test script.

31) After assigning marks to tests, register them on *pytest.ini*.

```pytest.ini
# content of pytest.ini. pytest.ini located in where pytest is executed.
[pytest]
markers =
    basics: basic assertions
    addition: a marker meaning addition
```

32) To run test in test_demo.py whose marks are 'basics'

```
pytest test_demo.py -m basics
```

33) Default markers are below obtained via `pytest --markers`:

- @pytest.mark.filterwarnings(warning): add a warning filter to the given test. see https://docs.pytest.org/en/stable/how-to/capture-warnings.- html#pytest-mark-filterwarnings 

- @pytest.mark.skip(reason=None): skip the given test function with an optional reason. Example: skip(reason="no way of currently testing this") - skips the test.

- @pytest.mark.skipif(condition, ..., *, reason=...): skip the given test function if any of the conditions evaluate to True. Example: skipif(sys.- platform == 'win32') skips the test if we are on the win32 platform. See https://docs.pytest.org/en/stable/reference/reference.- html#pytest-mark-skipif

- @pytest.mark.xfail(condition, ..., *, reason=..., run=True, raises=None, strict=xfail_strict): mark the test function as an expected failure if - any of the conditions evaluate to True. Optionally specify a reason for better reporting and run=False if you don't even want to execute the test - function. If only specific exception(s) are expected, you can list them in raises, and if the test fails in other ways, it will be reported as a - true failure. See https://docs.pytest.org/en/stable/reference/reference.html#pytest-mark-xfail

- @pytest.mark.parametrize(argnames, argvalues): call a test function multiple times passing in different arguments in turn. argvalues generally - needs to be a list of values if argnames specifies only one name or a list of tuples of values if argnames specifies multiple names. Example: - @parametrize('arg1', [1,2]) would lead to two calls of the decorated test function, one with arg1=1 and another with arg1=2.see https://docs.- pytest.org/en/stable/how-to/parametrize.html for more info and examples.

- @pytest.mark.usefixtures(fixturename1, fixturename2, ...): mark tests as needing all of the specified fixtures. see https://docs.pytest.org/en/- stable/explanation/fixtures.html#usefixtures 

- @pytest.mark.tryfirst: mark a hook implementation function such that the plugin machinery will try to call it first/as early as possible.

- @pytest.mark.trylast: mark a hook implementation function such that the plugin machinery will try to call it last/as late as possible.

34) To show the slowest 3 tests

```
pytest --durations=3
```

35) Some useful Pytest plugins:

- pytest-randomly
- pytest-cov
- pytest-django
- pytest-bdd






