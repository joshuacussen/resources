---
title: Keyword arguments
layout: default
parent: Subprograms
has_children: true
---

{% include article_header.md %}

## What
Keyword arguments explicitly match arguments to parameters using the parameters' identifiers.

## Why
Using keyword arguments makes longer function calls more readable by explicitly naming the parameters and assigning their values.

Additionally, keyword arguments match by name rather than position.
Keyword arguments do not change whether an argument is required or not, they just give flexibility about ordering in subprogram calls.

The flexibility of ordering enabled by keyword arguments is extremely helpful when using [default parameters](default-parameters) as it allows their use irrespective of position.

## Examples

### Ordering parameters
If you use keyword arguments for all the arguments in the subprogram call, the order does not matter at all.

```python
{% include_relative examples/kwargs_simple.py %}
```

### Default parameters
Keyword arguments are useful and improve readability when using [default parameters](default-parameters).

```python
{% include_relative examples/kwargs_default_param.py %}
```