import streamlit as st
import numpy as np

def main():
    st.title("배열 인덱싱과 슬라이싱")
    
    array_string = st.text_input("배열 입력:")
    
    array = np.fromstring(array_string, dtype=int, sep=",")
    st.write("입력된 배열:", array)
    
    start = st.number_input("시작 인덱스:", min_value=0, step=1, value=0)
    end = st.number_input("끝 인덱스:", min_value=0, step=1, value=len(array))
    
    sliced_array = array[start:end]
    st.write("슬라이싱 결과:", sliced_array)

if __name__ == "__main__":
    try:
        main()
    except:
        st.error("😺 값을 입력해주세요!")