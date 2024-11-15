import streamlit as st
import pandas as pd
import ast 
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

def app():

    with open('datasets/similarity.pkl','rb') as f:
        similarity = pickle.load(f)

    df = pd.read_csv('datasets/anime_df.csv')


    # function to get list of similar anime 
    def get_anime(name):

        # list to store anime indexes
        recom_idx = []

        #get the index of selected
        anime_idx = df[df['name'] == name].index[0]

        # storing the indexes
        for idx,simi in similarity[anime_idx]:
            recom_idx.append(idx)

        # returning the selected anime index and the recomendation animes index
        return anime_idx, recom_idx

    def get_eval(ele):

        ele = ast.literal_eval(ele)
        return ', '.join(ele)

    st.write("<h1 style ='text-align:center' >  ANIME RECOMMENDER </h1>",
                    unsafe_allow_html=True)

    anime_names = df['name'].tolist()
    anime_names.insert(0,'Select Anime')
    anime_name = st.selectbox('Select the Anime that you have already watched to view recommandation',
                                options=anime_names,
                                placeholder='Select Anime')

    if anime_name != 'Select Anime':

        idx,recom_idx = get_anime(anime_name)

        c1,c2 = st.columns([0.3, 0.7])

        c1.image(df['image'][idx])

        with c2:
            st.subheader(df['name'][idx])

            st.write(f'<b>Jname:</b> {df['jname'][idx]}', unsafe_allow_html=True)

            st.write(f'<b>Genres:</b> {get_eval(df['genre'][idx])}', unsafe_allow_html=True)

            st.write(f'<b>Aired:</b> {get_eval(df['aired'][idx])}', unsafe_allow_html=True)

            st.write(f'<b>Studio:</b> {df['studio'][idx]}', unsafe_allow_html=True)

            st.write(f'<b>PG Rating:</b> {df['pganime'][idx]}', unsafe_allow_html=True)

            st.write(f'<b>Format:</b> {df['formats'][idx]}', unsafe_allow_html=True)
        
        desc = df['desc'][idx].split('           ')[0]
        st.write(f"<p style='text-align: justify;'> <b>Description:</b> {desc}</p>",
                unsafe_allow_html=True)

        # st.markdown(
        #     f"<span> <b>Description:</b> {df['desc'][idx]}</span>",
        #     unsafe_allow_html=True
        #     )
        
        st.subheader("The Recommendations are:")

        c1,c2,c3,c4,c5 = st.columns(5)

        img_ls = []
        title = []

        for i,idx in enumerate(recom_idx):
            img_ls.append(df['image'][idx])
            title.append(df['name'][idx]) 

        with c1:
                st.image(img_ls[0])
                st.write(f"<h6 style = 'text-align: center;'>{title[0]}</h6>",unsafe_allow_html=True)


        with c2:
            st.image(img_ls[1])
            st.write(f"<h6 style = 'text-align: center;'>{title[1]}</h6>",unsafe_allow_html=True)

        with c3:
            st.image(img_ls[2])
            st.write(f"<h6 style = 'text-align: center;'>{title[2]}</h6>",unsafe_allow_html=True)


        with c4:
            st.image(img_ls[3])
            st.write(f"<h6 style = 'text-align: center;'>{title[3]}</h6>",unsafe_allow_html=True)

        with c5:
            st.image(img_ls[4])
            st.write(f"<h6 style = 'text-align: center;'>{title[4]}</h6>",unsafe_allow_html=True)