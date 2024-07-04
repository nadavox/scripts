from pydub import AudioSegment

# Function to convert audio to OGG format
def convert_to_ogg(input_path, output_path):
    # Load the audio file
    audio = AudioSegment.from_file(input_path)
    
    # Export the audio file in OGG format
    audio.export(output_path, format='ogg')