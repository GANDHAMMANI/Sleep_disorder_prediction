import pickle as pkl 
import streamlit as st
import numpy as np
import sklearn

st.set_page_config(page_title="Sleep Predictor", page_icon="🏥", layout='wide', initial_sidebar_state="collapsed")

gender_mapping = {
    "Female": 0,
    "Male": 1
}

occupation_mapping = {
    "Accountant": 0,
    "Doctor": 1,
    "Engineer": 2,
    "Lawyer": 3,
    "Manager": 4,
    "Nurse": 5,
    "Sales Representative": 6,
    "Salesperson": 7,
    "Scientist": 8,
    "Software Engineer": 9,
    "Teacher": 10
}

body_type_mapping = {
    "Normal": 0,
    "Normal Weight": 1,
    "Obese": 2,
    "Overweight": 3,
}

blood_pressure_mapping = {
    "115/75": 0,
    "115/78": 1,
    "117/76": 2,
    "118/75": 3,
    "118/76": 4,
    "119/77": 5,
    "120/80": 6,
    "121/79": 7,
    "122/80": 8,
    "125/80": 9,
    "125/82": 10,
    "126/83": 11,
    "128/84": 12,
    "128/85": 13,
    "129/84": 14,
    "130/85": 15,
    "130/86": 16,
    "131/86": 17,
    "132/87": 18,
    "135/88": 19,
    "135/90": 20,
    "139/91": 21,
    "140/90": 22,
    "140/95": 23,
    "142/92": 24,
}

sleep_disorder = {
    "Insomnia": 0,
    "Your are Healthy": 1,
    "Sleep Apnea": 2
}


def load_model(modelfile):
    loaded_model = pkl.load(open(modelfile, 'rb'))
    return loaded_model


def main():
    col1, col2 = st.columns(2)
    col1.title('Sleep Health Tracker')
    col1.caption('### RestAssured: Your Sleep Wellness Companion')
    col1.markdown("""
            This is an machine learning application which the Interface is developed with "Streamlit". Designed  to predict the presence of a sleep disorder
            based on various input features. It is essensial to know that whether your are having any disorder or not cause if you neglect some changes in 
            your health it might lead to some dangerous health issues whcih you will suffer a lot. 
            So, definetly later you will regret that i should have taken more care about my health  after getting into some serious condition  
            """)
    col2.image('sleep_disorder.png', use_column_width=False, width=300)

    st.divider()

    col1, col2 = st.columns([2, 2])

    with col1:

        '''
        ## How does it work ❓ 
        Fill the details shown then the Model  will give you the prediction based on your details🥼.As this Machine Learning model has been trained with more data previously  
        '''
        st.subheader(" Find out How is your health is? 🩺")
        Gender = col1.selectbox("Select a Gender", list(gender_mapping.keys()))
        Age = col1.number_input("Enter your age ", 10, 100)
        Occupation = col1.selectbox("Select an Occupation", list(occupation_mapping.keys()))
        Sleep_Duration = col1.number_input("Sleep Duration per Day ", 1, 20)
        Quality_of_Sleep = col1.slider("Quality of Sleep", max_value=10, min_value=1, value=2)

    with col2:

        # Reading Pickle File
        with open("sleep_disorder_pred_RF.pickle", "rb") as f:
            model = pkl.load(f)

        # Function to predict sleep disorder
        def predict(gender, Age, Occupation, Sleep_Duration, Quality_of_Sleep, Physical_Activity_Level, Stress_Level,
                    BMI_Category, Blood_Pressure, Heart_Rate):
            selected_gender = gender_mapping[gender]
            selected_occupation = occupation_mapping[Occupation]
            selected_body_type = body_type_mapping[BMI_Category]
            selected_blood_pressure = blood_pressure_mapping[Blood_Pressure]
            input_data = np.array(
                [[selected_gender, Age, selected_occupation, Sleep_Duration, Quality_of_Sleep, Physical_Activity_Level,
                  Stress_Level, selected_body_type, selected_blood_pressure, Heart_Rate]])
            return model.predict(input_data)[0]

        col2.text('     ')
        col2.text("    ")
        col2.text('     ')
        col2.text("    ")
        col2.text('     ')
        col2.text("    ")
        col2.text('     ')
        col2.text("    ")
        col2.text('     ')
        col2.text("    ")

        Physical_Activity_Level = col2.slider("Physical Activity Level", max_value=10, min_value=1, value=2)
        Stress_Level = col2.slider("Stress Level", max_value=10, min_value=1, value=2)
        BMI_Category = col2.selectbox("Select the Body Type", list(body_type_mapping.keys()))
        Blood_Pressure = col2.selectbox("Select the Blood Pressure", list(blood_pressure_mapping.keys()))
        Heart_Rate = col2.number_input("Enter your Heart Rate ", 30, 250)

        # predicting result    
        result = predict(Gender, Age, Occupation, Sleep_Duration, Quality_of_Sleep, Physical_Activity_Level,
                         Stress_Level, BMI_Category, Blood_Pressure, Heart_Rate)
        sleep_disorder_result = list(sleep_disorder.keys())[list(sleep_disorder.values()).index(result)]
        submit_button = st.button("Predict")

    if submit_button:
        # Color for the result text based on the sleep disorder
        if result == 1:  # If the sleep disorder is 1
            color = "green"
            st.balloons()
        else:
            color = "red"

        # HTML string for displaying the result with the specified color
        larger_text = f"<h2 style='color: {color};'>The Condition of your health as per your details is {sleep_disorder_result} 🛏</h2>"
        st.markdown(larger_text, unsafe_allow_html=True)
        st.warning(
            "Note: This M.L application only based on your details as our model achieved 89% accuracy. However, it's always recommended to consult a doctor for a comprehensive evaluation if you are dealing with any disorder.")
        hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
        st.markdown(hide_menu_style, unsafe_allow_html=True)
        
        


hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
