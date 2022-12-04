#  pip install requests streamlit streamlit_lottie bokeh==2.4.1
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from bokeh.models.widgets import Div


st.set_page_config(
    page_title="Matt Majestic's Portfolio Page",
    page_icon=":rocket:",
    layout="wide",
)

st.snow()


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


#  To get rid of the Streamlit branding stuff
local_css("css/styles.css")

#  Anchor
st.title("#")  # This anchor is needed for the page to start at the top when it is called.

# --- INTRO ---
with st.container():
    col1, col2 = st.columns((2, 1))
    with col1:
        st.title("Welcome to my Majestic Portfolio")
        st.subheader("Hi, I'm Matt 💻")
        st.subheader(
            """
            I'm a EST based *Python Developer* & *R Programmer* who specializes in the broad fields of *Automation*, *Data*, *Web Apps*, *DevOps*, *etc*.
            """
        )
        st.write("""""")
        st.subheader(
            """
            This page is actually made with pure Python :snake: and the associated Streamlit library.
            """
        )
    with col2:
        st_lottie(
            load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_bniew9j6.json"),
            height=500,
        )


# --- ABOUT ---
with st.container():
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        st_lottie(
            load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_dh764zdr.json"),
            height=500,
        )
    with col2:
        st.header("About")
        st.write(
            """
            I have been programming professionally since 2019, starting with developing R Shiny apps for a contract at an Oil & Gas company 🐱‍👤
            
            Short facts & milestones:
            - Programmed a web app at *Coca Cola Beverages Florida* to enable Machine Learning for merchant discount levels.
            - MS Market Research & BS in Psychology
            - 4+ years of professional experience in software development teams
            - Enthusiasm for data engineering, automating things, soccer, and trying new cuisines 🍕🍟🥓🍔🥯🍨🍫
            If you are interested in building something together, have questions/suggestions about my code or just wanna connect, feel free to get in touch with me! 
            """
        )


# --- TECH STACK / SKILLS ---
with st.container():
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        st.header("Tech Stack / Skills")
        st.write(
            """
            Languages
            - Python, R, HTML, CSS, Bash, JS
            Frameworks
            - FastAPI, Dash, Django, Flask, Bootstrap, R Shiny, Plumber APIs, tidyverse
            Databases
            - MySQL, PostgreSQL, MongoDB, Snowflake, Spark
            Hosting & Cloud
            - AWS, Azure, Heroku, Vercel, Google Cloud, Streamlit Cloud 😉
            Miscellaneous
            - Git, Github, CI/CD, Docker, Bitbucket
             """
        )

    with col2:
        st_lottie(
            load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_ba013t74.json"),
            height=500,
        )


# --- PORTFOLIO ---
with st.container():
    st.write("---")
    st.header("Portfolio")
    st.write("##")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://csharpcorner-mindcrackerinc.netdna-ssl.com/UploadFile/NewsImages/08172020000734AM/Learn-Python.png")
        st.subheader("Check out my Google classroom")
        st.write("I have lessons on programming & devops there")
    with col2:
        st.image("https://csharpcorner-mindcrackerinc.netdna-ssl.com/UploadFile/NewsImages/08172020000734AM/Learn-Python.png")
        st.subheader("shinyCRM")
        st.write("A lightweight CRM system in R Shiny.")
    with col3:
        st.image("https://csharpcorner-mindcrackerinc.netdna-ssl.com/UploadFile/NewsImages/08172020000734AM/Learn-Python.png")
        st.subheader("Crypto Currency Watchlist")
        st.write("Django web application that shows some basic data of your favourite crypto currencies.")

with st.container():
    st.write("---")
    st.markdown("<h2 style='text-align: center;'>Contact</h2>", unsafe_allow_html=True)
    st.write("##")

    col1, col2, col3 = st.columns(3)
    with col2:
        contact_form = """
        <form action="https://formsubmit.co/805cc992f02da35ae356f2451ece18be" method="POST">
            <input type="hidden" name="_captcha" value="true">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)
