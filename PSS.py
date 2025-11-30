# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 16:25:40 2024

@author: Alberto
"""

 #!streamlit run C:\ACF1\ANALISIS.py

import streamlit as st
import datosPSS
import tempfile
import os
import shutil


def H2():
# Subir archivo .h2.db
    uploaded_file = st.file_uploader("Sube tu base de datos H3 (.h2.db)", type=["h2.db"])

    if uploaded_file is not None:
    # Guardar archivo temporalmente
        with tempfile.NamedTemporaryFile(delete=False, suffix=".h2.db") as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_file_path = tmp_file.name

    # H2 necesita el nombre base sin la extensión .h2.db
            db_base_path = tmp_file_path.replace(".h2.db", "")
            datosPSS.url=  f"jdbc:h2:{db_base_path}"
   







def main():
  
  #H2()
  
  # Subir archivo .h2.db
    uploaded_file = st.file_uploader("Sube tu base de datos H3 (.h2.db)", type=["h2.db"])

    if uploaded_file is not None:
      # Guardar archivo temporalmente
          with tempfile.NamedTemporaryFile(delete=False, suffix=".h2.db") as tmp_file:
              tmp_file.write(uploaded_file.read())
              tmp_file_path = tmp_file.name
              datosPSS.archivo = tmp_file_path

      # H2 necesita el nombre base sin la extensión .h2.db
              db_base_path = tmp_file_path.replace(".h2.db", "")
              
              datosPSS.url=  f"jdbc:h2:{db_base_path}"
     
  
  
    try:
     if st.button("Guardar copia modificada"):
            destino_dir = "C:/mis_bases_h2"
            os.makedirs(destino_dir, exist_ok=True)

            # Copiar archivo temporal a destino
            destino_path = os.path.join(destino_dir, "PSS_modificada.h2.db")
            shutil.copy(datosPSS.archivo, destino_path)

            st.success(f"Copia guardada en: {destino_path}")

    except Exception as e:
        st.error(f"Error al conectar o modificar: {e}")   
  
    
if __name__ == "__main__":
    main()