import streamlit as st

# 페이지 설정
st.set_page_config(page_title="MBTI 포켓몬 추천", page_icon="🧬", layout="centered")

# 제목 및 설명
st.title("🔮 MBTI 기반 포켓몬 추천기 🐾")
st.write("당신의 MBTI에 맞는 포켓몬을 추천해드려요! 어떤 포켓몬이 어울릴지 궁금하다면 시작해보세요!")

# MBTI 목록
mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# MBTI별 포켓몬 추천 딕셔너리 (포켓몬과 이모지를 추가)
pokemon_dict = {
    "INTJ": ("뮤츠", "🧠 지적인 전략가, 고독하지만 강한 힘을 지닌 전설의 포켓몬. 🦸‍♂️"),
    "INTP": ("프리져", "❄️ 호기심 많은 탐구자, 논리적이고 차가운 매력을 가진 얼음 타입 포켓몬. 🧊"),
    "ENTJ": ("리자몽", "🔥 강한 리더십과 추진력! 모두를 이끄는 카리스마의 화염 포켓몬. 🦸‍♀️"),
    "ENTP": ("피카츄", "⚡ 발랄하고 아이디어가 풍부한 성격, 모두에게 사랑받는 스타. 🌟"),
    "INFJ": ("에브이", "🌈 미래를 꿈꾸는 이상주의자, 다양한 가능성을 지닌 변화의 포켓몬. ✨"),
    "INFP": ("이브이", "💖 다정하고 순수한 영혼, 다양한 진화를 통해 자신만의 길을 찾아가는 포켓몬. 🦋"),
    "ENFJ": ("루카리오", "👑 타인을 이끄는 따뜻한 카리스마, 강한 정의감을 지닌 전사. 🛡️"),
    "ENFP": ("고라파덕", "💡 엉뚱하지만 창의력 넘치는 자유로운 영혼. 🌊"),
    "ISTJ": ("거북왕", "🛡️ 신중하고 책임감 있는 타입, 철저한 방어력으로 팀을 지키는 포켓몬. 🐢"),
    "ISFJ": ("라프라스", "🌊 조용하지만 따뜻한 돌봄 성향, 타인을 도와주는 힐러 역할. 🐉"),
    "ESTJ": ("카이리키", "💪 규칙을 중시하고 조직적, 강력한 추진력을 가진 격투 타입 포켓몬. 🥋"),
    "ESFJ": ("해피너스", "💖 주변을 챙기고 돕는 것을 좋아하는 마음 따뜻한 간호 포켓몬. 🏥"),
    "ISTP": ("팬텀", "🖤 조용하고 분석적인 전사, 싸움에 능한 그림자 같은 존재. ⚔️"),
    "ISFP": ("마자용", "🎨 감성적이고 예술적인 성향, 부끄러움도 많지만 내면이 빛나는 포켓몬. 🌟"),
    "ESTP": ("갸라도스", "🐉 행동이 빠르고 강력한 한방을 지닌 격정적인 성격. ⚡"),
    "ESFP": ("뮤", "🌟 순수하고 즐거움을 추구하는 자유로운 존재, 모두와 잘 어울리는 인기쟁이. 💫")
}

# 사용자 입력
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요", mbti_list)

# 추천 버튼
if st.button("포켓몬 추천 받기! 🐾"):
    pokemon_name, description = pokemon_dict[selected_mbti]
    # 포켓몬 이름과 설명을 화려하게 출력
    st.subheader(f"✨ 추천 포켓몬: {pokemon_name} ✨")
    st.image(f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{pokemon_name.lower()}.png", width=200)
    st.write(f"📌 {description}")
