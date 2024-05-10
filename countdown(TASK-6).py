from logging import root
import tkinter as tk
from tkinter import messagebox
import time

class CountdownTimerApp:
    def __init__(self, master):
        self.master=master
        self.master.title("Countdown Timer")
        
        self.label=tk.Label(master, text="Set timer(seconds):")
        self.label.pack()
        
        self.entry=tk.Entry(master)
        self.entry.pack()
        
        self.start_button=tk.Button(master,text="Start Timer",command=self.start_timer)
        self.start_button.pack()
        
        self.remaining_time=0
        self.timer_running=False
    
    def start_timer(self):
        if not self.timer_running:
            try:
                self.remaining_time=int(self.entry.get())
                if self.remaining_time > 0:
                    self.timer_running=True
                    self.update_timer()
                else:
                    messagebox.showwarning("Invalid Input", "Please enter a positive number.")
            except ValueError:
                messagebox.showwarning("Invalid Input", "Please enter a valid number.")
                
    def update_timer(self):
        if self.remaining_time > 0:
            self.label.config(text=f"Time remaining: {self.remaining_time} seconds")
            self.remaining_time -=1
            self.master.after(1000, self.update_timer)
        else:
            self.label.config(text="Time's up!")
            self.timer_running=False
            messagebox.showinfo("Timer Finished", "Time's up!")
            

def main():
    root=tk.Tk()
    app=CountdownTimerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

    app=CountdownTimerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
