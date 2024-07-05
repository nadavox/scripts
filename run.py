from utils import convert_video_to_audio, parser_json

courses = {}

def parse_args():
    # import argparse
    # parser = argparse.ArgumentParser(description="Convert an OGG audio file into words.")
    # parser.add_argument('-f', '--input_file', type=str, help='Path where the OGG audio files are saved')
    # parser.add_argument('-n', '--num_files', type=int, default=1, help='Number of files to process')
    # parser.add_argument('-o', '--output_file', type=str, help='Paths to save the conclution of the audio file')
    # return parser.parse_args()
    import argparse
    parser = argparse.ArgumentParser(description="Convert an OGG audio file into words.")
    parser.add_argument('-f', '--input_file', type=str, help='Path to the JSON file')
    parser.add_argument('-o', '--output_file', type=str, help='Path to save the conclution of the audio files')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    input_json = args.input_file
    output_path = args.output_file

    courses = parser_json(input_json)

    convert_video_to_audio(courses)