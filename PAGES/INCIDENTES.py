# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 16:25:40 2024

@author: Alberto
"""

 #!streamlit run C:\Users\Alberto\PycharmProjects\STREEAMLIT\H2_incidentes.py
import pandas as pd 
import streamlit as st
import jaydebeapi
import datetime
import Funciones_H2
import datosPSS

num_datos = 30
accion ='nada'


def H2():
   
    user ='sa'
    password =''
    dirver ='org.h2.Driver'
    jar ='c:\\acf\h2-1.3.176.jar'
    conn =jaydebeapi.connect(dirver,datosPSS.url,[user,password],jar)
    curs = conn.cursor()
 
 
    curs.execute("select * from incidentes order by fecha")
    data = curs.fetchall()
    
    # Obtener los nombres de las columnas
    #columnas = [desc[0] for desc in curs.description]
    columnas =['Fecha','  Incidentes',' Eventos','Desviaciones']
    # Crear un DataFrame
    df1 = pd.DataFrame(data, columns=columnas)
    
    #curs.close()
    #conn.close()
    return(df1)
   



def main():
    global accion, num_datos
    df1= H2()
    col11, col12, col13, col14 = st.columns(4)
    with col11:
       d = st.date_input("Escoja fecha", datetime.date.today())
         
    with col12:    
      incidentes = st.number_input("Incidentes", step=1, format="%i")
      if st.button('Añadir'):
             accion ='Añadir'     
    with col13:
        eventos = st.number_input("Eventos", step=1, format="%i")
        if st.button('Corregir'):
             accion ='Corregir'
    with col14:
        desviaciones = st.number_input("Desviaciones", step=1, format="%i")
        if st.button('Eliminar'):
            accion ='Eliminar'
    
        
    num_datos = st.slider('¿Cuantos valores desea muestrear?',0,200,10)
    st.bar_chart(df1.tail(num_datos),x='Fecha', stack=False)    
    #st.line_chart(df1,x='Fecha', y= ['Incid.', 'Eventos'])
    st.write(df1.sort_values('Fecha',ascending=False))  # LOS ORDENAMOS DESCENDENTE PARA QUE EN LA TABLA SALGAN PRIMERO LOS MÑAS RECIENTES  
    
    if accion == 'Añadir':   
         conexion =[datosPSS.url,str(d), incidentes, eventos, desviaciones]
         Funciones_H2.añadeI(conexion)
         st.rerun()
    if accion == 'Corregir':        
         conexion =[datosPSS.url,str(d), incidentes, eventos, desviaciones]
         Funciones_H2.corrigeI(conexion)
         st.rerun()
    if accion == 'Eliminar':        
         conexion =[datosPSS.url,str(d), incidentes, eventos, desviaciones]
         Funciones_H2.eliminaI(conexion)
         st.rerun()
    
if __name__ == "__main__":
    main()