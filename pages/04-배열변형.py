import streamlit as st
import numpy as np

def main():
    st.title("배열 변형")
    
    array_string = st.text_input("배열 입력:")
    array = np.fromstring(array_string, dtype=int, sep=",")
    
    reshaped_array = np.reshape(array, (2, 2))
    transposed_array = np.transpose(array)
    flattened_array = np.ravel(array)
    
    st.write("입력된 배열:", array)
    st.write("재구조화된 배열:", reshaped_array)
    st.write("전치된 배열:", transposed_array)
    st.write("평탄화된 배열:", flattened_array)

if __name__ == "__main__":
    main()
