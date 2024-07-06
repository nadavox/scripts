from pathlib import Path
from moviepy.editor import AudioFileClip
from click import secho

def convert_to_wav(input_file, output_dir=None):
    # Convert input file to Path object
    input_path = Path(input_file)
    
    # Get the base name of the input file (without extension)
    base_name = input_path.stem
    
    # Set output directory to current directory if not specified
    output_dir = Path(output_dir) if output_dir else Path.cwd()
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Set the output file path
    output_file = output_dir / f"{base_name}.wav"
    
    try:
        # Load the audio from the input file
        audio = AudioFileClip(str(input_path))
        
        # Write the audio to a WAV file
        audio.write_audiofile(str(output_file), codec='pcm_s16le')
        
        print(f"Conversion successful. Output file: {output_file}")
        return audio, output_file
    except Exception as e:
        secho(f"An error occurred during conversion: {str(e)}", fg='red')
        exit(1)

# Example usage
if __name__ == "__main__":
    input_file = input("Enter the path to the input video/audio file: ").strip()
    output_dir = input("Enter the output directory (leave blank for current directory): ").strip() or None
    
    audio, output_file = convert_to_wav(input_file, output_dir)
    if audio:
        print(f"Duration: {audio.duration:.2f} seconds")
        print(f"Output file: {output_file}")
        # close the audio
        audio.close()
    