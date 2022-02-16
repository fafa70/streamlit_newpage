import streamlit as st
import os
import keyboard
import threading
import time

'''author: seidfarbod seidali
unfortuantly streamlit do not support the feature that when you click a button, a new page opens. i wrote a code that does it in the simplest way'''

#wait time to close page and open a new one.
wait_second = 3.8

#thread for closing page
def threadFunc():
   time.sleep(wait_second)
   keyboard.press_and_release('ctrl+w')
   

if st.button('test'):
    th = threading.Thread(target=threadFunc)
    th.start()
    #address of streamlit page that you want to open after clicking button
    os.system('D:')
    os.system('cd python\Scripts')
    os.system(r"streamlit run D:\ui\login.py")
    th.join()
    