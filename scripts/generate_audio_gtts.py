from gtts import gTTS
import os

BASE = os.path.dirname(os.path.dirname(__file__))
IN_DIR = os.path.join(BASE, "interview", "lines")
OUT_DIR = os.path.join(BASE, "results")
os.makedirs(OUT_DIR, exist_ok=True)

def synthesize(file_name, lang="en", slow=False):
    path = os.path.join(IN_DIR, file_name)
    with open(path, "r", encoding="utf-8") as f:
        text = f.read().strip()
    tts = gTTS(text=text, lang=lang, slow=slow)
    out_path = os.path.join(OUT_DIR, file_name.replace(".txt", ".mp3"))
    tts.save(out_path)
    print(f"Saved: {out_path}")

if __name__ == "__main__":
    synthesize("interviewer_lines.txt")
    synthesize("guest_lines.txt")
    print("Done.")
