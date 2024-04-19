import os
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Department Information"
)
with st.form("department_form"):
    departmnet_number = st.number_input(
        "Enter department number", min_value=1, max_value=10)

    departmnet_name = st.text_input("Enter deaprtmnet name")

    department_location = st.text_input("Location of department")

    submitted = st.form_submit_button("Submit")

    if submitted:
        if (not department_location or not departmnet_number or not department_location):
            st.error("Please fill all the data")
        else:
            data_frame = pd.DataFrame({
                "dname": [departmnet_name],
                "dnumber": [departmnet_number],
                "dlocation": [department_location]})
            if (not os.path.isfile("department.csv")):
                data_frame.to_csv("department.csv", index=False)
            else:
                new_data = pd.read_csv("department.csv")

                df = pd.concat([new_data, data_frame], ignore_index=False)
                df = df.reset_index(drop=True)
                df.to_csv("department.csv")
                st.table(df)
