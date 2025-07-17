import streamlit as st
from openai import OpenAI

# 페이지 기본 설정
st.set_page_config(page_title="진로 추천기", page_icon="🎓", layout="centered")

# 사이드바에서 API 키 입력
openai_api_key = st.secrets["OPENAI_API_KEY"]

st.title("🧭 AI 진로 추천기")
st.markdown("학생의 관심사, 강점, 가치관을 바탕으로 AI가 직업을 추천해줘요!")

# 사용자 입력
interest = st.text_input("1️⃣ 관심 있는 분야는 무엇인가요?", placeholder="예: 컴퓨터, 예술, 심리학")
strength = st.text_input("2️⃣ 나의 강점은 무엇인가요?", placeholder="예: 논리적 사고, 창의력, 소통 능력")
value = st.text_input("3️⃣ 중요하게 생각하는 가치는 무엇인가요?", placeholder="예: 안정성, 자유, 성장")

# 버튼 클릭 시 동작
if st.button("🚀 진로 추천 받기"):
    if not (openai_api_key and interest and strength and value):
        st.warning("⚠️ 모든 항목과 API 키를 입력해주세요.")
    else:
        client = OpenAI(api_key=openai_api_key)

        with st.spinner("AI가 진로를 분석 중입니다..."):
            prompt = f"""
            다음 정보를 바탕으로 학생에게 적합한 직업 3가지를 추천해줘.
            각 직업에 대해 간단한 설명과 필요한 핵심 역량도 함께 설명해줘.

            관심 분야: {interest}
            강점: {strength}
            가치관: {value}

            형식:
            1. 직업명 - 설명
               - 필요 역량: 리스트
            """

            try:
                response = client.chat.completions.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "너는 진로 전문가이자 커리어 멘토야."},
                        {"role": "user", "content": prompt}
                    ]
                )

                result = response.choices[0].message.content
                st.success("✨ 추천 결과")
                st.markdown(result)

            except Exception as e:
                st.error(f"❌ 오류 발생: {e}")
