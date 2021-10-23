from dataclasses import dataclass
import subprocess
import ast
from typing import Union

from xdo import Xdo
x = Xdo()

def _active_window_id()->int:
	return x.get_focused_window()

def active_window_name()->str:
	return x.get_window_name(_active_window_id()).decode('u8')

def active_window_class()->tuple[str, ...]:
	result=bytes(x.get_window_property(_active_window_id(), b"WM_CLASS")).split(b"\0")
	assert not result[-1]
	return tuple(x.decode('u8') for x in result[:-1])
