# Mengimpor library
import pandas as pd
import streamlit as st
import pickle

# Menghilangkan warning
import warnings
warnings.filterwarnings("ignore")

# Menulis judul
st.markdown("<h1 style='text-align: center; '> Model Klasifikasi (Beli/Tidak) </h1>", unsafe_allow_html=True)
st.markdown('---'*10)


# Fungsi untuk prediksi
def final_prediction(values, model):
    global prediction
    prediction = model.predict(values)
    return prediction

# Ini merupakan fungsi utama
def main():
    
    # Nilai awal
    usia = 25
    gaji = 80000
    
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            usia = st.number_input('Usia', value=usia)
        with col2:
            gaji = st.number_input('Estimasi Gaji', value=gaji)
        with col3:
            Education = st.number_input('Education', value=gaji)
    
    st.markdown('---'*10)
    
    kelamin = st.selectbox('Jenis Kelamin', ('Laki', 'Perempuan'))
    
    data = {
        'Kelamin': kelamin,
        'Usia':usia,
        'EstimasiGaji': gaji
        }
    
    kolom = list(data.keys())
    
    df_final = pd.DataFrame([data.values()],columns=kolom)
    
    # load model
    my_model = pickle.load(open('model_klasifikasi_terbaik.pkl', 'rb'))
    
    # Predict
    result = int(final_prediction(df_final, my_model))
    
    hasil = []
    if result==0:
        hasil='Tidak Beli'
    else:
        hasil='Beli'
    
    st.markdown('---'*10)
    
    st.write('<center><b><h3>Predicted Beli/Tidak= ', hasil,'</b></h3>', unsafe_allow_html=True)
           
if __name__ == '__main__':
	main() 
