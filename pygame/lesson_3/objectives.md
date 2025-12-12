---
layout: default
title: Objectives
nav_order: 1
parent: Lesson 3
---

{% include article_header.md %}

## Working with multiple files
- Store configuration values in a separate file
- Explain the benefits of storing configuration values in a separate file

## Program structure
- Create a `main()` subprogram to control the flow of the whole program
- Decompose the responsibilities of `main()` to separate subprograms

## Object-oriented design
- Construct objects using keyword arguments to make code more readable
- Understand how objects can be composed of Pygame components
- Apply encapsulation and data hiding: distinguishing between public behaviour and private, internal methods
- Use getters/setters to safely access and modify private attributes

## Game loop and update cycle
- Read continuous input using `pygame.key.get_pressed()`
- Map key presses to object behaviour (e.g., velocity, direction)
- Describe the structure of a frame update:
    - event handling
    - input processing
    - updating objects
    - drawing

## Movement and velocity
- Update position by modifying the Rect each frame
- Understand how different input structures (if/elif) affect movement rules