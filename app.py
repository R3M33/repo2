import streamlit as st

st.header('tossing a Coin')

st.write('it is not a functional application yet. Under construction.')

checkbox = st.checkbox("too expensive")

if checkbox:
    st.write("Check, this car is over 50k. Too much")

#Next step is making the check box check off cars that cost more than 50k and then step 3