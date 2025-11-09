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

st.divider()
st.checkbox("i understood the terms")

st.toggle("click me")

choice=st.radio("select your fav num:",
                ["1","2","3","4","5","6","7","8","9"])

st.divider()

st.write("fav num is",choice)

city=st.selectbox("select your city:",
                  ["Hyderabad","Mumbai","Chennai","Delhi"])

colour=st.multiselect("Choose your fav colours:",
                       ["Red","Blue","Yellow","Green"])
st.write("Your selected colours are:",colour)

age=st.slider("select your age:",1,100,5)
st.write("Your age is",age)


rating = st.select_slider(
    'Rate your experience',
    options=['Poor', 'Average', 'Good', 'Excellent'])
st.write('You selected:', rating)

age_range = st.select_slider(
    'Select your age range',
    options=list(range(10, 81)),
    value=(20, 40))
st.write('You selected age range:', age_range)

name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")
