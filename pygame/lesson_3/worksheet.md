---
layout: default
title: Worksheet
nav_order: 3
parent: Lesson 3
---

{% include article_header.md %}

## Predict
Predict answers to the following questions without running the program.

1. What does `setup()` do in `main.py`?
1. What does this line do in `main.py`?
    ```python
    screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
    ```
1. What will the the initial x-coordinate of `player` be?
1. What colour will the player be?
1. What will happen to `player` when the right arrow key is pressed?
    - Predict how the player's movement will change
1. What will happen to `player` when the right and up arrow keys are pressed simultaneously?
    - Will the player move in a straight line, diagonally, or not at all?


## Run
Run the program.
Compare your predictions to the actual behaviour.

## Investigate
Answer these questions by examining the code.

1. Why is `setup()` separate from `main()`?
    - What responsibilities does `setup()` have?
    - What effect does separating these responsibilities have on readability and organisation?
    - Identify at least one other part of `main()` that could be separated into its own subprogram.
      Justify your answer.
1. How does the program know what `WIDTH` and `HEIGHT` are?
    - Which file defines them?
    - How does `main.py` gain access to them?
    - Does the `Player` class know anything about `WIDTH` and `HEIGHT`?
      Why or why not?
1. Look at how the `Player` object is created in `main()`.
    - Which parameters are passed to the constructor?
    - What is unusual about the way the parameters are passed?
    - What effect does this have on the code's readability? 
1. Look at the `Player` class constructor.
    - Which attributes are public?
    - Which attributes are private?
    - Why might private attributes be useful here?
    - Why does it not store x, y, width, and height?
      Where is this data stored instead?
1. What does the `set_velocity()` method do?
    - How does this relate to key presses in `main()`?
1. What does `player.update(screen)` do each frame?
    - Why does the order of method calls inside `update()` matter?
    - Why is this method public, but `__move()` and `__draw()` are private?

## Modify
Make changes to explore how the code works.

1. Change which keys move the player.
    - Rather than arrow keys, control the player with WASD
1. Enable diagonal movement.
    - Hint: how does `if` differ from `elif` in this context?
1. Implement `reset_position()`.
    - Pressing the R key should reset the player to their starting position (this should be controlled in `main()`)
    - Hint: does `Player` need to remember its initial position when created?
1. Make the player move continuously even after releasing a key.
    - Pressing a key should set the velocity
    - The player should continue moving after the key is released
    - Hint: which line currently overwrites the velocity each frame?
1. Stop the player leaving the window.
    - Modify `__move()` so the player cannot move off-screen.
    - Use `rect.x`, `rect.y`, `rect.width`, and `rect.height`
    - The player should stop at the boundary, they should not bounce.
1. Implement `increase_speed()`.
    - Pressing the spacebar should increase the player's speed (this should be controlled in `main()`)
    - The player's speed should not be able to exceed its max_speed.



## Make
Create a new class called `Enemy` that automatically moves toward the player each frame.

### Requirements
Your `Enemy` class must:
1. Use a `pygame.Rect` to represent position and size.
1. Store private attributes for:
    - colour
    - velocity (x and y)
    - speed
1. Implement:
    - a public `update(screen, player)` method
    - a private `__move(player)` method
    - a private `__draw(screen)` method
1. Move toward the player's position each frame.
    - Hint: compare the enemy's x/y coordinates to the player's.
1. Respect window boundaries and stop at the edges.
1. Appear on screen alongside the player.

### Hints

You can get the player's centre using:
```python
px = player.rect.centerx
py = player.rect.centery
```

To decide which way to move, imagine the enemy asking if the player is to their right or to their left:

```python
if px > self.rect.centerx:
    # player is to the right
elif px < self.rect.centerx:
    # player is to the left
```

When the enemy knows the player's direction, they just need to move!
The enemy doesn't teleport, they just take small steps towards the player.
Each small step should be the enemy's speed value.

You will need to extend this to work with the y-axis too.

### Options
Choose two or more optional enhancements:
- Fast and slow modes
    - Press a key to toggle between fast and slow chasing speeds
- Only chase when close
    - The enemy only starts moving if the player is within a certain distance (import `math` and use `distance = math.dist((x1, y1), (x2, y2))`)
- Enemy changes colour depending on distance:
    - Red when close
    - Blue when far
- Multiple enemies
    - Create a list of enemies and update them all
- Enemy freezes when the player isn't moving
- Implement a superclass that both `Player` and `Enemy` inherit from
