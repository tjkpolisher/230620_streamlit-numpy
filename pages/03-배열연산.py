import streamlit as st
import numpy as np

def main():
    st.title("배열 연산")
    
    array1_string = st.text_input("배열 1 입력:")
    array2_string = st.text_input("배열 2 입력:")
    
    array1 = np.fromstring(array1_string, dtype=int, sep=",")
    array2 = np.fromstring(array2_string, dtype=int, sep=",")
    
    st.write("배열 1:", array1)
    st.write("배열 2:", array2)
    
    result = array1 + array2
    st.write("덧셈 결과:", result)

if __name__ == "__main__":
    try:
        main()
    except:
        st.error("😺 값을 입력해주세요!")