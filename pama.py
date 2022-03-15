from pydub import AudioSegment
from os import listdir
from os.path import isfile, join
import os
import datetime
import sys
onlyfiles = [f for f in listdir(sys.argv[1]) if isfile(join(sys.argv[1], f))]
os.chdir(sys.argv[1])
sound1 = AudioSegment.from_ogg(onlyfiles[0])
lengs = []
lengs.append(sound1.duration_seconds)
lengs2 = []
lengs2.append(sound1.duration_seconds)
names = []
names.append(onlyfiles[0])
for i in range(1, len(onlyfiles)):
    print("Processing: " + onlyfiles[i])
    if (onlyfiles[i][-3:-1] == "og"):
        sound1 += AudioSegment.from_ogg(onlyfiles[i])
        lengs.append(AudioSegment.from_ogg(onlyfiles[i]).duration_seconds + sum(lengs2))
        lengs2.append(AudioSegment.from_ogg(onlyfiles[i]).duration_seconds)
    if (onlyfiles[i][-3:-1] == "mp"):
        sound1 += AudioSegment.from_mp3(onlyfiles[i])
        lengs.append(AudioSegment.from_mp3(onlyfiles[i]).duration_seconds + sum(lengs2))
        lengs2.append(AudioSegment.from_mp3(onlyfiles[i]).duration_seconds)
    if (onlyfiles[i][-3:-1] == "wa"):
        sound1 += AudioSegment.from_wav(onlyfiles[i])
        lengs.append(AudioSegment.from_wav(onlyfiles[i]).duration_seconds + sum(lengs2))
        lengs2.append(AudioSegment.from_wav(onlyfiles[i]).duration_seconds)
    names.append(onlyfiles[i])
lengs.insert(0, 0)
lengs.pop(-1)
lengs3 = []
for  i in lengs:
    lengs3.append(str(datetime.timedelta(seconds=i)))
    
df = []
for i in range(len(lengs3)):
    df.append(names[i] + ", " + str(lengs3[i]))
print("Exporting audio lengths csv...")
with open('lengths.csv', 'w') as f:
    for line in df:
        f.write(line)
        f.write('\n')
print("Exporting audio file...")
sound1.export("combined.mp3", format="mp3")
