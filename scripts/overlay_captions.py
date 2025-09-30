import sys, os, numpy as np
from moviepy.editor import VideoFileClip, CompositeVideoClip, ImageClip
from PIL import Image, ImageDraw, ImageFont

BASE = os.path.dirname(os.path.dirname(__file__))
RESULTS = os.path.join(BASE, "results")
video_path = os.path.join(RESULTS, "audiogram.mp4")

if not os.path.exists(video_path):
    raise SystemExit("Make an audiogram first (results/audiogram.mp4).")

caption = sys.argv[1] if len(sys.argv) > 1 else "This interview was created with AI tools."
clip = VideoFileClip(video_path)
W, H = clip.size

# banner 12% of height, semi-transparent white
banner_h = max(80, int(0.12 * H))
img = Image.new("RGBA", (W, banner_h), (255, 255, 255, 200))
draw = ImageDraw.Draw(img)
try:
    # use a system font if available; fallback to default
    font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Unicode.ttf", size=max(24, int(banner_h*0.35)))
except:
    font = ImageFont.load_default()

# center the text
bbox = draw.textbbox((0, 0), caption, font=font)
tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
draw.text(((W - tw) // 2, (banner_h - th) // 2), caption, fill=(0, 0, 0, 255), font=font)

banner_clip = ImageClip(np.array(img)).set_duration(clip.duration).set_position(("center", "bottom"))
final = CompositeVideoClip([clip, banner_clip])

out = os.path.join(RESULTS, "audiogram_captioned.mp4")
final.write_videofile(out, fps=24)
print(f"Saved: {out}")
