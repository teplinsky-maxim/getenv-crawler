from dataclasses import dataclass


@dataclass
class Env:
    filename: str
    line_no: int
    string: str
