# getactivewindow-x
Separate component to get information on the active window in X.

### Why?

In an attempt to be portable between operating systems.

### Internal details

Use a fork of `python-libxdo`.

### API

Currently there are only 2 functions.

```
def active_window_name()->str:
def active_window_class()->tuple[str, ...]:
```
