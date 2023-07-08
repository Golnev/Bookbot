import os
import re

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    end_symbol = ['.', ',', '!', ':', ';', '?']
    end = start+size
    while text[end:][:1] in end_symbol:
        end -= 1
    text = text[start:end]
    text = text[: max(map(text.rfind, end_symbol))+1]
    return text, len(text)


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(path, 'r', encoding='utf-8') as file:
        txt = file.read()
        txt = re.sub(r"\s", " ", txt)

    start = 0
    pre_res = _get_part_text(txt, start, PAGE_SIZE)
    res_lst = [pre_res[0]]
    amount_symbols = pre_res[1]
    while PAGE_SIZE < len(txt) - amount_symbols:
        pre_res_loop = _get_part_text(txt, amount_symbols, PAGE_SIZE)
        res_lst.append(pre_res_loop[0])
        amount_symbols += pre_res_loop[1]

    res_lst.append(txt[amount_symbols::])

    num = 1
    for book_list in res_lst:
        book[num] = book_list.lstrip()
        num += 1


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(os.getcwd(), BOOK_PATH))
