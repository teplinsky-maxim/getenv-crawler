import ast
import glob

from core.env import Env
from core.visitor import EnvVisitor


def get_files_to_crawl(initial_directory: str) -> list[str]:
    files = glob.glob(initial_directory + '/**/*.py', recursive=True)
    files = [file for file in files if not file.startswith(f'{initial_directory}/venv')]
    return files


def crawl(path_to_file: str, visitor: EnvVisitor) -> list[Env]:
    result = []
    content = open(path_to_file, 'r').read()
    node = ast.parse(content)
    args = visitor.visit(node)
    if args is not None:
        ...
        # env = Env(
        #     filename=path_to_file
        # )

    # for idx, line in enumerate(lines):
    #     r = re.search(r'os\.getenv\(.*\)', line)
    #     if r:
    #         result.append(Env(
    #             filename=path_to_file,
    #             line_no=idx,
    #             string=line.strip()
    #         ))
    return result
