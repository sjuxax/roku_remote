from tkinter import *
from contextlib import closing
try:
    from urllib.parse import urlencode
    from urllib.request import urlopen
except ImportError:
    from urllib import urlencode
    from urllib2 import urlopen


class RokuRemote:
    def __init__(self, master):
        self.master = master
        master.title("ROKU REMOTE")
        master.configure(bg="#F2F2F2")
        self.base_url = ""
        self.imagePath = PhotoImage(file="icon.png")
        self.image = Label(master, image=self.imagePath)
        # widgets/ UI elements:
        self.title_label = Label(
            master, text="Enter your Roku Server IP: ",
            bg="#327AF3", font="Helvetica 10 bold")
        self.blank_label1 = Label(master, bg="#F2F2F2")
        self.blank_label2 = Label(master, bg="#F2F2F2")
        self.status_label = Label(master, bg="#F2F2F2")
        self.server_ip_addr = Text(
            master, height=1, width=15,
            fg="#F2F2F2", bg="#888888")
        self.up_button = Button(
            master, fg="#33CC00", bg="#000",
            text="UP", width=5, command=self.up)
        self.down_button = Button(
            master, fg="#33CC00", text="DOWN",
            bg="#000", width=5, command=self.down)
        self.left_button = Button(
            master, fg="#33CC00", bg="#000",
            text="LEFT", width=5, command=self.left)
        self.right_button = Button(
            master, fg="#33CC00", bg="#000",
            text="RIGHT", width=5, command=self.right)
        self.power_button = Button(
            master, fg="#33CC00", bg="#FF3346",
            text="POWER", command=self.power)
        self.home_button = Button(
            master, fg="#33CC00", text="HOME",
            bg="#000", command=self.home)
        self.play_pause_button = Button(
            master, fg="#33CC00", bg="#000", text="PLAY",
            width=6, command=self.play_pause)
        self.back_button = Button(
            master, fg="#33CC00", bg="#000", text="BACK",
            width=6, command=self.back)
        self.select_button = Button(
            master, fg="#33CC00", bg="#000", text="OK",
            width=5, command=self.select)
        # begin grid placement
        self.image.grid(row=0, sticky=W + E + N)
        self.title_label.grid(row=1, sticky=W,)
        self.server_ip_addr.grid(row=1, sticky=E)
        self.blank_label1.grid(row=2, sticky=W, padx=40, pady=1)
        self.status_label.grid(row=3, sticky=W + E, padx=40, pady=2)
        self.up_button.grid(row=4, padx=10, pady=10,)
        self.left_button.grid(row=5, padx=10, pady=1, sticky=W)
        self.right_button.grid(row=5, padx=10, pady=1, sticky=E)
        self.select_button.grid(row=5, padx=10, pady=10, sticky=S)
        self.down_button.grid(row=6, padx=10, pady=10)
        self.blank_label1.grid(row=7, pady=10)
        self.play_pause_button.grid(row=8, pady=0, sticky=E + W)
        self.blank_label2.grid(row=9, pady=10)
        self.back_button.grid(row=10, sticky=E + W)
        self.home_button.grid(row=11, sticky=E + W)
        self.power_button.grid(row=12, sticky=E + W)
        self.status_label.grid(row=13, stick=E + W)

    def up(self):
        self.status_label.config(text="entered UP", fg="#888888")
        ip = self.server_ip_addr.get("1.0", END).strip()
        self.make_request(ip, "up")

    def down(self):
        self.status_label.config(text="entered DOWN", fg="#888888")
        ip = self.server_ip_addr.get("1.0", END).strip()
        self.make_request(ip, "down")

    def left(self):
        self.status_label.config(text="entered LEFT", fg="#888888")
        ip = self.server_ip_addr.get("1.0", END).strip()
        self.make_request(ip, "left")

    def right(self):
        self.status_label.config(text="entered RIGHT", fg="#888888")
        ip = self.server_ip_addr.get("1.0", END).strip()
        self.make_request(ip, "right")

    def power(self):
        self.status_label.config(text="entered POWER", fg="#888888")
        ip = self.server_ip_addr.get("1.0", END).strip()
        self.make_request(ip, "power")

    def home(self):
        self.status_label.config(text="entered HOME", fg="#888888")
        ip = self.server_ip_addr.get("1.0", END).strip()
        self.make_request(ip, "home")

    def back(self):
        self.status_label.config(text="entered BACK", fg="#888888")
        ip = self.server_ip_addr.get("1.0", END).strip()
        self.make_request(ip, "back")

    def play_pause(self):
        self.status_label.config(text="entered PLAY/PAUSE", fg="#888888")
        ip = self.server_ip_addr.get("1.0", END).strip()
        self.make_request(ip, "play")

    def select(self):
        self.status_label.config(text="entered OK", fg="#888888")
        ip = self.server_ip_addr.get("1.0", END).strip()
        self.make_request(ip, "select")

    def make_request(self, ip_addr, btn_cmd):
        url = "http://" + ip_addr + ":8060/keypress/" + btn_cmd
        data = urlencode('').encode()
        try:
            with closing(urlopen(url, data)) as response:
                response.read().decode()
        except Exception:
            print("invalid entry")


if __name__ == "__main__":
    root = Tk()
    roku_remote = RokuRemote(root)
    root.mainloop()
