import streamlit as st 

if "v" not in st.session_state:
     st.session_state.v=0
def incre():
     st.session_state.v+=1
     return st.session_state.v

def decr():
     st.session_state.v-=1
     return st.session_state.v


b=st.button("increment")
b1=st.button("decrement")

if b:
     st.write(incre())

if b1:
     st.write(decr())
