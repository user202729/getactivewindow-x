from dataclasses import dataclass
import subprocess
import ast
from typing import Union

def _active_window_id()->int:
	return int(subprocess.run(
			["xdotool", "getwindowfocus"],
			stdout=subprocess.PIPE,
			check=True).stdout)

def active_window_name()->str:
	return subprocess.run(
			["xdotool", "getwindowfocus", "getwindowname"],
			stdout=subprocess.PIPE,
			check=True).stdout.decode('u8')

def active_window_class()->tuple[str, ...]:
	result: str=subprocess.run(
			["xprop", "-id", str(_active_window_id()), "WM_CLASS"],
			stdout=subprocess.PIPE,
			check=True).stdout.decode('u8')
	result=result.removeprefix("WM_CLASS(STRING) = ")
	result_1: Union[str, tuple[str, ...]]=ast.literal_eval(result)
	if isinstance(result_1, str):
		return result_1,
	else:
		return result_1
