import streamlit as st
import matplotlib.pyplot as plt

st.title("Теплопровідність композиту A–B")
st.write("Послідовна модель: 1/κc = Φf/κf + Φm/κm")

k_a = st.number_input("κ матриці A, Вт/(м·К)")
k_b = st.number_input("κ наповнювача B, Вт/(м·К)")
p_min = st.number_input("Вміст B від, %")
p_max = st.number_input("Вміст B до, %")
step = st.number_input("Крок, %")

if st.button("Розрахувати"):
    n = int((p_max - p_min) / step) + 1
    phi = [p_min + i * step for i in range(n)]
    kc = [1 / ((p / 100) / k_b + (1 - p / 100) / k_a) for p in phi]

    st.table({"Φ_B, %": phi, "κc, Вт/(м·К)": [round(k, 4) for k in kc]})

    fig, ax = plt.subplots()
    ax.plot(phi, kc)
    ax.set_xlabel("Вміст B, %")
    ax.set_ylabel("κc, Вт/(м·К)")
    ax.grid()
    st.pyplot(fig)