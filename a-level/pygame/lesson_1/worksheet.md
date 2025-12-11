---
layout: default
title: Worksheet
nav_order: 3
parent: Lesson 1
---

{% include article_header.md %}

## Predict

Predict answers to the following questions without running the program.

1. What colour will the background be?
1. What shape will be drawn? Where?
1. What will happen to the shape over time?
1. What does `clock.tick(60)` control?
1. What will happen when you close the window?

## Run

Run the program.
Compare your predictions to the actual behaviour.

## Investigate

Answer these questions by examining the code.

1. On what line is the window size set?
1. How would you double the window size?
1. What does changing
   `pygame.draw.circle(screen, (0, 0, 255), (x, 200), 40)`
   to
   `pygame.draw.circle(screen, (0, 255, 0), (x, 200), 40)`
   do?
    - What does this tell you about how Pygame represents colours?

1. Which line number makes the shape move?
1. Which line number is responsible for drawing the shape?
1. What happens if you comment out the line `pygame.display.flip()`?
    - What does this tell you about what this line does?
1. What happens if you comment out the line `clock.tick(60)`?
    - What does this tell you about what this line does?
1. What happens when the shape reaches the edge of the window?

## Modify
Make changes to explore how the code works.

1. Identify and remove at least three magic numbers by replacing them with variables.
1. Change the colour of the background to a colour of your choosing.
1. Replace the circle with a rectangle (see the [docs](https://www.pygame.org/docs/ref/draw.html))
1. Make changes to the movement of the shape:
    1. Make it move faster
    1. Make it move in the opposite direction
    1. Make it move diagonally
1. Add a new shape that is centered based on a calculation using `WIDTH` and `HEIGHT`
1. Prevent the shape from leaving the window.
    - Hint: use selection and check the x-coordinate relative to `WIDTH` and `0`

## Make
Create a small animation scene using only things covered so far.

### Requirements
Your animation must include:
- One static shape
- One moving shape
- At least one colour change
- One use of `WIDTH` or `HEIGHT` in a calculation

### Ideas to try
- A rectangle sliding across the screen
- A circle moving diagonally
- A shape that changes colour once at startup
- A shape that changes colour every 10 clock ticks
- Something positioned using `WIDTH // 3` or `HEIGHT // 4`