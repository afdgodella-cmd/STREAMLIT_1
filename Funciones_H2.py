# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 10:45:08 2024

@author: Alberto
"""

#!streamlit run C:\Users\Alberto\PycharmProjects\STREEAMLIT\H2_2.py
import pandas as pd 
import streamlit as st
import jaydebeapi

user ='sa'
password =''
dirver ='org.h2.Driver'
jar ='c:\\acf\h2-1.3.176.jar'


   
def añade(conexion):
    url =conexion[0]
    conn =jaydebeapi.connect(dirver,url,[user,password],jar)

    curs = conn.cursor()

    try:
        sql =f"insert into lotes (fecha, abiertos,analisis, liberacion) values ('{conexion[1]}','{conexion[2]}','{conexion[3]}','{conexion[4]}')"
        #return(sql)
        curs.execute(sql)
        return('Datos añadidos')
      
        curs.close()
        conn.close()
    #return(df)
    except Exception as inst:
        return(inst)#'Errror al añadir los datos')
    
def corrige(conexion):
     url =conexion[0]
     conn =jaydebeapi.connect(dirver,url,[user,password],jar)

     curs = conn.cursor()

     try:
         sql =f"update lotes set abiertos = '{conexion[2]}', analisis = '{conexion[3]}', liberacion = '{conexion[4]}' where fecha = '{conexion[1]}'"
         #return(sql)
         curs.execute(sql)
         return('Datos Corregidos')
       
         curs.close()
         conn.close()
     #return(df)
     except Exception as inst:
         return(inst)#'Errror al añadir los datos')   
     
def elimina(conexion):
     url =conexion[0]
     conn =jaydebeapi.connect(dirver,url,[user,password],jar)

     curs = conn.cursor()

     try:
         sql =f"delete from lotes where fecha = '{conexion[1]}'"
         #return(sql)
         curs.execute(sql)
         return('Datos Eliminados')
       
         curs.close()
         conn.close()
     #return(df)
     except Exception as inst:
         return(inst)#'Errror al añadir los datos')         
 
    
def añadeI(conexion):
     url =conexion[0]
     conn =jaydebeapi.connect(dirver,url,[user,password],jar)
     curs = conn.cursor()
     try:
         sql =f"insert into incidentes (fecha, incidentes,eventos, desviaciones) values ('{conexion[1]}','{conexion[2]}','{conexion[3]}','{conexion[4]}')"
         curs.execute(sql)
         return(sql)
       
         curs.close()
         conn.close()
     except Exception as inst:
         return(inst)#'Errror al añadir los datos')
    
def corrigeI(conexion):
      url =conexion[0]
      conn =jaydebeapi.connect(dirver,url,[user,password],jar)

      curs = conn.cursor()

      try:
          sql =f"update incidentes set incidentes = '{conexion[2]}', eventos = '{conexion[3]}', desviaciones = '{conexion[4]}' where fecha = '{conexion[1]}'"
          curs.execute(sql)
          return('Datos Corregidos')
          curs.close()
          conn.close()
  
      except Exception as inst:
          return(inst)#'Errror al añadir los datos')   
      
def eliminaI(conexion):
      url =conexion[0]
      conn =jaydebeapi.connect(dirver,url,[user,password],jar)
      curs = conn.cursor()

      try:
          sql =f"delete from incidentes where fecha = '{conexion[1]}'"
          #return(sql)
          curs.execute(sql)
          curs.close()
          conn.close()
     
      except Exception as inst:
          return(inst)#'Errror al añadir los datos') 
    
def añadeOOS(conexion):
    url =conexion[0]
    conn =jaydebeapi.connect(dirver,url,[user,password],jar)

    curs = conn.cursor()

    try:
        sql =f"insert into OOS (id,fecha, estado,causa) values ('{conexion[1]}','{conexion[2]}','{conexion[3]}','{conexion[4]}')"
        curs.execute(sql)
        #return('Datos añadidos')
      
        curs.close()
        conn.close()
       
    except Exception as inst:
        return(inst)#'Errror al añadir los datos')

def corrigeOOS(conexion):
      url =conexion[0]
      conn =jaydebeapi.connect(dirver,url,[user,password],jar)

      curs = conn.cursor()

      try:
          sql =f"update OOS set fecha = '{conexion[2]}', estado = '{conexion[3]}', causa = '{conexion[4]}' where id = '{conexion[1]}'"
          curs.execute(sql)
          #return('Datos Corregidos')
          curs.close()
          conn.close()
  
      except Exception as inst:
          return(inst)#'Errror al añadir los datos')  
        
def eliminaOOS(conexion):
      url =conexion[0]
      conn =jaydebeapi.connect(dirver,url,[user,password],jar)
      curs = conn.cursor()

      try:
          sql =f"delete from OOS where ID = '{conexion[1]}'"
          #return(sql)
          curs.execute(sql)
          curs.close()
          conn.close()
     
      except Exception as inst:
          return(inst)#'Errror al añadir los datos') 


def añadeV(conexion):
     url =conexion[0]
     conn =jaydebeapi.connect(dirver,url,[user,password],jar)
     curs = conn.cursor()
     try:
         sql =f"insert into varios (fecha, estabilidad,paradas, accidentes) values ('{conexion[1]}','{conexion[2]}','{conexion[3]}','{conexion[4]}')"
         curs.execute(sql)
         return(sql)
       
         curs.close()
         conn.close()
     except Exception as inst:
         return(inst)#'Errror al añadir los datos')
    
def corrigeV(conexion):
      url =conexion[0]
      conn =jaydebeapi.connect(dirver,url,[user,password],jar)

      curs = conn.cursor()

      try:
          sql =f"update varios set estabilidad = '{conexion[2]}', paradas = '{conexion[3]}', accidentes = '{conexion[4]}' where fecha = '{conexion[1]}'"
          curs.execute(sql)
          return('Datos Corregidos')
          curs.close()
          conn.close()
  
      except Exception as inst:
          return(inst)#'Errror al añadir los datos')   
      
def eliminaV(conexion):
      url =conexion[0]
      conn =jaydebeapi.connect(dirver,url,[user,password],jar)
      curs = conn.cursor()

      try:
          sql =f"delete from varios where fecha = '{conexion[1]}'"
          #return(sql)
          curs.execute(sql)
          curs.close()
          conn.close()
     
      except Exception as inst:
          return(inst)#'Errror al añadir los datos') 