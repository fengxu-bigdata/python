from moviepy.editor import AudioFileClip

vide_path = input("请输入视频文件的路径：")
mp3_path = input("请输入音频文件保存路径：")
audio = AudioFileClip(vide_path)
audio.write_audiofile(mp3_path)
