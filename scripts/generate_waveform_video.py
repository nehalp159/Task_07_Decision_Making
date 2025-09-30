import os, sys, numpy as np
from PIL import Image, ImageDraw
from moviepy.editor import AudioFileClip, ImageClip, CompositeVideoClip

BASE = os.path.dirname(os.path.dirname(__file__))
RESULTS = os.path.join(BASE, "results")
os.makedirs(RESULTS, exist_ok=True)

# optional CLI arg for audio path; otherwise fall back to known files
if len(sys.argv) > 1:
    audio_path = sys.argv[1]
else:
    cand = [
        os.path.join(RESULTS, "dialogue_aac.m4a"),
        os.path.join(RESULTS, "interviewer_lines.mp3"),
        os.path.join(RESULTS, "guest_lines.mp3"),
    ]
    audio_path = next((p for p in cand if os.path.exists(p)), None)

if not audio_path or not os.path.exists(audio_path):
    raise SystemExit("No audio found. Provide a path or run generate_audio_gtts.py first.")

clip = AudioFileClip(audio_path)
duration = clip.duration
if not duration or duration <= 0:
    raise SystemExit("Audio duration is zero or unknown.")

W, H = 1280, 720
amps = np.empty(W, dtype=np.float32)
for x in range(W):
    t = (x / max(1, W - 1)) * duration
    frame = clip.get_frame(t)     # [-1..1]
    amps[x] = float(np.mean(frame))

mx = float(np.max(np.abs(amps))) or 1.0
amps /= mx

img = Image.new("RGB", (W, H), color=(255, 255, 255))
draw = ImageDraw.Draw(img)
mid, scale = H // 2, int(H * 0.35)
for x, v in enumerate(amps):
    y = mid - int(v * scale)
    draw.line([(x, mid), (x, y)], fill=(0, 0, 0))

bg = ImageClip(np.array(img)).set_duration(duration)
final = CompositeVideoClip([bg]).set_audio(clip)

out = os.path.join(RESULTS, "audiogram.mp4")
final.write_videofile(
    out,
    fps=24,
    codec="libx264",
    audio_codec="aac",
    audio_bitrate="192k",
    temp_audiofile=os.path.join(RESULTS, "temp-audio.m4a"),
    remove_temp=True,
)
print(f"Saved: {out}")
