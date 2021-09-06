import random
import unicodedata
from typing import Callable


def chunkIt(seq: list, num: int):
    # FIXME:
    # https://stackoverflow.com/questions/2130016/splitting-a-list-into-n-parts-of-approximately-equal-length
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out


def flatten_list(container: list) -> list:
    for item in container:
        if isinstance(item, (list, tuple)):
            for j in flatten_list(item):
                yield j
        else:
            yield item


def filter_dict(dictionary: dict, func: Callable) -> dict:
    # https://blog.finxter.com/how-to-filter-a-dictionary-in-python/
    newdict = {}
    for key, value in dictionary.items():
        if func(key, value):
            newdict[key] = value
    return newdict


def filter_list(seg: list, func: Callable) -> list:
    newlist = []
    for item in seg:
        if func(item):
            newlist.append(item)
    return newlist


def sorted_sample_list(seg: list, sample_size: int) -> list:
    return [seg[i] for i in sorted(
        random.sample(range(len(seg)), sample_size))]


def to_string(value):
    try:
        return str(value)
    except Exception:
        raise TypeError('Cannot convert {} to string.'.format(type(value)))


def normalize_text(text: str) -> str:
    parsed_text = to_string(text)
    parsed_text = unicodedata.normalize("NFD", parsed_text)
    parsed_text = parsed_text.encode("ascii", "ignore")
    parsed_text = parsed_text.decode("utf-8")
    return parsed_text.lower().strip()
