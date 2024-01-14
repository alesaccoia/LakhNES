import os
import glob
import shutil
import multiprocessing
import sys
from tqdm import tqdm
from tx1_midi import midi_to_tx1  # Assuming the tx1_midi module is in the same directory

def convert_midi_to_tx1(midi_file, out_dir):
    with open(midi_file, 'rb') as f:
        midi_content = f.read()

    tx1_content = midi_to_tx1(midi_content)

    # Generate the output file name
    tx1_name = os.path.join(out_dir, os.path.split(midi_file)[1].split('.')[0] + '.tx1.txt')

    with open(tx1_name, 'w') as f:
        f.write(tx1_content)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python main_script.py <input_directory> <output_directory>")
        sys.exit(1)

    input_directory = sys.argv[1]
    output_directory = sys.argv[2]

    midi_fps = glob.glob(os.path.join(input_directory, '*.mid*'))

    if os.path.isdir(output_directory):
        shutil.rmtree(output_directory)
    os.makedirs(output_directory)

    def _task(x):
        convert_midi_to_tx1(x, output_directory)

    with multiprocessing.Pool(8) as p:
        r = list(tqdm(p.imap(_task, midi_fps), total=len(midi_fps)))
