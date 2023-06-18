from dataclasses import dataclass
import subprocess
import ast
from typing import Union
import threading

from Xlib import X, display  # type: ignore
from ewmh import EWMH  # type: ignore

class MyLocal(threading.local):
	def __init__(self)->None:
		self.display = display.Display()
		self.ewmh = EWMH(self.display)

_thread=MyLocal()

def active_window_id()->int:
	focus=_thread.display.get_input_focus().focus
	if focus==0: return 0  # oops
	return focus.id

def _window_from_id(window_id: int)->display.drawable.Window:
	return _thread.display.create_resource_object('window', window_id)

def window_name(window_id: int)->str:
	if window_id==0: return ""
	w=_window_from_id(window_id)
	name=_thread.ewmh.getWmName(w)
	while not name:
		w=w.query_tree().parent
		if w==0: return ""
		name=_thread.ewmh.getWmName(w)
	try: return name.decode("UTF-8")
	except: return name.decode("latin1")

def window_class(window_id: int)->'tuple[str, ...]':
	if window_id==0: return ()
	w=_window_from_id(window_id)
	name=_thread.ewmh.getWmName(w)
	while not name:
		w=w.query_tree().parent
		if w==0: return ()
		name=_thread.ewmh.getWmName(w)
	cls=w.get_wm_class()
	if cls is None: return ()
	return cls
