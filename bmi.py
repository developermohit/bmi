import streamlit as st
st.title("BMI Calculator")
name=st.text_input("Enter your name")
weight=st.number_input("Enter your weight(kg)",min_value=1.0,max_value=200.0,value=60.0)
height=st.number_input("Enter your height(m)",min_value=0.5,max_value=2.5,value=1.65)
if st.button("calculate bmi"):
    bmi=weight/(height**2)
    st.write(f"Hello,{name}")
    st.metric("your BMI",round(bmi,2))
    if bmi<18.5:
       st.warning("underweight")
    if bmi<25:
       st.success("normal weight")
    if bmi<30:
       st.warning("Overweight")
    else:
       st.error("Obesity")