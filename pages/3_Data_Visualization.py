import matplotlib.pyplot as plt
from matplotlib import image
import pandas as pd
import seaborn as sns
import plotly.express as px
import streamlit as st
import os

st.title(":red[Heart Disease Diagnostic Visualization]")

st.image("heart-vis.png")

df = pd.read_csv("heart.csv")
df.drop('Unnamed: 0',axis=1,inplace=True)
# st.dataframe(df)
df1 = pd.read_csv("heart_disease_dataset.csv")



st.header(":blue[Visualizaiton of the Dataset] ")


# age = st.selectbox("Select The Age Category:", df['age'].unique())

# col1, col2 = st.columns(2)


# fig_1 = px.pie(df, names='age', hole=0.5)
# col1.plotly_chart(fig_1)


# # if age == df.age.unique()[0]:
# #     col1.plotly_chart(age, use_container_width=True)

# sex = st.radio("Select the Gender : ", df['sex'].unique())

# sex = st.selectbox("Select the Chest pain experienced : ", df['cp'].unique())

# exang = st.radio("Exercise Induced Angina : ", df['exang'].sort_values(ascending=False).unique())

# slope = st.selectbox("Select the Slope of the peak Exercise ST Segment : ", df['slope'].sort_values(ascending=True).unique())

# num = st.radio("Heart Disease :", df['num'].unique())


data_info = st.radio(':blue[Click to view the Visualization of the Dataset]:',
                      ('Ages', 'Gender', 'Chest Pain','Angina', 'Slope', 'Thalassemia', 'Heart Disease'),
                      horizontal=True)


if data_info == 'Ages':
    st.markdown(" ## Ages Category")

    col1, col2 = st.columns(2)
    fig_1 = px.pie(df, names='age', hole=0.5, title='Age Pie Chart')
    col1.plotly_chart(fig_1)
    
    
    fig_1 = px.pie(df, names='age', hole=0.5, color='sex', title='Age vs Gender Pie Chart')
    col1.plotly_chart(fig_1)
    

elif data_info == 'Gender':
    st.markdown("## Gender Category")

    col1, col2 = st.columns(2)

    fig_1 = px.histogram(df, x='sex',  title='Gender vs Sex Histogram Chart')
    col1.plotly_chart(fig_1)
    
    fig_1 = px.histogram(df, x= 'age',color="sex", title='Gender vs Age Histogram Chart' )
    col1.plotly_chart(fig_1)





elif data_info == 'Chest Pain':
    st.markdown("## Chest Pain Experienced")

    col1, col2 = st.columns(2)

    fig_1 = px.histogram(df, x='cp', title='Chest Pain Histogram Chart')
    col1.plotly_chart(fig_1)
    
    fig_1 = px.histogram(df, x='cp', color='sex', title='Chest Pain vs Sex Histogram Chart')
    col1.plotly_chart(fig_1)
    
    fig_1 = px.histogram(df, x='cp', color='age', title='Chest Pain vs Age Histogram Chart')
    col1.plotly_chart(fig_1)



elif data_info == 'Angina':
    st.markdown("## Exercise Induced Angina")
    
    col1, col2 = st.columns(2)
    
    fig_1 = px.pie(df, names='exang', hole=0.5, title='Exercise Induced Angina Pie Chart')
    col1.plotly_chart(fig_1)
    
    fig_1 = px.histogram(df, x='exang', color='sex', title='Exercise Induced Angina vs Sex Histogram Chart')
    col1.plotly_chart(fig_1)
    
    fig_1 = px.histogram(df, x='exang', color='age', title='Exercise Induced Angina vs Age Histogram Chart')
    col1.plotly_chart(fig_1)




elif data_info == 'Slope':
    st.markdown("## The Slope of the Peak Exercise ST Segment")
    
    col1, col2 = st.columns(2)
    
    fig_1 = px.pie(df, names='slope', hole=0.5,  title='Slope Pie Chart')
    col1.plotly_chart(fig_1)
    
    fig_1 = px.histogram(df, x='slope', color='sex', title='Slope vs Gender Histogram Chart')
    col1.plotly_chart(fig_1)
    
    fig_1 = px.histogram(df, x='slope', color='age', title='Slope vs Age Histogram Chart')
    col1.plotly_chart(fig_1)



   
elif data_info == 'Thalassemia':
    st.markdown("## A Blood Disorder called Thalassemia")
    
    col1, col2 = st.columns(2)
    
    fig_1 = px.pie(df, names='thal', hole=0.5,  title='Thalassemia Pie Chart')
    col1.plotly_chart(fig_1)
    
    fig_1 = px.histogram(df, x='thal', color='sex',  title='Thalassemia vs Gender Histogram Chart')
    col1.plotly_chart(fig_1)
    
    fig_1 = px.histogram(df, x='thal', color='age',  title='Thalassemia vs Ages Histogram Chart')
    col1.plotly_chart(fig_1)




elif data_info == 'Heart Disease':
    st.markdown("## Heart Disease")
    
    col1, col2 = st.columns(2)
    
    fig_1 = px.pie(df, names='num', hole=0.5,  title='Heart Disease Pie Chart')
    col1.plotly_chart(fig_1)
    
    fig_1 = px.histogram(df, x='num', color='sex',  title='Heart Disease vs Sex Histogram Chart')
    col1.plotly_chart(fig_1)
    
    fig_1 = px.histogram(df, x='num', color='age',  title='Heart Disease vs Age Histogram Chart')
    col1.plotly_chart(fig_1)
    
    # fig_1 = px.histogram(df, x='num', color='age', pattern_shape="cp",  title='Heart Disease vs Age vs Sex Histogram Chart')
    # col1.plotly_chart(fig_1)





    
    
    
#     st.write(df.tail())
# elif data_info == 'Sample':
#     st.write(df.sample(5))  
# elif data_info == 'Columns':
#     for column in list(df.columns):
#         st.write(column)
# elif data_info == 'Info':
#     buffer = io.StringIO()
#     df.info(buf=buffer)
#     s = buffer.getvalue()
#     st.text(s)
# else:
#     st.write(df.describe())






# st.markdown(" ## Ages Category")

# col1, col2 = st.columns(2)

# fig_1 = px.pie(df, names='age', hole=0.5)
# col1.plotly_chart(fig_1)




# st.markdown("## Gender Category")

# col1, col2 = st.columns(2)


# fig_1 = px.histogram(df, x='sex')
# col1.plotly_chart(fig_1)

# fig_1 = px.pie(df, names='age', hole=0.5)
# col1.plotly_chart(fig_1)



# sex = st.radio("Select the Gender : ", df['sex'].unique())

# fig_1 = px.histogram(df[df['sex'] == sex], x="sex")
# col1.plotly_chart(fig_1, use_container_width=True)

# fig_2 = px.histogram(df[df['sex'] == sex], y="sex")
# col2.plotly_chart(fig_2, use_container_width=True)