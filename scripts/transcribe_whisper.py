import os
import sys

try:
    import whisper
except Exception as e:
    print('ERROR: whisper not installed:', e)
    sys.exit(2)

VIDEO_PATH = os.path.join('videos', 'entrevista.mp4')
OUT_PATH = os.path.join('videos', 'entrevista.vtt')

if not os.path.exists(VIDEO_PATH):
    print('ERROR: video not found at', VIDEO_PATH)
    sys.exit(3)

print('Loading model (small). This may take a while...')
model = whisper.load_model('small')
print('Transcribing...')
result = model.transcribe(VIDEO_PATH, language='pt')

def fmt(t):
    h = int(t // 3600)
    m = int((t % 3600) // 60)
    s = int(t % 60)
    ms = int((t - int(t)) * 1000)
    return f"{h:02d}:{m:02d}:{s:02d}.{ms:03d}"

vtt = 'WEBVTT\n\n'
for seg in result.get('segments', []):
    start = fmt(seg['start'])
    end = fmt(seg['end'])
    text = seg.get('text', '').strip()
    vtt += f"{start} --> {end}\n{text}\n\n"

os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
with open(OUT_PATH, 'w', encoding='utf-8') as f:
    f.write(vtt)

print('Wrote VTT to', OUT_PATH)
