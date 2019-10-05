# rootVIII
from tkinter import Tk, Label, Button, E, W
from tkinter import Text, PhotoImage, END
from os.path import realpath
from contextlib import closing
from threading import Thread
from urllib.parse import urlencode
from urllib.request import urlopen
import socket


class RokuRemote:
    def __init__(self, master):
        self.cached_ip = None
        self.last_ip_lookup = None
        self.netloc = None
        self.master = master
        master.title('ROKU REMOTE')
        master.configure(bg='#F2F2F2')
        icon = realpath(__file__)[:-14] + 'icon.png'
        self.imagePath = PhotoImage(file=icon)
        self.image = Label(master, image=self.imagePath)
        self.title_label = Label(
            master, text='Enter your Roku Server IP: ',
            bg='#327AF3', font='Arial 10 bold')
        self.blank_label1 = Label(master, bg='#F2F2F2')
        self.blank_label2 = Label(master, bg='#F2F2F2')
        self.status_label = Label(master, bg='#F2F2F2')
        self.server_ip_addr = Text(
            master, height=1, width=15,
            fg='#F2F2F2', bg='#888888')
        self.up_button = Button(
            master, fg='#33CC00', bg='#000',
            text='UP', width=5, command=self.up)
        self.down_button = Button(
            master, fg='#33CC00', text='DOWN',
            bg='#000', width=5, command=self.down)
        self.left_button = Button(
            master, fg='#33CC00', bg='#000',
            text='LEFT', width=5, command=self.left)
        self.right_button = Button(
            master, fg='#33CC00', bg='#000',
            text='RIGHT', width=5, command=self.right)
        self.power_button = Button(
            master, fg='#33CC00', bg='#FF3346',
            text='POWER', command=self.power)
        self.home_button = Button(
            master, fg='#33CC00', text='HOME',
            bg='#000', command=self.home)
        self.play_pause_button = Button(
            master, fg='#33CC00', bg='#000', text='PLAY',
            width=6, command=self.play_pause)
        self.back_button = Button(
            master, fg='#33CC00', bg='#000', text='BACK',
            width=6, command=self.back)
        self.select_button = Button(
            master, fg='#33CC00', bg='#000', text='OK',
            width=5, command=self.select)
        self.image.grid(row=0, sticky=W + E)
        self.title_label.grid(row=1, sticky=W,)
        self.server_ip_addr.grid(row=1, sticky=E)
        self.blank_label1.grid(row=2, sticky=W, padx=40, pady=1)
        self.status_label.grid(row=3, sticky=W + E, padx=40, pady=2)
        self.up_button.grid(row=4, padx=10, pady=10,)
        self.left_button.grid(row=5, padx=10, pady=1, sticky=W)
        self.right_button.grid(row=5, padx=10, pady=1, sticky=E)
        self.select_button.grid(row=5, padx=10, pady=10)
        self.down_button.grid(row=6, padx=10, pady=10)
        self.blank_label1.grid(row=7, pady=10)
        self.play_pause_button.grid(row=8, pady=0, sticky=E + W)
        self.blank_label2.grid(row=9, pady=10)
        self.back_button.grid(row=10, sticky=E + W)
        self.home_button.grid(row=11, sticky=E + W)
        self.power_button.grid(row=12, sticky=E + W)
        self.status_label.grid(row=13, stick=E + W)

    def up(self):
        self.status_label.config(text='UP', fg='#888888')
        self.make_request('up')

    def down(self):
        self.status_label.config(text='DOWN', fg='#888888')
        self.make_request('down')

    def left(self):
        self.status_label.config(text='LEFT', fg='#888888')
        self.make_request('left')

    def right(self):
        self.status_label.config(text='RIGHT', fg='#888888')
        self.make_request('right')

    def power(self):
        self.status_label.config(text='POWER', fg='#888888')
        self.make_request('power')

    def home(self):
        self.status_label.config(text='HOME', fg='#888888')
        self.make_request('home')

    def back(self):
        self.status_label.config(text='BACK', fg='#888888')
        self.make_request('back')

    def play_pause(self):
        self.status_label.config(text='PLAY/PAUSE', fg='#888888')
        self.make_request('play')

    def select(self):
        self.status_label.config(text='OK', fg='#888888')
        self.make_request('select')

    def make_request(self, btn_cmd):
        ip = self.server_ip_addr.get('1.0', END).strip()

        # if user inputs something that doesn't validate as an ip address, try
        # to resolve it as a hostname.
        # we still need to make the request from the IP because Roku disallows
        # access by hostname in an incorrect attempt to mitigate DNS rebinding
        # attacks. cf. https://community.roku.com/t5/Roku-Developer-Program/External-Control-API-suddenly-returns-403-Forbidden/m-p/499352/highlight/true#M42620
        try:
            socket.inet_aton(ip)
            self.netloc = ip
        except OSError:
            if not self.cached_ip or self.last_ip_lookup != ip:
                self.last_ip_lookup = ip
                self.cached_ip = socket.gethostbyname(ip)
                self.netloc = self.cached_ip
        url = 'http://' + self.netloc + ':8060/keypress/' + btn_cmd
        try:
            with closing(urlopen(url, urlencode('').encode())) as resp:
                resp.read().decode()
        except Exception:
            print('invalid entry')


def roku_thread():
    root = Tk()
    RokuRemote(root)
    root.mainloop()


def main():
    try:
        thread = Thread(target=roku_thread)
        thread.daemon = True
        thread.start()
        thread.join()
    except KeyboardInterrupt:
        pass
    print('\n\nClosing Roku Remote\n')


if __name__ == "__main__":
    main()
