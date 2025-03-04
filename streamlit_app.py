import streamlit as st
import clips

env = clips.Environment()
env.eval("(assert (v 2))")

for i in env.facts():
    st.write(i)

st.title("🎈 My new app2")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
