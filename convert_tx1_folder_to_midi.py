import os
from data.tx1_midi import tx1_to_midi

if __name__ == '__main__':
    import sys
    input_directory = sys.argv[1]
    output_directory = sys.argv[2]

    # Ensure the output directory exists
    os.makedirs(output_directory, exist_ok=True)

    # Iterate through all .txt files in the input directory
    for filename_in in os.listdir(input_directory):
        if filename_in.endswith(".txt"):
            # Construct the full input and output file paths
            input_file_path = os.path.join(input_directory, filename_in)
            base_name = os.path.splitext(filename_in)[0]
            output_file_path = os.path.join(output_directory, f"{base_name}.mid")

            # Read the .txt file
            with open(input_file_path, 'r') as f:
                tx1 = f.read()

            # Convert to MIDI
            midi = tx1_to_midi(tx1)

            # Write the MIDI file
            with open(output_file_path, 'wb') as f:
                f.write(midi)

