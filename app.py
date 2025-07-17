import streamlit as st
import openai

# OpenAI API 키 설정
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("🌱 진로 추천기")
st.write("질문에 답하면 당신에게 맞는 직업과 필요한 역량을 추천해 드릴게요!")

# 사용자 입력
interest = st.text_input("관심 있는 분야는 무엇인가요?")
strength = st.text_input("나의 강점은 무엇인가요?")
value = st.text_input("중요하게 생각하는 가치는 무엇인가요?")

if st.button("직업 추천 받기"):
    if not (interest and strength and value):
        st.warning("모든 질문에 답해주세요!")
    else:
        with st.spinner("추천 중..."):
            prompt = f"""
            다음 정보를 바탕으로 학생에게 맞는 직업 3개를 추천하고, 각 직업에 필요한 핵심 역량을 설명해줘:
            관심 분야: {interest}
            강점: {strength}
            가치관: {value}
            형식: 직업명 - 간단한 설명 / 필요한 역량 리스트
            """
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "너는 진로 추천 전문가야."},
                    {"role": "user", "content": prompt}
                ]
            )
            result = response["choices"][0]["message"]["content"]
            st.success("추천 결과:")
            st.markdown(result)
