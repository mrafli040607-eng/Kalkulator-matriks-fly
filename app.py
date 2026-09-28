import streamlit as st
import numpy as np
import sympy as sp

# ==============================
# KONFIGURASI HALAMAN
# ==============================

st.set_page_config(
    page_title="Kalkulator Matriks",
    page_icon="🔢",
    layout="wide"
)

# ==============================
# JUDUL
# ==============================

st.title("🔢 Kalkulator Matriks")

st.write(
    "Aplikasi kalkulator matriks berbasis Python "
    "untuk melakukan berbagai operasi matriks."
)

st.divider()

# ==============================
# PILIH OPERASI
# ==============================

operasi = st.selectbox(
    "Pilih Operasi Matriks",
    [
        "Penjumlahan",
        "Pengurangan",
        "Perkalian",
        "Transpose",
        "Determinan",
        "Invers",
        "Rank",
        "Trace"
    ]
)

# ==============================
# UKURAN MATRIKS A
# ==============================

st.subheader("Matriks A")

col1, col2 = st.columns(2)

with col1:
    baris_a = st.number_input(
        "Jumlah Baris A",
        min_value=1,
        max_value=10,
        value=2
    )

with col2:
    kolom_a = st.number_input(
        "Jumlah Kolom A",
        min_value=1,
        max_value=10,
        value=2
    )

# ==============================
# INPUT MATRIKS A
# ==============================

A = []

for i in range(baris_a):

    kolom_input = st.columns(kolom_a)

    baris = []

    for j in range(kolom_a):

        nilai = kolom_input[j].number_input(
            f"A{i+1}{j+1}",
            value=0.0,
            key=f"A_{i}_{j}"
        )

        baris.append(nilai)

    A.append(baris)

A = np.array(A)

st.write("Matriks A:")

st.write(A)

# ==============================
# INPUT MATRIKS B
# ==============================

B = None

if operasi in [
    "Penjumlahan",
    "Pengurangan",
    "Perkalian"
]:

    st.subheader("Matriks B")

    if operasi == "Perkalian":

        baris_b = kolom_a

        st.info(
            "Untuk perkalian A × B, jumlah baris B "
            "harus sama dengan jumlah kolom A."
        )

        kolom_b = st.number_input(
            "Jumlah Kolom B",
            min_value=1,
            max_value=10,
            value=2
        )

    else:

        baris_b = baris_a
        kolom_b = kolom_a

    B = []

    for i in range(baris_b):

        kolom_input = st.columns(kolom_b)

        baris = []

        for j in range(kolom_b):

            nilai = kolom_input[j].number_input(
                f"B{i+1}{j+1}",
                value=0.0,
                key=f"B_{i}_{j}"
            )

            baris.append(nilai)

        B.append(baris)

    B = np.array(B)

    st.write("Matriks B:")

    st.write(B)

# ==============================
# TOMBOL HITUNG
# ==============================

st.divider()

if st.button(
    "🔢 HITUNG",
    type="primary",
    use_container_width=True
):

    try:

        # ==========================
        # PENJUMLAHAN
        # ==========================

        if operasi == "Penjumlahan":

            hasil = A + B

            st.subheader("Hasil Penjumlahan")

            st.write(hasil)

            st.code(
                "A + B = Hasil"
            )

        # ==========================
        # PENGURANGAN
        # ==========================

        elif operasi == "Pengurangan":

            hasil = A - B

            st.subheader("Hasil Pengurangan")

            st.write(hasil)

            st.code(
                "A - B = Hasil"
            )

        # ==========================
        # PERKALIAN
        # ==========================

        elif operasi == "Perkalian":

            if A.shape[1] != B.shape[0]:

                st.error(
                    "Perkalian tidak dapat dilakukan. "
                    "Jumlah kolom A harus sama dengan "
                    "jumlah baris B."
                )

            else:

                hasil = A @ B

                st.subheader("Hasil Perkalian")

                st.write(hasil)

                st.code(
                    "A × B = Hasil"
                )

        # ==========================
        # TRANSPOSE
        # ==========================

        elif operasi == "Transpose":

            hasil = A.T

            st.subheader("Transpose Matriks A")

            st.write(hasil)

            st.code(
                "Aᵀ = Transpose A"
            )

        # ==========================
        # DETERMINAN
        # ==========================

        elif operasi == "Determinan":

            if baris_a != kolom_a:

                st.error(
                    "Determinan hanya dapat dihitung "
                    "untuk matriks persegi."
                )

            else:

                hasil = np.linalg.det(A)

                st.subheader("Determinan Matriks A")

                st.write(
                    f"det(A) = {hasil:.4f}"
                )

        # ==========================
        # INVERS
        # ==========================

        elif operasi == "Invers":

            if baris_a != kolom_a:

                st.error(
                    "Invers hanya dapat dihitung "
                    "untuk matriks persegi."
                )

            else:

                determinan = np.linalg.det(A)

                if abs(determinan) < 1e-10:

                    st.error(
                        "Matriks tidak memiliki invers "
                        "karena determinannya = 0."
                    )

                else:

                    hasil = np.linalg.inv(A)

                    st.subheader("Invers Matriks A")

                    st.write(hasil)

        # ==========================
        # RANK
        # ==========================

        elif operasi == "Rank":

            hasil = np.linalg.matrix_rank(A)

            st.subheader("Rank Matriks A")

            st.write(
                f"Rank(A) = {hasil}"
            )

        # ==========================
        # TRACE
        # ==========================

        elif operasi == "Trace":

            if baris_a != kolom_a:

                st.error(
                    "Trace hanya dapat dihitung "
                    "untuk matriks persegi."
                )

            else:

                hasil = np.trace(A)

                st.subheader("Trace Matriks A")

                st.write(
                    f"Tr(A) = {hasil}"
                )

    except Exception as e:

        st.error(
            f"Terjadi kesalahan: {e}"
        )

# ==============================
# INFORMASI
# ==============================

st.divider()

st.caption(
    "Kalkulator Matriks | Dibuat menggunakan Python, "
    "NumPy, SymPy, dan Streamlit"
)
