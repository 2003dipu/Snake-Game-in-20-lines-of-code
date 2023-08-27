# Snake-Game-in-20-lines-of-code
Sure, I'd be happy to explain each line of the provided code snippet:

```python
# snake game in 20 lines of code
import pygame as pg
y, step, head = segments = [15,16,17]
n, apple = step, 99
screen_fill = pg.display.set_mode([255] * 2, pg.SCALED).fill

while segments.count(head) % 2 * head % n * (head & 240):
    if e := pg.event.get(768):
        step = (e[0].key % 4 *17 + 15) % 49 - n
    segments = segments[apple != head:] + [head + step]

    screen_fill('black')
    if apple == head:
        apple = segments[0]
    for i, v in enumerate([apple] + segments):
        screen_fill('green' if i else 'red',
                    ((v-1)%n * y, (v-n)// n*y , y,y))
    pg.display.flip()
    head += step
    pg.time.wait(150)
```

Here's a breakdown of each line:

1. `import pygame as pg`: Imports the pygame library using the alias `pg`.

2. `y, step, head = segments = [15,16,17]`: Initializes the variables `y`, `step`, and `head` with values 15, 16, and 17, respectively. The `segments`
3. list is also initialized with the same values.

4. `n, apple = step, 99`: Initializes the variables `n` with the value of `step` and `apple` with the value 99.

5. `screen_fill = pg.display.set_mode([255] * 2, pg.SCALED).fill`: Creates a screen with dimensions 255x255 using `pg.display.set_mode()`
6. and assigns its `fill` method to the `screen_fill` variable.

7. The `while` loop begins, which serves as the main game loop. The loop continues as long as the condition in the loop header is true.

8. `if e := pg.event.get(768):`: Checks if any pygame events of type 768 (KEYDOWN events) have occurred. If an event is present,
9.  it assigns the first event to the variable `e`.

10. The next line calculates the new value for the `step` variable based on the pressed key and updates it.

11. `segments = segments[apple != head:] + [head + step]`: Updates the segments of the snake by appending the new head position to the list and removing the tail
12.  if the snake didn't eat an apple.

13. `screen_fill('black')`: Fills the screen with a black color.

14. `if apple == head:`: Checks if the head of the snake is at the same position as the apple.

15. If the apple was at the same position as the head, it assigns a new position for the apple.

16. The `for` loop iterates through each element (apple and segments) and draws them on the screen with colors green and red.

17. `pg.display.flip()`: Updates the display to show the new frame.

18. `head += step`: Updates the head position based on the current step.

19. `pg.time.wait(150)`: Pauses the program for 150 milliseconds, controlling the speed of the game loop.

The provided code is a compact implementation of a simple snake game using the pygame library. The code may seem quite condensed, and some expressions
might be a bit cryptic, but it demonstrates a creative approach to achieve functionality within a limited number of lines.
