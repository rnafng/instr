import os
from collections import defaultdict
from sf2utils.sf2parse import Sf2File
import random
from instruments import INSTRUMENT_TYPES, categorize

presets = { val : [] for val in INSTRUMENT_TYPES }

def store_sf2_presets(sf2_path):
    # tbh dont need this anymore, refactor/change later
    with open(sf2_path, 'rb') as file:
        sf2 = Sf2File(file)
        sf2_presets = sf2.presets
        for i in range(len(sf2_presets)):
            if hasattr(sf2_presets[i], "bank"): # index number
                gm_number = sf2_presets[i].bank * 128 + sf2_presets[i].preset
                category = categorize(gm_number)
                presets[category].append((sf2_path, i))
       
def get_random_inst(instrument_number):
    category = categorize(instrument_number)
    return presets[category][random.randint(0, len(presets[category])-1)]

def generate_presets():
    current_dir = os.getcwd()
    sf2_directory = os.path.join(current_dir, 'data/SF2')
    for sf2_file in os.listdir(sf2_directory):
        if sf2_file.lower().endswith('.sf2'):
            print(sf2_file)
            sf2_path = os.path.join(sf2_directory, sf2_file)
            store_sf2_presets(sf2_path)
            print([len(presets[key]) for key in presets.keys()])