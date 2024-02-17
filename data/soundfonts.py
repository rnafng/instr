from collections import defaultdict
import os
from sf2utils.sf2parse import Sf2File

from instruments import INSTRUMENT_TYPES, categorize

current_dir = os.getcwd()
sf2_directory = os.path.join(current_dir, 'data/SF2')

presets = { val : [] for val in INSTRUMENT_TYPES }
def store_sf2_presets(sf2_path):
    with open(sf2_path, 'rb') as file:
        sf2 = Sf2File(file)
        sf2_presets = sf2.presets
        for i in range(len(sf2_presets)):
            if hasattr(sf2_presets[i], "bank"):
                gm_number = sf2_presets[i].bank * 128 + sf2_presets[i].preset  # General MIDI number from bank and preset
                category = categorize(gm_number)
                # when we generate midi, we want the file path and the index
                presets[category].append((sf2_path, i))
       
for sf2_file in os.listdir(sf2_directory):
    if sf2_file.lower().endswith('.sf2'):
        print(sf2_file)
        sf2_path = os.path.join(sf2_directory, sf2_file)
        store_sf2_presets(sf2_path)
        print([len(presets[key]) for key in presets.keys()])



