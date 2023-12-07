from tkinter import *
import time
import winsound


class Clock:
    def __init__(self, root):
        self.clk = Label(root, font=('DS-DIGITAL', 60, 'bold'), bg="#068ad6")
        self.clk.pack(anchor='center')
        self.time()

    def time(self):
        self.clk.config(text=time.strftime('%H:%M:%S \n %x\n %A \n %z,\n %Z'))
        self.clk.after(1000, self.time)

    def alarm_clock(self, set_alarm_time):
        while True:
            time.sleep(1)
            actual_time = time.localtime()
            cur_time = time.strftime("%H:%M:%S", actual_time)
            if cur_time == set_alarm_time:
                winsound.PlaySound("Music.wav", winsound.SND_ASYNC)
                break

    def start_alarm_clock(self):
        try:
            hour = int(self.hour.get())
            min = int(self.min.get())
            sec = int(self.sec.get())
            alarm_set_time = f"{hour}:{min}:{sec}"
            self.alarm_clock(alarm_set_time)
        except ValueError:
            print("Invalid input! Please input numbers only.")


class AlarmClock(Clock):
    def __init__(self, root):
        super().__init__(root)

        self.window = Label(font=('DS-DIGITAL', 60, 'bold'), bg="#107985")
        self.window.pack(anchor="center")

        self.time_format = Label(self.window, text="Remember to set time in 24 hour format!", fg="white", bg="#922B21",
                                 font=("Arial", 15)).place(x=20, y=120)
        self.addTime = Label(self.window, text="Hour     Min     Sec", font=60, fg="white", bg="black").place(x=210)
        self.setYourAlarm = Label(self.window, text="Set Time for Alarm: ")

        self.hour = StringVar()
        self.min = StringVar()
        self.sec = StringVar()

        self.hourTime = Entry(self.window, textvariable=self.hour, width=4, font=(20)).place(x=210, y=40)
        self.minTime = Entry(self.window, textvariable=self.min, width=4, font=(20)).place(x=270, y=40)
        self.secTime = Entry(self.window, textvariable=self.sec, width=4, font=(20)).place(x=330, y=40)

        self.submit = Button(self.window, text="Set Your Alarm", fg="Black", bg="#D4AC0D", width=15, command=self.start_alarm_clock,
                             font=(20)).place(x=100, y=80)


root = Tk()
AlarmClock(root)
root.mainloop()