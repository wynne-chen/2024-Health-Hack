#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 16:12:22 2024

@author: wynne
"""
import streamlit as st



st.title('Health Hack 2024')
st.subheader('by Eugenia, Mei Qi, Wynne, Sheila, and Yvonne', divider = 'green')

st.subheader(':pill: What Can I Donate?')
st.caption('Source: https://sirum.org/donate/')

batch = st.text_input('Batch Number: ', help = 'You can normally find the batch number near the expiration or prescription date.')
try:
    last = int(batch[-1])
    st.success('This batch of medicine can be donated.')
except:
    st.error('This is not a valid batch of medicine.')
    


# Acceptable vs Unacceptable Table
col1, col2 = st.columns(2)

## Acceptable Meds
with col1:

    st.markdown("""
    <div style='text-align: left;'>
        <span style='color: green; font-size: 20px;'>&#10004;</span>
        <span style='font-size: 22px;'>Prescription medication</span>
    </div>
""", unsafe_allow_html=True)
    
    st.markdown("""
    <div style='text-align: left;'>
        <span style='color: green; font-size: 20px;'>&#10004;</span>
        <span style='font-size: 22px;'>Over-the-counter medication</span>
    </div>
""", unsafe_allow_html=True)
    
    st.markdown("""
    <div style='text-align: left;'>
        <span style='color: green; font-size: 20px;'>&#10004;</span>
        <span style='font-size: 22px;'>Supplements</span>
    </div>
""", unsafe_allow_html=True)
    
## Unacceptable Meds
with col2:

    st.markdown("""
    <div style='text-align: left;'>
        <span style='color: red; font-size: 20px;'>&#10060;</span>
        <span style='font-size: 22px;'>IV medication</span>
    </div>
""", unsafe_allow_html=True)
    
    st.markdown("""
    <div style='text-align: left;'>
        <span style='color: red; font-size: 20px;'>&#10060;</span>
        <span style='font-size: 22px;'>Controlled drugs</span>
    </div>
""", unsafe_allow_html=True)
    
    st.markdown("""
    <div style='text-align: left;'>
        <span style='color: red; font-size: 20px;'>&#10060;</span>
        <span style='font-size: 22px;'>Refrigerated drugs</span>
    </div>
""", unsafe_allow_html=True)
    
    st.markdown("""
    <div style='text-align: left;'>
        <span style='color: red; font-size: 20px;'>&#10060;</span>
        <span style='font-size: 22px;'>Medication expiring in less than 6 months</span>
    </div>
""", unsafe_allow_html=True)

st.markdown("")
st.markdown("")
st.markdown("")
    
st.subheader(':speech_balloon: Frequently Asked Questions')

# List of FAQ 
faq_data = {
    'Condition of medicine to be donated': "Ensure that they are not expiring within 6 months, sealed/unopened, non-controlled and non-refrigerated. Remove any personal data such as your name form the medicine package, container, or bag.",
    'Can I donate self-injectable medication?': "Yes, you can donate self-injectable medications such as epi-pens or other pre-filled syringes if they are unexpired, sealed/unopened, non-controlled, and non-refrigerated.",
    'Can I donate liquid medication?': "Yes, you can donate liquid medication if it is unexpired, sealed/unopened, non-controlled, and non-refrigerated.",
    'What happens if my donated medicine is not suitable?': "Unfortunately, medicine that are in undesirable conditions or are unsuitable to be passed on to the other patients will be rejected. Hence, please ensure that you are donating medicines that are not expiring within 6 months, sealed/unopened, non-controlled and non-refrigerated. Prescription medication, over-the-counter medication, and supplements are all eligible for donation."
}

for question, answer in faq_data.items():
    with st.expander(question):
        st.write(answer)
