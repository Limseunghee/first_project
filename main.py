import streamlit as st
import random

# 제목
st.title("✊ ✋ ✌️ 가위바위보 게임")

# 선택지
choices = ["가위", "바위", "보"]

# 사용자 선택
user_choice = st.radio("당신의 선택은?", choices)

# 게임 시작 버튼
if st.button("게임 시작!"):
    # 컴퓨터 선택
    computer_choice = random.choice(choices)

    # 결과 판단
    result = ""
    if user_choice == computer_choice:
        result = "😐 무승부!"
    elif (
        (user_choice == "가위" and computer_choice == "보") or
        (user_choice == "바위" and computer_choice == "가위") or
        (user_choice == "보" and computer_choice == "바위")
    ):
        result = "🎉 당신이 이겼어요!"
    else:
        result = "😢 컴퓨터가 이겼어요."

    # 결과 출력
    st.write(f"🧑 당신: {user_choice}")
    st.write(f"🤖 컴퓨터: {computer_choice}")
    st.subheader(result)
