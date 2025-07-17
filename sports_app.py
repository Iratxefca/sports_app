import streamlit as st
import home
import soccer
import basketball
import american_football
import golf

st.set_page_config(page_title="Sports Popularity Dashboard", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Soccer", "Basketball", "American Football", "Golf"])

if page == "Home":
    home.app()
elif page == "Soccer":
    soccer.app()
elif page == "Basketball":
    basketball.app()
elif page == "American Football":
    american_football.app()
elif page == "Golf":
    golf.app()
