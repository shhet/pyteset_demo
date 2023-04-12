from flask import request


def some_process(d: dict):
    print('\n[processing ...]')
    return d


def create_note():

    q: str = request.args.get('q')
    print()
    print(f'q: {q}')
    d: dict = request.get_json()
    print(f'd: {d}')

    if request.args and q != 'query':
        return -1

    if not d:
        return -2

    return some_process(d)