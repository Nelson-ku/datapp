import streamlit as st
import pandas as pd
import numpy as np
st.header('The data analytics app')

if st.button('Check designer'):
    st.write('Nelson')
else:
    st.write('welcome data is beautiful')


    
st.header('Data analytics with streamlit')
st.write('Streamlit is a powerful and user-friendly data analytics tool that has been gaining popularity in recent years. With Streamlit, users can create highly customizable dashboards, visualizations, and reports, all without having to write complex code or rely on a web developer.')

st.header('using data frame')
df=pd.DataFrame({
    'index':[1,2,3,4],
    'scores':[10,20,30,40]
})

df 

# used to draw a table of random values  Numpy to generate a random sample, and the st.dataframe() method to draw an interactive table.

# dataframe=np.random.randn(10,20)
# st.dataframe(dataframe)

 
st.header('highlighting data')
dataframe= pd.DataFrame(
    np.random.randn(10,20),
    columns=(' col %d' % i for i in range(20))
)

st.dataframe(dataframe.style.highlight_max(axis=0))#highlighting your table

#drawing another a table using the st.table() function
# st.table(dataframe)


#drawing a line chart using st.line_chart() function
st.write('chart data')
chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a', 'b', 'c']

 )

st.header('using Charts in streamlit')
st.write('Streamlit provides a simple and intuitive way to create interactive charts and visualizations for your data. With the st.line_chart, st.bar_chart, and st.area_chart functions, you can easily create line, bar, and area charts that allow you to explore your data. Streamlit also provides built-in support for more advanced visualizations, including histograms, scatter plots, and box plots. With its built-in support for popular data visualization libraries like plotly, you can also create custom visualizations that meet your specific needs. Streamlit makes it easy to create beautiful and informative visualizations that provide insights into your data, whether you are working with small or large datasets.')
st.line_chart(chart_data)

st.write('plot a map using st.map() function of the san fransisco')

map_data=pd.DataFrame(
    np.random.randn(1000,2) /[50,50]+ [37.76, -122.4],
    columns=['lat','lon']
)
st.header('using maps in streamlit')
st.write('Streamlit allows for the integration of maps into your data analytics applications, making it a great tool for geospatial data analysis. The platform provides a number of libraries and APIs that can be used to create interactive maps, including folium, plotly, and kepler.gl. These libraries allow you to create maps with custom markers, pop-ups, and polyglines, as well as add heatmaps and choropleth maps to your visualizations.')

st.map(map_data)


st.write('working with widgets ')
st.write('this slider returns the squares of the number selected')


x= st.slider('x')# this is a widget
st.write(x, 'squared is', x * x)


#create an  input box 
st.text_input('your name', key='name')

st.session_state.name
 

#use a checkbox to display data in a table
if st.checkbox('show dataframe'):
    chart_data=pd.DataFrame(
        np.random.randn(20,3),
        columns=['a','b','c']
    )
    chart_data

#using a selectbox to choose from a series where you can write in the options you want, or pass through an array or data frame column
df=pd.DataFrame({
     'column1':[1,2,3,4],
     'second  column':[10,20,30,40]
})


option =st.selectbox(
    'which number do you like best',
    df['column1'])
'you selected :',option


#working with layouts 
#add a selectbox to the  sidebar
add_select=st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email','Home phone', 'Mobile phone')
)

#add a slider to the sidebar
add_slider =st.sidebar.slider(
    'select a range of values from this data ',
    0.0, 100.0,(25.0,75.0)
)

# controlling layout using st.columns

left_column , right_column= st.columns(2)

left_column.button('Press me!')

# Or even better, call streamlit functions inside a 'with" block


with right_column:
    chosen = st.sidebar.radio(
        'sorting hat',
        ('kisumu', 'nairobi', 'mombasa','eldoret','kakamega'))
    st.write(f'you are in {chosen} town!')


