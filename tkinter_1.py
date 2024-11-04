import tkinter as tk
from chat import connector, reader, send_msg, read_msg
import threading


MSG_HEIGHT = 2
MAX_MSGS = 10
user_name = 'Anonymous'
msgs = []
msg_lbls = []

def  init_gui():
    root = tk.Tk()
    return root


def init_input(fr_list, fr_input):
    txt_entry = tk.Entry(fr_input)
    label = tk.Label(text='Никнейм')
    name_entry = tk.Entry()
    name_entry.insert(0, user_name)
    def click(txt_entry):
        text = txt_entry.get()
        msg = {
            'user':name_entry.get(),
            'text': text
        }
        send_msg(msg)
    btn_send = tk.Button(fr_input, text='Send', command= lambda: click(txt_entry))

    txt_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
    btn_send.pack(side=tk.LEFT)
    label.pack(side=tk.LEFT)
    name_entry.pack(side=tk.LEFT)


def add_label (text):
    lbl_msg = tk.Label(
        fr_list_msg,
        text=text,
        height= MSG_HEIGHT,
        background='#92c2f2')
    lbl_msg.pack(side=tk.TOP, anchor='ne', padx=2, pady=2)
    msg_lbls.append(lbl_msg)
    print(len(msg_lbls))
    if len(msg_lbls) > MAX_MSGS:
        label = msg_lbls.pop(0)
        label.destroy()


def init_frames(root):
    fr_list_msg = tk.Frame(root)
    fr_input_msg = tk.Frame(root)
    fr_list_msg.pack(fill=tk.BOTH, expand=True)
    fr_input_msg.pack(fill=tk.X, side=tk.BOTTOM)

    lbl_greet = tk.Label(fr_list_msg, text="Chat started..", height=MSG_HEIGHT)
    lbl_greet.pack(side=tk.TOP)
    return fr_list_msg, fr_input_msg


if __name__ == '__main__':
    root = init_gui()
    fr_list_msg, fr_input_msg = init_frames(root)
    th = threading.Thread(target=read_msg, args=(add_label, ))
    th.start()
    init_input(fr_list_msg, fr_input_msg)
    root.mainloop()