---
title: Return multiple values
layout: default
parent: Subprograms
has_children: true
---

{% include article_header.md %}

## What
Python provides nice syntax for 'returning multiple values'.
In reality, only one value is returned: a tuple containing all the specified values.

Python does not allow returning multiple values but its syntax gives the illusion of doing so:
- Python can return a tuple (parentheses optional)
- Syntax for multiple assignments makes unpacking the tuple trivial

## Why
By 'returning multiple values' and using Python's convenient syntax, you group return values without using or defining a complex data structure.
This can make your code more readable.

## Examples

### Return a tuple explicitly
We could similarly return a list or dictionary.
```python
{% include_relative examples/multiple-returns-explicit.py %}
```

### Return a tuple implicitly
Python does not require parentheses around the grouped values being returned, it groups them in a tuple automatically.
```python
{% include_relative examples/multiple-returns-implicit.py %}
```

### Things you should know
You are encouraged to question whether returning values grouped in a tuple is sensible.
Just because you can do it, doesn't mean that you should.

When you start returning more than a couple of grouped values, it's probably time to start thinking about using a custom data structure/class to better organise your data.
