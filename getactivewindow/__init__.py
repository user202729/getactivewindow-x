from dataclasses import dataclass
import subprocess
import ast
from typing import Union

from xdo import Xdo, XdoException
x = Xdo()

def active_window_id()->int:
	return x.get_focused_window()

def window_name(window_id: int)->str:
	return x.get_window_name(window_id).decode('u8')

def window_class(window_id: int)->tuple[str, ...]:
	try:
		result=bytes(x.get_window_property(window_id, b"WM_CLASS")).split(b"\0")
	except XdoException:
		return ()
	assert not result[-1]
	return tuple(x.decode('u8') for x in result[:-1])
