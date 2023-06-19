import streamlit as st
import numpy as np

def main():
    st.title("1차원 배열 생성하기")
    
    size = st.number_input("배열 크기:", min_value=1, step=1)
    
    if st.button("배열 생성"):
        array = np.arange(size)
        st.write("생성된 배열:", array)

if __name__ == "__main__":
    try:
        main()
    except:
        st.error("😺 값을 입력해주세요!")