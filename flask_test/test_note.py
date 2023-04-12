from note import create_note, some_process

from flask import Flask
import pytest
import pytest_mock

app = Flask('test')


def test_some_process():
    d = {'t': 0}
    assert d == some_process(d)


def test_create_note_query_invalid():
    # flask test
    # https://flask.palletsprojects.com/en/2.2.x/api/#flask.Flask.test_request_context
    with app.test_request_context(
        path='/note?q=quick',
        method='POST',
        json={}
    ):
        res = create_note()
        assert res == -1


def test_create_note_json_invalid():

    with app.test_request_context(
        path='/note',
        method='POST',
        json={}
    ):
        res = create_note()
        assert res == -2


def test_create_note_ok(mocker):

    d = {'a': 1, 'b': 2}

    with app.test_request_context(
        path='/note',
        method='POST',
        json=d
    ):
        mocker.patch('note.some_process', return_value=d)
        res = create_note()
        assert res == d
