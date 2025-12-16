---
title: Default parameters
layout: default
parent: Subprograms
has_children: true
---

{% include article_header.md %}

## What
Python allows setting default values for parameters in subprograms.
Default parameters have values specified in the subprogram's signature; their values can be overridden when the subprogram is called.

Including a default value for a parameter makes the parameter optional, meaning any calls of the subprogram do not need to provide a value for that parameter.
When an override value is not provided, the value of the parameter falls back to its default.

## Why
Default parameters are never mandatory, their inclusion is a design choice.

By making a parameter optional and explicitly stating a default value, callers of a subprogram only need to provide values to parameters when they should differ from the default.
This makes subprogram calls that use default parameters (and do not override them) shorter and more readable as their values are already included in the subprogram's definition.

## Examples

### Default parameter with simple value
The default value represents the most common use of the subprogram.
```python
{% include_relative examples/default_param_greeting.py %}
```

### Default parameters using boolean flags
The default value controls optional behaviour rather than storing required data; such boolean parameters are often called flags.
```python
{% include_relative examples/default_param_boolean_flag.py %}
```

### Default parameters in constructors
The default value sets the initial state of the object when no explict value is provided.
```python
{% include_relative examples/default_param_constructor.py %}
```

## Things you should know
### Ordering of parameters
You cannot place required (positional) parameters after parameters with default values.
For this reason, all default parameters must appear at the end of a subprogram's signature.

Although default parameters can be passed positionally, it is generally clearer to supply them using named arguments, especially when a subprogram has multiple optional parameters.

The following example shows multiple default parameters being passed both positionally and using named arguments.
Using named arguments makes it possible to ignore parameters whose default values you want to keep, and makes code more readable.
```python
{% include_relative examples/default_param_multiple.py %}
```