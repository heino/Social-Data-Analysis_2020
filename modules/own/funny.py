from enum import Enum

class Method(Enum):
    DISPLAY = 1
    SAVE_TO_PUBLIC = 2
    SAVE_FOR_LATER = 3

saved = {}

#method = Method.DISPLAY
method = Method.SAVE_TO_PUBLIC
#method = Method.SAVE_FOR_LATER

def set_display():
    global method
    method = Method.DISPLAY

def set_save_to_public():
    global method
    method = Method.SAVE_TO_PUBLIC

def set_save_for_later():
    global method
    method = Method.SAVE_FOR_LATER

def is_display():
    return method == Method.DISPLAY

def is_save_to_public():
    return method == Method.SAVE_TO_PUBLIC

def is_save_for_later():
    return method == Method.SAVE_FOR_LATER

def save_for_later(name, data):
    saved[name] = data

def get_saved():
    return saved[name]

def get_saved(name):
    return saved[name]
