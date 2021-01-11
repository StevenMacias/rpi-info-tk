import tkinter as tk
import netifaces as ni

wlan0_ip = "0.0.0.0"
eth0_ip = "0.0.0.0"
try: 
    ni.ifaddresses('wlan0')
    wlan0_ip = ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']
except: 
    wlan0_ip = "No wlan0 interface"
    
try: 
    ni.ifaddresses('eth0')
    eth0_ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
except: 
    eth0_ip = "No eth0 interface"

class FullScreenApp(object):
    padding=3
    dimensions="{0}x{1}+0+0"

    def __init__(self, master, **kwargs):
        self.master=master
        width=master.winfo_screenwidth()-self.padding
        height=master.winfo_screenheight()-self.padding
        master.geometry(self.dimensions.format(width, height))

        b = tk.Button(self.master, text="Press me!", command=lambda: self.pressed())
        b.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        T = tk.Text(self.master, height=2, width=30)
        T.pack()
        T.insert(tk.END, wlan0_ip+"\n")
        T.insert(tk.END, eth0_ip)

    def pressed(self):
        print("clicked!")

root=tk.Tk()
root.wm_attributes('-fullscreen','false')

app=FullScreenApp(root)

root.mainloop()
