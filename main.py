import argparse

from core.crawler import get_files_to_crawl, crawl
from core.env import Env
from core.visitor import EnvVisitor


def display_result(result: list[Env]):
    for item in result:
        print(f'{item.filename}:{item.line_no}: {item.string}')


def main():
    parser = argparse.ArgumentParser(description='Description of your program')
    parser.add_argument('directory', help='Directory to start', type=str)
    parser.add_argument('-r', '--relative', help='Check getenv usage with relative import', type=bool)
    parser.add_argument('-a', '--arguments', help='Check getenv call arguments', type=bool)
    args = vars(parser.parse_args())
    files = get_files_to_crawl(args['directory'])

    result = []
    check_relative = args['relative']
    check_arguments = args['arguments']
    visitor = EnvVisitor(check_relative, check_arguments)
    for file in files:
        result.extend(crawl(file, visitor))

    display_result(result)


if __name__ == '__main__':
    main()
