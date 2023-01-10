import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "/Users/anugu/Desktop/Python/103_1"
to_dir = "/Users/anugu/Desktop/Python/103_2"

class FilesEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Hey, {event.src_path} has been created!")
    
    def on_deleted(self, event):
        print(f"Oops! Someone deleted {event.src_path}!")

    def on_modified(self, event):
        print(f"Someone modified {event.src_path}!")
    
    def on_moved(self, event):
        print(f"Oops! Someone moved {event.src_path}!")

event_handler = FilesEventHandler()
observer = Observer()
observer.schedule(event_handler, from_dir, recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...") 
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()