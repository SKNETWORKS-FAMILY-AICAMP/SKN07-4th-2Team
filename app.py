# 패키지 임포트
import streamlit as st
from DBClient import DBClient
from GptAgent import GptAgent
from pdf_util import PdfUploader

# Croma DB 접속용 클라이언트 인스턴스화
db_client = DBClient()
gpt_agent = GptAgent(retriever=db_client.get_retriever())
pdf_uploader = PdfUploader()

# 데이터 업로드 및 크로마DB 저장
@st.cache_data # decorator 1번만 실행후 재실행 금지
def init(uploaded_file):
    if uploaded_file is None:
        return
    
    success, summary =  pdf_uploader.upload(uploaded_file)

    if success:
        st.success("PDF 파일이 성공적으로 처리되었습니다!")
    else:
        st.error("PDF 파일 처리에 실패했습니다!")
        return
    
    if summary is not None:
    # 사이드바에 요약 표시
        st.write("📜 PDF 요약")
        st.write(summary)

# 초기화
if 'conversation' not in st.session_state:
    st.session_state.conversation = []

# 페이지 세팅
st.set_page_config(page_title="SKNETWORKS-FAMILY-AICAMP/SKN07-4th-2Team", layout='wide')
st.title('📑 사용자별 문서 기반 Q&A')

# 탭 구성
tab1, tab2 = st.tabs(["📄 파일 업로드 및 요약", "💬 질문 및 답변"])

# 파일 업로드 탭
with tab1:
    st.header("PDF 파일 업로드 및 요약")
    uploaded_file = st.file_uploader("🗂️ PDF 파일을 업로드하세요", type=["pdf"])
    if uploaded_file:
        init(uploaded_file)

# 질문 탭
with tab2:
    st.header("문서 기반 질문 및 답변")
    with st.expander("질문&답변 히스토리 보기", expanded=False):
        for q, a in st.session_state.conversation:
            with st.chat_message('user'):
                st.write(q)
            with st.chat_message('assistant'):
                st.write(a)

    # 프롬프트 입력 box
    question = st.chat_input('질문을 입력하세요')
    if question:
        with st.chat_message('user'):
            st.write(question)
        
        with st.chat_message('assistant'):
            with st.spinner('답변을 생성 중입니다...'):
                answer = gpt_agent.send_message(question)
                st.session_state.conversation.append((question, answer))
                st.write(answer)
            
