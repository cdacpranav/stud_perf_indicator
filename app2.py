import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

def main():
    st.set_page_config(page_title="Prediction App", layout="centered")

    # Title of the app
    st.title("Prediction App")
    st.write("Fill in the details below and get predictions instantly.")

    # Input fields
    gender = st.selectbox("Gender", ["Male", "Female"])
    race_ethnicity = st.selectbox("Race/Ethnicity", ["Group A", "Group B", "Group C", "Group D", "Group E"])
    parental_level_of_education = st.selectbox(
        "Parental Level of Education",
        [
            "Some high school",
            "High school",
            "Some college",
            "Associate's degree",
            "Bachelor's degree",
            "Master's degree",
        ],
    )
    lunch = st.selectbox("Lunch Type", ["Standard", "Free/reduced"])
    test_preparation_course = st.selectbox(
        "Test Preparation Course", ["None", "Completed"]
    )
    reading_score = st.number_input(
        "Reading Score", min_value=0, max_value=100, value=50, step=1
    )
    writing_score = st.number_input(
        "Writing Score", min_value=0, max_value=100, value=50, step=1
    )

    # Predict button
    if st.button("Predict"):
        # Collect the data
        data = CustomData(
            gender=gender,
            race_ethnicity=race_ethnicity,
            parental_level_of_education=parental_level_of_education,
            lunch=lunch,
            test_preparation_course=test_preparation_course,
            reading_score=reading_score,
            writing_score=writing_score,
        )

        pred_df = data.get_data_as_data_frame()
        st.write("Input Data:")
        st.dataframe(pred_df)

        # Make predictions
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)

        # Display results
        st.success(f"Predicted Result: {round(results[0], 2)}")

if __name__ == "__main__":
    main()
