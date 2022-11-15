import numpy as np
import pandas as pd
import streamlit as st
import random
import re
from string import Template
from main import inference, random_sentence, randomize
import json


def getting_template(temp):
    t = Template(temp)
    return t

sh = """


        Before start, see the instruction below:
        
        1. If you want to have options for a specific term put it into a curly brace and divide options with pipe. Checkout the below example:
            
            e.g. {can|could|would}
        
        2. For your important keywords place a $ before it (Consider that you can apply the first instruction here as well.) Take a look at below example:
        
            e.g. if you change your $feature
            
        Let's begin!


        """

st.title('Welcome to STTG: Smart Text Template Generator')
st.header(sh)
temp = st.text_input('Please provide your template:\n', ' STTG is { amazing | great } !')
st.write('The current template is:\n', temp)

template_dict = {
    "CHANGE":"increase|raise|make an increase to",
    "FEATURE":"loan amount"
}

str_dict =  st.text_input('Now please enter your specific properties with their values in a dictionary format:\n','{"CHANGE":"increase|raise|make an increase to","FEATURE":"loan amount"}')
# printing original string 
dict = json.loads(str(str_dict))
template = getting_template(temp)
x = inference(dict, template)
st.write('Your generated text:\n', x)