#!/usr/bin/env python
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    st.title("Machine Learning web App")
    st.header("This WebApp was created for solve your Machine Learning problem")
    st.subheader("Import your csv file")
    st.file_uploader("Choose your file", type = 'csv')

    radio = st.sidebar.radio('Select the type of your problem',("Regression", "Classification"))
    if radio == "Regression":
        st.markdown("Reg problem")
    if radio == "Classification":
        st.markdown("Classification problem")


if __name__ == '__main__':
    main()
