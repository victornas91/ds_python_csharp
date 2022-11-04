import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(page_title = 'Sales',
                   
                   page_icon = ':bar_chart:',
                   
                   layout = 'wide'
                   )


df = pd.read_excel(
    
    io = 'sample.xlsx',
    
    engine = 'openpyxl',
    
    sheet_name = 'Sales',
    
    skiprows = 0,
    
    usecols = 'A:G',
    
    nrows = 44,
    
       

)

region = st.sidebar.multiselect(
    
    "Select the Region:",
    
    options = df['Region'].unique(),
    default = df['Region'].unique()
)

rep = st.sidebar.multiselect(
    
    "Select the Representative:",
    
    options = df['Rep'].unique(),
    default = df['Rep'].unique()
)

item = st.sidebar.multiselect(
    
    "Select the Item:",
    
    options = df['Item'].unique(),
    default = df['Item'].unique()
)

df_selection = df.query(
    
    'Region == @region & Rep == @rep & Item == @item'
)

st.title(':bar_chart: Sales per Region / Rep')

st.markdown('##')

total_sales = int(df_selection['Total'].sum())

average_sale = round(df_selection['Total'].mean(), 1)

left_column, right_column = st.columns(2)

with left_column:
    
    st.subheader('Total Sales:')
    
    st.subheader(f'R$ {total_sales:,}')
    
with right_column:
    
    st.subheader('Average Sales Per Rep:')
    
    st.subheader(f'R$ {average_sale}')
    
st.markdown('---')

sales_by_item = (
    
    df_selection.groupby(by = ['Item']).sum()[['Total']].sort_values(by = 'Total'))

fig_product_sales = px.bar(
    
    sales_by_item,
    
    x = 'Total',
    
    y = sales_by_item.index,
    
    orientation = 'h',
    
    title = '<b>Sales by Item</b>',
    
    color_discrete_sequence = ['#000000'] * len(sales_by_item),
    
    template = 'plotly_white',   
)

fig_product_sales.update_layout(
    
    plot_bgcolor = 'rgba(0,0,0,0)',
    
    xaxis = (dict(showgrid = False))
)

st.plotly_chart(fig_product_sales)