---
layout: default
title: Worksheet
nav_order: 3
parent: Lesson 2
---

{% include article_header.md %}

## Investigate
Answer these questions by examining the code.

1. What does `from models import Ball` do in `main.py`?
1. Why does `main.py` create a list of balls instead of storing them in separate variables?
1. What do the two `for` loops do in `main.py`?
1. What is unusual about the constructor signature?
  - What does `p_color=(255, 0, 0), p_vx=0, p_vy=0` mean in the constructor signature in `models.py`?
  - Why do the other parameters not have `=` signs?
  - What do the `=` signs mean?
1. Why does the `Ball` object need all of the parameters as attributes? 
1. Why are the `__draw()` and `__move()` methods private?
1. Why does `update()` call both `__move()` and `__draw()`?
1. Why does the `__draw()` method need `screen` as a parameter?

## Modify
Make changes to explore how the code works.

1. Implement the constructor using the information below:

    | Visibility | Name   | Type | Description |
    |-----------|--------|------|-------------|
    | private   | `x`    | int  | Horizontal position of the ball’s centre |
    | private   | `y`    | int  | Vertical position of the ball’s centre |
    | private   | `vx`   | int  | Horizontal velocity (change in x each frame) |
    | private   | `vy`   | int  | Vertical velocity (change in y each frame) |
    | private   | `color` | tuple  | Colour in `(R, G, B)` format|
    | private   | `radius` | int | Size of the ball |

2. Implement the `__draw()` method
3. Implement the `__move()` method
    - At this stage, **do not** implement bouncing



## Make
1. Use the information below to implement the missing `get` methods (`get_coords()`, `__get_left()`, `__get_right()`, `__get_top()`, `__get_bottom()`).

    The `__get_<direction>()` methods should return the position of the ball's edge in that direction (hint: how can you use the ball's radius to work this out?).

| Visibility | Method Signature | Returns | Description |
|-----------|------------------|---------|-------------|
| public    | `get_coords()` | tuple[int, int] | Returns `(x, y)`, the ball’s current position |
| private   | `__get_left()`   | int | Returns the x-coordinate of the left edge (`x - radius`) |
| private   | `__get_right()`  | int | Returns the x-coordinate of the right edge (`x + radius`) |
| private   | `__get_top()`    | int | Returns the y-coordinate of the top edge (`y - radius`) |
| private   | `__get_bottom()` | int | Returns the y-coordinate of the bottom edge (`y + radius`) |
| private   | `__draw(screen)` | None | Draws the ball on the given `screen` |
| private   | `__move(x_bounds, y_bounds)` | None | Updates the ball’s position (later: add bouncing) |
| public    | `update(screen, x_bounds, y_bounds)` | None | Calls `__move` then `__draw` each frame |


2. Once all the getters work, update `__move` so the ball cannot leave the window.
    - When the ball reaches and edge, it should bounce by reversing the appropriate velocity.

You will need to update the `update()` method:
```python
def update(self, screen, x_bounds, y_bounds):
    """
    Move and draw the ball.

    Parameters:
        screen: a pygame screen
        x_bounds: a tuple containing the lower and upper x bounds, e.g. (0, WIDTH)
        y_bounds: a tuple containing the lower and upper y bounds, e.g. (0, HEIGHT)
    """
    self.__move(x_bounds, y_bounds)
    self.__draw(screen)
```

## Extensions
Complete these tasks in any order.

### Colour changing
1. Implement a `__change_color(new_color)` method to change the ball's colour
1. Modify `__move` so the ball changes colour each time it bounces.

### Inside-bounds?
Implement a `inside_bounds(x_bounds, y_bounds)` method:
- Returns True if every part of the ball is within given bounds
- Returns False otherwise

### Randomised bounce velocities
Change `__move()` so that, when the ball bounces, the velocity is slightly randomised.
Make sure the ball cannot become frozen!

### Decaying velocity
Create a `DecayingBall` class that inherits from `Ball`.
- Add a new attribute, `decay_factor` (e.g., 0.9)
- Override `__move()` so that velocity is scaled after each bounce
