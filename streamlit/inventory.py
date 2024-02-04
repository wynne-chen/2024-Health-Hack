#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on Wed Jan 31 16:11:22 2024

@author: wynne
'''

import pandas as pd
import streamlit as st
import numpy as np


from pathlib import Path

st.title('Health Hack 2024')
st.subheader('by Eugenia, Mei Qi, Wynne, Sheila, and Yvonne', divider = 'green')

st.subheader(':clipboard: Personal Medicine Inventory')

# import medicine inventory
df_path = Path(__file__).parent / 'data/inventory.csv'
df = pd.read_csv(df_path)

# preparing empty check boxes for the dataframe
df['selected'] = [False for i in range(df.shape[0])]

# preparing sub-category names for the selectbox
list_sub_category = df['purpose'].sort_values().unique().tolist()

if st.session_state["authentication_status"]:
    st.write(f'Welcome *{st.session_state["name"]}*')


    # defining dataframe we want to dynamically interact with and 
    # make changes to within streamlit session. 
    # it is to be declared once at the beginning, like this:
    if 'df' not in st.session_state:
            st.session_state.df = pd.DataFrame(columns = df.columns)
    if 'full' not in st.session_state:
            st.session_state.full = df.copy()
    
    a1,a2,a3 = st.columns([.75,.25,2])
    
    with a1:
        # writing title to give users a lead
        st.subheader('Add/Remove Item')
      
        # selecting medical use before scrolling through medicine
        sub_category = st.selectbox('Select purpose:', list_sub_category)
        
        # retrieving list of recorded items in inventory
        list_item = df['medicine'][df['purpose'] == sub_category].sort_values().unique().tolist()
    
        # to give an option to search items within all medicines:
        if st.toggle('Search all medicines'):
            list_item = df['medicine'].sort_values().unique().tolist()
        
        st.write('Num. of medicines in this category:',len(list_item))
        st.write(' ')
        st.write(' ')
        # setting up a variable to save a product name that will be chosen by user during the interaction
        name = ''
        name = st.selectbox('Medicine:', list_item)
        
        # option to put a new item in the list if the product is not yet recorded in inventory list
        not_in_list = st.checkbox('Item not in the list.')
        if not_in_list:
            name = st.text_input('Medicine Name:')
            name = name.title()
            category = st.selectbox('Category:', ('Over the counter', 'Pharmacy', 'Prescription'))
            purpose = st.selectbox('Purpose:', ('Antihistamine (runny nose)', 'Cough', 'Reduce phlegm', 'Lozenges', 'Painkiller and muscle relaxant', 'Fever', 'Antibiotics', 
                                                'Antiseptic', 'Antifungal', 'Contraceptive', 'Mood stabiliser', 'Other'))
            if purpose == 'Other':
                purpose = st.text_input('Other: ')
            form = st.selectbox('Form: ', ('Tablet', 'Liquid', 'Inhaler', 'Cream/Lotion', 'Drops', 'Suppository', 'Injection'))
        
        
        # setting up variables to fill in other columns for each entry (row)
        sel = False
        if not_in_list == False:
            category = df['category'][df['medicine'] == name].values[0]
            purpose = df['purpose'][df['medicine'] == name].values[0]
            form = df['form'][df['medicine'] == name].values[0]
        
        purchase_date = st.date_input('Purchase Date: ')
        expiry_date = st.selectbox('Is there an expiry date?', ('Yes', 'No'))
        if expiry_date == 'Yes':
            expiry_date = st.date_input('Expiry Date: ')
        else:
            expiry_date = np.NaN
        
        if form == 'Liquid':
            quantity = st.text_input('Quantity (in ml):')
        else:
            quantity = st.text_input('Quantity:')
    
        # check if the quantity is a number
        # technically we could use the number_input but this is a bit more polished i feel
        q_isnumber = False
        if quantity != '':
            try:
                quantity = float(quantity)
                q_isnumber = True
            except:
                st.error('Quantity must be a number.')
    
    # ['medicine', 'category', 'purpose', 'form', 'quantity', 'purchase_date', 'expiry_date']
    
        # preparing a button that records/appends the user input to the list/dataframe
        if st.button('Add to cart') and q_isnumber == True:
            st.session_state.df = st.session_state.df.append({
            'selected': sel, 
            'medicine': name,
            'category': category,
            'purpose': purpose,
            'form': form, 
            'quantity': quantity,
            'purchase_date': purchase_date,
            'expiry_date': expiry_date
            }, ignore_index = True)
    
            # pops a small notification on below-right
            st.toast('Added to list.')
    
    with a3:
        st.subheader('Items to be added')
        if 'df' not in st.session_state:
            st.session_state.df = df.copy()
        
        # toggle button
        if st.toggle('Show data'):
            # to display the number of item in the list
            st.write('Num. of entry:', st.session_state.df.shape[0])
    
            # displaying dataframe with st.data_editor
            # and applying st.column_config inside data_editor
            # 1. creating df.groupby to merge items with identical product name
            # 2. adding checkbox inside column_config parameter with False (unchecked) as default value
            # 3. hiding dataframe index so it will appear a bit 'cleaner' without index column
            st.session_state.df = st.data_editor(
            st.session_state.df.groupby(['selected', 'medicine', 'category', 'purpose', 'form', 'purchase_date', 'expiry_date']).agg({'quantity':'sum'}).reset_index(), 
            column_config = {
                'selected': st.column_config.CheckboxColumn('selected', default = False)
                }, hide_index = True, use_container_width=True)
            
            b1,b2,b3 = st.columns([1,1.5,1.5])
            with b1:
            # setting up button to delete selected rows
                if st.button('Delete selected'):
                    st.session_state.df = st.session_state.df[st.session_state.df['selected'] == False]
                    st.success('Data deleted.')
            with b2:
            # setting up button to empty the cart
                if st.button('Delete all'):
                    cols = st.session_state.df.columns
                    st.session_state.df = pd.DataFrame(columns = cols)
                    st.success('Data deleted.')
            with b3:
            # setting up button to add the quantity to the 
            # actual quantity of mentioned item in the inventory data.
                if st.button('Save changes to inventory data'):
                    for i,j in list(zip(st.session_state.df['medicine'],st.session_state.df['quantity'])):
                        st.session_state.full['quantity'][st.session_state.full['product_name'] == i] += j
                    cols = st.session_state.df.columns
                    st.session_state.df = pd.DataFrame(columns = cols)
                    st.success('Inventory updated. Scroll down to see your inventory data.')
        
    
    st.divider()
    
    st.subheader('Current Inventory')
    
    search_sub_category = st.selectbox('Select medicine category to display:', list_sub_category)
    sorter = st.radio('Sort by:', ('Purchase Date', 'Expiry Date'))
    if sorter == 'Purchase Date':
        sorter = 'purchase_date'
    elif sorter == 'Expiry Date':
        sorter = 'expiry_date'
        
    
    if st.toggle('Display full inventory'):
        st.dataframe(st.session_state.full.sort_values(by = sorter, ascending = True).drop(['selected'], axis = 1))
    else:
        st.dataframe(st.session_state.full[st.session_state.full['purpose'] == search_sub_category].sort_values(by = sorter, ascending = True).drop(['selected'], axis = 1))
        
elif st.session_state["authentication_status"] is None:
    st.warning('Please login on the Home page.')