import streamlit as st
import pandas as pd
import os

st.write("## Employee information")


with st.form("employee_form"):
    st.write("Employee form")
    name = st.text_input("Enter your name")

    number = st.number_input("Enter your employee number", min_value=1)

    job = st.text_input("Enter your job")

    departmnet_number = st.number_input(
        "Enter your department number", min_value=1, max_value=10)
    submitted = st.form_submit_button("Submit")
    if submitted:
        if (not name or not number or not job or not departmnet_number):
            st.error("Please fill all the data")
        else:
            data_frame = pd.DataFrame({"ename": [name], "enumber": [number], "ejob": [
                                      job], "dnumber": [departmnet_number]})
            if (not os.path.isfile("employee.csv")):
                data_frame.to_csv("employee.csv", index=False)
            else:
                new_data = pd.read_csv("employee.csv")
                check = list(new_data["enumber"])
                print(number in check)
                if (number in check):
                    st.error("Invalid employee number")
                else:
                    df = pd.concat([new_data, data_frame],
                                   ignore_index=True)
                    df.to_csv("employee.csv", index=False)
                    st.info("Submission sucessful")
                    table_data = df
                    st.table(df)
