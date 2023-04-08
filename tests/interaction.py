from module_a import A
from module_b import B


class Main:
    def __init__(self) -> None:
        pass

    def main(self):

        a = A().func_a()
        b = B(a).func_b()

        res = b
        if b > 10:
            res = 100
        if b < 0:
            res = -100

        return res