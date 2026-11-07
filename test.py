import streamlit as st

st.title("This is DK's first streamlit application")
st.write("Hello! Welcome to Streamlit.")

city = st.selectbox("Choose your city", ["Chennai","Bangalore", "Hyderabad", "Pune","Delhi", "Mumbai"])
st.write("You selected:", city)

# Checkbox
agree = st.checkbox("I agree to the terms")
if agree:
    st.write("Thank you for agreeing!")

    
st.success("This is a success message (green).")
st.info("This is an info message (blue).")
st.warning("This is a warning message (yellow).")
st.error("This is an error message (red).")