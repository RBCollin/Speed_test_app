import sched
import time
import pandas as pd
import pyspeedtest
import speedtest
import sqlite3
import os
from datetime import datetime
import schedule
import getpass
import pywintypes

import plyer.platforms.win.notification
from plyer import notification


from retrying import retry
import socket


## Send notification to windows

notification.notify("Ping Monitoring", "The process has been started")


hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

import plyer.platforms.win.notification
from plyer import notification





try:
    @retry (wait_fixed = 60000, stop_max_attempt_number = 10)
    def get_conect():
        s = pyspeedtest.SpeedTest()
        stt = speedtest.Speedtest()
        scheduler = sched.scheduler()
        stt.get_best_server()
        USER_NAME = getpass.getuser()

        return s, stt, scheduler

    s, stt, scheduler = get_conect()
    

except:
    notification.notify("Ping Error", "Forbidden 403")





datetime_list = []

# inicializa as lista/variaveis que irão armazernar as velocidades medidas
download = []
upload = []
ping = []
excel_speedtest = pd.DataFrame()

try:
    def variaveis():

        import requests

        print('Coletando dados')

        ### CONSULTANDO PCS NA BASE

        pcs = 'http://sia:3000/backend/busca_generica/buscaGenerica?view=AGDTI.BCDW_DISPOSITIVOS_MONITORADOS'

        data_pcs = requests.get(pcs)

        print('Request feito')

        json_data = data_pcs.json()
        df_piv_2=pd.json_normalize(json_data)
        df_piv_2 = pd.DataFrame.from_dict(df_piv_2)
        data_PC = pd.DataFrame(df_piv_2)

        print('Dados normalizados')

        data_pcs.close()

        print('Dados coletados com sucesso')


        if 3 in data_PC.values :
            print("\n PC de Danillo está no DF, iniciando..")


            print('Testando Download...')
            aux_download = float('{:.2f}'.format(stt.download() / (10 ** 6))) #MB/s
            print(aux_download)
            
            print('Testando Upload...')
            aux_upload = float('{:.2f}'.format(stt.upload() / (10 ** 6)))     #MB/s
            print(aux_upload)
            
            print('Testando Ping...')
            aux_ping = float('{:.2f}'.format(s.ping()))       #ms 
            print(aux_ping)

            usuario = str(os.getlogin())

            data = str(datetime.today().strftime('%Y-%m-%d %H:%M:%S'))


            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)

            download.append(aux_download)
            upload.append(aux_upload)
            ping.append(aux_ping)
            datetime_list.append(data)

            ###### INSERINDO DADOS NO BANCO

            aa = f"http://sia:3000/backend/bernard/salvarPing?DOWNLOAD={aux_download}&UPLOAD={aux_upload}&PING={aux_ping}&USUARIO={usuario}&DATA={data}&HOSTNAME={hostname}&LOCAL_IP={local_ip}"
            inserir = requests.get(aa)
            inserir.close()

            print('Dados armazenados no banco')

            notification.notify("Ping information", "Inserted into database")
            
        else :
            print("\nPC de Danillo não está no DF")

    schedule.every(10).seconds.do(variaveis)

    while True:
        schedule.run_pending()
        print('Running...')
        time.sleep(1)
except:
    notification.notify("Ping Stopped", "Some error occurred")






