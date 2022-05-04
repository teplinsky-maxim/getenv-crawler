import glob
import re
from pathlib import Path

from core.env import Env


def get_files_to_crawl(initial_directory: str) -> list[str]:
    files = glob.glob(initial_directory + '/**/*.py', recursive=True)
    files = [file for file in files if not file.startswith(f'{initial_directory}/venv')]
    return files


def crawl(path_to_file: str) -> list[Env]:
    result = []
    lines = open(path_to_file, 'r').readlines()
    for idx, line in enumerate(lines):
        r = re.search(r'os\.getenv\(.*\)', line)
        if r:
            result.append(Env(
                filename=path_to_file,
                line_no=idx,
                string=line.strip()
            ))
    return result
