import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('EMPLEATRONIX')
st.write('Todos los datos sobre los empleados en una aplicación.')

dataset = 'csv/employees.csv'
data = pd.read_csv(dataset)

st.write(data)
st.markdown("---")
columna1, columna2, columna3 = st.columns(3)

with columna1:
  colores = st.color_picker('Elige un color', '#2300F9')
with columna2:
  activarNombre = st.toggle('Mostar el nombre')
with columna3:
  activarSueldo = st.toggle('Mostar el sueldo')
nombres = data["full name"]
salarios = data['salary']

fig, ax = plt.subplots(figsize=(15,8))
bars = ax.barh(nombres,salarios,color = colores)
if not activarNombre:
  plt.yticks([])
if activarSueldo:
  ax.bar_label(bars, fmt='%d €', padding=2)

plt.xticks(rotation=90)
st.pyplot(plt)

st.markdown('© José Antonio Díaz Aranda - CPIFP Alan Turing')
