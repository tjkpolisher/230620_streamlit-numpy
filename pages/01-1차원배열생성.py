import streamlit as st
import numpy as np

def main():
    st.title("1차원 배열 생성하기")
    
    size = st.number_input("배열 크기:", min_value=1, step=1) # 배열 크기 입력, 최소값 1, 간격 1
    
    if st.button("배열 생성"): # 배열 생성 버튼을 눌렀을 경우
        array = np.arange(size) # 입력받은 size를 인수로 arange 메서드 호출
        st.write("생성된 배열:", array) # 생성된 배열 출력

if __name__ == "__main__":
    try:
        main()
    except:
        st.error("😺 값을 입력해주세요!") # 값을 입력받지 않았을 경우 예외 처리