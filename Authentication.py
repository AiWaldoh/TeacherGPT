import streamlit as st
 
def check_password():
        """Returns `True` if the user had the correct password."""

        def password_entered():
            """Checks whether a password entered by the user is correct."""
            if st.session_state["password"] == st.secrets["password"]:
                st.session_state["password_correct"] = True
                del st.session_state[
                    "password"
                ]  # Don't store password in session_state
            else:
                st.session_state["password_correct"] = False

        # Check if "password_correct" is in the session state
        if "password_correct" not in st.session_state:
            # If not present, it's the first run. Show the input field for the password.
            st.text_input(
                "Mot de passe",
                type="password",
                on_change=password_entered,
                key="password",
            )
            return False
        elif not st.session_state["password_correct"]:
            # If password is incorrect, show the input field again + error message.
            st.text_input(
                "Password", type="password", on_change=password_entered, key="password"
            )
            st.error("😕 Mot de passe incorrect")
            return False
        else:
            # Password is correct. Do not display the password input field.
            return True
