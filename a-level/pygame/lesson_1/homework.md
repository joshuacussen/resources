---
layout: default
title: Homework
nav_order: 4
parent: Lesson 1
---

{% include article_header.md %}

## Requirements
Create a short Pygame 'screensaver' with multiple animated elements.
Be as creative as you like.

- At least four animated shapes
- At least one shape whose movement changes over time (e.g., speed or direction)
- At least one shape that bounces off the edge of the window (separate to the shape above)
- A colour change that happens during the animation
- A timed event: after some amount of time, something must change (e.g., a shape appears/disappears, colour change, movement change)

## Options

Choose two or more optional enhancements:
- A shape that follows a curved path
    - Hint: change both x and y each frame by different amounts
- A shape that grows or shrinks in size
- A fade effect using gradually changing background colours
- A simple caption or title drawn using `pygame.font`
- A shape that 'reacts' to another (e.g., follows it, changes colour when near it)
- Encapsulate a shape and appropriate attributes in a class (e.g., position, speed, colour, update method)