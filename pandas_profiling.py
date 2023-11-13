import streamlit as st
import pandas as pd
from pandas_profiling import ProfileReport

# Function to load data
def load_data(file_path, file_format):
    if file_format == 'csv':
        return pd.read_csv(file_path)
    elif file_format == 'excel':
        return pd.read_excel(file_path)
    # Add more file formats if needed

# Function to perform EDA using pandas_profiling
def perform_eda(data):
    profile = ProfileReport(data, explorative=True)
    return profile

def main():
    st.title('Pandas Profiling in Streamlit')

    # Upload data
    st.sidebar.subheader("File Selection")

    # File format selection
    file_format = st.sidebar.selectbox("Select File Format", ['csv', 'excel'])

    # File upload
    filepath = st.sidebar.file_uploader("Upload File", type=[file_format])

    if filepath is not None:
        try:
            data = load_data(filepath, file_format)
            st.sidebar.success('Data successfully loaded!')
            st.write(data.head())
        except Exception as e:
            st.error(f"Error: {str(e)}")
            return

        if st.button('Generate EDA Report'):
            eda_report = perform_eda(data)
            st_profile_report(eda_report)

if __name__ == '__main__':
    main()
