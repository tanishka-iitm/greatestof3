import streamlit as st
print("Enter 3 numbers")
a=input()
b=input()
c=input()
if a>b:
  if a>c:
    print(a+" is the greatest number")
  else:
    print(c+" is the greatest number")
else:
  if b>c:
    print(b+" is the greatest number")
  else:
    print(c+" is the greatest number")
