import streamlit as st
import numpy as np
import random

def main():
    st.title("로또 번호 추천 프로그램")

    num_count = st.number_input("로또 번호 개수:", min_value=1, step=1)
    num_range = st.number_input("로또 번호 범위:", min_value=1, step=1)

    if st.button("번호 추천"):
        recommended_numbers = generate_lotto_numbers(num_count, num_range)
        st.write("추천된 번호:", recommended_numbers)

def generate_lotto_numbers(num_count, num_range):
    numbers = np.arange(1, num_range+1)
    recommended_numbers = random.sample(list(numbers), num_count)
    return recommended_numbers

if __name__ == "__main__":
    main()
