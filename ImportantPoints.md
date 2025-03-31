# Python Type Hinting

## Overview

Type hinting in Python allows you to specify the expected types of variables, function arguments, and return values. This helps improve code readability, maintainability, and allows for type checking tools like `mypy` to validate code.

## Common Type Hinting Examples

### `List[str]`

- Represents a **list of strings**.

#### Example:

```python
from typing import List

def print_strings(lst: List[str]) -> None:
    for string in lst:
        print(string)

print_strings(["apple", "banana", "cherry"])
# Output:
# apple
# banana
# cherry
```
