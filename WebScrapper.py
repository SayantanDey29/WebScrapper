import streamlit as st
import requests
from bs4 import BeautifulSoup
import webbrowser 
st.set_page_config(
    page_title="WebScapper",
    layout="wide"
)
st.markdown("<h1 style='text-align:center'>Web Scrapper</h1>",unsafe_allow_html=True)
hide_st_style="""
    <style>
        #MainMenu {visibility:hidden;}
        footer {visibility:hidden;}
        p{visibility:hidden;}
        button p{visibility:visible;}
        img{height:500px;}
    </style>
"""
st.markdown(hide_st_style,unsafe_allow_html=True)
with st.form("search"):
    keyword=st.text_input("**Enter your keywprd**")
    search=st.form_submit_button("Search")

placeholder=st.empty()
if keyword:
    page=requests.get(f"https://unsplash.com/s/photos/{keyword}")
    soup=BeautifulSoup(page.content,'lxml')
    rows=soup.find_all("div",class_="ripi6")
    col1,col2=placeholder.columns(2)
    for index,row in enumerate(rows):
        figures=row.find_all("figure")
        for i in range(2):
            img=figures[i].find("img",class_="tB6UZ a5VGX")
            list=img['srcset'].split('?')
            anchor=figures[i].find("a",class_="rEAWd")
            anchor["href"]
            if i==0:
                col1.image(list[0],width=600)
                btn=col1.button("Donwload",key=str(index)+str(i))
                if btn:
                    webbrowser.open_new_tab("https://unsplash.com"+anchor["href"])

            else:
                col2.image(list[0],width=600)
                btn=col2.button("Donwload",key=str(index)+str(i))
                if btn:
                    webbrowser.open_new_tab("https://unsplash.com"+anchor["href"])



