# Attempts Log — Task 06 (AI “Street Interview”)
_Date: Aug 30, 2025 · Platform: macOS (Apple Silicon) · Python 3.13 (venv)_

## Attempt 1 — Project bootstrap
**Goal:** Create folders, venv, and dependencies.  
**Steps:**
- `mkdir -p scripts interview/lines results assets`
- `python3 -m venv .venv && source .venv/bin/activate`
- `pip install -r requirements.txt` (gTTS, moviepy, numpy, Pillow, imageio-ffmpeg)
**Outcome:** Environment ready.  
**Notes:** Avoided pydub/audioop due to Python 3.13 removal of `audioop`.

---

## Attempt 2 — Text-to-Speech (TTS) audio
**Goal:** Generate MP3s for interviewer and guest.  
**Steps:**
- Wrote interview text files to `interview/lines/`.
- Ran `python scripts/generate_audio_gtts.py`.  
**Outcome:** `results/interviewer_lines.mp3`, `results/guest_lines.mp3`.  
**Issue:** Initially only the first line seemed audible in quick tests.  
**Fix:** Updated script to join non-empty lines into one paragraph; confirmed full playback with `afplay` and `afinfo`.

---

## Attempt 3 — MoviePy ffmpeg resolution (no Homebrew)
**Goal:** Enable video creation.  
**Issue:** `RuntimeError: No ffmpeg exe could be found.`  
**Tried:** `imageio_ffmpeg.get_ffmpeg_exe()` → failed on this setup.  
**Fix (working):**
1. Downloaded static `ffmpeg` (Apple Silicon).
2. Removed quarantine & made executable:
   - `xattr -dr com.apple.quarantine ffmpeg`
   - `chmod +x ffmpeg`
3. Pointed MoviePy to it:
   - `export IMAGEIO_FFMPEG_EXE="$HOME/Desktop/Task_06_Deep_Fake/ffmpeg"`
**Outcome:** ffmpeg available for MoviePy.

---

## Attempt 4 — Waveform video (no pydub)
**Goal:** Build audiogram video without pydub/audioop.  
**Issue:** MoviePy `to_soundarray` + NumPy stacking error on Python 3.13.  
**Fix:** Rewrote waveform sampler to iterate with `clip.get_frame()` across duration; drew waveform via Pillow.  
**Steps:** `python scripts/generate_waveform_video.py`  
**Outcome:** `results/audiogram.mp4`

---

## Attempt 5 — Caption overlay without ImageMagick
**Goal:** Add visible disclosure on video.  
**Issue:** `TextClip` often requires ImageMagick.  
**Fix:** Switched to Pillow banner (RGBA) and composited over video.  
**Steps:**  
`python scripts/overlay_captions.py "This interview was created with AI tools."`  
**Outcome:** `results/audiogram_captioned.mp4`

---

## Attempt 6 — Silent MP4 in QuickTime (MP3-in-MP4)
**Goal:** Ensure audio plays in macOS player.  
**Issue:** QuickTime silent with MP3 audio inside MP4.  
**Quick Fix:** Remux audio track to AAC:  
```
./ffmpeg -y -i results/audiogram.mp4 -c:v copy -c:a aac -b:a 192k results/audiogram_aac.mp4
./ffmpeg -y -i results/audiogram_captioned.mp4 -c:v copy -c:a aac -b:a 192k results/audiogram_captioned_aac.mp4
```
**Permanent Fix:** In both scripts’ `write_videofile(...)`, set:
`codec="libx264", audio_codec="aac", audio_bitrate="192k", temp_audiofile="temp-audio.m4a"`  
**Outcome:** `results/audiogram_captioned_aac.mp4` (audible in QuickTime).

---

## Attempt 7 — Include both voices
**Goal:** Combine interviewer + guest in one track.  
**Steps (optional enhancement):**
```
printf "file 'interviewer_lines.mp3'\nfile 'guest_lines.mp3'\n" > results/concat.txt
./ffmpeg -y -f concat -safe 0 -i results/concat.txt -c:a aac -b:a 192k results/dialogue_aac.m4a
python scripts/generate_waveform_video.py results/dialogue_aac.m4a
python scripts/overlay_captions.py "This interview was created with AI tools."
```
**Outcome:** Continuous Q→A audio in single video (when used).

---

## Final Artifacts
- `results/interviewer_lines.mp3`
- `results/guest_lines.mp3`
- `results/audiogram.mp4`
- `results/audiogram_captioned.mp4`
- `results/audiogram_aac.mp4`
- `results/audiogram_captioned_aac.mp4`  ← **final** (also copied as `AI_Street_Interview_Final.mp4`)

---

## Environment Snapshot
- Python: `python --version` → 3.13.x  
- Packages: `pip freeze` saved to `results/ENV_INFO.txt`  
- ffmpeg: `./ffmpeg -version` (static, Apple Silicon)
