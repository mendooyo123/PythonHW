from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
import shutil
def select_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)

def download_file():
    get_link = link_field.get()
    user_path = path_label.cget("text")
    screen.title('다운로드 중...')
    #Download Video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    #select directory
    shutil.move(mp4_video, user_path)
    screen.title('다운로드가 완료되었습니다! 다른 파일을 다운로드하기...')
screen = Tk()
title = screen.title('Youtube Downloader')
canvas = Canvas(screen, width=500, height=500)
canvas.pack()
#logo
logo_img = PhotoImage(file='yt.png')
logo_img = logo_img.subsample(4, 4)
canvas.create_image(250, 80, image=logo_img)
#link
link_field = Entry(screen, width=40, font=('맑은 고딕', 15) )
link_label = Label(screen, text="다운로드 링크를 입력하십시오: ", font=('맑은 고딕', 15))
#Select folder
path_label = Label(screen, text="경로를 선택", font=('맑은 고딕', 15))
select_btn =  Button(screen, text="다운로드 위치 선택", bg='red', padx='22', pady='5',font=('맑은 고딕', 15), fg='#fff', command=select_path)

canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_btn)
canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 220, window=link_field)
#Download button
download_btn = Button(screen, text="다운로드",bg='green', padx='22', pady='5',font=('맑은 고딕', 15), fg='#fff', command=download_file)
canvas.create_window(250, 390, window=download_btn)

screen.mainloop()