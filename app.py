import streamlit as st

def page_one():
    st.title("User Information - Page 1")
    st.markdown("---")

    name = st.text_input("Full Name")
    roll_no = st.text_input("Roll Number")
    gender = st.text_input("Gender")

    if st.button("Next", key='next_button'):
        user_info['Full Name'] = name
        user_info['Roll Number'] = roll_no
        user_info['Gender'] = gender
        st.session_state['page'] = 2

def page_two():
    st.title("User Information - Page 2")
    st.markdown("---")

    father_name = st.text_input("Father's Full Name")
    mother_name = st.text_input("Mother's Full Name")
    department = st.text_input("Department")
    specialization = st.text_input("Specialization")

    if st.button("Next", key='next_button'):
        user_info["Father's Full Name"] = father_name
        user_info["Mother's Full Name"] = mother_name
        user_info['Department'] = department
        user_info['Specialization'] = specialization
        st.session_state['page'] = 3

def page_three():
    st.title("User Information - Page 3")
    st.markdown("---")

    phone_no = st.text_input("Contact Number")
    aadhar_no = st.text_input("Aadhar Number")
    year_of_study = st.text_input("Year of Study")

    if st.button("Submit", key='submit_button'):
        user_info['Contact Number'] = phone_no
        user_info['Aadhar Number'] = aadhar_no
        user_info['Year of Study'] = year_of_study
        st.success("User Information Submitted Successfully!")

# Main function to control page navigation
def main():
    global user_info
    user_info = {}

    page = st.session_state.get('page', 1)

    if page == 1:
        page_one()
    elif page == 2:
        page_two()
    elif page == 3:
        page_three()

if __name__ == "__main__":
    st.markdown(
        """
        <style>
            .reportview-container .main .block-container {
                padding-top: 0px;
            }
            .reportview-container .main {
                max-width: 600px;
                padding-left: 50px;
                padding-right: 50px;
                display: flex;
                flex-direction: column;
                align-items: center;
            }
            .btn-outline-secondary {
                color: #fff;
                background-color: #008cba;
                border-color: #008cba;
                margin-top: 20px;
            }
            .btn-outline-secondary:hover {
                background-color: #005f79;
                border-color: #005f79;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    main()
