from typing import List

def definitions(search_result: dict) -> List:
    definitions_ = []
    for result in search_result["results"]:
        for lexical_entry in result["lexicalEntries"]:
            for entry in lexical_entry["entries"]:
                for sense in entry["senses"]:
                    definitions_.extend(sense["definitions"])
    return definitions_

def synonyms(search_result: dict) -> List:
    synonyms_ = []
    for result in search_result["results"]:
        for lexical_entry in result["lexicalEntries"]:
            for entry in lexical_entry["entries"]:
                for sense in entry["senses"]:
                    for synonym in sense["synonyms"]:
                        synonyms_.append(synonym["text"])
    return synonyms_