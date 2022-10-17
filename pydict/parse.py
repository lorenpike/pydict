from collections import defaultdict
from typing import Any, List, Union

def definitions(search_result: dict) -> List:
    definitions_ = []
    for result in _make_defaultdict(search_result["results"]):
        for lexical_entry in result["lexicalEntries"]:
            for entry in lexical_entry["entries"]:
                for sense in entry["senses"]:
                    definitions_.extend(sense["definitions"])
    return definitions_

def synonyms(search_result: dict) -> List:
    synonyms_ = []
    for result in _make_defaultdict(search_result["results"]):
        for lexical_entry in result["lexicalEntries"]:
            for entry in lexical_entry["entries"]:
                for sense in entry["senses"]:
                    for synonym in sense["synonyms"]:
                        synonyms_.append(synonym["text"])
    return synonyms_


def _make_defaultdict(obj: Union[dict, list, Any] ):
    if isinstance(obj, dict):
        return defaultdict(list, **{k: _make_defaultdict(v) for k, v in obj.items()})
    elif isinstance(obj, list):
        return [_make_defaultdict(v) for v in obj]
    else:
        return obj
    