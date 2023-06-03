# getactivewindow-x

# Deprecated

maybe use `pywinctl` instead or one of the solutions in https://stackoverflow.com/q/10266281/5267751

See also https://github.com/Kalmat/PyWinCtl/issues/64

-----

Separate component to get information on the active window in X.


### Why?

In an attempt to be portable between operating systems.

The user can install another package that provides the same interface.

### Internal details

There's another branch [user202729/getactivewindow-x at spawn-xdotool-xprop-process](https://github.com/user202729/getactivewindow-x/tree/spawn-xdotool-xprop-process)
that uses subprocess, `xdotool` and `xprop`.

### API

Currently there are only these functions.

```python
def active_window_id()->WindowID:
def window_name(window_id: WindowID)->str:
def window_class(window_id: WindowID)->tuple[str, ...]:
```

The window name should not (but may) change if the window ID is constant.

Packages should not rely on `WindowID` type being `int`.
