from dataclasses import dataclass
import subprocess
import ast
from typing import Union
import threading

from Xlib import X, display  # type: ignore
from ewmh import EWMH

class MyLocal(threading.local):
	def __init__(self)->None:
		self.display = display.Display()
		self.ewmh = EWMH(self.display)

_thread=MyLocal()

def active_window_id()->int:
	return _thread.display.get_input_focus().focus.id

def _window_from_id(window_id: int)->display.drawable.Window:
	return _thread.display.create_resource_object('window', window_id)

def window_name(window_id: int)->str:
	w=_window_from_id(window_id)
	name=_thread.ewmh.getWmName(w)
	while not name:
		w=w.query_tree().parent
		if w==0: return ""
		name=_thread.ewmh.getWmName(w)
	return name

def window_class(window_id: int)->'tuple[str, ...]':
	w=_window_from_id(window_id)
	name=_thread.ewmh.getWmName(w)
	while not name:
		w=w.query_tree().parent
		if w==0: return ()
		name=_thread.ewmh.getWmName(w)
	cls=w.get_wm_class()
	if cls is None: return ()
	return cls
