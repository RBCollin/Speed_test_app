import streamlit as st
import sqlite3
import pandas as pd
import requests
from streamlit_lottie import st_lottie


st.set_page_config(layout="wide")

coluna1, coluna2 = st.columns(2)
with coluna1:
    st.success(""" 
        #  Speed Test - Painel Control
            """)


    list_pcs = ['Bernard','Servidor','Danilo']

    pc1 = 'Bernard'
    pc2 = 'Servidor'
    pc3 = 'Danilo'


    pcs = st.multiselect('Selecione os PCs', options = list_pcs)
    lista = (pcs)
    lista2 = pd.DataFrame(lista, columns = ['LISTA_PCS'])


    check_BERNARD = lista2.LISTA_PCS.isin([pc1]).any().any()
    check_PC2 = lista2.LISTA_PCS.isin([pc2]).any().any()
    check_PC3 = lista2.LISTA_PCS.isin([pc3]).any().any()

    #### OS NUMEROS DE INPUT VAO SER OS IPS COLETADOS OU USUARIOS

    result_pc1 = lista2.LISTA_PCS.isin([pc1]).any().any()
    if result_pc1:
        lista2 = lista2.append({'LISTA_PCS':'1'}, ignore_index=True)
    else:
        print(' ')

    result_pc2 = lista2.LISTA_PCS.isin([pc2]).any().any()
    if result_pc2:
        lista2 = lista2.append({'LISTA_PCS':'2'}, ignore_index=True)
    else:
        print(' ')

    result_pc3 = lista2.LISTA_PCS.isin([pc3]).any().any()
    if result_pc3:
        lista2 = lista2.append({'LISTA_PCS':'3'}, ignore_index=True)
    else:
        print(' ')







    col_insert = list(lista2["LISTA_PCS"])

    import pandas as pd
    import requests

    pcs = 'http://sia:3000/backend/busca_generica/buscaGenerica?view=AGDTI.BCDW_DISPOSITIVOS_MONITORADOS'
    data_pcs = requests.get(pcs)
    json_data = data_pcs.json()
    df_piv_2=pd.json_normalize(json_data)
    df_piv_2 = pd.DataFrame.from_dict(df_piv_2)
    data_PC = pd.DataFrame(df_piv_2)
    data_pcs.close()


    if len(data_PC) == 0:
        ### INSERINDO UM PC PRA CRIAR A COLUNA E ENTAO DELETRA TUDO PRA DA O INSERT
        aa = f"http://sia:3000/backend/bernard/salvarDispositivo?PC=404"
        inserir = requests.get(aa)
        inserir.close()

        pcs = 'http://sia:3000/backend/busca_generica/buscaGenerica?view=AGDTI.BCDW_DISPOSITIVOS_MONITORADOS'
        data_pcs = requests.get(pcs)
        json_data = data_pcs.json()
        df_piv_2=pd.json_normalize(json_data)
        df_piv_2 = pd.DataFrame.from_dict(df_piv_2)
        data_PC = pd.DataFrame(df_piv_2)
        data_pcs.close()



    col_list =  list(data_PC["PC"])

    if st.button('Monitorar conexão'):


    ######## DATABSE DE INFORMAÇOES
        ### ATUALIZAR INFORMAÇÃO

        #### DELETE - TENHO QUE DELETAR TUDO


        for i in col_list:
            cc = f"http://sia:3000/backend/bernard/deletarDispositivo?PC={i}"
            delete = requests.get(cc)
            delete.close()


        #### INSERT PCS - TENHO QUE INSERIR TUDO


        for i in col_insert:
            aa = f"http://sia:3000/backend/bernard/salvarDispositivo?PC={i}"
            inserir = requests.get(aa)
            inserir.close()

        ## CONSULTANDO BASE PARA CHECK

        pcs = 'http://sia:3000/backend/busca_generica/buscaGenerica?view=AGDTI.BCDW_DISPOSITIVOS_MONITORADOS'
        data_pcs = requests.get(pcs)
        json_data = data_pcs.json()
        df_piv_2=pd.json_normalize(json_data)
        df_piv_2 = pd.DataFrame.from_dict(df_piv_2)
        data_PC = pd.DataFrame(df_piv_2)
        data_pcs.close()



    #### AQUI VAI SER UM ARWQUIVO POR PC COM O CODIGO DO PC
    #### MAS ESSA LINHA SO SERVE PRO MEU CHECK
        
        #data_PC

        

        with coluna2:
            lottie_1 = 'https://assets9.lottiefiles.com/packages/lf20_rkra4gwo.json'
            lottie_2 = 'https://assets9.lottiefiles.com/packages/lf20_zmrp62ng.json'
            
            def get_lottie(url):
                    r = requests.get(url)
                    if r.status_code != 200:
                        return None
                    return r.json()

            
            lottie_icon = get_lottie(lottie_2)
            st_lottie(lottie_icon, height = 300, key = 'lttie')
            st.info("PC's em monitoramento...")
            st.write('___')





