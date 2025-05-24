import os 
import openai 
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip 
from gtts import gTTS 
import tempfile 
# Set your OpenAI API Key 
openai.api_key = "YOUR_OPENAI_API_KEY" 
def transcribe_audio(audio_path): 
    """Transcribe audio using Whisper via OpenAI API""" 
 
    with open(audio_path, "rb") as f: 
        transcript = openai.Audio.transcribe("whisper-1", f) 
    return transcript["text"] 
 
def generate_tts_audio(text, lang='en', output_path="dubbed_audio.mp3"): 
    """Generate TTS audio using gTTS""" 
    tts = gTTS(text=text, lang=lang) 
    tts.save(output_path) 
    return output_path 
def create_subtitled_video(video_path, transcript_text, 
output_path="output_with_subs.mp4"): 
    """Add subtitles to the video""" 
    video = VideoFileClip(video_path) 
    subtitle = TextClip(transcript_text, fontsize=24, color='white', bg_color='black', size=video.size) 
    subtitle = subtitle.set_duration(video.duration).set_position(("center", "bottom")) 
 
    final = CompositeVideoClip([video, subtitle]) 
    final.write_videofile(output_path, codec='libx264', audio_codec='aac') 
    return output_path 
def extract_audio_from_video(video_path, audio_path="temp_audio.wav"): 
    """Extract audio from video file using ffmpeg""" 
    os.system(f"ffmpeg -y -i \"{video_path}\" -q:a 0 -map a \"{audio_path}\"") 
    return audio_path 
def replace_audio_in_video(video_path, new_audio_path, output_path="dubbed_video.mp4"): 
    """Replace the audio in video with new dubbed audio""" 
    os.system(f"ffmpeg -y -i \"{video_path}\" -i \"{new_audio_path}\" -c:v copy -map 0:v:0 -map 1:a:0 -shortest \"{output_path}\"") 
    return output_path 
 
# Main pipeline 
def ai_dub_and_subtitle(video_path, lang='en'): 
    with tempfile.TemporaryDirectory() as tmp: 
        audio_path = os.path.join(tmp, "audio.wav") 
        extract_audio_from_video(video_path, audio_path) 
        transcript = transcribe_audio(audio_path) 
        print(f"Transcript: {transcript}") 
        # Optional: Translate transcript (e.g., using openai.ChatCompletion or DeepL API) 
        subtitled_video = create_subtitled_video(video_path, transcript, os.path.join(tmp, "with_subs.mp4")) 
        # Generate new audio 
        tts_audio = generate_tts_audio(transcript, lang=lang, output_path=os.path.join(tmp, "dubbed.mp3")) 
        # Replace audio with dubbed 
        final_video = replace_audio_in_video(subtitled_video, tts_audio, output_path="final_dubbed_video.mp4") 
        print(f"Final dubbed and subtitled video saved to: {final_video}") 
# Example usage 
ai_dub_and_subtitle("example_video.mp4", lang='en') 