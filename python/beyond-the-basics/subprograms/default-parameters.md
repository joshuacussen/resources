---
title: Default parameters
layout: default
parent: Subprograms
has_children: true
---

{% include article_header.md %}

## What
Python allows us to set default values for parameters in subprograms.
Default parameters have values specified in the subprogram's signature; their values can be overridden when the subprogram is called.

Including a default value for a parameter makes the parameter optional, meaning any calls of the subprogram do not need to provide a value for that parameter.

## Why
Default parameters are never mandatory, their inclusion is a design choice.

They allow the default use-case of a subprogram to be expressed directly in its signature.

As a result, callers only need to provide information when they want behaviour that differs from the default.
Calls that rely on the defaults are shorter and more readable, because the intended behaviour is already clear from the subprogram’s signature.

## Examples

### Default parameter with simple value
The default value represents the most common use of the subprogram.
```python
{% include_relative "examples/default_param_greeting.py" %}
```

### Default parameters using boolean flags
The default value controls optional behaviour rather than storing required data; such boolean parameters are often called flags.
```python
{% include_relative "examples/default_param_boolean_flag.py" %}
```

### Default parameters in constructors
The default value sets the initial state of the object when no explict value is provided.
```python
{% include_relative "examples/default_param_constructor.py" %}
```

## Things you should know
### Ordering of parameters
You cannot place required (positional) parameters after parameters with default values.
For this reason, all default parameters must appear at the end of a subprogram's signature.



Although default parameters can be passed positionally, it is generally clearer to supply them using named arguments, especially when a subprogram has multiple optional parameters.