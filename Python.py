showPyplotGlobalUse = 'false'
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.header("ANALISIS DATA STUDI KASUS BIKE SHARING DATASET")
st.caption("Disusun Oleh: Satrio Mangkunegoro")

st.write("Bike Sharing merupakan generasi baru dari penyewaan sepeda tradisional di mana seluruh proses mulai dari keanggotaan, penyewaan, hingga pengembalian telah menjadi otomatis. Melalui sistem ini, pengguna dapat dengan mudah menyewa sepeda dari posisi tertentu dan mengembalikannya di posisi lain. Saat ini, terdapat lebih dari 500 program berbagi sepeda di seluruh dunia yang terdiri dari lebih dari 500 ribu sepeda. Ada minat besar pada sistem-sistem ini karena peran pentingnya dalam masalah lalu lintas, lingkungan, dan kesehatan.")

st.subheader("Data")
st.write("Dataset terkait dengan catatan historis dua tahun yang sesuai dengan tahun 2011 dan 2012 dari sistem Capital Bikeshare, Washington D.C., AS yang tersedia secara publik di http://capitalbikeshare.com/system-data.")
day_df = pd.read_csv("day.csv")
st.dataframe(data=day_df, width=750, height=300)

st.subheader("Distribusi Data")
st.write("Pada subbab ini dijelaskan mengenai distribusi data dari variabel cnt, casual, dan registered")
columns_to_plot = ['cnt', 'casual', 'registered']

sns.boxplot(data=day_df[columns_to_plot])

plt.ylabel('Count')
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()

nilai_skewed_cnt = day_df['cnt'].skew()
st.write("Nilai skewness untuk variabel cnt adalah:", nilai_skewed_cnt)

nilai_skewed_casual = day_df['casual'].skew()
st.write("Nilai skewness untuk variabel casual adalah:", nilai_skewed_casual)

nilai_skewed_registered = day_df['registered'].skew()
st.write("Nilai skewness untuk variabel registered adalah:", nilai_skewed_registered)

with st.expander("Interpretasi variabel cnt (total peminjaman):"):
  st.write("Variabel cnt (total peminjaman sepeda) termasuk normal distribution karena nilai median berada ditengah IQR dan tidak terdapat outlier atau pencilan. Hal ini juga ditunjukkan dengan nilai skewed yang mendekati 0")

with st.expander("Interpretasi variabel casual (peminjam casual):"):
  st.write("Variabel casual (peminjam casual) termasuk right-skewed distribution karena sebagian besar data terkonsentrasi pada bagian kiri (mean > median). Hal ini juga ditunjukkan dengan nilai skewed sebesar 1.27. Selain itu, terdapat juga outlier atau pencilan")

with st.expander("Interpretasi variabel registered (peminjam registered):"):
  st.write("Variabel registered (peminjam registered) termasuk normal distribution karena nilai median berada ditengah IQR dan tidak terdapat outlier atau pencilan. Hal ini juga ditunjukkan dengan niai skewed yang mendekati 0.")

st.subheader("Grafik Peminjaman Sepeda")
st.write("Pada subbab ini menampilkan diagram clustered untuk mengetahui perbandingan jumlah peminjaman sepeda berdasarkan musim dalam 2 tahun berbeda")
sns.barplot(data=day_df, x="season", y="cnt", hue="yr", errorbar=None)
st.pyplot()

st.write("Keterangan:") 
st.write("(season) 1: Musim Panas, 2: Musim Semi, 3: Musim Gugur, 4: Musim Dingin")
st.write("(yr) 0: 2011, 1: 2012")
with st.expander("Interpretasi:"):
  st.write("Berdasarkan diagram batang di atas, dapat disimpulkan bahwa jumlah peminjaman sepeda berdasarkan musim pada tahun 2012 lebih tinggi dibandingkan tahun 2011. Jumlah peminjaman tertinggi terjadi pada musim gugur tahun 2012 dan jumlah peminjaman terendah terjadi pada musim panas tahun 2011.")
