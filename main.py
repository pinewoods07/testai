import streamlit as st
import anthropic
import json
import os
import hashlib
from datetime import datetime

# ── 페이지 설정 ────────────────────────────────────────────────
st.set_page_config(
    page_title="창작 AI 어시스턴트",
    page_icon="📖",
    layout="wide",
)

# ── 테마 CSS ───────────────────────────────────────────────────
LIGHT_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700&family=Playfair+Display:wght@400;700&display=swap');
.stApp { background: #f8f7f4; font-family: 'Noto Sans KR', sans-serif; }
.main .block-container {
    background: #ffffff; border-radius: 16px; border: 1px solid #e8e3dc;
    padding: 2rem 2.5rem; box-shadow: 0 2px 20px rgba(0,0,0,0.06);
}
[data-testid="stSidebar"] { background: #faf9f6 !important; border-right: 1px solid #e8e3dc; }
[data-testid="stSidebar"] .stMarkdown p, [data-testid="stSidebar"] label { color: #4a4540 !important; }
h1 { font-family: 'Playfair Display', serif !important; color: #2c2420 !important; letter-spacing: 1px; }
h2, h3 { color: #3d3530 !important; }
.stTabs [data-baseweb="tab-list"] {
    background: #f0ede8; border-radius: 12px; padding: 4px; gap: 4px; border: 1px solid #e0dbd4;
}
.stTabs [data-baseweb="tab"] { border-radius: 8px; color: #7a706a !important; font-weight: 500; transition: all 0.2s ease; padding: 8px 20px; }
.stTabs [aria-selected="true"] { background: #ffffff !important; color: #2c2420 !important; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
[data-testid="stChatMessage"] { border-radius: 14px; padding: 1rem; margin-bottom: 0.8rem; animation: fadeInUp 0.3s ease; border: 1px solid transparent; }
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) { background: #f0ede8; border-color: #e0dbd4; }
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) { background: #fdfcfb; border-color: #e8e3dc; box-shadow: 0 2px 12px rgba(0,0,0,0.05); }
[data-testid="stChatInput"] { background: #ffffff !important; border: 1px solid #d0c9c0 !important; border-radius: 14px !important; color: #2c2420 !important; }
[data-testid="stChatInput"]:focus-within { border-color: #a09080 !important; box-shadow: 0 0 0 3px rgba(160,144,128,0.15) !important; }
.stButton > button { background: #ffffff !important; color: #4a4540 !important; border: 1px solid #d0c9c0 !important; border-radius: 10px !important; font-family: 'Noto Sans KR', sans-serif !important; transition: all 0.2s ease !important; font-weight: 500; }
.stButton > button:hover { background: #f0ede8 !important; border-color: #a09080 !important; color: #2c2420 !important; box-shadow: 0 2px 8px rgba(0,0,0,0.1) !important; transform: translateY(-1px); }
.stButton > button[kind="primary"] { background: #2c2420 !important; color: #ffffff !important; border: none !important; box-shadow: 0 2px 8px rgba(44,36,32,0.25); }
.stButton > button[kind="primary"]:hover { background: #4a4540 !important; box-shadow: 0 4px 16px rgba(44,36,32,0.3) !important; transform: translateY(-2px); }
.stTextInput > div > div > input, .stTextArea > div > div > textarea { background: #ffffff !important; border: 1px solid #d0c9c0 !important; border-radius: 10px !important; color: #2c2420 !important; font-family: 'Noto Sans KR', sans-serif !important; }
.stTextInput > div > div > input:focus, .stTextArea > div > div > textarea:focus { border-color: #a09080 !important; box-shadow: 0 0 0 3px rgba(160,144,128,0.15) !important; }
.stSelectbox > div > div { background: #ffffff !important; border: 1px solid #d0c9c0 !important; border-radius: 10px !important; color: #2c2420 !important; }
.streamlit-expanderHeader { background: #f5f2ee !important; border: 1px solid #e0dbd4 !important; border-radius: 10px !important; color: #4a4540 !important; font-weight: 500; transition: all 0.2s ease; }
.streamlit-expanderHeader:hover { background: #ede9e3 !important; }
.streamlit-expanderContent { background: #fdfcfb !important; border: 1px solid #e0dbd4 !important; border-top: none !important; border-radius: 0 0 10px 10px !important; }
div[data-testid="column"] .stButton > button { height: auto; white-space: normal; text-align: left; padding: 12px 14px; line-height: 1.5; font-size: 0.85rem; }
hr { border-color: #e8e3dc !important; }
.stCaption, [data-testid="stCaptionContainer"] { color: #9a9088 !important; }
.stAlert { background: #f5f2ee !important; border: 1px solid #d0c9c0 !important; border-radius: 12px !important; color: #4a4540 !important; }
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #f0ede8; }
::-webkit-scrollbar-thumb { background: #c8c0b8; border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: #a09080; }
.stMarkdown, p, li { color: #3d3530 !important; }
strong { color: #2c2420 !important; }
code { background: #f0ede8 !important; color: #7a4030 !important; border-radius: 4px; }
.stDownloadButton > button { background: #f0f7f0 !important; border-color: #b0ccb0 !important; color: #3a6040 !important; }
.stDownloadButton > button:hover { background: #dff0df !important; color: #2a4a30 !important; }
@keyframes fadeInUp { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: translateY(0); } }
</style>
"""

DARK_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700&family=Playfair+Display:wght@400;700&display=swap');
.stApp { background: #141414; font-family: 'Noto Sans KR', sans-serif; }
.main .block-container { background: #1c1c1c; border-radius: 16px; border: 1px solid #2e2e2e; padding: 2rem 2.5rem; box-shadow: 0 4px 24px rgba(0,0,0,0.4); }
[data-testid="stSidebar"] { background: #181818 !important; border-right: 1px solid #2e2e2e; }
[data-testid="stSidebar"] .stMarkdown p, [data-testid="stSidebar"] label { color: #c8c8c8 !important; }
h1 { font-family: 'Playfair Display', serif !important; color: #f0f0f0 !important; letter-spacing: 1px; }
h2, h3 { color: #d8d8d8 !important; }
.stTabs [data-baseweb="tab-list"] { background: #242424; border-radius: 12px; padding: 4px; gap: 4px; border: 1px solid #333333; }
.stTabs [data-baseweb="tab"] { border-radius: 8px; color: #888888 !important; font-weight: 500; transition: all 0.2s ease; padding: 8px 20px; }
.stTabs [aria-selected="true"] { background: #333333 !important; color: #f0f0f0 !important; box-shadow: 0 2px 8px rgba(0,0,0,0.3); }
[data-testid="stChatMessage"] { border-radius: 14px; padding: 1rem; margin-bottom: 0.8rem; animation: fadeInUp 0.3s ease; border: 1px solid transparent; }
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) { background: #242424; border-color: #333333; }
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) { background: #1e1e1e; border-color: #2e2e2e; box-shadow: 0 4px 16px rgba(0,0,0,0.3); }
[data-testid="stChatInput"] { background: #242424 !important; border: 1px solid #3a3a3a !important; border-radius: 14px !important; color: #e8e8e8 !important; }
[data-testid="stChatInput"]:focus-within { border-color: #666666 !important; box-shadow: 0 0 0 3px rgba(255,255,255,0.05) !important; }
.stButton > button { background: #242424 !important; color: #c8c8c8 !important; border: 1px solid #3a3a3a !important; border-radius: 10px !important; font-family: 'Noto Sans KR', sans-serif !important; transition: all 0.2s ease !important; font-weight: 500; }
.stButton > button:hover { background: #2e2e2e !important; border-color: #555555 !important; color: #f0f0f0 !important; box-shadow: 0 2px 12px rgba(0,0,0,0.4) !important; transform: translateY(-1px); }
.stButton > button[kind="primary"] { background: #e8e8e8 !important; color: #141414 !important; border: none !important; box-shadow: 0 2px 8px rgba(255,255,255,0.1); }
.stButton > button[kind="primary"]:hover { background: #ffffff !important; box-shadow: 0 4px 16px rgba(255,255,255,0.15) !important; transform: translateY(-2px); }
.stTextInput > div > div > input, .stTextArea > div > div > textarea { background: #242424 !important; border: 1px solid #3a3a3a !important; border-radius: 10px !important; color: #e8e8e8 !important; font-family: 'Noto Sans KR', sans-serif !important; }
.stTextInput > div > div > input:focus, .stTextArea > div > div > textarea:focus { border-color: #666666 !important; box-shadow: 0 0 0 3px rgba(255,255,255,0.05) !important; }
.stSelectbox > div > div { background: #242424 !important; border: 1px solid #3a3a3a !important; border-radius: 10px !important; color: #e8e8e8 !important; }
.streamlit-expanderHeader { background: #242424 !important; border: 1px solid #333333 !important; border-radius: 10px !important; color: #c8c8c8 !important; font-weight: 500; transition: all 0.2s ease; }
.streamlit-expanderHeader:hover { background: #2e2e2e !important; border-color: #444444 !important; }
.streamlit-expanderContent { background: #1e1e1e !important; border: 1px solid #2e2e2e !important; border-top: none !important; border-radius: 0 0 10px 10px !important; }
div[data-testid="column"] .stButton > button { height: auto; white-space: normal; text-align: left; padding: 12px 14px; line-height: 1.5; font-size: 0.85rem; }
hr { border-color: #2e2e2e !important; }
.stCaption, [data-testid="stCaptionContainer"] { color: #666666 !important; }
.stAlert { background: #242424 !important; border: 1px solid #3a3a3a !important; border-radius: 12px !important; color: #c8c8c8 !important; }
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #1c1c1c; }
::-webkit-scrollbar-thumb { background: #3a3a3a; border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: #555555; }
.stMarkdown, p, li { color: #c8c8c8 !important; }
strong { color: #f0f0f0 !important; }
code { background: #2e2e2e !important; color: #a8c8a8 !important; border-radius: 4px; }
.stDownloadButton > button { background: #1e2a1e !important; border-color: #3a5a3a !important; color: #90c890 !important; }
.stDownloadButton > button:hover { background: #263626 !important; color: #b0e8b0 !important; }
@keyframes fadeInUp { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: translateY(0); } }
</style>
"""

def inject_css(theme: str):
    st.markdown(LIGHT_CSS if theme == "☀️ 라이트" else DARK_CSS, unsafe_allow_html=True)


# ── 유저 DB 경로 ───────────────────────────────────────────────
DATA_DIR   = "data"
USERS_FILE = f"{DATA_DIR}/users.json"   # 회원 정보 저장 파일

def hash_pw(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()

# ── 유저 DB 로드/저장 ──────────────────────────────────────────
def load_users() -> dict:
    """{ "alice": {"pw_hash": "...", "created_at": "..."} }"""
    try:
        with open(USERS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}

def save_users(users: dict):
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=2)

# ── 회원가입 ───────────────────────────────────────────────────
def register(username: str, password: str) -> tuple[bool, str]:
    """성공 여부, 메시지 반환"""
    if not username or not password:
        return False, "아이디와 비밀번호를 입력해주세요."
    if len(username) < 2:
        return False, "아이디는 2자 이상이어야 해요."
    if len(password) < 4:
        return False, "비밀번호는 4자 이상이어야 해요."

    users = load_users()
    if username in users:
        return False, "이미 사용 중인 아이디예요."

    users[username] = {
        "pw_hash":    hash_pw(password),
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    save_users(users)
    return True, "회원가입 완료!"

# ── 로그인 ─────────────────────────────────────────────────────
def verify_login(username: str, password: str) -> bool:
    users = load_users()
    user  = users.get(username.strip())
    if not user:
        return False
    return hash_pw(password) == user["pw_hash"]

# ── 로그인/회원가입 화면 ───────────────────────────────────────
def render_auth():
    inject_css(st.session_state.get("theme", "☀️ 라이트"))

    st.markdown("<br><br>", unsafe_allow_html=True)
    _, col, _ = st.columns([1, 1.2, 1])

    with col:
        st.markdown("## 📖 창작 AI 어시스턴트")
        st.markdown("##### 당신만의 창작 공간에 오신 걸 환영해요.")
        st.divider()

        tab_login, tab_signup = st.tabs(["🔐 로그인", "✏️ 회원가입"])

        # ── 로그인 탭 ──────────────────────────────────────────
        with tab_login:
            with st.form("login_form"):
                username = st.text_input("아이디", placeholder="아이디를 입력하세요")
                password = st.text_input("비밀번호", type="password", placeholder="비밀번호를 입력하세요")
                if st.form_submit_button("로그인", use_container_width=True, type="primary"):
                    if not username or not password:
                        st.error("아이디와 비밀번호를 모두 입력해주세요.")
                    elif verify_login(username, password):
                        st.session_state.logged_in = True
                        st.session_state.username  = username.strip()
                        st.rerun()
                    else:
                        st.error("아이디 또는 비밀번호가 틀렸어요.")

        # ── 회원가입 탭 ────────────────────────────────────────
        with tab_signup:
            with st.form("signup_form"):
                new_id   = st.text_input("아이디", placeholder="2자 이상")
                new_pw   = st.text_input("비밀번호", type="password", placeholder="4자 이상")
                new_pw2  = st.text_input("비밀번호 확인", type="password", placeholder="비밀번호를 다시 입력하세요")
                if st.form_submit_button("회원가입", use_container_width=True, type="primary"):
                    if new_pw != new_pw2:
                        st.error("비밀번호가 일치하지 않아요.")
                    else:
                        ok, msg = register(new_id, new_pw)
                        if ok:
                            st.success(f"{msg} 이제 로그인해주세요 😊")
                        else:
                            st.error(msg)

        # 테마 토글
        st.divider()
        theme_pick = st.radio(
            "테마", ["☀️ 라이트", "🌙 다크"],
            index=0 if st.session_state.get("theme", "☀️ 라이트") == "☀️ 라이트" else 1,
            horizontal=True,
            label_visibility="collapsed",
        )
        if theme_pick != st.session_state.get("theme", "☀️ 라이트"):
            st.session_state.theme = theme_pick
            st.rerun()


# ── 데이터 경로 (유저별 분리) ──────────────────────────────────
def user_dir(username: str) -> str:
    return f"{DATA_DIR}/users/{username}"

def proj_dir(username: str, proj: str) -> str:
    return f"{user_dir(username)}/{proj}"

def load_json(path: str, default):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return default

def save_json(path: str, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def get_projects(username: str):
    return load_json(f"{user_dir(username)}/projects.json", [])

def save_projects(username: str, projects: list):
    path = f"{user_dir(username)}/projects.json"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    save_json(path, projects)

def load_project_data(username: str, proj: str, key: str, default):
    return load_json(f"{proj_dir(username, proj)}/{key}.json", default)

def save_project_data(username: str, proj: str, key: str, data):
    save_json(f"{proj_dir(username, proj)}/{key}.json", data)


# ── 모드별 시스템 프롬프트 ──────────────────────────────────────
SYSTEM_PROMPTS = {
    "🌍 세계관 빌더": """당신은 판타지, SF, 현대물 등 다양한 장르의 세계관 설계 전문가입니다.
사용자가 창작 중인 세계의 역사, 지리, 문화, 마법 체계, 기술 수준, 종족, 정치 구조 등을
체계적으로 구축할 수 있도록 돕습니다.
- 구체적이고 일관성 있는 설정을 제안하세요.
- 필요하면 표나 목록으로 정리해 시각적으로 보여주세요.
한국어로 대화합니다.""",
    "👤 캐릭터 디자이너": """당신은 소설과 웹소설의 캐릭터 설계 전문가입니다.
주인공, 조연, 빌런 등 다양한 캐릭터의 외형, 성격, 배경, 동기, 트라우마, 성장 호를
깊이 있게 설계할 수 있도록 돕습니다.
- MBTI, 심리학적 배경을 활용해 입체적 캐릭터를 만드세요.
한국어로 대화합니다.""",
    "📋 플롯 플래너": """당신은 소설의 구성과 플롯 설계 전문가입니다.
3막 구조, 영웅의 여정, 기승전결 등 다양한 스토리텔링 기법을 활용하여
탄탄한 이야기 구조를 만들 수 있도록 돕습니다.
한국어로 대화합니다.""",
    "✍️ 문장 코치": """당신은 소설 문장력 향상을 도와주는 전문 문학 편집자입니다.
- 묘사가 부족한 부분에 감각적 디테일을 추가하세요.
- 진부한 표현을 참신한 비유로 바꿔주세요.
한국어로 대화합니다.""",
    "💬 대화 작가": """당신은 소설 속 캐릭터 대화 작성 전문가입니다.
- 캐릭터마다 고유한 어조와 어휘를 사용하세요.
- 대화 속에 갈등, 서브텍스트, 감정 변화를 녹여내세요.
한국어로 대화합니다.""",
    "🔮 자유 창작": """당신은 창의적인 소설 창작 파트너입니다.
세계관, 캐릭터, 플롯, 문장, 대화 등 창작의 모든 분야를 자유롭게 도와드립니다.
한국어로 대화합니다.""",
}

MODE_HINTS = {
    "🌍 세계관 빌더": ["마법이 사라진 제국을 배경으로 세계관을 만들고 싶어요.", "하늘에 떠 있는 섬들로 이루어진 세계의 문명은 어떨까요?", "디스토피아 SF 배경의 감시 사회 기술 설정 도와주세요."],
    "👤 캐릭터 디자이너": ["냉철한 척하지만 내면이 불안한 빌런을 만들고 싶어요.", "17세 여성 마법사 가문 출신 주인공 캐릭터 시트를 채워주세요.", "두 캐릭터의 앙숙 관계를 설정하고 싶어요."],
    "📋 플롯 플래너": ["3막 구조로 내 소설 개요를 짜고 싶어요.", "결말을 정했는데 거기까지 가는 경로를 설계해주세요.", "복선과 반전 포인트를 어디에 넣으면 좋을까요?"],
    "✍️ 문장 코치": ["이 문단을 더 생생하게 고쳐주세요: [붙여넣기]", "감정 묘사가 너무 직접적인 것 같아요.", "강렬한 오프닝 문장 10개만 써줘요."],
    "💬 대화 작가": ["차갑고 말수 적은 캐릭터가 처음으로 감사를 표현하는 장면을 써주세요.", "서로 좋아하면서도 티 내지 않으려는 대화를 써주세요.", "긴장감 있는 심문 장면 대화를 써주세요."],
    "🔮 자유 창작": ["새 소설 아이디어 브레인스토밍 도와주세요.", "현재 쓰고 있는 소설의 막힌 부분을 함께 풀어봐요.", "내 장르에 맞는 세계관을 처음부터 만들어봐요."],
}


# ── 세션 상태 초기화 ────────────────────────────────────────────
defaults = {
    "logged_in":       False,
    "username":        None,
    "mode":            "🔮 자유 창작",
    "messages":        [],
    "favorites":       [],
    "current_project": None,
    "theme":           "☀️ 라이트",
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v


# ── 로그인 게이트 ───────────────────────────────────────────────
if not st.session_state.logged_in:
    render_auth()
    st.stop()


# ── 로그인 이후 ─────────────────────────────────────────────────
inject_css(st.session_state.theme)

try:
    API_KEY = st.secrets["ANTHROPIC_API_KEY"]
except KeyError:
    st.error("⚠️ Streamlit Secrets에 ANTHROPIC_API_KEY 가 없어요.")
    st.stop()

username = st.session_state.username

def load_project(proj: str):
    st.session_state.current_project = proj
    st.session_state.messages  = load_project_data(username, proj, "history",   [])
    st.session_state.favorites = load_project_data(username, proj, "favorites", [])

def save_current_state():
    proj = st.session_state.current_project
    if proj:
        save_project_data(username, proj, "history",   st.session_state.messages)
        save_project_data(username, proj, "favorites", st.session_state.favorites)


# ── 사이드바 ────────────────────────────────────────────────────
with st.sidebar:
    st.title("📖 창작 AI 어시스턴트")

    st.markdown(f"**👤 {username}** 님 환영해요!")
    if st.button("로그아웃", use_container_width=True):
        save_current_state()
        for k in ["logged_in", "username", "messages", "favorites", "current_project"]:
            st.session_state[k] = defaults[k]
        st.rerun()

    st.divider()

    # 테마 토글
    selected_theme = st.radio(
        "테마", ["☀️ 라이트", "🌙 다크"],
        index=0 if st.session_state.theme == "☀️ 라이트" else 1,
        horizontal=True,
        label_visibility="collapsed",
    )
    if selected_theme != st.session_state.theme:
        st.session_state.theme = selected_theme
        st.rerun()

    st.divider()

    # 프로젝트 관리
    st.subheader("📁 프로젝트")
    projects = get_projects(username)

    with st.expander("➕ 새 프로젝트 만들기"):
        new_proj_name = st.text_input("프로젝트 이름", placeholder="예: 마법사의 귀환", label_visibility="collapsed")
        if st.button("만들기", use_container_width=True):
            if new_proj_name.strip() and new_proj_name not in projects:
                projects.append(new_proj_name)
                save_projects(username, projects)
                load_project(new_proj_name)
                st.rerun()
            elif new_proj_name in projects:
                st.warning("이미 존재하는 이름이에요.")

    if projects:
        selected_proj = st.selectbox(
            "프로젝트 선택", projects,
            index=projects.index(st.session_state.current_project)
                  if st.session_state.current_project in projects else 0,
            label_visibility="collapsed",
        )
        if selected_proj != st.session_state.current_project:
            save_current_state()
            load_project(selected_proj)
            st.rerun()

        with st.expander("🗑️ 프로젝트 삭제"):
            st.caption(f"'{st.session_state.current_project}' 를 삭제합니다.")
            if st.button("삭제 확인", type="primary", use_container_width=True):
                projects.remove(st.session_state.current_project)
                save_projects(username, projects)
                st.session_state.current_project = projects[0] if projects else None
                if st.session_state.current_project:
                    load_project(st.session_state.current_project)
                else:
                    st.session_state.messages  = []
                    st.session_state.favorites = []
                st.rerun()
    else:
        st.info("프로젝트를 먼저 만들어주세요.")

    st.divider()

    st.subheader("✨ 어시스턴트 모드")
    selected_mode = st.radio(
        "모드", list(SYSTEM_PROMPTS.keys()),
        index=list(SYSTEM_PROMPTS.keys()).index(st.session_state.mode),
        label_visibility="collapsed",
    )
    if selected_mode != st.session_state.mode:
        st.session_state.mode = selected_mode
        st.rerun()

    st.divider()

    if st.button("🗑️ 대화 초기화", use_container_width=True):
        st.session_state.messages = []
        save_current_state()
        st.rerun()

    st.caption("Made with ❤️ using Claude API + Streamlit")


# ── 프로젝트 미선택 안내 ────────────────────────────────────────
if not st.session_state.current_project:
    st.title("📖 창작 AI 어시스턴트")
    st.info("사이드바에서 프로젝트를 먼저 만들어주세요.")
    st.stop()

proj = st.session_state.current_project

# ── 헤더 배너 ──────────────────────────────────────────────────
if st.session_state.theme == "☀️ 라이트":
    banner_bg = "linear-gradient(135deg, #f5f2ee, #ede9e3)"
    banner_border = "#d0c9c0"
    title_color = "#2c2420"
    sub_color = "#9a9088"
else:
    banner_bg = "linear-gradient(135deg, #242424, #1e1e1e)"
    banner_border = "#3a3a3a"
    title_color = "#f0f0f0"
    sub_color = "#666666"

st.markdown(f"""
<div style="
    background: {banner_bg}; border: 1px solid {banner_border};
    border-radius: 16px; padding: 1.2rem 1.8rem; margin-bottom: 1rem;
    display: flex; align-items: center; gap: 12px;
">
    <span style="font-size:2rem;">📖</span>
    <div>
        <h2 style="margin:0; color:{title_color}; font-family:'Playfair Display',serif; letter-spacing:1px;">{proj}</h2>
        <p style="margin:0; color:{sub_color}; font-size:0.85rem;">창작 AI 어시스턴트 · {st.session_state.mode}</p>
    </div>
</div>
""", unsafe_allow_html=True)

# ── 메인 탭 ────────────────────────────────────────────────────
tab_chat, tab_chars, tab_world, tab_fav = st.tabs(["💬 대화", "👤 캐릭터 DB", "🌍 세계관 DB", "⭐ 즐겨찾기"])


# ════════════════════════════════════════════════════════════════
# TAB 1: 대화
# ════════════════════════════════════════════════════════════════
with tab_chat:
    col_mode, col_exp = st.columns([3, 1])
    with col_mode:
        st.caption(f"현재 모드: **{st.session_state.mode}**")
    with col_exp:
        if st.session_state.messages:
            now = datetime.now().strftime("%Y%m%d_%H%M")
            chat_txt = "\n\n".join([f"[{'나' if m['role']=='user' else 'AI'}]\n{m['content']}" for m in st.session_state.messages])
            chat_md  = "\n\n".join([f"**{'나' if m['role']=='user' else 'AI ✨'}**\n\n{m['content']}" for m in st.session_state.messages])
            with st.popover("💾 내보내기"):
                st.download_button("📄 .txt로 저장", chat_txt, f"{proj}_{now}.txt", "text/plain",    use_container_width=True)
                st.download_button("📝 .md로 저장",  chat_md,  f"{proj}_{now}.md",  "text/markdown", use_container_width=True)

    if not st.session_state.messages:
        hints = MODE_HINTS.get(st.session_state.mode, [])
        st.markdown("#### 💡 이렇게 시작해보세요")
        cols = st.columns(len(hints))
        for i, (col, hint) in enumerate(zip(cols, hints)):
            with col:
                if st.button(hint, key=f"hint_{i}", use_container_width=True):
                    st.session_state.messages.append({"role": "user", "content": hint})
                    save_current_state()
                    st.rerun()

    world_db = load_project_data(username, proj, "world",      {})
    char_db  = load_project_data(username, proj, "characters", [])

    for i, msg in enumerate(st.session_state.messages):
        with st.chat_message(msg["role"], avatar="🧑‍💻" if msg["role"] == "user" else "📖"):
            st.markdown(msg["content"])
            if msg["role"] == "assistant":
                fav_ids   = [f["id"] for f in st.session_state.favorites]
                is_fav    = i in fav_ids
                btn_label = "⭐ 즐겨찾기 해제" if is_fav else "☆ 즐겨찾기"
                if st.button(btn_label, key=f"fav_{i}"):
                    if is_fav:
                        st.session_state.favorites = [f for f in st.session_state.favorites if f["id"] != i]
                    else:
                        st.session_state.favorites.append({
                            "id": i, "content": msg["content"],
                            "mode": st.session_state.mode,
                            "saved_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
                        })
                    save_current_state()
                    st.rerun()

    if prompt := st.chat_input("창작에 대해 무엇이든 물어보세요..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user", avatar="🧑‍💻"):
            st.markdown(prompt)

        system = SYSTEM_PROMPTS[st.session_state.mode]
        context_parts = []
        if world_db:
            context_parts.append("## 세계관 설정\n" + "\n".join([f"**{k}**: {v}" for k, v in world_db.items() if v]))
        if char_db:
            char_summary = "\n".join([f"- {c['name']} ({c.get('role','')}) : {c.get('personality','')}" for c in char_db])
            context_parts.append(f"## 등장인물\n{char_summary}")
        if context_parts:
            system += "\n\n" + "\n\n".join(context_parts)

        with st.chat_message("assistant", avatar="📖"):
            placeholder   = st.empty()
            full_response = ""
            try:
                client = anthropic.Anthropic(api_key=API_KEY)
                with client.messages.stream(
                    model="claude-sonnet-4-20250514",
                    max_tokens=2048,
                    system=system,
                    messages=st.session_state.messages,
                ) as stream:
                    for text in stream.text_stream:
                        full_response += text
                        placeholder.markdown(full_response + "▌")
                placeholder.markdown(full_response)
            except anthropic.AuthenticationError:
                st.error("❌ API 키가 올바르지 않습니다.")
                st.session_state.messages.pop()
                st.stop()
            except Exception as e:
                st.error(f"❌ 오류: {str(e)}")
                st.session_state.messages.pop()
                st.stop()

        st.session_state.messages.append({"role": "assistant", "content": full_response})
        save_current_state()
        st.rerun()


# ════════════════════════════════════════════════════════════════
# TAB 2: 캐릭터 DB
# ════════════════════════════════════════════════════════════════
with tab_chars:
    char_db = load_project_data(username, proj, "characters", [])
    st.subheader("👤 캐릭터 목록")

    with st.expander("➕ 새 캐릭터 추가"):
        with st.form("new_char_form", clear_on_submit=True):
            c1, c2, c3 = st.columns(3)
            name    = c1.text_input("이름 *")
            role    = c2.selectbox("역할", ["주인공", "조연", "빌런", "조력자", "기타"])
            age     = c3.text_input("나이/나이대")
            d1, d2  = st.columns(2)
            appearance  = d1.text_area("외형",     height=80, placeholder="키, 머리색, 눈색, 특징 등")
            personality = d2.text_area("성격",     height=80, placeholder="MBTI, 핵심 성격, 말투 등")
            e1, e2  = st.columns(2)
            background  = e1.text_area("배경",     height=80, placeholder="출신, 과거, 트라우마 등")
            motivation  = e2.text_area("동기/목표", height=80, placeholder="원하는 것, 두려운 것 등")
            notes = st.text_area("메모", height=60, placeholder="관계, 비밀, 기타 설정 등")

            if st.form_submit_button("캐릭터 저장", use_container_width=True, type="primary"):
                if name.strip():
                    char_db.append({
                        "name": name, "role": role, "age": age,
                        "appearance": appearance, "personality": personality,
                        "background": background, "motivation": motivation,
                        "notes": notes,
                    })
                    save_project_data(username, proj, "characters", char_db)
                    st.success(f"'{name}' 캐릭터가 추가됐어요!")
                    st.rerun()

    if not char_db:
        st.info("아직 캐릭터가 없어요. 위에서 추가해보세요!")
    else:
        role_colors = {"주인공": "🟡", "빌런": "🔴", "조연": "🔵", "조력자": "🟢", "기타": "⚪"}
        for i, char in enumerate(char_db):
            icon = role_colors.get(char.get("role", "기타"), "⚪")
            with st.expander(f"{icon} {char['name']}  |  {char.get('role','')}  |  {char.get('age','')}"):
                col_a, col_b = st.columns(2)
                with col_a:
                    if char.get("appearance"):  st.markdown(f"**👁 외형**\n{char['appearance']}")
                    if char.get("background"):  st.markdown(f"**📜 배경**\n{char['background']}")
                with col_b:
                    if char.get("personality"): st.markdown(f"**💭 성격**\n{char['personality']}")
                    if char.get("motivation"):  st.markdown(f"**🎯 동기**\n{char['motivation']}")
                if char.get("notes"):           st.markdown(f"**📝 메모**\n{char['notes']}")
                if st.button("🗑️ 삭제", key=f"del_char_{i}"):
                    char_db.pop(i)
                    save_project_data(username, proj, "characters", char_db)
                    st.rerun()


# ════════════════════════════════════════════════════════════════
# TAB 3: 세계관 DB
# ════════════════════════════════════════════════════════════════
with tab_world:
    world_db = load_project_data(username, proj, "world", {})
    st.subheader("🌍 세계관 설정")
    st.caption("입력한 내용은 대화 탭의 AI에게 자동으로 전달됩니다.")

    WORLD_FIELDS = {
        "장르": "판타지, SF, 현대물 등",
        "배경 시대": "중세, 근미래, 현대 등",
        "지리/세계 구조": "대륙, 국가, 도시 구성 등",
        "역사/연대기": "주요 사건, 전쟁, 신화 등",
        "마법/기술 체계": "마법 원리, 기술 수준, 제한 등",
        "종족/세력": "주요 종족, 국가, 조직 등",
        "문화/종교": "풍습, 신앙, 가치관 등",
        "핵심 갈등": "세계관의 중심 갈등, 위기 등",
        "기타 메모": "위 항목에 맞지 않는 설정",
    }

    with st.form("world_form"):
        updated = {}
        for field, placeholder in WORLD_FIELDS.items():
            updated[field] = st.text_area(field, value=world_db.get(field, ""), placeholder=placeholder, height=80)
        if st.form_submit_button("💾 저장", use_container_width=True, type="primary"):
            save_project_data(username, proj, "world", updated)
            st.success("세계관 설정이 저장됐어요!")
            st.rerun()


# ════════════════════════════════════════════════════════════════
# TAB 4: 즐겨찾기
# ════════════════════════════════════════════════════════════════
with tab_fav:
    st.subheader("⭐ 즐겨찾기한 답변")
    favs = load_project_data(username, proj, "favorites", [])
    st.session_state.favorites = favs

    if not favs:
        st.info("아직 즐겨찾기한 답변이 없어요.\n대화 탭에서 AI 답변 아래 ☆ 버튼을 눌러보세요!")
    else:
        now_str = datetime.now().strftime("%Y%m%d_%H%M")
        fav_md  = "\n\n---\n\n".join([f"**[{f.get('mode','')} | {f.get('saved_at','')}]**\n\n{f['content']}" for f in favs])
        st.download_button("📝 즐겨찾기 전체 .md 저장", fav_md, f"{proj}_즐겨찾기_{now_str}.md", "text/markdown")
        st.divider()

        for i, fav in enumerate(favs):
            with st.expander(f"⭐ {fav.get('mode','')}  |  {fav.get('saved_at','')}"):
                st.markdown(fav["content"])
                if st.button("⭐ 즐겨찾기 해제", key=f"unfav_{i}"):
                    favs.pop(i)
                    save_project_data(username, proj, "favorites", favs)
                    st.session_state.favorites = favs
                    st.rerun()
