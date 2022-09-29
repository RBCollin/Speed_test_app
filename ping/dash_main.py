import streamlit as st
import sqlite3
import pandas as pd




list_pcs = ['Bernard','PC1','PC2']

pc1 = 'Bernard'
pc2 = 'PC1'
pc3 = 'PC2'



pcs = st.multiselect('Selecione os PCs', options = list_pcs)
lista = (pcs)
lista2 = pd.DataFrame(lista, columns = ['LISTA_PCS'])
lista2




check_BERNARD = lista2.LISTA_PCS.isin([pc1]).any().any()
check_PC2 = lista2.LISTA_PCS.isin([pc2]).any().any()
check_PC3 = lista2.LISTA_PCS.isin([pc3]).any().any()



result_pc1 = lista2.LISTA_PCS.isin([pc1]).any().any()
if result_pc1:
    print(' ')
else:
    lista2 = lista2.append({'LISTA_PCS':'1'}, ignore_index=True)


result_pc2 = lista2.LISTA_PCS.isin([pc2]).any().any()
if result_pc2:
    print(' ')
else:
    lista2 = lista2.append({'LISTA_PCS':'2'}, ignore_index=True)


result_pc3 = lista2.LISTA_PCS.isin([pc3]).any().any()
if result_pc3:
    print(' ')
else:
    lista2 = lista2.append({'LISTA_PCS':'3'}, ignore_index=True)


lista2




if st.button('Monitorar conexão'):
    paramns = lista2['LISTA_PCS']
    
    conn = sqlite3.connect(r"C:\Users\bernard.collin\Desktop\Chinook.db", timeout=15)
    cursor = conn.cursor()

    #df_sql_count = pd.read_sql_query("""SELECT * FROM speed_test """, conn)
    
    ### TEM QUE TER O DELETE AQUI

    cursor.execute("""
        DELETE FROM consult_pcs; 
        """)

    cursor.execute("""
        INSERT INTO consult_pcs (pc1, pc2, pc3)
        VALUES (?, ?, ?)
        """, paramns )

    data_check = pd.read_sql_query("""SELECT * FROM consult_pcs """, conn)

    conn.commit()
    conn.close()

    if 'Bernard' in data_check.values :
        st.write("\n PC de Bernard está no DF")
    
    else :
        st.write("\nPC de Bernard não está no DF")





