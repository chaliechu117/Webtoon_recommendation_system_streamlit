import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from genre_model import genre_model
from IPython.core.display import HTML



st.set_page_config(
    page_title="Webtoon Recommender App Page Introduction",
    page_icon="๐",
    layout="wide",
)

title_name = []
st.markdown("# ์ ์ฌํ ์ฅ๋ฅด์ ์นํฐ์ ์ถ์ฒ๋๋ ค์ ๐")

st.balloons()

webtoon_df = pd.read_csv("webtoon_total_final.csv")
title_list = webtoon_df["title"].tolist()

options = st.multiselect(
     '๐ ์ ํธํ๋ ์นํฐ ์ ๋ชฉ์ ์๋ ฅํ๊ณ  Enter๋ฅผ ๋๋ฌ์ฃผ์ธ์. (๋ณต์ ์๋ ฅ ๊ฐ๋ฅํ๋ฉฐ, ์นด์นด์ค/๋ค์ด๋ฒ ์นํฐ๋ง ์๋ ฅ ๊ฐ๋ฅ)',
     title_list
     )


# st.write('You selected:', options)

select_area = st.empty()
st.write("""---""")

if not options:
    print(st.empty().info("์๋ ฅ ๊ธฐ๋ค๋ฆฌ๋ ์คโฆโณ"))
    image = Image.open('wating.jpg')
    st.image(image)
 
# if options:
#     genre_recommend_df = genre_model(options)
#     st.write(genre_recommend_df)
    
   
def to_img_tag(path):
    return '<img src="'+ path + '" width="200" >'


if options:
    genre_recommend_df = genre_model(options)
    genre_recommend_df = genre_recommend_df[["title", "image", "genre", "artist", "story", "score"]]
    genre_recommend_df.rename(columns={"title":"์ ๋ชฉ", "image":"์นํฐ", "genre":"์ฅ๋ฅด", "artist":"์๊ฐ", "story":"์ค๊ฑฐ๋ฆฌ", "score":"ํ์ "},
                                       inplace=True)

    table = HTML(genre_recommend_df.to_html(escape=False,index=False,
                                         float_format='{0:.4g}'.format,formatters=dict(์นํฐ=to_img_tag)))
#     df = pd.read_html(table)
#     df = pd.DataFrame(df)
  
#     for l in range(10):
#         l_title = genre_recommend_df["์ ๋ชฉ"].iloc(l)
#         st.write(l_title)

#     df=pd.DataFrame(html_table[1:], columns=html_table[0])
    st.write(table)



    




    
    
