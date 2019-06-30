# Auteurs: Benjamin BEYERLE - Philippe DA SILVA OLIVEIRA - Karthike EZHILARASAN - Alexandre KOSTAS
# Classe: SRC1 - 3E
# Projet - ClicMed

import settings


settings.log.init_log('bruteforce')

done = False


def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    global done
    done = True
    settings.sys.exit(0)


def animate():
    for c in settings.itertools.cycle(['|', '/', '-', '\\']):
        if done is True:
            break

        settings.sys.stdout.write('\rloading ' + c)
        settings.sys.stdout.flush()
        settings.time.sleep(0.1)


def _attack(chrs, inputt):
    print("[+] Start Time: ", settings.time.strftime('%H:%M:%S'))
    start_time = settings.time.time()
    t = settings.threading.Thread(target=animate)
    t.start()
    total_pass_try=0
    for n in range(1, 31+1):
        characterstart_time = settings.time.time()
        print("\n[!] I'm at ", n , "-character")
      
        for xs in settings.itertools.product(chrs, repeat=n):
            saved = ''.join(xs)
            stringg = saved
            m = settings.hashlib.md5()
            m.update(bytes(saved, encoding='utf-8'))
            total_pass_try +=1
            if m.hexdigest() == inputt:
                settings.time.sleep(10)
                global done
                done = True

                print("\n[!] found ", stringg)
                print("\n[-] End Time: ", settings.time.strftime('%H:%M:%S'))
                print("\n[-] Total Keyword attempted: ", total_pass_try)
                print("\n---Md5 cracked at %s seconds ---" % (settings.time.time() - start_time))
                settings.sys.exit("Thank You !")
        
        print("\n[!]",n,"-character finished in %s seconds ---" % (settings.time.time() - characterstart_time))


def main():
    
    inp_usr = input(" add md5\n")
    chrs = settings.string.printable.replace(' \t\n\r\x0b\x0c', '')
    print(chrs)
    settings.signal.signal(settings.signal.SIGINT, signal_handler)
    return _attack(chrs, inp_usr)


if __name__ == "__main__":
    main()

