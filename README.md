# My-Helper-Functions
This repository is containing functions that I use in Python a lot.

# Important Python Concepts in OOP

1) Inheritance: Using methods and attributes of a parent Class in Child Class

2) Encapsulation: Accessing the attribute of a Class only in itself(private) by defining the attributes starting with double underscore __. Single underscore _ used for defining protected attributes in a class. Protected means accesible with the Class and its subclasses. No underscore for public attributes.

3) Polymorphism: Being available to send different inputs to a method or a function like Python's built-in len function.

4) Method Overriding: Rewriting a method inherited from a parent class in the Child class.

5) Method Overloading: Calling same method with different number of parameters like we did in C#. Two methods can't have the same name in Python. Not possible in Python.

6) property usage in Python classes. property is making a method as an attribute of a Class

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

a = 2

b = 0

```
try:
    mysub = a /b
except:
    logging.critical("exception occurred: ",exc_info=True)
    #The above line prints traceback errors

```

21) The standard logging format is `'%(asctime)s - %(levelname)s - %(message)s'`



