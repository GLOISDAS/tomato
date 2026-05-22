import streamlit as st
import joblib
import numpy as np

# 페이지 설정
st.set_page_config(
    page_title="🍅 토마토 착과율 예측",
    page_icon="🍅",
    layout="centered"
)

# CSS 스타일
st.markdown("""
<style>

.main {
    background: linear-gradient(to bottom, #fff5f5, #ffecec);
}

.title {
    text-align: center;
    font-size: 48px;
    font-weight: bold;
    color: #ff4d6d;
    margin-top: -20px;
}

.subtitle {
    text-align: center;
    font-size: 20px;
    color: #777;
    margin-bottom: 30px;
}

.card {
    background-color: white;
    padding: 25px;
    border-radius: 25px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}

.result-box {
    background: linear-gradient(to right, #ffccd5, #ffc2d1);
    padding: 25px;
    border-radius: 25px;
    text-align: center;
    font-size: 32px;
    font-weight: bold;
    color: #d6336c;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    margin-top: 20px;
}

.stButton > button {
    width: 100%;
    height: 60px;
    border-radius: 20px;
    border: none;
    background: linear-gradient(to right, #ff758f, #ff4d6d);
    color: white;
    font-size: 24px;
    font-weight: bold;
    transition: 0.3s;
}

.stButton > button:hover {
    transform: scale(1.03);
    background: linear-gradient(to right, #ff4d6d, #ff758f);
}

[data-testid="stSidebar"] {
    background-color: #fff0f3;
}

</style>
""", unsafe_allow_html=True)

# 제목
st.markdown(
    '<div class="title">🍅 토마토 착과율 예측기 🍅</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI가 토마토의 환경 상태를 분석해 착과율을 예측해줘요 💖</div>',
    unsafe_allow_html=True
)

# 모델 불러오기
model = joblib.load("tomato_model2.pkl")

# 사이드바
st.sidebar.title("🌱 환경 데이터 입력")

st.sidebar.write("토마토가 자라는 환경을 입력해주세요!")

# 입력창
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)

    temp_in = st.slider("🌡 내부온도 (°C)", 0.0, 50.0, 25.0)
    humidity_in = st.slider("💧 내부습도 (%)", 0.0, 100.0, 60.0)
    co2_in = st.slider("🫧 내부 CO₂ (ppm)", 0.0, 2000.0, 500.0)
    temp_out = st.slider("☀ 외부온도 (°C)", -10.0, 50.0, 20.0)

    st.markdown('</div>', unsafe_allow_html=True)

# 입력 데이터
X = np.array([[temp_in, humidity_in, co2_in, temp_out]])

# 버튼
if st.button("🍅 착과율 예측하기"):

    prediction = model.predict(X)
    result = prediction[0]

    st.markdown(
        f"""
        <div class="result-box">
            🍅 예측 착과율 🍅<br><br>
            {result:.2f} %
        </div>
        """,
        unsafe_allow_html=True
    )

    # 상태 메시지
    if result >= 80:
        st.balloons()
        st.success("🌟 토마토가 엄청 건강하게 자라고 있어요!")

    elif result >= 60:
        st.info("😊 좋은 환경이에요! 조금만 더 관리해봐요!")

    else:
        st.warning("⚠ 환경을 조금 개선하면 더 잘 자랄 수 있어요!")

# 하단 문구
st.markdown("""
<br><br>
<div style='text-align:center; color:gray; font-size:15px;'>
made with 💖 using Streamlit
</div>
""", unsafe_allow_html=True)