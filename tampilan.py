import os
from time import sleep


def keluar():
       print '\x1b[34mwassalamu`alaikum'
       sleep(3)
       os.system('clear')
       os.system('exit')

logo = '\x1b[92m  _      _     ----   ----   _  \n\x1b[92m |||____|||   / /| | /_/| | |_| \n\x1b[92m |||====|||  / /_| |_   | | ||| \n\x1b[92m |||    ||| /_/--| |-   | | ||| \n\x1b[92m |||    |||      |_|    |_| ||| '

def awal():
       os.system('clear')
       print logo
       print '\x1b[49mDAFTAR KEMAMPUAN'
       print '\x1b[49m1. Ubah key extra'
       print '\x1b[49m2. Ubah $'
       print '\x1b[49m3. Hapus / ubah welcome bawaan'
       print '\x1b[49m4. Buat / ubah welcome'
       print '\x1b[49m5. Install bahan untuk mempercantik tampilan'
       print '\x1b[49m6. Install ohmyzsh'
       print '\x1b[49m7. Ke menu tampilan ohmyzsh'
       print '\x1b[48m8. Install kali linux'
       print '\x1b[48m9. Masuk kali linux'
       print '\x1b[48m0. Keluar'
       print
       main()

def main():
       ham = raw_input('\x1b[1;91m-\xe2\x96\xba\x1b[1;97m ')
       if ham == '':
         os.system('clear')
         print '\x1b[1;91m[!] Jangan kosong'
         main()
       else:
          if ham == '1':
             key()
          else:
            if ham == '2':
               s()
            else:
               if ham == '3':
                  welcome()
               else:
                  if ham == '4':
                     welcom()
                  else:
                    if ham == '5':
                        bahan()
                    else:
                      if ham == '6':
                        zsh()
                      else:
                        if ham == '7':
                           zshrc()
                        else:
                           if ham == '8':
                             kali()
                           else:
                             if ham == '9':
                               os.system('./start-kali.sh')
                             else:
                              if ham == '0':
                                keluar()
                              else:
                                print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + ham + ' \x1b[1;91mTidak Ada'
                                sleep(2)
                                awal()

def key():
     try:
        os.mkdir('/data/data/com.termux/files/home/.termux')
     except:
         pass

     key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
     kontol = open('/data/data/com.termux/files/home/.termux/termux.properties', 'w')
     kontol.write(key)
     kontol.close()
     os.system('termux-reload-settings')
     sleep(3)
     print 'Success !'
     awal()

def s():
       os.system('clear')
       os.system('nano /data/data/com.termux/files/usr/etc/bash.bashrc')
       awal()
 
def welcome():
       os.system('clear')
       os.system('nano /data/data/com.termux/files/usr/etc/motd')
       awal()

def welcome():
       os.system('clear')
       os.system('nano /data/data/com.termux/files/home/.bashrc')
       awal()

def bahan():
      os.system('clear')
      os.system('pkg update && pkg update && pkg install ruby && pkg install toilet && pkg install figlet && pkg install cowsay && pkg install vim && pkg install neofetch && pkg install screenfetch')
      os.system('gem install lolcat')
      awal()

def zsh():
       os.system('clear')
       os.system('cd /data/data/com.termux/files/home && pkg install curl && pkg install grep')
       os.system(' sh -c "$(curl -fsSL https://github.com/Cabbagec/termux-ohmyzsh/raw/master/install.sh)"')
       awal()

def kali():
        os.system('clear')
        os.system('cd /data/data/com.termux/files/home/')
        sleep(3)
        os.system('pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Kali/kali.sh && bash kali.sh')
        print 'ke mode kali linux? y/n'
        print
        mode()

def mode():
        hal = raw_input('\x1b[1;91my/n-\xe2\x96\xba\x1b[1;97m ')
        if hal == '':
            os.system('clear')
            print '\x1b[1;91m[!] Jangan kosong'
            mode()
        else:
           if hal == 'y':
             os.system('./start-kali.sh')
           else:
              if hal == 'n':
                 awal()

def zshrc():
       os.system('clear')
       print logo
       print '\x1b[38mDAFTAR MENU ZSH'
       print '\x1b[38m1. Ubah welcome'
       print '\x1b[38m2. Ubah tema atau welcome'
       print '\x1b[38m3. Ubah warna'
       print '\x1b[38m4. Ubah font'
       print '\x1b[38m5. Daftar tema'
       print '\x1b[38m0. Ke bali'
       print
       menu()

def menu():
       zsh = raw_input('\x1b[35m-\xe2\x96\xba\x1b[1;97m ')
       if zsh == '':
         os.system('clear')
         print '\x1b[1;91m[!] Jangan kosong'
         zshrc()
       else:
           if zsh == '1':
               os.system('nano /data/data/com.termux/files/usr/etc/zshrc')
               os.system('termux-reload-settings')
               zshrc()
           else:
              if zsh == '2':
                  os.system('nano /data/data/com.termux/files/home/.zshrc')
                  os.system('termux-reload-settings')
                  zshrc()
              else:
                 if zsh == '3':
                    os.system('~/.termux/colors.sh')
                    zshrc()
                 else:
                    if zsh == '4':
                       os.system('~/.termux/fonts.sh')
                    else:
                        if zsh == '5':
                           os.system('xdg-open https://github.com/robbyrussell/oh-my-zsh/wiki/themes')
                           zshrc()
                        else:
                           if zsh == '0':
                               awal()


awal()
