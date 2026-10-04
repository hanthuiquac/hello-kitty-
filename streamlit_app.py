import random
import streamlit as st

st.set_page_config(
    page_title="Cute Makeup Game", page_icon="💗", layout="centered"
)

# =========================
# CSS
# =========================
st.markdown(
    """
<style>
.stApp {
    background: linear-gradient(135deg, #ffd6ec, #fff0f8);
}

.title {
    text-align: center;
    color: #ff4fa3;
    font-size: 42px;
    font-weight: bold;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #9b4d78;
    font-size: 18px;
}

.card {
    background: rgba(255,255,255,0.85);
    border-radius: 30px;
    padding: 25px;
    box-shadow: 0 8px 25px rgba(255,80,160,0.2);
    text-align: center;
}

.face {
    width: 260px;
    height: 260px;
    margin: auto;
    background: #fffdf8;
    border: 6px solid #333;
    border-radius: 48% 48% 45% 45%;
    position: relative;
}

.ear1, .ear2 {
    position: absolute;
    width: 70px;
    height: 70px;
    background: #fffdf8;
    border: 6px solid #333;
    top: -25px;
}

.ear1 {
    left: 15px;
    transform: rotate(-35deg);
    border-radius: 15px 45px 10px 35px;
}

.ear2 {
    right: 15px;
    transform: rotate(35deg);
    border-radius: 45px 15px 35px 10px;
}

.eye {
    position: absolute;
    width: 18px;
    height: 28px;
    background: #111;
    border-radius: 50%;
    top: 105px;
}

.eye1 { left: 65px; }
.eye2 { right: 65px; }

.nose {
    position: absolute;
    top: 145px;
    left: 50%;
    transform: translateX(-50%);
    width: 27px;
    height: 19px;
    background: #ffbd32;
    border: 4px solid #111;
    border-radius: 50%;
}

.bow {
    position: absolute;
    top: 25px;
    right: 15px;
    font-size: 65px;
}

.makeup {
    font-size: 45px;
    margin-top: 10px;
}

.score {
    color: #ff3f98;
    font-size: 25px;
    font-weight: bold;
}

.stButton > button {
    border-radius: 20px;
    border: none;
    background: #ff69b4;
    color: white;
    font-weight: bold;
    padding: 10px 25px;
}

.stButton > button:hover {
    background: #ff3f98;
    color: white;
}
</style>
""",
    unsafe_allow_html=True,
)

# =========================
# SESSION
# =========================
if "score" not in st.session_state:
    st.session_state.score = 0

if "look" not in st.session_state:
    st.session_state.look = {"mascara": "❌", "blush": "❌", "lip": "❌"}

if "target" not in st.session_state:
    st.session_state.target = random.choice([
        "🎀 Pink Princess",
        "🌸 Sweet Girl",
        "✨ Sparkle Queen",
        "🍓 Strawberry",
    ])

# =========================
# TITLE
# =========================
st.markdown(
    '<div class="title">💗 CUTE MAKEUP GAME 💗</div>', unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Trang điểm cho cô mèo đáng yêu của bạn ✨</div>',
    unsafe_allow_html=True,
)

st.write("")

# =========================
# TARGET
# =========================
st.markdown(
    f"""
    <div class="card">
        <h3>🎯 Chủ đề hôm nay</h3>
        <h2>{st.session_state.target}</h2>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")

# =========================
# CHARACTER
# =========================
mascara = st.session_state.look["mascara"]
blush = st.session_state.look["blush"]
lip = st.session_state.look["lip"]

st.markdown(
    f"""
    <div class="card">
        <div class="face">
            <div class="ear1"></div>
            <div class="ear2"></div>

            <div class="bow">🎀</div>

            <div class="eye eye1"></div>
            <div class="eye eye2"></div>

            <div class="nose"></div>
        </div>

        <div class="makeup">
            👁️ {mascara}
            &nbsp;&nbsp;
            🌸 {blush}
            &nbsp;&nbsp;
            💄 {lip}
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")

# =========================
# MAKEUP OPTIONS
# =========================
st.subheader("💄 Chọn đồ trang điểm")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 👁️ Mascara")

    if st.button("🖤 Black", use_container_width=True):
        st.session_state.look["mascara"] = "🖤"
        st.session_state.score += 10

    if st.button("💗 Pink", use_container_width=True):
        st.session_state.look["mascara"] = "💗"
        st.session_state.score += 15

with col2:
    st.markdown("### 🌸 Blush")

    if st.button("🌸 Pink", use_container_width=True):
        st.session_state.look["blush"] = "🌸"
        st.session_state.score += 15

    if st.button("🍑 Peach", use_container_width=True):
        st.session_state.look["blush"] = "🍑"
        st.session_state.score += 10

with col3:
    st.markdown("### 💄 Lip")

    if st.button("💗 Pink Lip", use_container_width=True):
        st.session_state.look["lip"] = "💗"
        st.session_state.score += 15

    if st.button("❤️ Red Lip", use_container_width=True):
        st.session_state.look["lip"] = "❤️"
        st.session_state.score += 10

# =========================
# SCORE
# =========================
st.write("")

st.markdown(
    f'<div class="score">⭐ Điểm của bạn: {st.session_state.score}</div>',
    unsafe_allow_html=True,
)

# =========================
# FINISH
# =========================
if st.button("✨ HOÀN THÀNH ✨", use_container_width=True):

    if (
        st.session_state.look["mascara"] != "❌"
        and st.session_state.look["blush"] != "❌"
        and st.session_state.look["lip"] != "❌"
    ):
        st.balloons()

        st.success("🎉 Hoàn thành! Cô mèo của bạn thật xinh!")

        if st.session_state.score >= 40:
            st.write("💖 Bạn nhận được danh hiệu: **MAKEUP QUEEN 👑**")
        else:
            st.write("🌸 Bạn nhận được danh hiệu: **CUTE GIRL 🎀**")
    else:
        st.warning("💄 Hãy chọn đủ mascara, má hồng và son nhé!")

# =========================
# RESET
# =========================
if st.button("🔄 Chơi lại", use_container_width=True):

    st.session_state.score = 0

    st.session_state.look = {"mascara": "❌", "blush": "❌", "lip": "❌"}

    st.session_state.target = random.choice([
        "🎀 Pink Princess",
        "🌸 Sweet Girl",
        "✨ Sparkle Queen",
        "🍓 Strawberry",
    ])

    st.rerun()
