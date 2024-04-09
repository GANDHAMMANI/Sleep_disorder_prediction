import pickle as pkl 
import streamlit as st
import numpy as np
import time
import random


st.set_page_config(page_title="Sleep Predictor", page_icon="🏥", layout='wide', initial_sidebar_state="collapsed")

# Define mappings and other necessary data
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

# Load model function
def load_model(modelfile):
    loaded_model = pkl.load(open(modelfile, 'rb'))
    return loaded_model

# Streamed response emulator
def response_generator(user_input):
    custom_responses = {
        "greeting": ["Hello!", "Hi there!", "Hey, how can I help you?"],
        "farewell": ["Goodbye!", "See you later!", "Take care!"],
        "thanks": ["You're welcome!", "No problem!", "Glad I could help!"]
    }
    
    if  "hi"   in user_input.lower():
        return random.choice(custom_responses["greeting"])
    elif "bye" in user_input.lower():
        return random.choice(custom_responses["farewell"])
    elif "thank" in user_input.lower():
        return random.choice(custom_responses["thanks"])
    elif "result" in user_input.lower() and "correct" in user_input.lower():
        return "Yes, of course. The machine learning model has been trained with 89% accuracy."
    elif "insomnia" in user_input.lower():
        return "Insomnia is a sleep disorder that makes it difficult for a person to fall asleep or stay asleep. It can have various causes and treatments. It's important to consult a healthcare professional if you're experiencing insomnia regularly."
    elif "apnea" in user_input.lower():
        return "Sleep apnea is a sleep disorder characterized by pauses in breathing or shallow breaths during sleep. It can lead to disrupted sleep and daytime fatigue. There are different types of sleep apnea, including obstructive sleep apnea and central sleep apnea. Treatment options may include lifestyle changes, breathing devices, or surgery. If you suspect you have sleep apnea, it's important to seek medical advice for proper diagnosis and treatment."
    elif "develop" in user_input.lower():
        return "The  application was build by Gandham Mani Saketh, using Python ,Machine Learning, Streamlit Web-Framework & HTML& CSS"
    elif "application" in user_input.lower():
        return "The  application was build by Mani Saketh, which aims to assist users in identifying potential sleep disorders such as Insomnia and Apnea. By analyzing user input and patterns, Astra provides personalized guidance and encourages users to seek medical advice if necessary."
    elif "purpose" in user_input.lower():
        return "The purpose of our application is to raise awareness about sleep disorders and empower users to take proactive steps towards better sleep health. By leveraging AI technology and healthcare insights, we aim to help individuals identify potential sleep issues and seek appropriate support."
    elif "yourself" in user_input.lower():
        return "My name manu and i am the virtual assistant chat bot i build by the same creater of the application that you are using.. if want any assistence feel free to ask i would try my best to assist you"
    elif "benefits" in user_input.lower():
        return "Some benefits of our application include early detection of sleep disorders, personalized guidance based on user input, and promoting proactive healthcare management. By empowering users with information and support, we aim to improve overall sleep health and well-being."
    elif "accuracy" in user_input.lower():
        return "Our application utilizes machine learning algorithms, including Naïve Bayes, Random Forest, and XGBoost, to achieve high accuracy in predicting sleep disorders. Through rigorous testing and validation, we selected Random forest classifoer where have ensured that our models provide reliable results."
    elif "data collection" in user_input.lower():
        return "We collected data for training our models from various sources, including Kaggle datasets and real-world data obtained through surveys. The dataset encompasses diverse demographics and sleep-related attributes, enabling robust model training and evaluation."
    elif "user interface" in user_input.lower():
        return "Our application features a user-friendly chat-style interface, allowing seamless interaction between users and the chatbot. The interface is designed to be intuitive and accessible, facilitating easy communication and engagement with Astra."
    elif "privacy" in user_input.lower():
        return "Privacy and data security are paramount concerns in our application. We adhere to strict data protection protocols and comply with relevant privacy regulations to safeguard user information. Any data collected is anonymized and used solely for improving our services."
    elif "limitations" in user_input.lower():
        return "While our application strives to provide accurate insights, it's important to note its limitations. The  guidance  given by the application should not substitute professional medical advice, and users with serious sleep concerns should consult healthcare professionals for proper diagnosis and treatment."
    elif "future development" in user_input.lower():
        return "We are continuously working on enhancing our application's capabilities and expanding its features. Future developments may include integrating additional machine learning models, incorporating user feedback for improvement, and extending support for a wider range of sleep disorders."
    else:
        return "I'm sorry, but I'm not sure how to respond to that question. Could you please ask something else?"


def footer():
    # Footer Section
    st.markdown('<style>div.block-container{padding-bottom: 100px;,text-align: center;}</style>', unsafe_allow_html=True)
    st.markdown("""
        <p  
        align='center'>Developed by </p>
        """, unsafe_allow_html=True)
    st.markdown("""
        <p  
        align='center'>Gandham Mani Saketh</p>
        """, unsafe_allow_html=True)

   
    st.markdown(""" <p align="center">If you want any assistances go to the sidebar where there is an virtual assistant. </p>
                    <p align="center">If you like my work, connect me at !</p>
          <p align="center">
        <a href="https://www.linkedin.com/in/gandhammanisaketh2421/" target="_blank">
            <img src="https://img.icons8.com/fluent/48/000000/linkedin.png" alt="LinkedIn" style="width:40px;"/>
        </a>
        <a href="https://github.com/GANDHAMMANI" target="_blank">
            <img src="https://img.icons8.com/fluent/48/000000/github.png" alt="GitHub" style="width:40px;"/>
        </a>
        <a href="mailto:gandhammani2421@gmail.com" target="_blank">
            <img src="https://img.icons8.com/fluent/48/000000/gmail.png" alt="GitHub" style="width:40px;"/>
        </a>
        <a href="https://www.instagram.com/mr.pandapal/">
            <img src="https://img.icons8.com/fluent/48/000000/instagram-new.png" alt="Instagram" style="width: 40px;">
        </a>
    </p>
""", unsafe_allow_html=True)
    st.markdown("""  <p align="center"> -Saketh07</p>""", unsafe_allow_html=True)


# Main function
def main():
    col1, col2 = st.columns(2)
    col1.title('Sleep Health Tracker')
    col1.caption('### RestAssured: Your Sleep Wellness Companion')
    col1.markdown("""
            <div style="text-align: justify;">
            This is an machine learning application which the Interface is developed with "Streamlit". Designed  to predict the presence of a sleep disorder
            based on various input features. It is essential to know that whether your are having any disorder or not cause if you neglect some changes in 
            your health it might lead to some dangerous health issues which you will suffer a lot. 
            So, definitely later you will regret that I should have taken more care about my health  after getting into some serious condition  


            </div>
            """, unsafe_allow_html=True)

    col2.image('sleep_disorder.png', use_column_width=False, width=300)


    st.sidebar.title('Virtual Assistant' )
    st.sidebar.caption('Hey there feel free to ask anything about the application only 😅 ')

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.sidebar:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    # Accept user input
    if prompt := st.sidebar.chat_input("ask for any assistence "):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.sidebar.chat_message("user"):
            st.markdown(prompt)

        # Get assistant response
        assistant_response = response_generator(prompt)
        with st.sidebar.chat_message("assistant"):
            words = assistant_response.split()
            combined_words = ' '.join(words)
            st.markdown(combined_words)
            
                         # Add delay between each word

        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})

        # the main part of the application begins here
    col1, col2 = st.columns([2, 2])

    with col1:
        st.header('How does it work ❓') 
        st.info('Fill the details shown then the Model  will give you the prediction based on your details🥼.As this Machine Learning model has been trained with more data previously ')
        st.subheader(" Find out How is your health is? 🩺")
        name = col1.text_input("Enter Your Name:")
        Gender = col1.selectbox("Select a Gender", list(gender_mapping.keys()))
        Age = col1.number_input("Enter your age ", 10, 100)
        Occupation = col1.selectbox("Select an Occupation", list(occupation_mapping.keys()))
        Sleep_Duration = col1.number_input("Sleep Duration per Day ", 1, 20)
        Quality_of_Sleep = col1.slider("Quality of Sleep", max_value=10, min_value=1, value=2)

    with col2:
        # Reading Pickle File
        with open("sleep_disorder_prediction.pkl", "rb") as f:
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

        col2.write('    ')    
        col2.write('    ')  
        col2.write('    ')  
        col2.write('    ')  
        col2.write('    ')  
        col2.write('    ')  
        col2.write('    ')  
        Physical_Activity_Level = col2.slider("Physical Activity Level", max_value=10, min_value=1, value=2)
        Stress_Level = col2.slider("Stress Level", max_value=10, min_value=1, value=2)
        BMI_Category = col2.selectbox("Select the Body Type", list(body_type_mapping.keys()))
        Blood_Pressure = col2.selectbox("Select the Blood Pressure", list(blood_pressure_mapping.keys()))
        Heart_Rate = col2.number_input("Enter your Heart Rate ", 30, 250)

        # Prediction button
        submit_button = st.button("Predict")
        # Spinner
        spinner = st.empty()

        # Perform prediction when the button is clicked
        if submit_button:
            with spinner:
                with st.spinner(f'Processing, Please wait...'):
                    # Delay for demonstration purposes
                    time.sleep(2)

            # Perform prediction...
            result = predict(Gender, Age, Occupation, Sleep_Duration, Quality_of_Sleep, Physical_Activity_Level,
                             Stress_Level, BMI_Category, Blood_Pressure, Heart_Rate)
            sleep_disorder_result = list(sleep_disorder.keys())[list(sleep_disorder.values()).index(result)]

            # Display the result...
            if result == 1:  # If the sleep disorder is 1
                color = "green"
                st.balloons()
            else:
                color = "red"
            larger_text = f"<h2 style='color: {color};'>The Condition of your health as per your details is {sleep_disorder_result} 🛏</h2>"
            st.markdown(larger_text, unsafe_allow_html=True)
            st.warning(
                "Note: This M.L application only based on your details as our model achieved 89% accuracy. However, it's always recommended to consult a doctor for a comprehensive evaluation if you are dealing with any disorder.")

            st.subheader("Prediction Report")
            report = f"""
                Name: {name} 
                Gender: {Gender} 
                Age: {Age}
                Occupation: {Occupation} 
                Sleep Duration: {Sleep_Duration} 
                Quality of Sleep: {Quality_of_Sleep}
                Physical Activity Level: {Physical_Activity_Level}
                Stress Level: {Stress_Level}
                BMI Category: {BMI_Category}
                Blood Pressure: {Blood_Pressure} 
                Heart Rate: {Heart_Rate}

                Result: {sleep_disorder_result}

                """
          
            st.code(report, language='python')
    st.divider()
    footer()        
if __name__ == '__main__':
    main()
