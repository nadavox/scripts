from pathlib import Path
from pydub import AudioSegment
from pydub.silence import detect_silence
import os
import json

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


def split_audio(audio, segment_length_ms = 200000):
    # Get the duration of the audio in milliseconds
    num_segments = len(audio) // segment_length_ms + 1
    parts = []
    # Split the audio into segments
    start_time = 0
    for i in range(num_segments):
        end_time = (i + 1) * segment_length_ms
        actual_end_time = find_nearest_silence(audio, end_time)
        segment = audio[start_time:actual_end_time]
        start_time = actual_end_time
        parts.append(segment)

    return parts


def convert_video_to_audio(courses):
    for course, in_path in courses.items():
        for file_path in Path(in_path).iterdir():
            if file_path.is_file() and file_path.suffix.lower() in ['.mp4', '.mp3', '.ogg', '.flac', '.m4a', '.aac', '.wav']:
                audio = AudioSegment.from_file(str(file_path))
            else: continue # when the file is not lecture
            
            parts = split_audio(audio)
            # Export the parts
            for i, part in enumerate(parts):
                out_cur_file = f'{in_path}\{file_path.stem}_{i+1}.wav'
                part.export(out_cur_file, format="wav")
                print(f"Part {i+1} saved as {out_cur_file} (duration: {len(part)/1000:.2f} seconds)")


def parser_json(json_file):
    with open(json_file, 'r') as f:
        parsed_data = json.load(f)
    courses_dict = {course_name: path for course_name, path in parsed_data["courses"].items()}
    return courses_dict
