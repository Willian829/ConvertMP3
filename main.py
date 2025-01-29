import pafy
import os
import glob

pc_username = os.getenv('username')
# print(pc_username)
DOWNLOAD_PATH = f'C:/Users/{pc_username}/Music'

url = input('Enter the URL of the video: ')
video = pafy.new(url)
# audiostreams = video.audiostreams
# for audio in audiostreams:
#    print(audio)
bestaudio = video.getbestaudio(preftype = "webm")
bestaudio.download(filepath = DOWNLOAD_PATH)

filename = glob.glob(f'C:/Users/{pc_username}/Music/*.webm')
# print(filename)
audio_webm = filename[0]
# print(audio_webm)

audio_title = ""
audio_title = audio_webm.replace(".webm", "")
# print(audio_title)

command = f'ffmpeg -i "{audio_webm}" -vn -ab 128k -ar 44100 -y "{audio_title}.mp3"'
os.system(command)

if os.path.exists(audio_webm):
    os.remove(audio_webm)
else:
    print("file does not exist")

print("file downloaded and converted successfully")
print(f"Output folder: C:/Users/{pc_username}/Music")