import streamlit as st

# Set page title and icon
st.set_page_config(page_title="Student Portfolio", page_icon="🎓")

# Sidebar navigation
st.sidebar.title("📍 Navigation")
page = st.sidebar.radio("Go To:", ["Home", "Projects", "Skills", "Settings", "Contact"])

# Home section
if page == "Home":
    st.title("🎓 Student Portfolio")

    # Profile image upload
    uploaded_image = st.file_uploader("Upload Profile Picture", type=["jpg", "png"])
    if uploaded_image is not None:
        st.image(uploaded_image, width=150, caption="Uploaded image")
    else:
        st.image("person.jpeg", width=150, caption="Default image")

    # Student details (Editable!)
    name = st.text_input("Name: ", "NIYONSENGA Philimine")
    location = st.text_input("Location: ", "Rwamagana, Rwanda")
    field_of_study = st.text_input("Field of Study: ", "Computer Science, SWE (year 3)")
    university = st.text_input("University: ", "INES - Ruhengeri")

    st.write(f"📍 {location}")
    st.write(f"📚 {field_of_study}")
    st.write(f"🎓 {university}")

    # Resume download button
    with open("resume.pdf", "rb") as file:
        resume_bytes = file.read()
    st.download_button(label="📄 Download Resume", data=resume_bytes, file_name="resume.pdf", mime="application/pdf")

    st.markdown("---")
    st.subheader("About Me")
    about_me = st.text_area("Short introduction about myself:", "I am a passionate AI engineer!")
    st.write(about_me)

# Projects section
elif page == "Projects":
    st.title("💻 My Projects")

    # Add interactive project details with GitHub links
    with st.expander("📖 Attendance Management System"):
        st.write("Project Type: (Individual)")
        st.write("Brief Description: (Updating student's list by adding/removing students and marking attendance/absence)")
        st.write("🔗 [View on GitHub](https://github.com/YourGitHub/attendance-system)")

    with st.expander("🏡 Stock Management"):
        st.write("Project Type: (Group work)")
        st.write("Description: (Managing product movement in stock, including deleting/adding products and handling import/export reports)")
        st.write("🔗 [View on GitHub](https://github.com/YourGitHub/stock-management)")

    with st.expander("🩸 Blood Donation Website"):
        st.write("Project Type: (Final Year Project / Dissertation)")
        st.write("Description: (This system streamlines the blood donation process by allowing potential donors to register and verify their eligibility online.)")
        st.write("🔗 [View on GitHub](https://github.com/YourGitHub/blood-donation)")

# Skills section
elif page == "Skills":
    st.title("🏹 Skills and Achievements")

    # Programming Skills with Progress Bars
    st.subheader("Programming Languages")
    skill_python = st.slider("Python", 10, 100, 90)
    st.progress(skill_python / 100)
    skill_js = st.slider("JavaScript", 0, 100, 75)
    st.progress(skill_js / 100)
    skill_sql = st.slider("SQL", 0, 100, 65)
    st.progress(skill_sql / 100)

    st.subheader("Machine Learning")
    skill_ds = st.slider("Data Science", 20, 100, 80)
    st.progress(skill_ds / 100)

    st.subheader("Web Development")
    skill_html = st.slider("HTML", 20, 100, 80)
    st.progress(skill_html / 100)
    skill_css = st.slider("CSS", 20, 100, 80)
    st.progress(skill_css / 100)
    skill_react = st.slider("React", 20, 100, 80)
    st.progress(skill_react / 100)
    skill_flask = st.slider("Flask", 20, 100, 80)
    st.progress(skill_flask / 100)

    st.subheader("Certifications & Achievements")
    st.write("✅ Completed Microsoft Office Specialist in PowerPoint, Word, and Excel")
    st.write("✅ Certified achievement for being in the third place at the Science Club Web Design Competition @ Agahozo Shalom Youth Village")

# Settings section for profile customization
elif page == "Settings":
    st.title("🎨 Customize your profile")

    # Upload profile picture
    st.subheader("Upload a Profile Picture")
    uploaded_image = st.file_uploader("Choose a file", type=["jpg", "png"])
    if uploaded_image:
        st.image(uploaded_image, width=150)

    # Edit personal info
    st.subheader("✍ Edit Personal Info")
    new_name = st.text_input("Name", "NIYONSENGA Philimine")
    new_bio = st.text_area("Short Bio", "I am a passionate AI engineer!")
    if st.button("Save Changes"):
        st.success("Profile Updated Successfully!")

# Contact section
elif page == "Contact":
    st.title("🤳 Contact Me")

    # Contact form with form submission
    with st.form("contact_form"):
        contact_name = st.text_input("Your Name")
        contact_email = st.text_input("Your Email")
        message = st.text_area("Your Message 💌")

        submitted = st.form_submit_button("Send Message")
        if submitted:
            st.success("✅ Message sent successfully!")

    st.write("📧 Email: philiminiyo1@gmail.com")
    st.write("[🔗 LinkedIn](https://www.linkedin.com/feed/)")
    st.write("[📂 GitHub](https://phinah2020.rw)")

st.sidebar.write("---")
st.sidebar.write("🔹 Made with ❤ using My Watermelon")
