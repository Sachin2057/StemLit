import streamlit as st
import os
import pandas as pd
import numpy as np

st.write("# Output Page")


if (os.path.exists("employee.csv") and os.path.exists("department.csv")):
    st.write("Employee information")
    df_employee = pd.read_csv("employee.csv")
    df_department = pd.read_csv("department.csv")
    df = pd.merge(df_employee, df_department, on="dnumber")
    df = df.drop(labels=["ejob", "dlocation"], axis=1)
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    st.table(df)
else:
    st.warning("Please fill both forms")
