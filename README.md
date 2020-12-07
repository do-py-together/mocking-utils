# mocking-utils
![release](https://img.shields.io/github/package-json/v/do-py-together/mocking-utils?label=release&logo=release&style=flat-square)
![build](https://img.shields.io/github/workflow/status/do-py-together/mocking-utils/test?style=flat-square)
![coverage](https://img.shields.io/codecov/c/github/do-py-together/mocking-utils?style=flat-square)
![dependencies](https://img.shields.io/librariesio/release/pypi/mocking-utils?style=flat-square)

Highly useful utilities for mocking execution flow during unit test execution.

## Quick Start
### Installation
```pip install mocking-utils```
### Usage
```
from mocking_utils import MockFunction

class A(object):
    def my_method(self):
        print('I am in my_method')

a = A()
a.my_method()  # Out: 'I am in my_method'
mock = MockFunction(A, 'my_method', lambda x: print('lambda function'), call=True)
a.my_method()  # Out: 'lambda function'
mock.reset()
a.my_method()  # Out: 'I am in my_method'
```
### Examples
pytest
```
from mocking_utils import MockFunction

@pytest.fixture(scope='module', autouse=True)
def setup__teardown():
    """
    Standard setup & teardown within a module of unit tests.
    """
    mocks = [
        MockFunction(A, 'my_method', lambda x: print('lambda function'), call=True)
        ]
    yield 'Setup complete'
    [mock.reset() for mock in mocks]
```

### Testing & Code Quality
Code coverage reports for master, branches, and PRs 
are posted [here in CodeCov](https://codecov.io/gh/do-py-together/mocking-utils).

