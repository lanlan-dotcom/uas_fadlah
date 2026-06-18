import streamlit as st
import base64

from nodes import start

def load_css():
    with open("styles/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Horror Survival Fadlah",
    layout="centered"
)

load_css()

#css horor
st.markdown("""
<style>

/* Tombol */
.stButton > button {
    background-color: #330000;
    color: white;
    border: 2px solid #ff0000;
    border-radius: 10px;
    font-weight: bold;
    width: 100%;
}

/* Saat mouse diarahkan */
.stButton > button:hover {
    background-color: #990000;
    color: white;
    box-shadow: 0px 0px 15px red;
}

</style>
""", unsafe_allow_html=True)


st.markdown("""
    <style>

    .stApp {
        background-color: #0d0d0d;
        color: white;
    }

    </style>
    """, unsafe_allow_html=True)

# =========================
# AUDIO FUNCTION
# =========================

def autoplay_audio(file_path):

    with open(file_path, "rb") as f:
        data = f.read()

    b64 = base64.b64encode(data).decode()

    audio_html = f"""
    <audio autoplay loop hidden>
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    </audio>
    """

    st.iframe(
        audio_html,
        height=100
    )

# =========================
# SESSION STATE
# =========================

if "current_node" not in st.session_state:
    st.session_state.current_node = start

if "path" not in st.session_state:
    st.session_state.path = []

if "game_started" not in st.session_state:
    st.session_state.game_started = False

# =========================
# START SCREEN
# =========================


if not st.session_state.game_started:

    st.markdown("""
    <div style="
        text-align:center;
        color:#ff3333;
        letter-spacing:4px;
        font-weight:bold;
        margin-bottom:20px;
    ">
    🔴 HORROR PATH • DECISION GAME
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <h1 style="
        text-align:center;
        color:white;
        font-size:50px;
        letter-spacing:2px;
    ">
        THE HOUSE I
        <span class="glow-red">WOKE UP</span>
        IN
    </h1>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p style="
        text-align:center;
        color:#aaaaaa;
        font-size:18px;
        margin-bottom:30px;
    ">
    Tersesat di rumah berhantu tua terkutuk.<br>
    Setiap keputusan menentukan hidup atau mati.
    </p>
    """, unsafe_allow_html=True)

    st.image(
        "asset/image/rumah.png",
        use_container_width=True
    )

    st.error("""
🎧 Rekomendasi Utama:
Gunakan headphone atau headset dan aktifkan volume audio
untuk pengalaman horror yang lebih imersif.
""")

    if st.button("🎮 MEMULAI PETUALANGAN"):
        st.session_state.game_started = True
        st.rerun()

    st.stop()

# =========================
# CURRENT NODE
# =========================

current = st.session_state.current_node

# =========================
# TITLE
# =========================

st.markdown("""
<h1 class="game-title">
The House I Woke Up In
</h1>
""", unsafe_allow_html=True)

# =========================
# SOUND
# =========================

if current.sound:
    autoplay_audio(current.sound)

# =========================
# GAMBAR
# =========================

if current.image:

    st.image(
        current.image,
        use_container_width=True
    )

# =========================
# CERITA
# =========================

st.markdown(f"""
<div class="story-box">
{current.text}
</div>
""", unsafe_allow_html=True)

# =========================
# PILIHAN
# =========================

if not current.ending:

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div style="
    color:#888;
    letter-spacing:3px;
    margin-bottom:15px;
    font-size:14px;
    ">
    🔴 TENTUKAN PILIHANMU
    </div>
    """, unsafe_allow_html=True)

    btn1, btn2 = st.columns(2)

    with btn1:

        if st.button(current.choice1):

            next_node = current.next1

            st.session_state.path.append({
                "room": current.title,
                "choice": current.choice1
            })

            if next_node.ending:
                st.session_state.path.append({
                    "room": next_node.title,
                    "choice": "GAME OVER"
                })

            st.session_state.current_node = next_node
            st.rerun()

    with btn2:

        if st.button(current.choice2):

            next_node = current.next2

            st.session_state.path.append({
                "room": current.title,
                "choice": current.choice2
            })

            if next_node.ending:
                st.session_state.path.append({
                    "room": next_node.title,
                    "choice": "GAME OVER"
            })

            st.session_state.current_node = next_node
            st.rerun()

# =========================
# ENDING
# =========================

if current.ending:

    st.error("🎮 GAME SELESAI")

    st.subheader("🗺️ ALUR RIWAYAT KEPUTUSAN")

    for i, step in enumerate(st.session_state.path, start=1):

        with st.container(border=True):

            st.caption(f"LANGKAH {i}")

            st.markdown(
                f"### {step['room']}"
            )

            st.markdown(
                f"➜ **{step['choice']}**"
            )

    if st.button(
        "🔄 MAIN LAGI",
        use_container_width=True
    ):
        st.session_state.current_node = start
        st.session_state.path = []
        st.session_state.game_started = False
        st.rerun()