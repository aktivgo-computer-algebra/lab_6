import string

from polynom.config import PolynomialConfig

class PolynomialParser:
    def parse(self, config: PolynomialConfig, polynom: str):
        for i in range(len(polynom)):
            if polynom[i] in ['+', '-']:
                return self.__sign(polynom[i + 1:])
            if polynom[i] in string.digits:
                return self.__num(polynom[i + 1:])
            if polynom[i] == config.variable:
                return self.__variable(polynom[i + 1:])
            return self.__err('non supported symbol')

    def __sign(self, polynom: str):
        for i in range(len(polynom)):
            if polynom[i] not in string.digits:
                return self.__err('non number after sign')
            return self.__num(polynom[i + 1:])

    def __num(self, polynom: str):
        print()

    def __variable(self, polynom: str):
        print()

    def __degree(self, polynom: str):
        print()

    def __err(self, reason: str):
        raise BaseException('error:', reason)