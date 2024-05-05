import time
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import backend

st.set_page_config(
    page_title="Main Page",
    page_icon="👋",
)

# Custom CSS to increase font size and change font style
st.markdown("""
<style>
    .big-font {
        font-size: 300%;
        font-style: san-serif; /* Change font style here */
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='big-font'>Welcome to RxSage! 🤖</h1>", unsafe_allow_html=True,)
st.markdown(
    '''### RxSage is an AI powered health advisor that helps you to maintain a healthy lifestyle.'''
)
st.markdown(
    '''

'''
)
st.markdown("## Lets get started!")

page_1 = st.button("Enter your medical Data")
if page_1:
    switch_page("Enter your Data📝")