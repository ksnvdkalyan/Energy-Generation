import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

#st.title('ENERGY ')


# DATE_COLUMN = 'date/time'
# DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
#          'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

#####################################################################

Technology = ['Hydropower', 'Renewable hydropower', 'Pumped storage', 'Wind',
'Onshore wind energy', 'Offshore wind energy','Solar' , 'Solar photovoltaic','Concentrated solar power',
'Bioenergy','Solid biofuels','Bagasse','Renewable municipal waste','Other solid biofuels','Liquid biofuels','Biogas']


years = ["2010", "2011", "2012","2013","2014","2015","2016","2017","2018"]

data = {'Technology' : Technology,
        '2010'   : [112125, 107175, 4949, 16104, 16104,0,65,65,0,17049,17048,0,71,16977,0,1],
        '2011'   : [124673 , 119724, 4949, 19528, 19528, 0, 309, 305, 4, 17700, 17694, 0, 75, 17619, 0, 6],
        '2012'   : [ 133094, 128145, 4949, 23069, 23069, 0, 975, 969, 6,24068,24058,0,81,23977,0,10],
        '2013'   : [125953,121004,4949,24640,24640,0,1684,1600,84,28772,28759,0,93,28667,0,13],
        '2014'   : [140814,135865,4949,27235,27235,0,3100,2739,360,33465,33450,0,105,33345,0,16],
        '2015'   : [135512,130562,4949,31873,31873,0,5979,5619,360,29015,28993,0,119,28874,0,22],
        '2016'   : [130161,125211,4949,36273,36273,0,10182,9822,360,18404,18380,0,123,18257,0,24],
        '2017'   : [131351,126402,4949,47670,47670,0,18128,17768,360,16872,16843,0,111,16732,0,29],
        '2018'   : [136599,131650,4949,55009,55009,0,31067,30707,360,17997,17969,0,188,17781,0,29],
       }


df = pd.DataFrame(data)


df1 = df[["2010", "2011", "2012","2013","2014","2015","2016","2017","2018"]]
x = df1.values
x1 = x.transpose()
df2 = pd.DataFrame(x1,columns = Technology)
df2["year"] = ["2010", "2011", "2012","2013","2014","2015","2016","2017","2018"]
df3  = df.set_index('Technology')
df4= df2.set_index('year')

##################################################################3333

# @st.cache
# def load_data(nrows):
#     data = pd.read_csv(DATA_URL, nrows=nrows)
#     lowercase = lambda x: str(x).lower()
#     data.rename(lowercase, axis='columns', inplace=True)
#     data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
#     return data
#

# data_load_state = st.text('Loading data...')
# # Load 10,000 rows of data into the dataframe.
# # data = load_data(10000)
# # # Notify the reader that the data was successfully loaded.
# data_load_state.text('Loading data...done!')




if st.sidebar.checkbox("Year wise"):
    st.subheader("Data")
    st.write(df3)

if st.sidebar.checkbox("Technology wise"):
    st.subheader("Data")
    st.write(df4)

#st.sidebar.text("")


add_selectbox = st.sidebar.selectbox(
    "Select The year",
    ["2010", "2011", "2012","2013","2014","2015","2016","2017","2018"]
)
# add_selectbox1 = st.sidebar.selectbox(
#     "How would you like to be contacted?",
#     ["ALL",'Hydropower', 'Renewable hydropower', 'Pumped storage', 'Wind',
#     'Onshore wind energy', 'Offshore wind energy','Solar' , 'Solar photovoltaic','Concentrated solar power',
#     'Bioenergy','Solid biofuels','Bagasse','Renewable municipal waste','Other solid biofuels','Liquid biofuels','Biogas']
# )

st.sidebar.text("")


if st.sidebar.button('PLOT BAR GRAPH'):

    fig = px.bar(df,x='Technology',y = add_selectbox)
    st.plotly_chart(fig,use_container_width=5)


if st.sidebar.button('PLOT PIE CHART'):
    fig = px.pie(df, values=add_selectbox, names='Technology', title='Pie chart')
    st.plotly_chart(fig,use_container_width=5)

st.sidebar.text("")


add_selectbox1 = st.sidebar.selectbox(
    "Select The Technology",

    ['Hydropower', 'Renewable hydropower', 'Pumped storage', 'Wind',
    'Onshore wind energy', 'Offshore wind energy','Solar' , 'Solar photovoltaic','Concentrated solar power',
    'Bioenergy','Solid biofuels','Bagasse','Renewable municipal waste','Other solid biofuels','Liquid biofuels','Biogas'])



st.sidebar.text("")

c =add_selectbox1.capitalize()

t1 ='PLOT BAR GRAPH FOR ' + c
x = st.sidebar.button(t1)
if x :
    fig = px.bar(df2,x="year",y = add_selectbox1)
    st.plotly_chart(fig,use_container_width=5)

c =add_selectbox1.capitalize()
t2 ='PLOT PIE CHART FOR ' + c
x1 = st.sidebar.button(t2)

if x1 :
    fig = px.pie(df2, values=add_selectbox1, names='year', title='Pie chart')
    st.plotly_chart(fig,use_container_width=5)








page_bg_img = '''
<style>
body {
background-image: url("https://github.com/ajayjalluri/Heroku-Flask-Deployment/blob/main/ess.png?raw=true");
background-size: cover;
}
</style>
'''

#st.markdown(page_bg_img, unsafe_allow_html=True)
