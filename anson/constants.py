from enum import Enum


class Compression(Enum, str):
    NONE = "NONE"
    DICTIONARY = "DICTIONARY"
    CONSTANT = "CONSTANT"
