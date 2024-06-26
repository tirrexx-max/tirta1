import streamlit as st
import requests
from PIL import Image
from streamlit_lottie import st_lottie



st.set_page_config(page_title="Tirta Rendy Siahaan",page_icon="⚓", layout="wide")

#function animasi via url
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()


lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("image/3-Easy-Eco-Friendly-Lifestyle-Changes-You-Need-To-Make-7.webp")

with st.container():
    st.subheader("Halo,aku Tirta Rendy Siahaan:wave:")
    st.title("Data Operation - Universtias Indonesia")
    st.write("Saya adalah seorang mahasiswa baru Universitas Indonesia jurusan Computer Science")


    st.write("[Selengkapnya>](https://www.linkedin.com/in/tirta-rendy-siahaan-838bb01b4/)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    
    with left_column:
        st.header("Apa yang saya kerjakan?")
        st.write("##")
        st.write("""
                 Beberapa bidang yang saya kuasai :
                 - Digital Marketing
                 - Business Plan
                 - Web Development
                 - Music Education
                 
                 """)
        
    with right_column:
        st.lottie(lottie_coding,height=300,key="coding")

        #konten project
       
        with left_column:
            st.write("---")
            st.header("Daftar Projek")
            st.write("##")
        with left_column:
            image_column, text_column = st.columns((1,2))
            with image_column:
                st.image(img_contact_form)
            with text_column:
                st.subheader("Environmental Sustainability using Eco-Friendly goods")
                st.write("Menggunakan bahan-bahan ramah lingkungan dalam sektor industri untuk mempertahankan bumi")
                st.markdown("[matira timah proposal](https://www.canva.com/design/DAF0hQ06510/ILYpTn0vX827eMBzYeVl5g/edit)")



        





