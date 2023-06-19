import streamlit as st
import numpy as np

def main():
    st.title("배열 연산과 집계 함수")
    
    array_string = st.text_input("배열 입력:")
    array = np.fromstring(array_string, dtype=int, sep=",")
    
    sum_result = np.sum(array)
    mean_result = np.mean(array)
    min_result = np.min(array)
    max_result = np.max(array)
    
    st.write("입력된 배열:", array)
    st.write("합계:", sum_result)
    st.write("평균:", mean_result)
    st.write("최솟값:", min_result)
    st.write("최댓값:", max_result)

if __name__ == "__main__":
    main()
