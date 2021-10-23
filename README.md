# getactivewindow-x
Separate component to get information on the active window in X. Requires the executable xdotool (and xprop to get the window class).

### Why?

In an attempt to be portable between operating systems.

### Internal details

Use `xdotool` and `xprop`.

* **Why not python-libxdo?**

   Currently the library is (unfortunately) mostly unmaintained,
   although the cost of spawning a process can be expensive.

### API

Currently there are only 2 functions.

```
def active_window_name()->str:
def active_window_class()->tuple[str, ...]:
```
