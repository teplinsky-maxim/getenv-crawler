from dataclasses import dataclass
from typing import Any


@dataclass
class Args:
    name: Any
    default: Any
    types_are_ok: None | bool


@dataclass
class Env:
    filename: str
    line_no: int
    string: str
    args: Args
