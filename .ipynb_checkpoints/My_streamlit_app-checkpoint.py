import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Primary accent for interactive elements
primaryColor = '#77FFE3'


st.title('Welcome to my App!')

link='https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv'
dfcar = pd.read_csv(link)
#st.table(dfcar)

# Using object notation
add_selectbox = st.selectbox(
    "Which region are you interested in?",
    [" US.", " Europe.", " Japan."],
    )
#st.multiselect

fig, ax = plt.subplots(figsize = (20, 5)) 

sns.regplot(x=dfcar[dfcar['continent']==add_selectbox]["mpg"], y=dfcar[dfcar['continent']==add_selectbox]["hp"])
ax.set_title("Are mpg and horse power related?")
ax.set_xlabel("mpg")
st.pyplot(fig)
st.text('A car with a high horse power will drive less miles per gallon, as the consumption is higher')

fig2, ax = plt.subplots(figsize = (20, 5)) 
sns.barplot(x=dfcar[dfcar['continent']==add_selectbox]["time-to-60"], y=dfcar[dfcar['continent']==add_selectbox]["hp"], color='b')
ax.set_title("Horsepower vs Time to 60kmh")
st.pyplot(fig2);
st.text('When the horsepower is higher, the lower time the car will take to achieve 60kmh') 

fig3, ax = plt.subplots(figsize = (20, 5)) 
sns.scatterplot(x=dfcar[dfcar['continent']==add_selectbox]["mpg"], y=dfcar[dfcar['continent']==add_selectbox]["weightlbs"], color='b')
ax.set_title("Miles per gallon vs Weight")
st.pyplot(fig3);
st.text('The lighest the car is, the more miles it can achieve per gallon') 
    
    








# # Using "with" notation
# with st.sidebar:
#     add_radio = st.radio(
#         "Choose a shipping method",
#         ("Sales", "Finance")
#     )

#if add_selectbox == 'Sales':
 #   st.markdown('''Welcome to *Sales*''')
#elif add_selectbox == 'HR':
  #  st.markdown('''Hi, _this_ is **HR**''')
#else:
 #   st.markdown('Helloooooo')
