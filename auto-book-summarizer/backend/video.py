
import os

def generate_video(tts_id):
    for mp3 in os.listdir():
        if mp3.endswith(".mp3"):
            output = mp3.replace(".mp3", ".mp4")
            os.system(f"ffmpeg -loop 1 -i static.jpg -i {mp3} -c:v libx264 -c:a aac -shortest -y {output}")
    return {"status": "video_created"}
