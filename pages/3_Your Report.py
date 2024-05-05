import streamlit as st
from backend import gemini
from backend import backend
from contextlib import suppress

st.cache_data.clear()
report_lis = backend.send_report()
st.markdown("<h1 class='big-font'>Your Health Report🩺</h1>", unsafe_allow_html=True)
# print("Report from page 3 : "+report)
with suppress(IndexError): # Ignore if the list is empty
    st.markdown(f"#### BMI : {report_lis[1]}")
    if report_lis[1] < 18.5:
        st.markdown(f"#### Health Advice : :blue[{report_lis[2]}]")
    elif report_lis[1] < 25:
        st.markdown(f"#### Health Advice : :green[{report_lis[2]}]")
    elif report_lis[1] < 30:
        st.markdown(f"#### Health Advice : :orange[{report_lis[2]}]")
    else:
        st.markdown(f"#### Health Advice : :red[{report_lis[2]}]")
    
    st.markdown(f"#### Today's Steps : {report_lis[3]}")
    st.markdown(f"#### Today's Calories Burnt : {report_lis[4]}\n\n")
    st.markdown("### Your Health Report :")
    st.markdown(f"##### {report_lis[0]}")
# st.caching.clear_cache()
# import pyautogui

 
# if st.button("Reset"):
#     pyautogui.hotkey("ctrl","F5")