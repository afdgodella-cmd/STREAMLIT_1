# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 16:25:40 2024

@author: Alberto
"""

import pandas as pd 
import streamlit as st
import jaydebeapi
import datetime
import Funciones_H2
import datosPSS

accion ='nada'


def H2():
    
    user ='sa'
    password =''
    dirver ='org.h2.Driver'
    jar ='c:\\acf\h2-1.3.176.jar'
    conn =jaydebeapi.connect(dirver,datosPSS.url,[user,password],jar)
    curs = conn.cursor()
 
 
    curs.execute("select * from OOS order by ID")
    data = curs.fetchall()
    
    # Obtener los nombres de las columnas
    #columnas = [desc[0] for desc in curs.description]
    columnas =['ID', 'Fecha','Estado','Causa']
    # Crear un DataFrame
    df1 = pd.DataFrame(data, columns=columnas)
    #curs.close()
    
    curs.execute("select causa, count(causa) from OOS where estado = 'Confirmado' group by causa")
    data = curs.fetchall()
    columnas =['Causa','Número']
    # Crear un DataFrame
    df2 = pd.DataFrame(data, columns=columnas)
    #curs.close()
    
    
    #conn.close()
    return df1,df2
   



def main():
    global accion
    df1, df2 = H2()
    col10, col11, col12, col13 = st.columns(4)
    
    with col10:
        id = st.text_input('Número de OOS')
    
    with col11:
       d = st.date_input("Fercha del OOS", datetime.date.today())
       if st.button('Añadir'):
              accion ='Añadir'       
    with col12:    
        estado = st.selectbox('Estado del OOS', ("Confirmado", "No confirmado", "Pendiente"))
        if st.button('Corregir'):
               accion ='Corregir'  
    with col13:
        causa = st.selectbox('Causa', ("N.A.", "Material", "Máquina", "Método","Humano","Ambiente"))
        if st.button('Eliminar'):
            accion ='Eliminar'
      
        
    col1, col2 = st.columns([5,4])
    with col1:
        st.markdown('')
        st.markdown('FUERAS DE ESPECIFICACIÓN TOTALES')
        st.write(df1)
    with col2:
        st.markdown('')
        st.markdown('CLASIFICACIÓN OOS CONFIRMADOS')
        st.bar_chart(df2,x='Causa')
        st.write(df2)
    if accion == 'Añadir':   
         conexion =[datosPSS.url,id, str(d), estado, causa]
         Funciones_H2.añadeOOS(conexion)
         st.rerun()
    if accion == 'Corregir':   
         conexion =[datosPSS.url,id, str(d), estado, causa]
         st.write(Funciones_H2.corrigeOOS(conexion))
         st.rerun()
    if accion == 'Eliminar':        
         conexion =[datosPSS.url,id]
         Funciones_H2.eliminaOOS(conexion)
         st.rerun()
   
if __name__ == "__main__":
    main()