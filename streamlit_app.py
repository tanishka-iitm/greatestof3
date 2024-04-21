import streamlit as st
st.print("Enter 3 numbers")
float a=st.input()
float b=st.input()
float c=st.input()
if a>b:
  if a>c:
    st.print(a+" is the greatest number")
  else:
    st.print(c+" is the greatest number")
else:
  if b>c:
    st.print(b+" is the greatest number")
  else:
    st.print(c+" is the greatest number")
