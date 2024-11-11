import cv2
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import threading

class VideoPlayer:
    def __init__(self, window, window_title, video_source):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source

        # Open a video file or capture device or a URL or a camera
        self.vid = cv2.VideoCapture(video_source)
        self.length = int(self.vid.get(cv2.CAP_PROP_FRAME_COUNT))

        self.canvas = tk.Label(window)
        self.canvas.pack()

        # Button to play/pause the video
        self.btn_play_pause = ttk.Button(window, text="Pause", command=self.toggle_play_pause)
        self.btn_play_pause.pack(side='left')

        # Button to stop the video
        self.btn_stop = ttk.Button(window, text="Stop", command=self.stop)
        self.btn_stop.pack(side='left')

        # Button to rewind the video
        self.btn_rewind = ttk.Button(window, text="Rewind", command=self.rewind)
        self.btn_rewind.pack(side='left')

        # Button to fast forward the video
        self.btn_fast_forward = ttk.Button(window, text="Fast Forward", command=self.fast_forward)
        self.btn_fast_forward.pack(side='left')

        # Progress bar
        self.progress = ttk.Progressbar(window, length=500, mode='determinate')
        self.progress.pack(side='bottom', fill='x')
        self.progress.bind("<Button-1>", self.seek)

        self.delay = 15  # ms
        self.running = True
        self.playing = True
        self.update()

        self.window.mainloop()

    def update(self):
        if self.running:
            ret, frame = self.vid.read()
            if ret:
                self.progress['value'] = int(self.vid.get(cv2.CAP_PROP_POS_FRAMES) / self.length * 100)
                self.window.update_idletasks()
                self.window.update()
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = Image.fromarray(frame)
                frame = ImageTk.PhotoImage(frame)
                self.canvas.configure(image=frame)
                self.canvas.image = frame
                if self.playing:
                    self.window.after(self.delay, self.update)
            else:
                self.stop()

    def toggle_play_pause(self):
        self.playing = not self.playing
        if self.playing:
            self.btn_play_pause.config(text="Pause")
            self.update()
        else:
            self.btn_play_pause.config(text="Play")

    def stop(self):
        self.running = False
        self.vid.set(cv2.CAP_PROP_POS_FRAMES, 0)
        self.vid.release()

    def rewind(self):
        current_frame = self.vid.get(cv2.CAP_PROP_POS_FRAMES)
        self.vid.set(cv2.CAP_PROP_POS_FRAMES, current_frame - 10)

    def fast_forward(self):
        current_frame = self.vid.get(cv2.CAP_PROP_POS_FRAMES)
        self.vid.set(cv2.CAP_PROP_POS_FRAMES, current_frame + 10)

    def seek(self, event):
        # Calculate seek position
        seek_pos = (event.x / self.progress.winfo_width()) * 100
        self.vid.set(cv2.CAP_PROP_POS_FRAMES, (seek_pos / 100) * self.length)
        if not self.playing:
            self.update()

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

# Create a window and pass it to the VideoPlayer class
root = tk.Tk()
VideoPlayer(root, "Tkinter and OpenCV", "E:\BaiduNetdiskDownload\测试视频14种\jellyfish-25-mbps-hd-hevc.mp4")
