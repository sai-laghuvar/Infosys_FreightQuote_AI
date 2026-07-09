
import streamlit as st
import json
import hashlib
import jwt
import datetime
import os
from email_validator import validate_email, EmailNotValidError
import re
import random
import smtplib
import ssl
from email.message import EmailMessage

USER_FILE = "users.json"
JWT_SECRET = os.environ.get("JWT_SECRET")

JWT_ALGORITHM = "HS256"

EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")


def load_users():

    if not os.path.exists(USER_FILE):
        return {}

    with open(USER_FILE, "r") as file:
        return json.load(file)


def save_users(users):

    with open(USER_FILE, "w") as file:
        json.dump(users, file, indent=4)


def hash_password(password):

    return hashlib.sha256(password.encode()).hexdigest()

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = hash_password("Admin@123")

def generate_token(username):

    payload = {

        "username": username,

        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)

    }

    token = jwt.encode(
        payload,
        JWT_SECRET,
        algorithm=JWT_ALGORITHM
    )

    return token


def verify_token(token):

    try:

        payload = jwt.decode(
            token,
            JWT_SECRET,
            algorithms=[JWT_ALGORITHM]
        )

        return payload

    except:

        return None

# =====================================================
# SEND OTP EMAIL
# =====================================================

def send_otp_email(receiver_email, otp):

    try:

        subject = "Password Reset OTP"

        body = f"""
Hello,

Your OTP for resetting your password is:

{otp}

This OTP is valid for 5 minutes.

Regards,
Secure User Authentication System
"""

        message = EmailMessage()

        message["Subject"] = subject
        message["From"] = EMAIL_ADDRESS
        message["To"] = receiver_email

        message.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:

            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

            smtp.send_message(message)

        return True

    except Exception as e:

        st.error(f"Email Error: {e}")

        return False
# =====================================================
# OTP FUNCTIONS
# =====================================================

OTP_FILE = "otp_storage.json"

def load_otps():

    if not os.path.exists(OTP_FILE):
        return {}

    with open(OTP_FILE, "r") as file:
        return json.load(file)


def save_otps(otps):

    with open(OTP_FILE, "w") as file:
        json.dump(otps, file, indent=4)


def generate_otp():

    return str(random.randint(100000, 999999))
# =====================================================
# VALIDATION FUNCTIONS
# =====================================================

def is_valid_email(email):

    try:
        validate_email(email)
        return True

    except EmailNotValidError:
        return False


def is_strong_password(password):

    if len(password) < 8:
        return False

    if not re.search(r"[A-Z]", password):
        return False

    if not re.search(r"[a-z]", password):
        return False

    if not re.search(r"[0-9]", password):
        return False

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False

    return True

from streamlit_option_menu import option_menu

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------

st.set_page_config(
    page_title="Smart Authentication Portal",
    page_icon="🔐",
    layout="centered"
)

# -----------------------------
# Session State Initialization
# -----------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

if "token" not in st.session_state:
    st.session_state.token = None

# -------------------------------------------------
# Custom CSS
# -------------------------------------------------
st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<style>

/* ==========================
Main Background
========================== */

.stApp{

background:
linear-gradient(
135deg,
#081229 0%,
#0F1E4A 45%,
#19376D 100%
);

}


/* ==========================
Titles
========================== */

h1{
    color:#60A5FA;
    text-align:center;
    font-weight:800;
}

h2,h3{
    color:#93C5FD;
}

/* ==========================
Normal Text
========================== */

p,label,span{
    color:#F8FAFC !important;
}

/* ==========================
Input Boxes
========================== */

.stTextInput input{

    background:white !important;
    
    color:#111827 !important;
    
    border:2px solid #2563EB !important;

    border-radius:12px !important;

}

.stTextInput input:focus{

    border:2px solid #60A5FA !important;

}

/* ==========================
Select Box
========================== */

.stSelectbox{

    color:white;

}

/* ==========================
Buttons
========================== */

.stButton>button{

    width:100%;

    height:48px;

    border:none;

    border-radius:12px;

    background: linear-gradient(
    90deg,
    #2563EB,
    #3B82F6,
    #60A5FA);

    color:white;

    font-size:17px;

    font-weight:bold;

    transition:0.3s;

}

.stButton>button:hover{

    background:linear-gradient(90deg,#3B82F6,#2563EB);

    transform:scale(1.03);

}

/* ==========================
Sidebar/Menu
========================== */

section[data-testid="stSidebar"]{

    background:#111827;

}

/* ==========================
Success/Error/Warning
========================== */

.stSuccess,
.stWarning,
.stError{

    border-radius:12px;

}

/* ==========================
Login Card
========================== */

div[data-testid="stVerticalBlock"] > div:has(.login-card){

    background:#14213D;

    padding:35px;

    border-radius:22px;

    border:1px solid rgba(255,255,255,0.08);

    box-shadow:0px 10px 35px rgba(0,0,0,0.45);

}

/* ==========================
Hide Footer
========================== */

footer{

    visibility:hidden;

}

header[data-testid="stHeader"]{
    background: #0B1120;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Navigation
# -------------------------------------------------

if st.session_state.logged_in:

    selected = option_menu(
        menu_title=None,
        options=["Dashboard", "Logout"],
        icons=["house-fill", "box-arrow-right"],
        orientation="horizontal",
        default_index=0
    )

else:

    selected = option_menu(
        menu_title=None,
        options=["Login", "Signup", "Forgot Password", "Admin"],
        icons=["box-arrow-in-right", "person-plus", "key", "shield-lock"],
        orientation="horizontal",
        default_index=0
    )

st.markdown("""
<h1>
🚚 Infosys FreightQuote
</h1>

<p style='text-align:center;
color:#CBD5E1;
font-size:18px;'>

Smart Logistics Quotation & Authentication Portal

</p>
""", unsafe_allow_html=True)


# =====================================================
# LOGIN PAGE
# =====================================================

if selected=="Login":

    st.subheader("🔑 User Login")
    

    login_input = st.text_input(
        "Username / Email *",
        placeholder="Enter Username or Email"
    ).strip()

    password = st.text_input(
        "Password *",
        type="password",
        placeholder="Enter Password"
    )

    remember = st.checkbox("Remember Me")

    login = st.button("Login")

    if login:

        if login_input == "" or password == "":

            st.warning("Please fill all mandatory fields.")

        else:

            users = load_users()

            login_success = False
            logged_user = ""

            for username, details in users.items():

                if (
                    login_input.lower() == username.lower()
                    or login_input.lower() == details["email"].lower()
                    ):

                    if details["password"] == hash_password(password):

                        login_success = True
                        logged_user = username
                        break

            if login_success:
              token = generate_token(logged_user)

              st.session_state.logged_in = True
              st.session_state.username = logged_user
              st.session_state.token = token

              st.success(f"Welcome, {logged_user}!")
              st.rerun()

            else:
              st.error("Invalid Username or Password")
            

# =====================================================
# SIGNUP PAGE
# =====================================================

elif selected=="Signup":

    st.subheader("Create New Account")

    username = st.text_input(
        "Username *",
        placeholder="Enter Username"
    ).strip()

    email = st.text_input(
        "Email Address *",
        placeholder="Enter Email"
    ).strip().lower()

    password = st.text_input(
        "Password *",
        type="password",
        placeholder="Enter Password"
    )

    confirm_password = st.text_input(
        "Confirm Password *",
        type="password",
        placeholder="Confirm Password"
    )

    security_question = st.selectbox(
        "Security Question *",
        [
            "Select a Question",
            "What is your favourite teacher's name?",
            "What was your first school?",
            "What is your favourite movie?",
            "What is your favourite food?",
            "What is your pet's name?"
        ]
    )

    security_answer = st.text_input(
        "Security Answer *",
        placeholder="Enter your answer"
    ).strip()

    signup = st.button("Create Account")
    if signup:
      users = load_users()
      # Check empty fields
      if username == "" or email == "" or password == "" or confirm_password == "" or security_answer == "":
        st.warning("Please fill all mandatory fields.")
      elif security_question == "Select a Question":
        st.warning("Please select a security question.")
      elif password != confirm_password:
        st.error("Passwords do not match.")
      elif not is_valid_email(email):
        st.error("Please enter a valid email address.")
      elif not is_strong_password(password):
        st.error("Password must be at least 8 characters and contain uppercase, lowercase, number and special character.")
      elif len(username) < 4:
        st.error("Username must contain at least 4 characters.")
      elif username in users:
        st.error("Username already exists.")

      else:
          # Check duplicate email
          email_exists = False
          for user in users.values():

            if user["email"].lower() == email.lower():

                email_exists = True
                break
          if email_exists:
            st.error("Email already registered.")
          else:
            users[username] = {

                "email": email.lower(),
                "password": hash_password(password),
                "security_question": security_question,
                "security_answer": security_answer

            }

            save_users(users)

            st.success("🎉 Account created successfully!")

# =====================================================
# FORGOT PASSWORD PAGE
# =====================================================

elif selected=="Forgot Password":

    st.subheader("Reset Your Password")

    recovery_option = st.radio(
        "Choose Recovery Method",
        [
            "Security Question",
            "Email OTP"
        ]
    )

    st.markdown("---")

    # -----------------------------
    # Security Question UI
    # -----------------------------

    if recovery_option == "Security Question":

        username = st.text_input(
            "Username *",
            placeholder="Enter Username"
        ).strip().lower()

        users = load_users()

        question = "User not found"

        if username in users:

          question = users[username]["security_question"]

        st.selectbox(
            "Security Question",
             [question],
             disabled=True
            )

        answer = st.text_input(
            "Security Answer *",
            placeholder="Enter Security Answer"
        )

        new_password = st.text_input(
            "New Password *",
            type="password"
        )

        confirm_password = st.text_input(
            "Confirm Password *",
            type="password"
        )

        reset_password = st.button("Reset Password")

        if reset_password:

          users = load_users()

          if username not in users:

            st.error("Username not found.")

          elif answer.strip().lower() != users[username]["security_answer"].strip().lower():

            st.error("Incorrect security answer.")

          elif new_password != confirm_password:

            st.error("Passwords do not match.")

          elif not is_strong_password(new_password):

            st.error(
                "Password must contain uppercase, lowercase, number and special character."
                )

          else:

            users[username]["password"] = hash_password(new_password)

            save_users(users)

            st.success("✅ Password reset successfully using Security Question.")

    # -----------------------------
    # Email OTP UI
    # -----------------------------

    else:

        email = st.text_input(
            "Registered Email *",
            placeholder="Enter Registered Email"
        )

        send_otp = st.button("Send OTP")

        if send_otp:
          users = load_users()

          email_found = False

          for username, details in users.items():
            if details["email"].lower() == email.lower():
              email_found = True

              otp = generate_otp()

              otps = load_otps()

              otps[email.lower()] = otp

              save_otps(otps)

              if send_otp_email(email.lower(), otp):
                st.success("OTP sent successfully to your registered email.")

              else:

                st.error("Failed to send OTP.")

              break
          if not email_found:

            st.error("Email is not registered.")


        otp = st.text_input(
            "Enter OTP"
        )

        new_password = st.text_input(
            "New Password *",
            type="password",
            key="otp_new_password"
        )

        confirm_password = st.text_input(
            "Confirm Password *",
            type="password",
            key="otp_confirm_password"
        )

        verify_otp = st.button("Verify OTP & Reset Password")

        if verify_otp:

          otps = load_otps()

          users = load_users()

          # Check OTP
          if email.lower() not in otps:

            st.error("Please generate OTP first.")

          elif otps[email.lower()] != otp:

            st.error("Invalid OTP.")

          elif new_password != confirm_password:

            st.error("Passwords do not match.")

          elif not is_strong_password(new_password):

            st.error(
            "Password must contain uppercase, lowercase, number and special character."
            )

          else:

            for username, details in users.items():

              if details["email"].lower() == email.lower():

                users[username]["password"] = hash_password(new_password)

                break

            save_users(users)

            del otps[email.lower()]

            save_otps(otps)

            st.success("✅ Password reset successfully.")

# =====================================================
# ADMIN LOGIN
# =====================================================

elif selected == "Admin":

    st.subheader("🛡 Admin Login")

    admin_user = st.text_input(
        "Admin Username"
    ).strip()

    admin_pass = st.text_input(
        "Admin Password",
        type="password"
    )

    admin_login = st.button("Login as Admin")

    if admin_login:

        if (
            admin_user == ADMIN_USERNAME
            and hash_password(admin_pass) == ADMIN_PASSWORD
        ):

            st.success("Admin Login Successful")

            users = load_users()

            st.markdown("## Registered Users")

            st.write(f"Total Users : {len(users)}")

            st.markdown("---")

            if len(users) == 0:

                st.info("No users registered.")

            else:

                for username, details in users.items():

                    st.write(f"👤 Username : {username}")

                    st.write(f"📧 Email : {details['email']}")

                    st.markdown("---")

        else:

            st.error("Invalid Admin Credentials")

st.markdown("---")
st.caption("Developed by Sai Laghuvar | Infosys Springboard 7.0")

# =====================================================
# USER DASHBOARD
# =====================================================

if st.session_state.logged_in:

    st.markdown("---")

    st.header("🏠 User Dashboard")

    st.success(f"Welcome, {st.session_state.username}")

    st.write("You have successfully logged in.")

    st.write("JWT Authentication Successful ✅")

    st.markdown("### Account Details")

    users = load_users()

    if st.session_state.username in users:

        st.write(f"**Username:** {st.session_state.username}")
        st.write(f"**Email:** {users[st.session_state.username]['email']}")

# =====================================================
# LOGOUT
# =====================================================

if selected == "Logout":

    st.session_state.logged_in = False
    st.session_state.username = ""
    st.session_state.token = None

    st.success("Logged out successfully.")

    st.rerun()
