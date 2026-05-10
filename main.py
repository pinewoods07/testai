import streamlit as st
import anthropic
import json

# ── 페이지 설정 ────────────────────────────────────────────────
st.set_page_config(
    page_title="창작 AI 어시스턴트",
    page_icon="📖",
    layout="wide",
)

# ── 모드별 시스템 프롬프트 ──────────────────────────────────────
SYSTEM_PROMPTS = {
    "🌍 세계관 빌더": """당신은 판타지, SF, 현대물 등 다양한 장르의 세계관 설계 전문가입니다.
사용자가 창작 중인 세계의 역사, 지리, 문화, 마법 체계, 기술 수준, 종족, 정치 구조 등을 
체계적으로 구축할 수 있도록 돕습니다.

- 구체적이고 일관성 있는 설정을 제안하세요.
- 이미 설정된 세계관과 충돌하지 않도록 주의하세요.
- 필요하면 표나 목록으로 정리해 시각적으로 보여주세요.
- 사용자가 미처 생각하지 못한 설정 요소를 자연스럽게 제안하세요.
- 한국어로 대화합니다.""",

    "👤 캐릭터 디자이너": """당신은 소설과 웹소설의 캐릭터 설계 전문가입니다.
주인공, 조연, 빌런 등 다양한 캐릭터의 외형, 성격, 배경, 동기, 트라우마, 성장 호弧를 
깊이 있게 설계할 수 있도록 돕습니다.

- MBTI, 에니어그램, 심리학적 배경을 활용해 입체적 캐릭터를 만드세요.
- 캐릭터 간의 관계 역학과 갈등 구조를 제안하세요.
- 캐릭터 시트 형식으로 정리해드릴 수 있습니다.
- 캐릭터의 말투, 버릇, 가치관을 구체적으로 설정하세요.
- 한국어로 대화합니다.""",

    "📋 플롯 플래너": """당신은 소설의 구성과 플롯 설계 전문가입니다.
3막 구조, 영웅의 여정, 기승전결 등 다양한 스토리텔링 기법을 활용하여 
탄탄한 이야기 구조를 만들 수 있도록 돕습니다.

- 복선, 반전, 클라이맥스 배치를 전략적으로 제안하세요.
- 각 장면의 목적(갈등, 성장, 반전 등)을 명확히 하세요.
- 플롯 홀이나 논리적 허점을 짚어주세요.
- 챕터별 요약이나 개요를 표로 정리해드릴 수 있습니다.
- 한국어로 대화합니다.""",

    "✍️ 문장 코치": """당신은 소설 문장력 향상을 도와주는 전문 문학 편집자입니다.
사용자가 쓴 문장을 더 생생하고, 리듬감 있고, 감동적으로 다듬을 수 있도록 돕습니다.

- 묘사가 부족한 부분에 감각적 디테일을 추가하세요.
- 문장 리듬과 호흡을 다양하게 조절하세요.
- 진부한 표현을 참신한 비유로 바꿔주세요.
- 원문의 의도를 최대한 살리면서 개선하세요.
- 개선 이유도 함께 설명하여 사용자가 배울 수 있게 하세요.
- 한국어로 대화합니다.""",

    "💬 대화 작가": """당신은 소설 속 캐릭터 대화 작성 전문가입니다.
각 캐릭터의 개성, 말투, 감정 상태에 맞는 생생한 대사를 작성할 수 있도록 돕습니다.

- 캐릭터마다 고유한 어조와 어휘를 사용하세요.
- 대화 속에 갈등, 서브텍스트, 감정 변화를 녹여내세요.
- 지문(행동 묘사)과 대사의 균형을 맞추세요.
- 대화가 이야기를 앞으로 나아가게 하세요.
- 한국어로 대화합니다.""",

    "🔮 자유 창작": """당신은 창의적인 소설 창작 파트너입니다.
세계관, 캐릭터, 플롯, 문장, 대화 등 창작의 모든 분야를 자유롭게 도와드립니다.
사용자의 창작 비전을 가장 잘 실현할 수 있도록 유연하게 지원합니다.
한국어로 대화합니다.""",
}

# ── 세션 상태 초기화 ────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []
if "mode" not in st.session_state:
    st.session_state.mode = "🔮 자유 창작"
if "world_notes" not in st.session_state:
    st.session_state.world_notes = ""

# ── 사이드바 ────────────────────────────────────────────────────
with st.sidebar:
    st.title("📖 창작 AI 어시스턴트")
    st.caption("Claude claude-sonnet-4-20250514 기반")

    st.divider()

    # 모드 선택
    st.subheader("✨ 어시스턴트 모드")
    selected_mode = st.radio(
        "목적에 맞는 모드를 선택하세요",
        list(SYSTEM_PROMPTS.keys()),
        index=list(SYSTEM_PROMPTS.keys()).index(st.session_state.mode),
        label_visibility="collapsed"
    )

    if selected_mode != st.session_state.mode:
        st.session_state.mode = selected_mode
        st.session_state.messages = []
        st.rerun()

    st.divider()

    # 세계관 메모장
    st.subheader("📝 세계관 메모")
    st.session_state.world_notes = st.text_area(
        "설정 메모 (대화 컨텍스트에 포함됩니다)",
        value=st.session_state.world_notes,
        height=180,
        placeholder="예:\n- 장르: 다크 판타지\n- 배경: 마법이 사라진 제국\n- 주인공: 17세 견습 마법사\n- 핵심 갈등: 마법의 부활을 막으려는 세력과의 대립",
        label_visibility="collapsed"
    )

    st.divider()

    # 대화 초기화
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🗑️ 대화 초기화", use_container_width=True):
            st.session_state.messages = []
            st.rerun()
    with col2:
        # 대화 내용 다운로드
        if st.session_state.messages:
            chat_export = "\n\n".join([
                f"[{'AI' if m['role'] == 'assistant' else '나'}]\n{m['content']}"
                for m in st.session_state.messages
            ])
            st.download_button(
                "💾 저장",
                chat_export,
                file_name="창작_대화.txt",
                mime="text/plain",
                use_container_width=True
            )

    st.divider()
    st.caption("Made with ❤️ using Claude API + Streamlit")

# ── 메인 화면 ────────────────────────────────────────────────────
st.title(f"{st.session_state.mode}")

# 모드 설명
mode_descriptions = {
    "🌍 세계관 빌더": "역사, 지리, 문화, 마법 체계 등 세계의 모든 설정을 함께 만들어요.",
    "👤 캐릭터 디자이너": "입체적이고 매력적인 캐릭터를 설계해드려요.",
    "📋 플롯 플래너": "탄탄한 이야기 구조와 플롯을 함께 설계해요.",
    "✍️ 문장 코치": "쓴 문장을 더 생생하고 감동적으로 다듬어드려요.",
    "💬 대화 작가": "캐릭터의 개성이 살아있는 대사를 작성해드려요.",
    "🔮 자유 창작": "창작의 모든 분야를 자유롭게 도와드려요.",
}
st.caption(mode_descriptions.get(st.session_state.mode, ""))

# 시작 안내 메시지
if not st.session_state.messages:
    starter_hints = {
        "🌍 세계관 빌더": [
            "중세 판타지 세계관을 만들고 싶어요. 마법 체계부터 시작해볼까요?",
            "제 세계는 바다가 없고 모든 땅이 하늘에 떠 있어요. 어떤 문명이 발달했을까요?",
            "디스토피아 SF 배경인데, 감시 사회의 기술 설정을 도와주세요.",
        ],
        "👤 캐릭터 디자이너": [
            "냉철한 척하지만 내면이 불안한 빌런을 만들고 싶어요.",
            "주인공 캐릭터 시트를 채워주세요. 17세 여성, 마법사 가문 출신이에요.",
            "두 캐릭터의 앙숙 관계를 설정하고 싶은데 도와주세요.",
        ],
        "📋 플롯 플래너": [
            "3막 구조로 내 소설 개요를 짜고 싶어요.",
            "1장 초안이 있는데, 복선과 반전 포인트를 어디에 넣으면 좋을까요?",
            "결말을 정했는데 거기까지 가는 경로를 함께 설계해주세요.",
        ],
        "✍️ 문장 코치": [
            "이 문단을 더 생생하게 고쳐주세요: [문단 붙여넣기]",
            "감정 묘사가 너무 직접적인 것 같아요. 더 세련되게 바꿔주세요.",
            "오프닝 문장이 약한 것 같은데, 강렬한 첫 문장 10개만 써줘요.",
        ],
        "💬 대화 작가": [
            "차갑고 말수 적은 캐릭터가 처음으로 감사를 표현하는 장면을 써주세요.",
            "두 캐릭터가 서로 좋아하면서도 티 내지 않으려는 대화를 써주세요.",
            "심문 장면인데 긴장감 있는 대화를 만들어주세요.",
        ],
        "🔮 자유 창작": [
            "새 소설을 시작하려는데 아이디어 브레인스토밍 도와주세요.",
            "현재 쓰고 있는 소설의 막힌 부분을 같이 풀어봐요.",
            "제 장르와 스타일에 맞는 세계관을 처음부터 만들어봐요.",
        ],
    }

    hints = starter_hints.get(st.session_state.mode, [])
    if hints:
        st.markdown("#### 💡 이렇게 시작해보세요")
        cols = st.columns(len(hints))
        for i, (col, hint) in enumerate(zip(cols, hints)):
            with col:
                if st.button(hint, key=f"hint_{i}", use_container_width=True):
                    st.session_state.messages.append({"role": "user", "content": hint})
                    st.rerun()

st.divider()

# ── 대화 내용 출력 ──────────────────────────────────────────────
for msg in st.session_state.messages:
    with st.chat_message(msg["role"], avatar="🧑‍💻" if msg["role"] == "user" else "📖"):
        st.markdown(msg["content"])

# ── 사용자 입력 처리 ────────────────────────────────────────────
if prompt := st.chat_input("창작에 대해 무엇이든 물어보세요..."):
    try:
        api_key = st.secrets["ANTHROPIC_API_KEY"]
    except KeyError:
        st.error("⚠️ Streamlit Secrets에 `ANTHROPIC_API_KEY`가 설정되지 않았습니다.")
        st.stop()

    # 사용자 메시지 추가
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="🧑‍💻"):
        st.markdown(prompt)

    # 시스템 프롬프트 구성
    system_prompt = SYSTEM_PROMPTS[st.session_state.mode]
    if st.session_state.world_notes.strip():
        system_prompt += f"\n\n## 현재 창작 설정 메모\n{st.session_state.world_notes}"

    # Claude API 스트리밍 호출
    with st.chat_message("assistant", avatar="📖"):
        response_placeholder = st.empty()
        full_response = ""

        try:
            client = anthropic.Anthropic(api_key=api_key)

            with client.messages.stream(
                model="claude-sonnet-4-20250514",
                max_tokens=2048,
                system=system_prompt,
                messages=st.session_state.messages,
            ) as stream:
                for text in stream.text_stream:
                    full_response += text
                    response_placeholder.markdown(full_response + "▌")

            response_placeholder.markdown(full_response)

        except anthropic.AuthenticationError:
            st.error("❌ API 키가 올바르지 않습니다. 사이드바에서 다시 확인해주세요.")
            st.session_state.messages.pop()
            st.stop()
        except anthropic.RateLimitError:
            st.error("⚠️ API 요청 한도를 초과했습니다. 잠시 후 다시 시도해주세요.")
            st.session_state.messages.pop()
            st.stop()
        except Exception as e:
            st.error(f"❌ 오류가 발생했습니다: {str(e)}")
            st.session_state.messages.pop()
            st.stop()

    st.session_state.messages.append({"role": "assistant", "content": full_response})
