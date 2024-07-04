from pathlib import Path
from pydub import AudioSegment
from pydub.silence import detect_silence
import os

root = os.path.dirname(os.path.abspath(__file__))

def find_nearest_silence(audio, target_position, min_silence_len=500, silence_thresh=-30):
    # Search for silence around the target position
    start = max(0, target_position - 5000)  # Look 5 seconds before
    end = min(len(audio), target_position + 5000)  # Look 5 seconds after
    
    # Detect silent chunks
    silent_ranges = detect_silence(audio[start:end], 
                                   min_silence_len=min_silence_len, 
                                   silence_thresh=silence_thresh)

    if not silent_ranges:
        return target_position
    
    # Find the nearest silence
    nearest_silence = min(silent_ranges, key=lambda x: abs((x[0] + x[1])/2 - (target_position - start)))
    return start + (nearest_silence[0] + nearest_silence[1]) // 2
 
def cut_ogg_in_thirds(input_file, output_files):
    # Load the OGG file
    audio = AudioSegment.from_ogg(input_file)

    # Get the duration of the audio in milliseconds
    duration = len(audio)

    # Calculate the ideal cut points
    first_cut = duration // 3
    second_cut = 2 * duration // 3

    # Find the nearest silence for each cut point
    actual_first_cut = find_nearest_silence(audio, first_cut)
    actual_second_cut = find_nearest_silence(audio, second_cut)

    # Ensure the cuts are different
    if abs(actual_first_cut - actual_second_cut) < 1000:  # If cuts are within 1 second
        actual_second_cut = second_cut  # Revert to original cut point

    # Cut the audio into thirds
    first_part = audio[:actual_first_cut]
    second_part = audio[actual_first_cut:actual_second_cut]
    third_part = audio[actual_second_cut:]

    temp_dir = "/Users/nadavox/Desktop/test_for_grock_audio_to_text/"

    # Export the parts
    for i, part in enumerate([first_part, second_part, third_part]):
        path = f'{temp_dir}_{i+1}.ogg'
        part.export(path, format="ogg")
        print(f"Part {i+1} saved as {path} (duration: {len(part)/1000:.2f} seconds)")

    print(f"Audio file cut into thirds.")

def parse_args():
    import argparse
    parser = argparse.ArgumentParser(description="Convert an OGG audio file into words.")
    parser.add_argument("input_file", help="Path to the input OGG audio file.")
    parser.add_argument("output_file", help="Paths to save the conclution of the audio file.")
    return parser.parse_args()

if __name__ == "__main__":
    from convert_to_mp4 import convert_to_ogg
    # Example usage
    input_file = "/Users/nadavox/Desktop/test_for_grock_audio_to_text/safe_programing_L1.ogg"
    output_files = [
        "/Users/nadavox/Desktop/test_for_grock_audio_to_text/safe_programing_L1_part1.ogg",
        "/Users/nadavox/Desktop/test_for_grock_audio_to_text/safe_programing_L1_part2.ogg",
        "/Users/nadavox/Desktop/test_for_grock_audio_to_text/safe_programing_L1_part3.ogg"
    ]

    convert_to_ogg(input_file, input_file)

    cut_ogg_in_thirds(input_file, output_files)