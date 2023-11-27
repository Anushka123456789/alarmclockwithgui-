import tkinter as tk
from tkinter import ttk
import time
from threading import Thread

class AlarmClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Alarm Clock")

        self.label = ttk.Label(root, text="Enter time (HH:MM):")
        self.label.pack(pady=10)

        self.entry = ttk.Entry(root)
        self.entry.pack(pady=10)

        self.button = ttk.Button(root, text="Set Alarm", command=self.set_alarm)
        self.button.pack(pady=20)

        self.status_label = ttk.Label(root, text="")
        self.status_label.pack(pady=10)

    def set_alarm(self):
        alarm_time_str = self.entry.get()
        try:
            alarm_time = time.strptime(alarm_time_str, "%H:%M")
            current_time = time.localtime(time.time())
            alarm_datetime = time.mktime(
                time.struct_time((current_time.tm_year, current_time.tm_mon, current_time.tm_mday,
                                  alarm_time.tm_hour, alarm_time.tm_min, 0, 0, 0, -1)))
            
            seconds_until_alarm = alarm_datetime - time.mktime(current_time)

            if seconds_until_alarm < 0:
                self.status_label.config(text="Invalid time. Please enter a future time.")
            else:
                self.status_label.config(text=f"Alarm set for {alarm_time_str}")
                Thread(target=self.wait_and_ring, args=(seconds_until_alarm,)).start()
        except ValueError:
            self.status_label.config(text="Invalid time format. Please use HH:MM")

    def wait_and_ring(self, seconds):
        time.sleep(seconds)
        self.status_label.config(text="Alarm ringing!")
        self.play_alarm_sound()

    def play_alarm_sound(self):
        # Add code to play alarm sound here
        print("Alarm sound should be played here")

if __name__ == "__main__":
    root = tk.Tk()
    alarm_clock = AlarmClock(root)
    root.mainloop()
