# Streamlit-интерфейс
import streamlit as st
import sys
sys.path.append('..')
from src.main import HypothesisGenerator

st.set_page_config(page_title="Генератор гипотез Норникель", layout="wide")
st.title("🧪 Генератор гипотез Норникель")

problem = st.text_area("Проблема", height=100)
constraints = st.text_area("Ограничения", height=100)

if st.button("🚀 Сгенерировать гипотезы"):
    if problem and constraints:
        with st.spinner("Генерация..."):
            generator = HypothesisGenerator()
            result = generator.generate(problem, constraints)
            st.json(result)
    else:
        st.warning("Заполните все поля")
