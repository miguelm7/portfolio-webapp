import streamlit as st
from PIL import Image

st.set_page_config(page_title="My Webapp", page_icon=":tada:", layout="wide")

# --- LOAD ASSETS ---

img_header = Image.open(".\images\\44922635.png")
img_sports = Image.open(".\images\\sports.jpg")

# --- ADD STYLE ---
def add_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

add_css(".\style\style.css")     


# --- HEADER ---
with st.container():
    st.subheader("Hi, I am Miguel :wave:", anchor=False) 
    st.title("A Data Scientist from Spain", anchor=False)
    st.write("I am passionate about finding ways to use Python to maximize the value of businesses data!")
    st.write("[Visit my GitHub!](https://github.com/miguelm7)")


# --- WHAT I DO ---

with st.container():
    st.write("---") # separator
    left_col, right_col = st.columns(2)
    with left_col:
        st.header("What I do", anchor=False)
        st.write("##") # space
        st.write(
            """
            Blablablabl ablablabalab lalbbalalb balbabalblabl:
            - Blablablabl ablablabalablalb balalbbalba balblablablalbalbab lablalbabl
            - Blablablab  lablablabal  ablalbbalalbbalbab alblablabla
            - Blablablabla  blablabalablalbbala lbbalba balblablablalb albablablalbabl
            - Blablablablablab  labalablalb balalbbalbabalblabl ablalbalbablabl albabl
            - Blabla blablablabla  balablalbbalalbbalbabalblablabl albalb ablablalbabl
            - Blablablablab  lablabalablalb  balalbbalbabalbla blablalbalbab lablalbabl

            Blablablablablablabal ablalbbalalbba lbabalblablablalbalbablablalbabl
            """
        )
    with right_col:
        col1, col2, col3 = st.columns(3) # to someway align, create two columns and set to the center one
        with col2:
            st.write("##") # space
            st.write("##") # space
            st.image(img_header, caption="logo image", width=300,)

# --- PROJECTS ---

with st.container():
    st.write("---")
    st.header("My Projects", anchor=False)
    st.write("##")

with st.container():
    img_col, txt_col = st.columns((1,2))
    with img_col:
        st.image(img_sports, caption="sports prediction", width=300,)
    with txt_col:
        st.subheader("Sports prediction", anchor=False)
        st.write(
        """
            Resumen del proyecto.
            Blablablabl ablablabalab lalbbalalb balbabalblabl:
            - Blablablabl ablablabalablalb balalbbalba balblablablalbalbab lablalbabl
            - Blablablab  lablablabal  ablalbbalalbbalbab alblablabla

        """
        )
        st.markdown("[Visita el repositorio del proyecto](https://github.com/miguelm7/sports_prediction)")

with st.container():
    img_col, txt_col = st.columns((1,2))
    with img_col:
        st.image(img_sports, caption="sports prediction", width=300,)
    with txt_col:
        st.subheader("Sports prediction", anchor=False)
        st.write(
        """
            Resumen del proyecto.
            Blablablabl ablablabalab lalbbalalb balbabalblabl:
            - Blablablabl ablablabalablalb balalbbalba balblablablalbalbab lablalbabl
            - Blablablab  lablablabal  ablalbbalalbbalbab alblablabla

        """
        )
        st.markdown("[Visita el repositorio del proyecto](https://github.com/miguelm7/sports_prediction)")

# --- CONTACT ---

with st.container():
    st.write("---")
    st.header("Get in Touch With Me!", anchor=False)
    st.write("##")

    contact_form = """
        <form action="https://formsubmit.co/00a231bcf9df9b3214abcc91a8e33774 " method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
        </form>
    """

    left_col_form, right_col_form = st.columns(2)
    with left_col_form:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_col_form:
        st.empty()