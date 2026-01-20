import streamlit as st

# 페이지 설정 (선택 사항이지만 깔끔한 브라우저 탭을 위해 권장)
st.set_page_config(page_title="Status Check", page_icon="✅")

# 화면에 "정상" 텍스트 표시
st.write("# 정상")

# 좀 더 직관적으로 보이고 싶다면 아래 스타일도 가능합니다 (선택 사항)
# st.success("서비스 상태: 정상")
