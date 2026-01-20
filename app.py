import streamlit as st
from googleapiclient.discovery import build
import google.generativeai as genai
import re
from datetime import datetime

# -----------------------------------------------
# API 설정 (Secrets 관리 권장)
# -----------------------------------------------
YOUTUBE_API_KEY = st.secrets["YOUTUBE_API_KEY"]
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]

# Gemini AI 설정
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

# -----------------------------------------------
# 함수: 유튜브 데이터 추출
# -----------------------------------------------
def get_youtube_data(url):
    # URL에서 Video ID 추출 로직
    video_id_match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", url)
    if not video_id_match:
        return None
    video_id = video_id_match.group(1)

    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
    
    # 영상 정보 가져오기
    video_response = youtube.videos().list(
        part='snippet,statistics',
        id=video_id
    ).execute()

    if not video_response['items']:
        return None

    item = video_response['items'][0]
    snippet = item['snippet']
    stats = item['statistics']

    # 채널 정보 가져오기 (구독자 수)
    channel_response = youtube.channels().list(
        part='statistics',
        id=snippet['channelId']
    ).execute()
    
    sub_count = channel_response['items'][0]['statistics'].get('subscriberCount', '0')

    return {
        "title": snippet['title'],
        "channel_name": snippet['channelTitle'],
        "subscribers": sub_count,
        "views": stats.get('viewCount', '0'),
        "published_at": snippet['publishedAt'].split('T')[0],
        "description": snippet['description'] # 요약을 위한 원문 데이터
    }

# -----------------------------------------------
# 함수: Gemini AI 요약
# -----------------------------------------------
def summarize_content(text):
    try:
        prompt = f"다음 내용을 핵심 위주로 3줄 내외로 요약해줘:\n\n{text}"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"요약 실패: {str(e)}"

# -----------------------------------------------
# 메인 로직 내 실행 부분 (버튼 클릭 시)
# -----------------------------------------------
# ... (기존 UI 코드 유지) ...

if generate_btn:
    if not url_input:
        st.warning("URL을 입력해 주세요.")
    else:
        with st.spinner('Gemini AI가 분석 중입니다...'):
            if "youtube.com" in url_input or "youtu.be" in url_input:
                yt_data = get_youtube_data(url_input)
                
                if yt_data:
                    # Gemini 요약 실행
                    summary = summarize_content(f"제목: {yt_data['title']}\n설명: {yt_data['description']}")
                    
                    # 최종 저장용 데이터 구조
                    result = {
                        "유튜브 제목": yt_data['title'],
                        "채널명": yt_data['channel_name'],
                        "구독자수": yt_data['subscribers'],
                        "조회수": yt_data['views'],
                        "업로드 일자": yt_data['published_at'],
                        "내용요약": summary
                    }
                    st.success("유튜브 데이터 분석 완료!")
                    st.table([result]) # 결과 확인용 테이블
                else:
                    st.error("유튜브 정보를 가져올 수 없습니다.")
