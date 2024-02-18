# Mengimpor library
import pandas as pd
import streamlit as st
import pickle

# Menghilangkan warning
import warnings
warnings.filterwarnings("ignore")

# Menulis judul
st.markdown("<h1 style='text-align: center; '> Attrition Prediction </h1>", unsafe_allow_html=True)
st.markdown('---'*10)

# Load model
my_model = pickle.load(open('model_klasifikasi_terbaik.pkl', 'rb'))

# Pilihan utama

pilihan = st.selectbox('Apa yang ingin Anda lakukan?',['Prediksi dari file csv','Input Manual'])

if pilihan == 'Prediksi dari file csv':
    # Mengupload file
    upload_file = st.file_uploader('Pilih file csv', type='csv')
    if upload_file is not None:
        dataku = pd.read_csv(upload_file)
        st.write(dataku)
        st.success('File berhasil diupload')
        hasil = my_model.predict(dataku)
        #st.write('Prediksi',hasil)
        # Keputusan
        for i in range(len(hasil)):
            if hasil[i] == 1:
                st.write('Attrition',dataku['Attrition'][i],'= diprediksi akan KELUAR PERUSAHAAN')
            else:
                st.write('Attrition',dataku['Attrition'][i],'= diprediksi akan KELUAR PERUSAHAAN')
    else:
        st.error('File yang diupload kosong, silakan pilih file yang valid')
        #st.markdown('File yang diupload kosong, silakan pilih file yang valid')
else:
   # Baris Pertama
    with st.container():
        col1, col2 = st.columns(2)
    with col1:
        age = st.number_input('Age', value=25)
    with col2:
        business_travel = st.selectbox('Business Travel', ['1', '2', '3'])     
   # Baris Kedua
    with st.container():
        col1, col2 = st.columns(2)
    with col1:
        DistanceFromHome = st.number_input('Distance From Home', value=5)
    with col2:
        Education = st.selectbox('Education', ['1', '2', '3','4','5'])

   # Baris Ketiga
    with st.container():
       col1, col2, col3 = st.columns(3)
    with col1:
       EnvironmentSatisfaction = st.selectbox('Satisfaction', ['1', '2', '3','4'])
    with col2:
       JobInvolvement = st.selectbox('Involvement', ['1', '2', '3','4'])        
    with col3:
       JobLevel = st.selectbox('Level',['1', '2', '3','4','5'])        
   # Baris Keempat
    with st.container():
        col1, col2, col3 = st.columns(3)
    with col1:
        MaritalStatus = st.selectbox('Marital Status',['Single', 'Married', 'Divorced'])    
    with col2:
        MonthlyIncome = st.number_input('Monthly Income', value=10000.0)
    with col3:
        EducationField = st.selectbox('EducationField',['Human Resources', 'Life Sciences', 'Marketing','Medical', 'Other', 'Technical Degree'])
       
   # Baris Kelima
    with st.container():
        col1, col2, col3 = st.columns(3)
    with col1:
        TotalWorkingYears = st.number_input('Total Working Years', value=5)
    with col2:
        YearsAtCompany = st.number_input('Years At Company', value=5) 
    with col3:
        OverTime = st.selectbox('EducationField',['Yes', 'No'])

   # Inference
    data = {
           'Loan ID': loan_id,
           'Customer ID': customer_id,
           'Term': term,
           'Years in current job': years_in_current_job,
           'Home Ownership': home_ownership,
           'Purpose': purpose,
           'Bankruptcies': bankruptcies,
           'Current Loan Amount': current_loan_amount, 
           'Credit Score': credit_score,
           'Annual Income': annual_income,
           'Monthly Debt': monthly_debt,
           'Years of Credit History': years_of_credit_history,
           'Months since last delinquent': months_since_last,
           'Number of Open Accounts': number_of_open_accounts,
           'Number of Credit Problems': number_of_credit_problems,
           'Current Credit Balance': current_credit_balance,
           'Maximum Open Credit': maximum_open_credit,
           'Tax Liens': tax_liens        
           }

   # Tabel data
    kolom = list(data.keys())
    df = pd.DataFrame([data.values()], columns=kolom)
   
   # Melakukan prediksi
    hasil = my_model.predict(df)
    hasil_proba = my_model.predict_proba(df)
    keputusan1 = round(float(hasil_proba[:,0])*100,2)
    keputusan2 = round(float(hasil_proba[:,1])*100,2)


   # Memunculkan hasil di Web 
    st.write('***'*10)
    st.write('<center><b><i><u><h3>Customer Loan ID', str(loan_id),'</b></i></u></h3>', unsafe_allow_html=True)
    st.write('<center><b><h4>Probabilitas bisa membayar = ', str(keputusan1),'%</b></h4>', unsafe_allow_html=True)
    st.write('<center><b><h4>Probabilitas gagal bayar = ', str(keputusan2),'%</b></h4>', unsafe_allow_html=True)
