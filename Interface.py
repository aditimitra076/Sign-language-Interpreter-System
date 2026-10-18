from tkinter import *
from subprocess import Popen
import tkinter as tk

w1=Tk()
w1.geometry("500x500")
w1.title("Main")

def open3():
    sign_interpret_path="/Users/Aditi Mitra/OneDrive/Desktop/signLanguageDetection/test.py"
    Popen(["python",sign_interpret_path])
    
def open():
    speech_recog_path="/Users/Aditi Mitra/OneDrive/Desktop/signLanguageDetection/voiceRecognition.py"
    Popen(["python",speech_recog_path])
    
def open2():
    eye_tracker_path="/Users/Aditi Mitra/OneDrive/Desktop/signLanguageDetection/eyeTracker.py"
    Popen(["python",eye_tracker_path])

btnOpen=Button(w1,text="Sign Language Interpretor",command=open3).pack(pady=10)
btnOpen1=Button(w1,text="Speech Recognition",command=open,).pack(pady=10)
btnOpen2=Button(w1,text="Eye Tracking",command=open2).pack(pady=10)

w1.mainloop()