---
title: Default parameters
layout: default
parent: Subprograms
has_children: true
---

{% include article_header.md %}

## What
Default parameters allow parameters to be initialised with default values if no value is provided in the subprogram call.
The default values of such parameters are specified in the subprogram signature; these default values can be overridden when the subprogram is called.

Providing a default value for a parameter makes the parameter optional in subprogram calls.
When an overriding value is not provided, the parameter is initialised with its default value.

## Why
Default parameters are never mandatory, their inclusion is a design choice.

As providing a default value for a parameter makes the parameter optional in subprogram calls, callers of the subprogram only need to provide values to such parameters when they should differ from the default.
This makes subprogram calls that use default parameters (and do not override them) shorter and can reduce repetition: rather than passing the same value again and again, the value is written once in the subprogram signature.

## Examples

### Simple value
The default value represents the most common use of the subprogram.
```python
{% include_relative examples/default_param_greeting.py %}
```

### Boolean flag
The default value controls optional behaviour rather than storing required data; such boolean parameters are often called flags.
```python
{% include_relative examples/default_param_boolean_flag.py %}
```

### Constructor
The default value sets the initial state of the object when no explict value is provided.
```python
{% include_relative examples/default_param_constructor.py %}
```

## Things you should know
### When to use
Default parameters are only useful when sensible default values exist.
There is no benefit to using default parameters that will be overridden all the time.

Including default parameters suggests the normal behaviour of your subprograms so default parameters should be chosen intentionally.

### Ordering of parameters
You cannot place required (positional) parameters after parameters with default values.
For this reason, all default parameters must appear at the end of a subprogram's signature.

Although default parameters can be passed positionally, it is generally clearer to use [keyword arguments](kwargs), especially when a subprogram has multiple default parameters.

The following example shows multiple default parameters being passed both positionally and using keyword arguments.
Using keyword arguments makes it possible to ignore parameters whose default values you want to keep, and makes code more readable.
```python
{% include_relative examples/default_param_multiple.py %}
```