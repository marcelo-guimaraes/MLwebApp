#!/usr/bin/env python
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

@st.cache(persist = True)
def load_data(csv_file):
    df = pd.read_csv(csv_file)
    return df

@st.cache(persist = True)
def print_stats(data):
    df = pd.DataFrame({'Missing': data.isna().sum(),
                       'Cardinality': data.nunique(),
                       'Type': data.dtypes})
    return df.sort_values('Type')

def input_values(data):
    obj_cols = data.select_dtypes('object').to_list()
    num_cols = data.select_dtypes(exclude=['object']).to_list()
    data[obj_cols] = data[obj_cols].fillna(data[obj_cols].mode().iloc[0])
    data[num_cols] = data[num_cols].fillna(data[num_cols].mode().iloc[0])

    return data

def main():
    st.title("Machine Learning web App")
    st.header("This WebApp was created for solve your Machine Learning problem")
    st.subheader("Import your csv file")

    file = st.file_uploader("Choose your file", type = 'csv')
    if file is not None:
        df = load_data(file)
        st.write(df)
        st.header("Data Cleansing and Basic Statistics of your Data")
        st.write(print_stats(df))
        if df.isnull().sum().sum() > 0:
            st.subheader("The Dataset have Missing Values. Presse the button below to handle with them")
            missing = st.button('Input values based on the mode')
            if missing:
                df = input_values(df)
                st.markdown("Done!!")



    radio = st.sidebar.radio('Select the type of your problem',("Regression", "Classification"))
    if radio == "Regression":
        st.sidebar.markdown("Reg problem")
    if radio == "Classification":
        st.sidebar.markdown("Classification problem")


if __name__ == '__main__':
    main()
