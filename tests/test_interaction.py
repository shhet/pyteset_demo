import pytest
import pytest_mock
from interaction import Main


def test_main(mocker):
    # テスト対象のモジュールから見たときの名前空間を記載する
    # https://gist.github.com/aodag/08d63828bb582fdb7599014d637cb863
    mocker.patch('interaction.A.func_a')
    mocker.patch('interaction.B.func_b', return_value=11)
    # mocker.patch('module_a.A.func_a')
    # mocker.patch('module_b.B.func_b', return_value=1)
    
    res = Main().main()
    assert res == 100

def test_main2(mocker):
    # テスト対象のモジュールから見たときの名前空間を記載する
    # https://gist.github.com/aodag/08d63828bb582fdb7599014d637cb863
    # mocker.patch('interaction.A.func_a')
    # mocker.patch('interaction.B.func_b', return_value=11)
    mocker.patch('module_a.A.func_a')
    mocker.patch('module_b.B.func_b', return_value=-1)
    
    res = Main().main()
    assert res == -100
