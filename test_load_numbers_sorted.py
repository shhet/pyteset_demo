import os
from typing import List, Tuple

import pytest

from prime import load_numbers_sorted

"""
function:   テスト関数ごとにフィクスチャを実行（デフォルト）
module:     同一モジュール（ソースコード）内で1回だけフィクスチャを実行
class:      同一クラス内で1回だけフィクスチャを実行
session:    テスト実行時に1回だけフィクスチャを実行
"""
@pytest.fixture(scope='module')
def txt(tmpdir) -> str:
    tmpfile = tmpdir / 'numbers.txt'
    with tmpfile.open('w') as f:
        for n in [2, 5, 4, 3, 1]:
            f.write('{}\n'.format(n))

    yield str(tmpfile)

    tmpfile.remove()


@pytest.fixture
def txt_and_list(txt) -> Tuple[str, List[int]]:
    yield txt, [1, 2, 3, 4, 5]


def test_load_numbers_sorted(txt_and_list):
    assert load_numbers_sorted(txt_and_list[0]) == txt_and_list[1]

