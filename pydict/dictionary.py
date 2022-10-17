"""
A simple english dictionary for python.

Author Noah Everett
Created: October 16, 2022
"""

__all__ = ["search"]


from typing import List
from threading import Thread

from . import parse
from .core import fetch


class Search:
    word: str

    def __init__(self, word: str) -> None:
        self.word = word
        self._search_thread = _SearchThread(word)

    def __repr__(self) -> str:
        return f"{self.__class__.__qualname__}({self.word})"
    
    def __str__(self) -> str:
        return self.word

    @property
    def synonyms(self) -> List:
        search_result = self._search_thread.results()
        return parse.synonyms(search_result) if search_result else []

    @property
    def definitions(self) -> List:
        search_result = self._search_thread.results()
        return parse.definitions(search_result) if search_result else []


class _SearchThread(Thread):
    LANGUAGE_CODE: str = "en"
    ENDPOINT: str = "entries"
    
    def __init__(self, word: str):
        super().__init__()
        self.word = word
        self.start()

    def results(self):
        if not self.is_alive():
            self.join()
        return self._results

    def run(self):
        self._results = fetch(self.ENDPOINT, self.LANGUAGE_CODE, self.word)


def search(word: str) -> Search:
    return Search(word)
