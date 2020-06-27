#!/usr/bin/env python
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

@st.cache(persist = True)
def load_data(csv_file):
    df = pd.read_csv(csv_file)
    return df

def print_missing_values(dataframe):
    df = pd.DataFrame({'Missing': dataframe.isna().sum()})
    st.write(df)

def main():
    st.title("Machine Learning web App")
    st.header("This WebApp was created for solve your Machine Learning problem")
    st.subheader("Import your csv file")

    file = st.file_uploader("Choose your file", type = 'csv')
    if file is not None:
        df = load_data(file)

    st.write(df)

    st.header("Data Cleansing and Basic Statistics of your Data")
    stats = st.selectbox("Select the  Statitics", ("% Missing Values", "Type", "Cardinality"))
    if stats == "% Missing Values":
        print_missing_values(df)



    radio = st.sidebar.radio('Select the type of your problem',("Regression", "Classification"))
    if radio == "Regression":
        st.sidebar.markdown("Reg problem")
    if radio == "Classification":
        st.sidebar.markdown("Classification problem")


if __name__ == '__main__':
    main()
