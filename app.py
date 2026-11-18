
import streamlit as st
from ai_engine import solve_real_life_problem

st.set_page_config(
    page_title="AI Helper",
    page_icon="✳",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------- DESIGN ----------
with open("style.css", encoding="utf-8") as css_file:
    st.markdown(
        f"<style>{css_file.read()}</style>",
        unsafe_allow_html=True
    )


# ---------- HEADER ----------
st.markdown("""
<div class="logo">✳ AI HELPER</div>

<div class="hero">
    <h1>Every problem has<br>a mathematical solution.</h1>
    <p>
        Explore the mathematics behind everyday life.<br>
        Ask a question. Understand the logic. Find the solution.
    </p>
</div>
""", unsafe_allow_html=True)


# ---------- QUESTION AREA ----------


st.markdown("### What would you like to solve?")

question = st.text_area(
    "Your question",
    placeholder="For example: How much money can I save if I save ₹50 every day for one year?",
    height=120,
    label_visibility="collapsed",
    key="main_question_box"
)

ask = st.button("✳  Solve with Mathematics", use_container_width=True)





# ---------- AI RESPONSE (INLINE) ----------

selected = st.session_state.get("selected_question", "")
final_question = selected or question

if ask and not question.strip():
    st.warning("Please enter a question first.")

if (ask and question.strip()) or selected:

    st.session_state.selected_question = ""

    with st.container(key="answer_card"):

        st.markdown("### Mathematical Solution")

        with st.spinner("Thinking through the mathematics..."):

            try:
                api_key = st.secrets["GEMINI_API_KEY"]

                answer = solve_real_life_problem(
                    final_question,
                    api_key
                )

                st.markdown(answer)

            except Exception as error:
                st.error("AI Helper is temporarily unavailable.")
                st.caption(str(error))


# ---------- EXAMPLES ----------
st.markdown("### Explore everyday mathematics")

examples = [
    "How do I calculate a 20% discount on ₹1,500?",
    "How much paint do I need for my bedroom?",
    "How long will it take to travel 30 km at 60 km/h?",
    "How much can I save by saving ₹50 every day?"
]

for i in range(0, len(examples), 2):
    col1, col2 = st.columns(2)

    with col1:
        if st.button(examples[i], key=f"example_{i}", use_container_width=True):
            st.session_state.selected_question = examples[i]
            st.rerun()

    with col2:
        if st.button(examples[i+1], key=f"example_{i+1}", use_container_width=True):
            st.session_state.selected_question = examples[i+1]
            st.rerun()


# ---------- FOOTER ----------
st.markdown("""
<div class="footer">
    THINK MATHEMATICALLY. SOLVE PRACTICALLY.<br><br>
    AI HELPER © 2026
</div>
""", unsafe_allow_html=True)


