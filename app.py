import streamlit as st
import pandas as pd

# -----------------------------------------------
# 0. 페이지 설정 및 구글 테마 CSS
# -----------------------------------------------
st.set_page_config(page_title="Content Summarizer", layout="centered")

st.markdown("""
<style>
    /* 구글 검색창 스타일 모방 */
    .main {
        background-color: white;
    }
    div.stTextInput > div > div > input {
        border-radius: 24px;
        padding: 12px 20px;
        border: 1px solid #dfe1e5;
        box-shadow: none;
        transition: box-shadow 0.2s;
    }
    div.stTextInput > div > div > input:hover, div.stTextInput > div > div > input:focus {
        box-shadow: 0 1px 6px rgba(32,33,36,.28);
        border-color: rgba(223,225,229,0);
    }
    /* 생성 버튼 스타일 */
    div.stButton > button {
        background-color: #f8f9fa;
        color: #3c4043;
        border: 1px solid #f8f9fa;
        border-radius: 4px;
        padding: 8px 16px;
        font-size: 14px;
        margin-top: 20px;
    }
    div.stButton > button:hover {
        border: 1px solid #dadce0;
        color: #202124;
        background-color: #f8f9fa;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------
# 1. 메인 UI 디자인
# -----------------------------------------------
st.markdown("<br><br><br>", unsafe_allow_html=True)
# 구글 로고 느낌의 타이틀 (텍스트)
st.markdown("<h1 style='text-align: center; color: #4285F4; font-size: 60px;'>Summarizer</h1>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# 검색창 영역
url_input = st.text_input("", placeholder="분석할 인스타그램 또는 유튜브 링크를 입력하세요", label_visibility="collapsed")

col1, col2, col3 = st.columns([1.5, 1, 1.5])
with col2:
    generate_btn = st.button("생성", use_container_width=True)

# -----------------------------------------------
# 2. 핵심 로직 (시뮬레이션)
# -----------------------------------------------
if generate_btn:
    if not url_input:
        st.warning("URL을 입력해 주세요.")
    else:
        with st.spinner('콘텐츠를 분석하고 요약하는 중입니다...'):
            # 여기에 실제 분석 함수들이 들어갈 자리입니다.
            if "youtube.com" in url_input or "youtu.be" in url_input:
                platform = "YouTube"
                # 예시 데이터
                data_to_save = {
                    "유튜브 제목": "테스트 영상",
                    "채널명": "테스트 채널",
                    "구독자수": "10만",
                    "조회수": "5,000",
                    "업로드 일자": "2024-05-20",
                    "내용요약": "이 영상은... (AI 요약본)"
                }
                st.success(f"{platform} 데이터가 수집되었습니다.")
                st.json(data_to_save)
                # TODO: Google Sheet 저장 로직 호출
                
            elif "instagram.com" in url_input:
                platform = "Instagram"
                data_to_save = {
                    "인스타 계정": "@user_test",
                    "팔로워수": "50k",
                    "조회수": "12,000",
                    "업로드 일자": "2024-05-19",
                    "내용 요약": "이 포스트는... (AI 요약본)"
                }
                st.success(f"{platform} 데이터가 수집되었습니다.")
                st.json(data_to_save)
                # TODO: Google Sheet 저장 로직 호출
                
            else:
                st.error("지원하지 않는 URL 형식입니다.")
