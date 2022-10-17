# PyDict

A simple wrapper around the Oxford dictionary API. It is recommended 
that you do **not** use this. 

## Usage

First, get an API key from Oxford dictionary website and set appropiate 
environment variables. Again, don't use this.

```python
import pydict

hello = pydict.search("hello")
print(hello.definitions.pop())
# say or shout ‘hello’
```