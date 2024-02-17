from enum import Enum

INSTRUMENT_TYPES = [
    "Piano",
    "Chromatic Percussion",
    "Organ",
    "Guitar",
    "Bass",
    "Strings",
    "Ensemble",
    "Brass",
    "Reed",
    "Pipe",
    "Synth Lead",
    "Synth Pad",
    "Synth Effects",
    "Ethnic",
    "Percussive",
    "Sound Effects"
]

def categorize(instrument_number):
    # Define the mapping of instrument numbers to categories
    categories = {
        range(1, 9): "Piano",
        range(9, 17): "Chromatic Percussion",
        range(17, 25): "Organ",
        range(25, 33): "Guitar",
        range(33, 41): "Bass",
        range(41, 49): "Strings",
        range(49, 57): "Ensemble",
        range(57, 65): "Brass",
        range(65, 73): "Reed",
        range(73, 81): "Pipe",
        range(81, 89): "Synth Lead",
        range(89, 97): "Synth Pad",
        range(97, 105): "Synth Effects",
        range(105, 113): "Ethnic",
        range(113, 121): "Percussive",
        range(121, 129): "Sound Effects"
    }
    for category_range, category_name in categories.items():
        if instrument_number in category_range:
            return category_name
    return "Piano"