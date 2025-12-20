import streamlit as st
import pandas as pd 
from datetime import datetime

# Page Config
st.set_page_config(
  page_title =' jesse | Portfolio',
  page_icon='🎯',
  layout = 'wide'


# Custom CSS (optional - for styling)
st.markdown('''
                <style>
                    .main-header {font-size: 42px; font-weight: bold; text-align:center;}
                    .sub-header {font-size: 24px; text-align:center; color: #666;}
                </style>
            ''', unsafe_allow_html = True)

# Sidebar
st.sidebar.title('📍 Navigation')
page = st.sidebar.radio('Go to',
                        ['🏠 Home', '🤠 About', ' 💼 Projects', '🛠 Skills' ,'📝 Resume', '📩 Contact' ])

# Home Page
if page == '🏠 Home':
  st.markdown('<p class="main-header"> JESSE AMOATENG p>', unsafe_allow_html=True)
  st.markdown('<p class="sub-header"> majoring in businnes  | Medgar Evers College</p>', unsafe_allow_html=True)

  # Three Columns for stats
  col1, col2, col3 = st.columns(3)

  with col1:
      st.metric('GPA', '3.2 ', '📚')
  with col2:
      st.metric('Projects', '5', '💻')
  with col3:
      st.metric('Skills', '7+', '🚀')

  st.write('---')

  # Introduction with columns
  col1, col2 = st.columns([2,1])
  with col1:
    st.subheader('Welcome to my digital space!👋')
    st.write('''
              i am a medgaedvers student majoring in buisness
            
                🎯 **Current Focus:**  trying to get a job wit y degree 
            
                📚 **Currently Learning:**  accountihg 
            
                🌱 **Fun Fact:** play basktbal 
            ''')
  with col2:
    # Placeholder for image
    st.image('https://www.georgesmusic.com/NEW-MAIN-p-38.jpg', use_column_width=True)
elif page == '🤠 About':
  st.title('About Me')

  # Timeline of my Professional Journey
  st.subheader('My Journey in buisnnes  )

  with st.expander('2025 - Present: Medgar Evers College'):
    st.write('''
                - Major: busisness 
                - Relevant Coursework: im taking accounting classes , and other buissness classes 
                - Activities: baskettball, 
            ''')

  st.subheader('Interests & Hobbies 🏀')
  interests =  music , ' accounting ', ' 'Basketball', 'Travel', 'Baseball']

  # Display the interests in columns
  cols = st.columns(3)
  for i, interest in enumerate(interests):
    with cols[i % 3]:
      st.info(f'🔷 {interest}')
      
elif page == '💼 Projects':
  st.title('My Projects')
  st.write( Im still working on a few but they arent really projects)
   with st.container():
    col1, col2 = st.columns([1, 2])
  
    with col1:
        st.image('https://iprx-cms-content.ams1.vultrobjects.com/Blog_How_To_Crawl_4_capcha_ded9206d5f.png', use_column_width = True)

    with col2:
        st.subheader('🛒 E-Commerce Price Tracker')
        st.write('Python web scraper that monitors Amazon prices and sends alerts')
        st.caption('**Technologies:** Python, BeautifulSoup, Streamlit')


  
elif page == '🛠 Skills':
  st.title(' music and math  )

  # Skills with progress bars
  st.subheader( making beats , and math ')

  skills_data = {
    'music  : 90,
    ' accounting' : 80,
    ' chuch events ' : 90
  }

  for skill, level in skills_data.items():
    col1, col2 = st.columns([1,3])
    with col1:
      st.write(skill)
    with col2:
      st.progress(level/100)

  st.subheader('Tools & Technologies')

  col1, col2, col3 = st.columns(3)
  with col1:
    st.success('Excel')
    st.info('Word')
    st.warning('Access')

  with col2:
    st.success(' church')
    st.info(' internships\s')
    st.warning('ChatGPT/AI Tools')
    
  with col3:
    st.success('Presentations')
    st.info('events ')
    st.warning('Social Media')

elif page == '📝 Resume':
  st.title('Resume')

  # Read PDF from my GitHub repository
  with open('my_resume.pdf', 'rb') as pdf_file:
    PDFbyte = pdf_file.read()
  
  st.download_button(
    label ='🔻 Download Full Resume (PDF)',
    data = PDFbyte,
    file_name = 'my_resume.pdf',
    mime ='application/pdf'
  )

elif page == '📩 Contact':
  st.title("Let's Connect!")

  col1, = st.columns(1)

  with col1:
    st.subheader('Send me a message.')

    st.write('''
        📧 **Email:**jesse.amoateng@com

        🏢 **LinkedIn:** [linkedin.com/in/Jesse Amoateng](https://linkedin.com)

        👩‍💻 **Github:** [https://Jwavyy885.(https://github.com)

        📷 **Instagram:** [@jesseamoateng](https://instagram.com)

    ''')

    # Fun interative element
    st.subheader('Current Status')

    status = st.selectbox(
        "I'm currently:",
        [
            '👩‍💻 busisnnes ',
            '📕 Studying',
            '☕ producing music ',
            '🎮 Gaming',
            '😴 at church '
        ]
    )


    st.info(f'Status: {status}')

    # Footer
    st.write('---')
    st.markdown(
        f'<center>Made with 💗 using Streamlit | © {datetime.now().year}  jesse Amoateng </center>',
        unsafe_allow_html = True












