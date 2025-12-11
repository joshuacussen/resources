---
layout: default
title: Objectives
nav_order: 2
parent: Lesson 2
---

{% include article_header.md %}

## Working with multiple files
- Explain what `from x import y` does
- Import a class definition from another file
- Explain the benefits of splitting code across multiple files

## Subprograms
- Set default values for parameters
- Explain the benefit of using parameters with default values

## Object-oriented fundamentals in Pygame
- Apply principles of object-oriented design to organise data and behaviour of game entitites
- Explain why game entities benefit from being stored as objects rather than in separate variables
- Understand why attributes like position, velocity, radius, and colour must be stored in the object

## Updating and drawing via an object
- Represent movement using velocity components
- Use iteration to update many objects each frame
- Understand the separation of concerns between
    - `update` (public, frame-level behaviour)
    - `_move` (private, internal position/physics logic)
    - `_draw` (private, internal rendering logic)


## Coordinates, edges, and boundaries
- Understand the difference between an object's position and its edge coordinates
- Implement methods to get an object's position and edge coordinates
    - Use bounds (e.g., `x_bounds`, `y_bounds`) to detect boundary interactions
    - Implement basic bouncing by reversing velocity when reaching an edge

## Code quality
- Apply encapsulation and good method design to keep responsibilities clear
- Use data hiding and getters to expose only information needed outside the class definition