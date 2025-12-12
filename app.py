import streamlit as st
import plotly.express as px
import pandas as pd
from PIL import Image
import io

# Page configuration
st.set_page_config(
    page_title="My Portfolio",
    page_icon="👨‍💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #2E86AB;
        text-align: center;
        margin-bottom: 1rem;
    }
    .section-header {
        font-size: 1.8rem;
        color: #2E86AB;
        border-bottom: 2px solid #2E86AB;
        padding-bottom: 0.5rem;
        margin-top: 1.5rem;
    }
    .project-card {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        border-left: 5px solid #2E86AB;
    }
    .skill-stat {
        background-color: #e9f7fe;
        border-radius: 10px;
        padding: 1rem;
        margin: 0.5rem 0;
    }
    .education-card {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 1.2rem;
        margin-bottom: 1rem;
    }
    .stProgress > div > div > div > div {
        background-color: #2E86AB;
    }
    .contact-info {
        background-color: #f0f8ff;
        border-radius: 10px;
        padding: 1.5rem;
        margin-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar for navigation
with st.sidebar:
    st.image("image.jpg", width=150)
    st.title("Navigation")
    page = st.radio("Go to", ["Home", "Skills", "Projects", "Education", "Contact"])
    
    st.markdown("---")
    st.markdown("### Quick Links")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/harini-rajendiran-b23857257/)")
    st.markdown("[GitHub](https://github.com/Harinirajendiran)")
    st.markdown("[Download Resume](resume.pdf)")
    
    st.markdown("---")
    st.markdown("### Contact Info")
    st.markdown("📧  harini.rajendiran18@gmail.com")
    st.markdown("📱 +91 8667620398")
    st.markdown("📍 Tamil Nadu,India")

# Main content based on selected page
if page == "Home":
    # Header section
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image("image.jpg", width=250)
    
    with col2:
        st.markdown('<h1 class="main-header">Harini Rajendiran</h1>', unsafe_allow_html=True)
        st.markdown("### BioMedical Engineer")
        st.markdown("Passionate about leveraging technology to solve real-world problems. Skilled in Python, AI, and web development using Streamlit.")
        
        st.markdown("---")
        
        # Quick stats
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            st.metric("Years Experience", "NIL")
        with col_b:
            st.metric("Projects Completed", "2")
        with col_c:
            st.metric("Certifications", "8")
    
    st.markdown("---")
    
    # About me section
    st.markdown('<h2 class="section-header">About Me</h2>', unsafe_allow_html=True)
    
    about_col1, about_col2 = st.columns(2)
    
    with about_col1:
        st.markdown("""
        I'm a dedicated professional with expertise in:
        - Python programming
        - AI concepts
        -Streamlit for web apps
        -strong knowledge about Medical devices
        I enjoy transforming complex data into actionable insights and building applications that solve real-world problems.
        """)
    
    with about_col2:
        st.markdown("""
        ### Professional Highlights
        -AI-Concept and technique[83%]
        -Microsensor,Implantable Device and Rodent Surgeries for Biomedical Applcation[68%]
        -Done workshop in Sathyabama Institude of Science and Technology as a topic of "Five day Workshop and Hands-on Traning on Advance Biomaterial"
        -Done hospital training in KAV Biomedical equipment Training and Education-1 week training
        I'm passionate about continuous learning and staying updated with the latest technologies in the fast-evolving tech landscape.
        """)
    
    # Recent projects preview
    st.markdown('<h2 class="section-header">Featured Projects</h2>', unsafe_allow_html=True)
    
    proj_col1, proj_col2, proj_col3 = st.columns(3)
    
    with proj_col1:
        card1 = st.container()
        with card1:
            st.markdown("**IoT based fall detection monitor**")
            st.markdown("Predict patient fall even when the jerk appear of accuracy 95%")
            st.markdown("`iot` `Scikit-learn` `XGBoost`")
    
    with proj_col2:
        card2 = st.container()
        with card2:
            st.markdown("**Real-time Analytics Dashboard**")
            st.markdown("Interactive dashboard for business metrics visualization")
            st.markdown("`Streamlit` `Plotly` `PostgreSQL`")
    
    with proj_col3:
        card3 = st.container()
        with card3:
            st.markdown("**Patient Monitoring system**")
            st.markdown("Official work based website help to monitor the patient information")
            st.markdown("`python` `streamlit` `pandas`")

elif page == "Skills":
    st.markdown('<h1 class="main-header">Skills & Expertise</h1>', unsafe_allow_html=True)
    
    # Technical Skills with progress bars
    st.markdown('<h2 class="section-header">Technical Skills</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Programming Languages")
        st.markdown("Python")
        st.progress(90)
        
        st.markdown("HTML,CSS")
        st.progress(85)
        
        st.markdown("SQL")
        st.progress(85)
        
    with col2:
        st.markdown("#### Technologies & Frameworks")
        st.markdown("Streamlite")
        st.progress(85)
        
        st.markdown("Django")
        st.progress(50)
        
        st.markdown("FastAPI")
        st.progress(35)
        
    # Skill statistics visualization
    st.markdown('<h2 class="section-header">Skill Statistics</h2>', unsafe_allow_html=True)
    
    # Create a DataFrame for skill visualization
    skill_data = pd.DataFrame({
        'Skill Category': ['Python','HTML','CSS','sQL'],
        'Proficiency': [90,85, 85, 85],
        'Years of Experience': [1,1,1,1]
    })
    
    # Create visualizations
    fig1 = px.bar(skill_data, x='Skill Category', y='Proficiency',title='Proficiency by Skill Category',color='Proficiency', color_continuous_scale='Blues')
    st.plotly_chart(fig1, use_container_width=True)
    
    col3, col4 = st.columns(2)
    
    with col3:
        fig2 = px.pie(skill_data, values='Years of Experience', names='Skill Category',title='Experience Distribution by Skill Category')
        st.plotly_chart(fig2, use_container_width=True)
    
    with col4:
        fig3 = px.line_polar(skill_data, r='Proficiency', theta='Skill Category',line_close=True, title='Skill Proficiency Radar')
        st.plotly_chart(fig3, use_container_width=True)
    
    # Soft Skills
    st.markdown('<h2 class="section-header">Soft Skills</h2>', unsafe_allow_html=True)
    
    soft_skills_col1, soft_skills_col2 = st.columns(2)
    
    with soft_skills_col1:
        st.markdown("""
        - **Communication**: Presenting technical concepts to non-technical stakeholders
        - **Problem Solving**: Analytical approach to complex challenges
        - **Team Leadership**: Experience leading cross-functional teams
        """)
    
    with soft_skills_col2:
        st.markdown("""
        - **Project Management**: Agile/Scrum methodologies
        - **Mentoring**: Guiding junior team members
        - **Adaptability**: Quickly learning new technologies
        """)

elif page == "Projects":
    st.markdown('<h1 class="main-header">Projects Portfolio</h1>', unsafe_allow_html=True)
    
    # Project 1
    with st.container():
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown("### Patient Monitoring System")
            st.markdown("""
            Developed a python and streamlit-based patient monitoring system that tracks vital signs and generates alerts for abnormal readings. 
            The system integrates with wearable devices to provide real-time data visualization and historical trend analysis.
            
            **Key Features:**
            - Real time vital signs monitoring
            - Alert system for abnormal readings
            - Data visualization dashboard
            """)
        
        with col2:
            st.markdown("**Technologies Used**")
            st.markdown("`Python` `Scikit-learn` `Streamlit` `Pandas`")
            st.markdown("**Project Duration**")
            st.markdown("4 months")
            st.markdown("**Team Size**")
            st.markdown("1 members")
    
    st.markdown("---")
    
    # Project 2
    with st.container():
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown("### IoT based fall detection monitor")
            st.markdown("""
            Created an interactive device ,which has specific feature of finding fall
            of the old age people and physically challenged people.
            
            
            **Key Features:**
            - Real-time data processing with cloud storage
            -IoT based indication
            -Buzzer indication of abnormal motion
            -Accuray is high than previews devices
            """)
        
        with col2:
            st.markdown("**Technologies Used**")
            st.markdown("`IoT` `Arduino` ")
            st.markdown("**Project Duration**")
            st.markdown("6 Month")
            st.markdown("**Team Size**")
            st.markdown("3 members")
    
    # Project filter
    st.markdown("---")
    st.markdown("### Filter Projects by Technology")
    
    tech_options = ["All", "Python", "Machine Learning", "Web Development", "Cloud", "Data Visualization"]
    selected_tech = st.selectbox("Select technology", tech_options)
    
    if selected_tech != "All":
        st.info(f"Showing projects related to {selected_tech}. Use the sidebar to see all projects.")

elif page == "Education":
    st.markdown('<h1 class="main-header">Education & Certifications</h1>', unsafe_allow_html=True)
    
    # Education
    st.markdown('<h2 class="section-header">Education</h2>', unsafe_allow_html=True)
    
    with st.container():
        col1, col2, col3 = st.columns([1, 3, 1])
        
        with col1:
            st.image("logo.jpg", width=100)
        
        with col2:
            st.markdown("### Bachelor of Enginering")
            st.markdown("**Dhanalakshmi Srinivasan Engineering College(A)**")
            st.markdown("Specialization in Biomedical Engineering")
            st.markdown("**Relevant Coursework:** Artificial Intelligence,Deep Neural Network,Advance Biomedical Instrumentation,Biomaterials,Medical Imaging")
        
        with col3:
            st.markdown("**2022-2026**")
            st.markdown("GPA: 8.80/10")
    
    # Certifications
    st.markdown('<h2 class="section-header">Certifications</h2>', unsafe_allow_html=True)
    
    cert_col1, cert_col2 = st.columns(2)
    
    with cert_col1:
        with st.container():
            st.markdown("**AI Concepts and Technique**")
            st.markdown("NPTEL")
            st.markdown("Issued: 2025| No Expiration")
        
        with st.container():
            st.markdown("**Microsenor,Implantable Devices and Rodent Surgeries for Biomedical Application**")
            st.markdown("NPTEL")
            st.markdown("Issued: 2025| No Expiration")
    
    with cert_col2:
        with st.container():
            st.markdown("**MongoDB Basics for Student**")
            st.markdown("MongoDB server")
            st.markdown("Issued: 2022 | No Expiration")
        
        with st.container():
            st.markdown("**Introduction to Formatting**")
            st.markdown("Linkedin Learning")
            st.markdown("Issued: 2023 | No Expiration")

else:  # Contact page
    st.markdown('<h1 class="main-header">Contact Me</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Get In Touch
        
        I'm always interested in hearing about new opportunities, 
        collaborations, or just chatting about technology and innovation.
        
        **Availability:** Currently open to freelance projects and full-time opportunities
        
        **Preferred Contact Method:** Email or LinkedIn
        """)
        
        st.markdown("---")
        
        # Contact form
        st.markdown("### Send a Message")
        
        with st.form("contact_form"):
            name = st.text_input("Name")
            email = st.text_input("Email")
            subject = st.selectbox("Subject",
                        ["Project Inquiry", "Job Opportunity", "Collaboration", "Other"])
            message = st.text_area("Message", height=150)
            
            submitted = st.form_submit_button("Send Message")
            
            if submitted:
                if name and email and message:
                    st.success("Message sent successfully! I'll get back to you soon.")
                else:
                    st.error("Please fill in all required fields.")
    
    with col2:
        st.markdown("### Contact Information")
        st.markdown("📧 **Email:** harini.rajendiran18@gmail.com")
        st.markdown("📱 **Phone:** +91 8667620398")
        st.markdown("💼 **LinkedIn:** https://www.linkedin.com/in/harini-rajendiran-b23857257/")
        st.markdown("🐙 **GitHub:** https://github.com/Harinirajendiran")
        st.markdown("📍 **Location:** Tamil Nadu,India")

# Footer
st.markdown("---")
footer_col1, footer_col2, footer_col3 = st.columns(3)
with footer_col2:
    st.markdown("<p style='text-align: center; color: gray;'>© 2025 Harini Rajendiran. All rights reserved.</p>", unsafe_allow_html=True)