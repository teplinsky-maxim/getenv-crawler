import argparse

from core.crawler import get_files_to_crawl, crawl
from core.env import Env


def display_result(result: list[Env]):
    for item in result:
        print(f'{item.filename}:{item.line_no}: {item.string}')


def main():
    parser = argparse.ArgumentParser(description='Description of your program')
    parser.add_argument('directory', help='Directory to start', type=str)
    args = vars(parser.parse_args())
    files = get_files_to_crawl(args['directory'])
    result = []
    for file in files:
        result.extend(crawl(file))

    display_result(result)


if __name__ == '__main__':
    main()
