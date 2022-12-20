import os
import re
from pytube import YouTube, Playlist

# Create songs folder
print(os.getcwd() + '/songs')
if not os.path.exists(os.getcwd() + '/songs'):
    os.mkdir('songs')

playlist = Playlist(str(input('Enter playlist link (must be unlisted or public!): ')))
# Iterate through playlist
dir = os.getcwd()

if len(os.listdir(os.getcwd() + '/songs')) == 0:
    reverse = False
else:
    reverse = True
print(reverse)
for index, video in sorted(enumerate(playlist.videos), reverse = reverse):
    title = re.sub('[\/:*?\"<>|«»]', '', video.title)
    print(dir + "/songs/" + title + ".mp3")
    if not os.path.exists(dir + "/songs/" + title + ".mp3"):
        print('Currently downloading song #' + str(index + 1) + ':')
        print('Song Name: ' + '\"' + video.title + '\"')
        song = video.streams.filter(only_audio = True).first().download(output_path = './songs')

        # Convert to MP3
        base, ext = os.path.splitext(song)
        new_file = dir + "/songs/" + title + '.mp3'

        os.rename(song, new_file)
        print('Finished downloading "' + video.title + '".')
    else:
        print('The playlist is already at it\'s latest version!')
        break

print('✔️  Successfully downloaded playlist!')
