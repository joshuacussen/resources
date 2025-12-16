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

## Things you should know