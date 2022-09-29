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
from win10toast import ToastNotifier
from retrying import retry
import socket


## Send notification to windows

toast = ToastNotifier()
toast.show_toast("Ping Monitoring", "The process has been started", duration = 15)

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

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
    toast = ToastNotifier()
    toast.show_toast("Ping Error", "Forbidden 403", duration = 10)




datetime_list = []

# inicializa as lista/variaveis que irão armazernar as velocidades medidas
download = []
upload = []
ping = []
excel_speedtest = pd.DataFrame()

try:
    def variaveis():

        conn = sqlite3.connect(r"C:\Users\bernard.collin\Desktop\Chinook.db", timeout=15)
        cursor = conn.cursor()
        data_check = pd.read_sql_query("""SELECT * FROM consult_pcs """, conn)

        conn.commit()
        conn.close()

        if 'Bernard' in data_check.values :
            print("\n PC de Bernard está no DF, iniciando..")


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

            params = (aux_download,aux_upload, aux_ping,usuario, data, hostname, local_ip)

            conn = sqlite3.connect(r"C:\Users\bernard.collin\Desktop\Chinook.db", timeout=15)
            cursor = conn.cursor()

            #df_sql_count = pd.read_sql_query("""SELECT * FROM speed_test """, conn)

            cursor.execute("""
                INSERT INTO speed_test (Download, Upload, Ping, User, Data, host_name, local_ip)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """, params )

            conn.commit()
            conn.close()

            print('Dados armazenados no banco')
            toast = ToastNotifier()
            toast.show_toast("Ping information", "Inserted into database", duration = 10)


            ### SALVANDO DADOS

            # data_speeds = {'Download': download, 'Upload': upload, 'Ping': ping}
            # data_speeds = pd.DataFrame(data_speeds, columns=['Download', 'Upload', 'Ping'])
            # # cria o dataframe de horarios de realizacao dos testes de velocidade
            # date_time = {'Datetime': datetime_list, }
            # df_date_time = pd.DataFrame(date_time, columns=['Datetime'])
            # # Junta os dois dataframe
            # dados_speedtest = pd.concat([df_date_time, data_speeds], axis=1, join='inner')
            # print(dados_speedtest)


            # # Junta os dois dataframe
            # excel_speedtest = pd.concat([df_date_time, data_speeds], axis=1, join='inner')
            # excel_speedtest.to_excel("dados_Speedtest.xlsx")

        else :
            print("\nPC de Bernard não está no DF")

    
    schedule.every(10).seconds.do(variaveis)

    while True:
        schedule.run_pending()
        print('Running...')
        time.sleep(1)
except:
    toast = ToastNotifier()
    toast.show_toast("Ping Stopped", "Some error occurred", duration = 30)



#     return aux_download, aux_upload, aux_ping, usuario, data

# aux_download, aux_upload, aux_ping, usuario, data =  variaveis() 


# data_speeds = {'Download': download, 'Upload': upload, 'Ping': ping}
# data_speeds = pd.DataFrame(data_speeds, columns=['Download', 'Upload', 'Ping'])
# # cria o dataframe de horarios de realizacao dos testes de velocidade
# date_time = {'Datetime': datetime_list, }
# df_date_time = pd.DataFrame(datetime_list, columns=['Datetime'])
# # Junta os dois dataframe
# dados_speedtest = pd.concat([df_date_time, data_speeds], axis=1, join='inner')
# print(dados_speedtest)


# # Junta os dois dataframe
# excel_speedtest = pd.concat([df_date_time, data_speeds], axis=1, join='inner')
# excel_speedtest.to_excel("dados_Speedtest.xlsx")



# armazena numa lista
# def armazena():

#     params = (aux_download,aux_upload, aux_ping,usuario, data)

#     conn = sqlite3.connect(r"C:\Users\bernard.collin\Desktop\Chinook.db", timeout=15)
#     cursor = conn.cursor()

#     df_sql_count = pd.read_sql_query("""SELECT * FROM speed_test """, conn)

#     cursor.execute("""
#         INSERT INTO speed_test (Download, Upload, Ping, User, Data)
#         VALUES (?, ?, ?, ?, ?)
#         """, params )

#     conn.commit()
#     conn.close()

#     print('Dados armazenados no banco')

# armazena()








# import scheduler
# import time

# def func():
#     print('Olha ta rodando em carai')

# scheduler.every(5).seconds.do(func)

# while True:
#     scheduler.run_peding()
#     print('Running...')
#     time.sleep(1)




