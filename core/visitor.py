import ast
from sys import stderr
from typing import Any

from core.env import Args


class EnvVisitor(ast.NodeVisitor):
    def __init__(self, check_relative: bool, check_types: bool, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._check_relative = check_relative
        self._check_types = check_types

    def _process_getenv_args(self, args: list[ast.Constant]) -> tuple[Any, Any, bool | None]:
        args_are_ok = None
        if 0 <= len(args) < 2:
            ...  # awkward
        name = args[0].value
        if not isinstance(name, str):
            if self._check_types:
                args_are_ok = False
                print(f'Warning! {name} is not a valid string for the 1st getenv argument', file=stderr)
            else:
                args_are_ok = True
        default = args[1].value
        print(f'{name = }, {default = }')
        return name, default, args_are_ok

    def visit_Call(self, node: ast.Call) -> Args | None:
        # TODO: add line number, extract code from string[col_offset:end_col_offset]
        if hasattr(node.func, 'value') and node.func.value.id == 'os' and node.func.attr == 'getenv':
            name, default, arg_are_ok = self._process_getenv_args(node.args)
            return Args(name, default, arg_are_ok)
        elif node.func.id == 'getenv' and self._check_relative:
            name, default, arg_are_ok = self._process_getenv_args(node.args)
            return Args(name, default, arg_are_ok)
