import streamlit as st
import pickle
import numpy as np

# import the model
pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))


st.title("Moble Price predictor")

# company name
company = st.selectbox("company", df['company'].unique())

# ram
ram = st.selectbox('Ram (choose 3 if apple )',df['Ram'].unique())

# internal
internal = st.selectbox('internal storage', df['internal'].unique())

#is expandable
expandable = st.selectbox("Is memory expandable",['Yes','No'])

# display size in inch
display_size = st.number_input("Display size in inches")

# retina display
retina = st.selectbox("Is Retina dispaly",['Yes','No'])

# rear camera
rear = st.number_input("First Rear camera")

# front camera
front = st.number_input("front camera")

#battery
battery = st.number_input("Battery size (choose 3500 if apple)")

# processor brand
processor = st.selectbox("Processor",df['Processor_type'].unique())

# colour
color = st.selectbox("color of phone", df['color'].unique())

btn = st.button("Predict Prize")

if btn:
    if expandable == 'Yes':
        expandable = 1
    else:
        expandable = 0

    if retina == 'Yes':
        retina = 1
    else:
        retina = 0        
    
    price = int(np.exp(pipe.predict([[company,ram,internal,expandable,display_size,retina,rear,front,battery,processor,color]])))
    st.subheader('The price is between ' + str(price - price*0.05) + ' - ' + str(price + price*0.05))

