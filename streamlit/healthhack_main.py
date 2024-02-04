#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 14:31:48 2024

@author: wynne
"""

import streamlit as st
import streamlit_authenticator as stauth
from st_pages import show_pages_from_config

import yaml
from yaml.loader import SafeLoader



# test shell with multi-page
st.set_page_config(
    page_title='Health Hack 2024',
    page_icon=':home:',
    layout='wide',
    initial_sidebar_state='expanded'
    )

show_pages_from_config()


# log-in widget. For now without a database etc this is a pre-created user
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

authenticator.login(location = 'main', 
                    fields = {'Form name':'Login',
                              'Username':'Username',
                              'Password':'Password',
                              'Login':'Login'})

if not st.session_state["authentication_status"]:
    col1, col2, col3, col4 = st.columns(4)
    
       
    # reset password
    with col1:
        reset_pw = st.button('Reset Password')
        if reset_pw:
            if st.session_state["authentication_status"]:
                try:
                    if authenticator.reset_password(st.session_state["username"]):
                        st.success('Password modified successfully')
                        with open('../config.yaml', 'w') as file:
                            yaml.dump(config, file, default_flow_style=False)
                except Exception as e:
                    st.error(e)
    
    # new user registration
    with col2:
        new_user = st.button('Register')
        if new_user:
            try:
                if authenticator.register_user(preauthorization=False):
                    st.success('User registered successfully')
            except Exception as e:
                st.error(e)
    
    # forgot password
    with col3:
        forgot_pw = st.button('Forgot Password')
        if forgot_pw:
            try:
                username_of_forgotten_password, email_of_forgotten_password, new_random_password = authenticator.forgot_password()
                if username_of_forgotten_password:
                    st.success('New password to be sent securely')
                    with open('../config.yaml', 'w') as file:
                        yaml.dump(config, file, default_flow_style=False)
                    # Random password should be transferred to the user securely
                else:
                    st.error('Username not found')
            except Exception as e:
                st.error(e)
    
    # forgot username
    with col4:
        forgot_user = st.button('Forgot Username')
        if forgot_user:
            try:
                username_of_forgotten_username, email_of_forgotten_username = authenticator.forgot_username()
                if username_of_forgotten_username:
                    st.success('Username to be sent securely')
                    # Username should be transferred to the user securely
                else:
                    st.error('Email not found')
            except Exception as e:
                st.error(e)

# update user details
if st.session_state["authentication_status"]:
    try:
        if authenticator.update_user_details(st.session_state["username"]):
            st.success('Entries updated successfully')
            with open('../config.yaml', 'w') as file:
                yaml.dump(config, file, default_flow_style=False)
    except Exception as e:
        st.error(e)



# login results
if st.session_state["authentication_status"]:
    authenticator.logout()
    st.write(f'Welcome *{st.session_state["name"]}*')
elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')



# main content -- about page 
st.title('Health Hack 2024')
st.subheader('by Eugenia, Mei Qi, Sheila, Wynne, and Yvonne', divider = 'green')

st.header('About')
st.write('This is a proof of concept app for managing a personal inventory of medication to prevent wastage.')
st.write('This has been conceptualised and produced for Health Hack 2024.')
st.write('Login to manage your own personal inventory of medication, or navigate to the') 
st.write('What Can I Donate or Closest Donation Box pages to find out how and what medication you can donate.')
