
import boto3
import uuid

polly = boto3.client("polly")

def generate_tts(summary_id):
    summaries = ["Summary for Chapter 1", "Summary for Chapter 2"]
    tts_files = []

    for i, text in enumerate(summaries):
        response = polly.synthesize_speech(
            Text=text,
            OutputFormat="mp3",
            VoiceId="Joanna"
        )
        filename = f"chapter_{i+1}.mp3"
        with open(filename, "wb") as f:
            f.write(response['AudioStream'].read())
        tts_files.append(filename)

    return {"tts_files": tts_files, "id": str(uuid.uuid4())}
