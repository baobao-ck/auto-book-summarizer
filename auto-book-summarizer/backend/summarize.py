
import anthropic

client = anthropic.Anthropic(api_key="your-anthropic-api-key")

def summarize_book(s3_key):
    chapters = ["Chapter 1 text...", "Chapter 2 text..."]
    summaries = []
    for i, chapter in enumerate(chapters):
        response = client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=1024,
            messages=[{"role": "user", "content": f"Summarize this: {chapter}"}]
        )
        summaries.append({"chapter": i+1, "summary": response.content[0].text})
    return {"summaries": summaries, "id": "summary-xyz"}
