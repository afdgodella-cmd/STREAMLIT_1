# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 16:25:40 2024

@author: Alberto
"""

 #!streamlit run C:\ACF1\ANALISIS.py
import pandas as pd 
import streamlit as st
import jaydebeapi
import datetime
import Funciones_H2
import datosPSS
import jpype
 
num_datos = 30
accion ='nada'

def H2():
    
    st.write(datosPSS.url)
    user ='sa'
    password =''
    dirver ='org.h2.Driver'
    jar ='c:\\acf\h2-1.3.176.jar'
    conn =jaydebeapi.connect(dirver,datosPSS.url,[user,password],jar)
    curs = conn.cursor()
 
 
    curs.execute("select * from Lotes order by fecha")
    data = curs.fetchall()
    
    # Obtener los nombres de las columnas
    #columnas = [desc[0] for desc in curs.description]
    columnas =['Fecha     ',' Totales','Analisis','Dictamen']
    # Crear un DataFrame
    df = pd.DataFrame(data, columns=columnas)
    
    curs.close()
    conn.close()
    return(df)
    print(df)



def main():
    
    global accion,num_datos
    df1= H2()
    col1, col2, col3, col4 = st.columns(4)
    with col1:
       d = st.date_input("Escoja fecha", datetime.date.today())           
    with col2:    
        totales = st.number_input("Totales", step=1, format="%i")
        if st.button('Añadir'):
            accion ='Añadir'     
    with col3:
        analisis = st.number_input("Analisis", step=1, format="%i")
        if st.button('Corregir'):
             accion ='Corregir'
    with col4:
        dictamen = st.number_input("Dictamen", step=1, format="%i")
        if st.button('Eliminar'):
             accion ='Eliminar'
    #archivo = st.file_uploader("Elige un archivo", type=["pdf", "txt"], help = None)  
    #if archivo is not None:
     #   st.write("archivo: ", archivo.name)    
    num_datos = st.slider('¿Cuantos valores desea mostrar?',0,200,10)
    st.bar_chart(df1.tail(num_datos),x='Fecha     ',stack=False)#ORDENA LAS BARRAS ALFABÉTICAMENTE, POR ESO PUSE UN ESPACI ANTES DE TOTALES PARA QUE SALGA LAA PRIMERA
    st.write(df1.sort_values('Fecha     ',ascending=False))  # LOS ORDENAMOS DESCENDENTE PARA QUE EN LA TABLA SALGAN PRIMERO LOS MÑAS RECIENTES  
        
     
  
    if accion == 'Añadir':        
         conexion =[datosPSS.url,str(d), totales, analisis, dictamen]
         Funciones_H2.añade(conexion)
         st.rerun()
    if accion == 'Corregir':        
         conexion =[datosPSS.url,str(d), totales, analisis, dictamen]
         Funciones_H2.corrige(conexion)
         st.rerun()
    if accion == 'Eliminar':        
         conexion =[datosPSS.url,str(d), totales, analisis, dictamen]
         st.write(Funciones_H2.elimina(conexion))
         st.rerun()
  
    
if __name__ == "__main__":
    main()