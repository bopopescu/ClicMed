# Auteurs: Benjamin BEYERLE - Philippe DA SILVA OLIVEIRA - Karthike EZHILARASAN - Alexandre KOSTAS
# Classe: SRC1 - 3E
# Projet - ClicMed

import settings

progress_bar = 1


def main_frame(root_frame, username, group):
    settings.login.clear_window(root_frame)
    root_frame.configure(background='#3c3f41')

    root_frame.title('Port Scanner')
    root_frame.geometry('310x190')
    root_frame.maxsize(310, 290)
    root_frame.minsize(310, 290)

    target = settings.tk.StringVar()
    port_min = settings.tk.StringVar()
    port_max = settings.tk.StringVar()
    port_min.set('1')
    port_max.set('443')

    global progress_bar

    canvas = settings.tk.Canvas(root_frame, background='white', width=150, height=150)
    canvas.grid(row=2, column=1, sticky="nswe")
    second_frame = settings.tk.Frame(canvas, background='blue')
    second_frame.grid(row=0, column=0, sticky='nw')
    scrollbar = settings.tk.Scrollbar(root_frame, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.create_window((0, 0), window=second_frame, anchor="nw", tags="second_frame")
    file_listbox = settings.tk.Listbox(second_frame, bd=0, selectmode='SINGLE', width=50, height=60,
                                       font=("Arial", 10), fg='white', bg='#3c3f41')
    file_listbox.grid(sticky='nw')
    scrollbar.grid(row=2, column=2, rowspan=2, sticky="nsw", pady=1, padx=1)

    filter1 = settings.tk.Label(root_frame, text='Enter target : ', font=("Arial", 10), fg='white', bg='#3c3f41')
    filter1.grid(row=0, column=0, pady=2, sticky="e")

    label11 = settings.tk.Entry(root_frame, textvariable=target, font=("Arial", 11), fg='black', bg='white')
    label11.grid(row=0, column=1, pady=2, sticky='we')

    filter23 = settings.tk.Label(root_frame, text='Port range : ', font=("Arial", 10), fg='white', bg='#3c3f41')
    filter23.grid(row=1, column=0, pady=2, sticky="e")

    label21 = settings.tk.Entry(root_frame, textvariable=port_min, font=("Arial", 11), fg='black', bg='white', width=7)
    label21.grid(row=1, column=1, pady=2, sticky='w')

    label31 = settings.tk.Entry(root_frame, textvariable=port_max, font=("Arial", 11), fg='black', bg='white', width=7)
    label31.grid(row=1, column=1, pady=2, sticky='e')

    scan_btn = settings.tk.Button(root_frame, text='Scan!',
                                  command=lambda: scanner(label11.get(), file_listbox, label21.get(), label31.get(),
                                                          username))
    scan_btn.grid(row=0, column=2, sticky="w", pady=2, padx=5)

    return_btn = settings.tk.Button(root_frame, text='Return',
                                    command=lambda: settings.menu.main_frame(root_frame, username, group))
    return_btn.grid(row=4, column=1, sticky="se", pady=2, padx=35)

    exit_btn = settings.tk.Button(root_frame, text='Exit', command=root_frame.destroy)
    exit_btn.grid(row=4, column=1, sticky="se", pady=2)


def scanner(target, listbox, port_min, port_max, username):

    port_list = []
    listbox.delete(0, settings.tk.END)
    start = settings.time.time()

    def portscan(port):
        s = settings.socket.socket(settings.socket.AF_INET, settings.socket.SOCK_STREAM)
        s.settimeout(0.2)
        try:
            con = s.connect((target, port))
            port_list.append(port)
            con.close()
        except:
            pass

    # The threader thread pulls an worker from the queue and processes it
    def threader():

        while True:
            worker = q.get()
            # Run the example job with the avail worker in queue (thread)
            portscan(worker)
            # completed with the job
            q.task_done()

    # Create the queue and threader
    q = settings.Queue()

    # how many threads are we going to allow for
    for x in range(50):
        t = settings.threading.Thread(target=threader)

        # classifying as a daemon, so they will die when the main dies
        t.daemon = True

        # begins, must come after daemon definition
        t.start()

    # 100 jobs assigned.
    for worker in range(int(port_min), int(port_max)):
        q.put(worker)

    # wait until the thread terminates.
    q.join()
    idx = 0
    for port in port_list:
        listbox.insert(idx, str(port) + ' is open !!')
        idx += 1

    listbox.insert(idx, 'Scanned in: ' + str(int(settings.time.time() - start)) + ' seconds')
    settings.log.log(username, ' did a ports scan')
    popup = settings.tk.Toplevel()
    popup.wm_title("Task done!")
    ico_popup = settings.tk.PhotoImage(file=settings.ICO)
    popup.configure(background='#3c3f41')
    popup.geometry('150x130')
    popup.maxsize(150, 70)
    popup.minsize(150, 70)
    popup.grab_set()
    popup.tk.call('wm', 'iconphoto', popup._w, ico_popup)
    label = settings.tk.Label(popup, text="Scan Finished !", font=("Arial", 11), fg='white', bg='#3c3f41')
    label.pack(side="top", fill="x", pady=10)
    okay_btn = settings.tk.Button(popup, text="Okay", command=popup.destroy)
    okay_btn.pack()
    popup.mainloop()
