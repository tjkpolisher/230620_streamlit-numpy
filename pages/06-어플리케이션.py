import streamlit as st
import numpy as np

def main():
    st.title("실생활 어플리케이션: 데이터 분석 도구")
    
    option = st.sidebar.selectbox("분석 종류", ("평균 계산", "표준 편차 계산", "배열 연산", "배열 변형", "집계 함수"))
    
    if option == "평균 계산":
        show_mean()
    elif option == "표준 편차 계산":
        show_std()
    elif option == "배열 연산":
        show_array_operation()
    elif option == "배열 변형":
        show_array_transformation()
    elif option == "집계 함수":
        show_aggregate_functions()

def show_mean():
    st.header("평균 계산")
    
    data_string = st.text_input("데이터 입력 (숫자 배열):")
    
    if st.button("계산"):
        data = np.fromstring(data_string, dtype=float, sep=",")
        mean = np.mean(data)
        
        st.write("입력된 데이터:", data)
        st.write("평균:", mean)

def show_std():
    st.header("표준 편차 계산")
    
    data_string = st.text_input("데이터 입력 (숫자 배열):")
    
    if st.button("계산"):
        data = np.fromstring(data_string, dtype=float, sep=",")
        std = np.std(data)
        
        st.write("입력된 데이터:", data)
        st.write("표준 편차:", std)

def show_array_operation():
    st.header("배열 연산")
    
    array1_string = st.text_input("배열 1 입력:")
    array2_string = st.text_input("배열 2 입력:")
    
    array1 = np.fromstring(array1_string, dtype=int, sep=",")
    array2 = np.fromstring(array2_string, dtype=int, sep=",")
    
    st.write("배열 1:", array1)
    st.write("배열 2:", array2)
    
    result = array1 + array2
    st.write("덧셈 결과:", result)

def show_array_transformation():
    st.header("배열 변형")
    
    array_string = st.text_input("배열 입력:")
    array = np.fromstring(array_string, dtype=int, sep=",")
    
    reshaped_array = np.reshape(array, (2, 2))
    transposed_array = np.transpose(array)
    flattened_array = np.ravel(array)
    
    st.write("입력된 배열:", array)
    st.write("재구조화된 배열:", reshaped_array)
    st.write("전치된 배열:", transposed_array)
    st.write("평탄화된 배열:", flattened_array)

def show_aggregate_functions():
    st.header("집계 함수")
    
    data_string = st.text_input("데이터 입력 (숫자 배열):")
    
    if st.button("계산"):
        data = np.fromstring(data_string, dtype=float, sep=",")
        sum_result = np.sum(data)
        mean_result = np.mean(data)
        min_result = np.min(data)
        max_result = np.max(data)
        
        st.write("입력된 데이터:", data)
        st.write("합계:", sum_result)
        st.write("평균:", mean_result)
        st.write("최솟값:", min_result)
        st.write("최댓값:", max_result)

if __name__ == "__main__":
    main()
