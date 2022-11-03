# -*- coding: utf-8 -*-

import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
from joblib import load

st.set_page_config(layout="wide")
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
# loading the saved models

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Medical assistant',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction',
                           'Symtom to disease'],
                          icons=['activity','heart','person','person',],
                          default_index=0)
if (selected == 'Kideny'):
    
    # page title
    st.title('Kidney')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'Diabetic'
        else:
          diab_diagnosis = 'Not diabetic'
        
    st.success(diab_diagnosis)   

if (selected=="Symtom to disease"):
    a=[0]*132
 
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        a[0]=st.checkbox('itching')
        a[1]=st.checkbox('skin_rash')
        a[2]=st.checkbox('nodal_skin_eruptions')
        a[3]=st.checkbox('continuous_sneezing')
        a[4]=st.checkbox('shivering')
        a[5]=st.checkbox('chills')
        a[6]=st.checkbox('joint_pain')
        a[7]=st.checkbox('stomach_pain')
        a[8]=st.checkbox('acidity')
        a[9]=st.checkbox('ulcers_on_tongue')
        a[10]=st.checkbox('muscle_wasting')
        a[11]=st.checkbox('vomiting')
        a[12]=st.checkbox('burning_micturition')
        a[13]=st.checkbox('spotting_ urination')
        a[14]=st.checkbox('fatigue')
        a[15]=st.checkbox('weight_gain')
        a[16]=st.checkbox('anxiety')
        a[17]=st.checkbox('cold_hands_and_feets')
        a[18]=st.checkbox('mood_swings')
        a[19]=st.checkbox('weight_loss')
        a[90]=st.checkbox('foul_smell_of urine')
        
    with col2:
        a[24]=st.checkbox('cough')
        a[25]=st.checkbox('high_fever')
        a[26]=st.checkbox('sunken_eyes')
        a[27]=st.checkbox('breathlessness')
        a[28]=st.checkbox('sweating')
        a[29]=st.checkbox('dehydration')
        a[30]=st.checkbox('indigestion')
        a[31]=st.checkbox('headache')
        a[32]=st.checkbox('yellowish_skin')
        a[33]=st.checkbox('dark_urine')
        a[34]=st.checkbox('nausea')
        a[35]=st.checkbox('loss_of_appetite')
        a[36]=st.checkbox('pain_behind_the_eyes')
        a[37]=st.checkbox('back_pain')
        a[38]=st.checkbox('constipation')
        a[39]=st.checkbox('abdominal_pain')
        a[40]=st.checkbox('diarrhoea')
        a[41]=st.checkbox('mild_fever')
        a[42]=st.checkbox('yellow_urine')
        a[43]=st.checkbox('yellowing_of_eyes')
        a[44]=st.checkbox('acute_liver_failure')
        
        
    with col3:
        a[46]=st.checkbox('swelling_of_stomach')
        a[47]=st.checkbox('swelled_lymph_nodes')
        a[48]=st.checkbox('malaise')
        a[49]=st.checkbox('blurred_and_distorted_vision')
        a[50]=st.checkbox('phlegm')
        a[51]=st.checkbox('throat_irritation')
        a[52]=st.checkbox('redness_of_eyes')
        a[53]=st.checkbox('sinus_pressure')
        a[54]=st.checkbox('runny_nose')
        a[55]=st.checkbox('congestion')
        a[56]=st.checkbox('chest_pain')
        a[57]=st.checkbox('weakness_in_limbs')
        a[58]=st.checkbox('fast_heart_rate')
        a[59]=st.checkbox('pain_during_bowel_movements')
        a[60]=st.checkbox('pain_in_anal_region')
        a[61]=st.checkbox('bloody_stool')
        a[62]=st.checkbox('irritation_in_anus')
        a[63]=st.checkbox('neck_pain')
        a[64]=st.checkbox('dizziness')
        a[65]=st.checkbox('cramps')
        a[66]=st.checkbox('bruising')
        
        
    with col4:
        a[69]=st.checkbox('swollen_blood_vessels')
        a[70]=st.checkbox('puffy_face_and_eyes')
        a[71]=st.checkbox('enlarged_thyroid')
        a[72]=st.checkbox('brittle_nails')
        a[73]=st.checkbox('swollen_extremeties')
        a[74]=st.checkbox('excessive_hunger')
        a[75]=st.checkbox('extra_marital_contacts')
        a[76]=st.checkbox('drying_and_tingling_lips')
        a[77]=st.checkbox('slurred_speech')
        a[78]=st.checkbox('knee_pain')
        a[79]=st.checkbox('hip_joint_pain')
        a[80]=st.checkbox('muscle_weakness')
        a[81]=st.checkbox('stiff_neck')
        a[82]=st.checkbox('swelling_joints')
        a[83]=st.checkbox('movement_stiffness')
        a[84]=st.checkbox('spinning_movements')
        a[85]=st.checkbox('loss_of_balance')
        a[86]=st.checkbox('unsteadiness')
        a[87]=st.checkbox('weakness_of_one_body_side')
        a[88]=st.checkbox('loss_of_smell')
        a[89]=st.checkbox('bladder_discomfort')
        
        
    with col5:
        a[91]=st.checkbox('continuous_feel_of_urine')
        a[92]=st.checkbox('passage_of_gases')
        a[120]=st.checkbox('palpitations')
        a[121]=st.checkbox('painful_walking')
        a[122]=st.checkbox('pus_filled_pimples')
        a[123]=st.checkbox('blackheads')
        a[124]=st.checkbox('scurring')
        a[125]=st.checkbox('skin_peeling')
        a[126]=st.checkbox('silver_like_dusting')
        a[127]=st.checkbox('small_dents_in_nails')
        a[128]=st.checkbox('inflammatory_nails')
        a[129]=st.checkbox('blister')
        a[130]=st.checkbox('red_sore_around_nose')
        a[131]=st.checkbox('yellow_crust_ooze')
        a[20]=st.checkbox('restlessness')
        a[21]=st.checkbox('lethargy')
        a[22]=st.checkbox('patches_in_throat')
        a[23]=st.checkbox('irregular_sugar_level')
        a[45]=st.checkbox('fluid_overload')
        a[67]=st.checkbox('obesity')
        a[68]=st.checkbox('swollen_legs')
    if sum(a)==0:
        st.metric(label="Disease", value="No disease selected")

    else:
        
        ref=['itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 'chills', 'joint_pain', 'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting', 'vomiting', 'burning_micturition', 'spotting_ urination', 'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets', 'mood_swings', 'weight_loss', 'restlessness', 'lethargy', 'patches_in_throat', 'irregular_sugar_level', 'cough', 'high_fever', 'sunken_eyes', 'breathlessness', 'sweating', 'dehydration', 'indigestion', 'headache', 'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes', 'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine', 'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach', 'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs', 'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips', 'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints', 'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine', 'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain', 'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes', 'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum', 'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion', 'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen', 'history_of_alcohol_consumption', 'fluid_overload.1', 'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose', 'yellow_crust_ooze']
        df_test = pd.DataFrame(columns=ref)
        df_test.loc[0] = np.array(a)
        clf = load(("random_forest.joblib"))
        
        result = clf.predict(df_test)
        st.metric(label="Disease", value=result[0])


        #st.subheader(result[0])

# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'Diabetic'
        else:
          diab_diagnosis = 'Not diabetic'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal:0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)


