from dataclasses import dataclass
import subprocess
import ast
from typing import Union
import threading

from Xlib import X, display  # type: ignore

_thread_local = threading.local()

def get_thread_display()->display.Display:
    if not hasattr(_thread_local, 'display'):
        _thread_local.display = display.Display()
    return _thread_local.display

def active_window_id()->int:
	return get_thread_display().get_input_focus().focus.id

def _window_from_id(window_id: int)->display.drawable.Window:
	return get_thread_display().create_resource_object('window', window_id)

def window_name(window_id: int)->str:
	w=_window_from_id(window_id)
	name=w.get_wm_name()
	while not name:
		w=w.query_tree().parent
		if w==0: return ""
		name=w.get_wm_name()
	return name

def window_class(window_id: int)->'tuple[str, ...]':
	w=_window_from_id(window_id)
	name=w.get_wm_name()
	while not name:
		w=w.query_tree().parent
		if w==0: return ()
		name=w.get_wm_name()
	cls=w.get_wm_class()
	if cls is None: return ()
	return cls
