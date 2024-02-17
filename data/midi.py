import os
import random
import mido
from mido import MidiFile
from pydub import AudioSegment
from soundfonts import get_random_inst
from midi2audio import FluidSynth
from collections import defaultdict
from mido import MidiFile, MidiTrack
import time
from pathlib import Path

def render_midi(midi_folder, name, sf2, output):
    fs = FluidSynth(sf2[0])
    Path(output+"/"+name).mkdir(parents=True, exist_ok=True)
    for midi in os.listdir(midi_folder):
        if midi.endswith(".mid"):
            fs.midi_to_audio(os.path.join(midi_folder, midi), os.path.join(output, name+"/"+midi)[:-4]+".wav")

def split_midi(midi_path, output_dir):
    # save midi for inidivdual tracks
    mid = None
    try:
        mid = MidiFile(midi_path)
    except:
        return

    # 16 channels max
    channels = {ch: MidiTrack() for ch in range(16)}

    for track in mid.tracks:
        for msg in track:
            if not msg.is_meta and hasattr(msg, 'channel'):
                channels[msg.channel].append(msg)

    for ch, track in channels.items():
        if track:
            new_mid = MidiFile()
            new_mid.tracks.append(track)
            channel_filename = f"{os.path.splitext(os.path.basename(midi_path))[0]}_channel_{ch}.mid"
            channel_path = os.path.join(output_dir, channel_filename)
            new_mid.save(channel_path)


def generate_midi():
    current_dir = os.getcwd()
    midi_dir = os.path.join(current_dir, 'data/MIDI')
    midi_output_dir = os.path.join(current_dir, 'data/MIDI_OUTPUT')

    for midi_file in os.listdir(midi_dir):
        output = os.path.join(midi_output_dir, midi_file[:midi_file.find(".")])
        Path(output).mkdir(parents=True, exist_ok=True)
        split_midi(os.path.join(midi_dir, midi_file), output)

def generate_wav():
    current_dir = os.getcwd()
    output_dir = os.path.join(current_dir, 'data/AUDIO_OUTPUT')
    midi_output_dir = os.path.join(current_dir, 'data/MIDI_OUTPUT')
    processes = []
    for midi_folder in os.listdir(midi_output_dir):
        if Path(os.path.join(midi_output_dir, midi_folder)).is_dir():
            render_midi(os.path.join(midi_output_dir, midi_folder),midi_folder, get_random_inst(1), output_dir)
