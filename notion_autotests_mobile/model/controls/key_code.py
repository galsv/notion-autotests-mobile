from enum import Enum
from selene import browser


class Alphabet(Enum):
    A = 29
    B = 30
    C = 31
    D = 32
    E = 33
    F = 34
    G = 35
    H = 36
    I = 37
    J = 38
    K = 39
    L = 40
    M = 41
    N = 42
    O = 43
    P = 44
    Q = 45
    R = 46
    S = 47
    T = 48
    U = 49
    V = 50
    W = 51
    X = 52
    Y = 53
    Z = 54


def code_from_alpha(alpha: str):
    code = Alphabet[alpha.upper()].value
    upper = 1 if alpha.isupper() else 0
    return code, upper


def fill_text_by_keycode(text: str):
    """Text only from number and alphabet"""
    for symbol in text:
        if symbol.isnumeric():
            browser.driver.press_keycode(int(symbol) + 7)
        if symbol.isalpha():
            code, upper = code_from_alpha(symbol)
            browser.driver.press_keycode(code, upper)
        if symbol.isspace():
            browser.driver.press_keycode(62)


def press_enter():
    browser.driver.press_keycode(66)
