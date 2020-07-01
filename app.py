#!/usr/bin/env python
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# @st.cache(persist = True)
def load_data(csv_file):
    df = pd.read_csv(csv_file)
    return df


@st.cache(persist=True)
def print_stats(data):
    df = pd.DataFrame({'Missing': data.isna().sum(),
                       'Cardinality': data.nunique(),
                       'Type': data.dtypes})
    return df.sort_values('Type')


def input_cat_values(data):
    obj_cols = data.select_dtypes('object').columns.to_list()
    data[obj_cols] = data[obj_cols].fillna(data[obj_cols].mode().iloc[0])

    return data


def input_num_values(data):
    num_cols = data.select_dtypes(exclude=['object']).columns.to_list()
    data[num_cols] = data[num_cols].fillna(data[num_cols].mode().iloc[0])

    return data


def cat_to_num(data):
    for col in data:
        data[col] = col.astype('float32')
    return data


def change_types(df, cols):
    df[cols] = df[cols].astype(np.float32)
    return df


def main():
    st.title("Machine Learning web App")
    st.header("This WebApp was created for solve your Machine Learning problem")
    st.subheader("Import your csv file")

    file = st.file_uploader("Choose your file", type='csv')
    if file is not None:
        df = load_data(file)
        st.write(df)
        st.header("Data Cleansing and Basic Statistics of your Data")
        st.write(print_stats(df))
        if df.isnull().sum().sum() > 0:
            st.subheader("The Dataset have Missing Values. Presse the button below to handle with them")
            missing = st.selectbox('Select columns type to input', ('Categorical', 'Numeric'))
            if missing == 'Categorical':
                input = st.button("Press to input")
                if input:
                    df = input_cat_values(df)
                    st.write(print_stats(df))

            if missing == 'Numeric':
                input = st.button("Press to input")
                if input:
                    df = input_num_values(df)
                    st.write(print_stats(df))
        cols = df.columns.to_list()
        change = st.multiselect("Select Cols to Change Type", (cols))
        df = change_types(df, change)
        st.write(df)

    radio = st.sidebar.radio('Select the type of your problem', ("Regression", "Classification"))
    if radio == "Regression":
        st.sidebar.markdown("Reg problem")
    if radio == "Classification":
        st.sidebar.markdown("Classification problem")


if __name__ == '__main__':
    main()
