# 패키지 임포트
import streamlit as st
from DBClient import DBClient
from GptAgent import GptAgent
from pdf_util import PdfUploader
import datetime 
import random

# Croma DB 접속용 클라이언트 인스턴스화
db_client = None
gpt_agent = None
pdf_uploader = None
UPLOAD_FILE_LIMIT = 2

def initDB(session_key:str):
    db_client = DBClient(session_key=session_key)
    gpt_agent = GptAgent(retriever=db_client.get_retriever())
    pdf_uploader = PdfUploader(db_client=db_client)
    return db_client, gpt_agent, pdf_uploader

# 데이터 업로드 및 크로마DB 저장
# @st.cache_data # decorator 1번만 실행후 재실행 금지
def uploadFile():
    if len(st.session_state.filenames) < UPLOAD_FILE_LIMIT:
        with st.empty():
            key = st.session_state.file_uploser_key
            file = st.file_uploader("🗂️ PDF 파일을 업로드하세요", type=["pdf"], key=key)
            if file is not None:
                success, summary =  pdf_uploader.upload(file)
                if success:
                    st.success("PDF 파일이 성공적으로 처리되었습니다!")
                    item = {'file_name':file.name, 'summary':summary}
                    st.session_state.filenames.append(item)
                else:
                    st.error("PDF 파일 처리에 실패했습니다!")
                
                import time
                time.sleep(1)

                st.session_state.file_uploser_key = get_key()
                uploadFile()
    else:
        st.error(f"PDF 파일이 최대치인 {UPLOAD_FILE_LIMIT}개 업로드 되었습니다.")
                

# 사이드바에 요약 표시
def print_file_list():
    print('check : list filenames')
    for item in st.session_state.filenames:
        with st.expander(f"📑 {item['file_name']}", expanded=True):
            st.write("📜 PDF 요약")
            st.write(item['summary'])

def get_key():
    return datetime.datetime.now().strftime('%Y%m%d%H%M%S') + str(random.randint(1000,1999))

def init():
    session_key = get_key()
    db_client, gpt_agent, pdf_uploader = initDB(session_key=session_key)

    st.session_state.session_key = session_key
    st.session_state.conversation = []
    st.session_state.filenames=[]
    st.session_state.file_uploser_key = get_key()
    st.session_state.is_reset = False

def reset():
    with bt_p:
        with st.spinner("시스템을 초기화 합니다."):
            init()
            bt_p.success('시스템 초기화를 완료하였습니다.')

# 초기화
if 'conversation' not in st.session_state:
    init()
else:
    session_key= st.session_state.session_key
    db_client, gpt_agent, pdf_uploader = initDB(session_key=session_key)

# 페이지 세팅
st.set_page_config(page_title="SKNETWORKS-FAMILY-AICAMP/SKN07-4th-2Team", layout='wide')
st.title('📑 사용자별 문서 기반 Q&A')

# 탭 구성
tab1, tab2 = st.tabs(["📄 파일 업로드 및 요약", "💬 질문 및 답변"])

# 파일 업로드 탭
with tab1:
    tab1.header("PDF 파일 업로드 및 요약")
    uploadFile()

    bt_p = st.empty()
    
    if len(st.session_state.filenames) > 0:
        st.button("초기화",on_click=reset)
    
    print_file_list()


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
    if question is not None:
        with st.chat_message('user'):
            st.write(question)
        
        with st.chat_message('assistant'):
            with st.spinner('답변을 생성 중입니다...'):
                answer = gpt_agent.send_message(question)
                st.session_state.conversation.append((question, answer))
                st.write(answer)
            
