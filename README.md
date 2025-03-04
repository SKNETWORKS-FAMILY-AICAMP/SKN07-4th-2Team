# SKN07-4th-2Team



---

# 팀명 : 개구리 삼총사 🏃🏃‍♂️🏃‍♀️
|<img src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN07-4th-2Team/blob/main/image/%E3%85%85%E3%84%B1.jpg" alt="김성근" width="120"/>|<img src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN07-4th-2Team/blob/main/image/%E3%85%85%E3%85%81.jpg" alt="윤수민" width="120"/>|<img src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN07-4th-2Team/blob/main/image/%E3%85%88%E3%85%8A.jpg" alt="이재철" width="120"/>|
|---|---|---|
| <div align="center">**김성근**</div> | <div align="center">**윤수민**</div> | <div align="center">**이재철**</div> |
| <div align="center">BackEnd<br>요구사항정의서</div> | <div align="center">FrontEnd<br>화면설계서</div> | <div align="center">BackEnd<br>화면설계서</div> |

 ---
 
# 📜 LLM을 연동한 내외부 문서 기반 질의 응답 웹페이지 개발

## 🔖 프로젝트 배경

![배경](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN07-4th-2Team/blob/main/image/%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8%20%EB%B0%B0%EA%B2%BD.jpg)
---

### 문서의 줄 길이와 정보탐색 유형이 읽기 행동에 미치는 영향

- 줄 길이가 길수록 시선 고정 시간이 증가하고, 이는 인지 부하를 높이며 **학습 이해도에 부정적인 영향**을 미칠 수 있다는 것을 발견

- 이에 따라 문서 기반 Q&A 모델은 가독성을 고려해 줄 길이를 최적화하고, **핵심 정보를 요약**하여 **효율적인 정보 탐색을 지원**할 수 있다.

[출처 : 류지헌 and 문제웅. (2013). 학습용 전자책의 텍스트 길이와 정보탐색 유형이 시선고정 시간, 인지부하, 학습이해도에 미치는 영향. 한국교육학연구, 19(3), 293-313.]

---

## 🔖 프로젝트 개요

- 긴 문서의 가독성을 높이기 위한 최적화된 Q&A 모델 제공

- 긴 문서의 핵심 내용을 요약하고, RAG 기반으로 가독성 높은 답변 제공

- 사용자의 인지 부하를 줄이고, 효율적인 정보 탐색을 지원하는 Q&A 시스템 구축

## 🔖 주요 산출물
1. [요구사항 정의서](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN07-4th-2Team/blob/main/%EC%82%B0%EC%B6%9C%EB%AC%BC/%EC%9A%94%EA%B5%AC%EC%82%AC%ED%95%AD%20%EC%A0%95%EC%9D%98%EC%84%9C.pdf)

2. [화면 설계서](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN07-4th-2Team/blob/main/%EC%82%B0%EC%B6%9C%EB%AC%BC/%ED%99%94%EB%A9%B4%20%EC%84%A4%EA%B3%84%EC%84%9C.pdf)

3. [개발된 LLM 연동 웹 애플리케이션](http://localhost:8501)

---

## 🔖 기술 스택
<div>
<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
<img src="https://a11ybadges.com/badge?logo=openai" alt="OpenAI" width="163" height="28"/>
<img src="https://img.shields.io/badge/langchain-F7DF1E?style=for-the-badge&logo=langchain&logoColor=black">
<img src="https://img.shields.io/badge/streamlit%20-%23FF0000.svg?style=for-the-badge&logo=streamlit&logoColor=white">
<img src="https://github.com/pladata-encore/SKN07-3rd-2Team/blob/main/image/chromadb.jpg" alt="chromadb" width="90" height="40">
<div>
</div>
<img src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white">
<img src="https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white">
<img src="https://img.shields.io/badge/Discord-%235865F2.svg?style=for-the-badge&logo=discord&logoColor=white">
</div>

---

### 베이스 모델

- gpt-4o-mini-2024-07-18
---

## 🔖 System Architecture
![architecture](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN07-3rd-2Team/blob/main/image/%EC%95%84%ED%82%A4%ED%85%8D%EC%B2%98.jpg)

## 🔖 요구사항 정의서
![요구사항](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN07-4th-2Team/blob/main/image/%EC%9A%94%EA%B5%AC%EC%82%AC%ED%95%AD%EC%A0%95%EC%9D%98%EC%84%9C.jpg)

## 🔖 애플리케이션 시연

![시연1](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN07-4th-2Team/blob/main/image/%EC%8B%9C%EC%97%B0%ED%99%94%EB%A9%B41.jpg)

![시연2](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN07-4th-2Team/blob/main/image/%EC%8B%9C%EC%97%B0%ED%99%94%EB%A9%B42.jpg)

---

## 🔖 한 줄 회고

김성근 : 

윤수민 : 지난번 프로젝트 내용을 고도화 하는게 재밌었다. 화면 구성도 바꾸고, 필요한 기능도 추가하며 시간이 더 있었으면 했다. 화면 구현보다 기능 추가가 더 우선적이라 장고가 아닌 스트림릿을 쓰며 장점과 한계점을 동시에 느꼈다.

이재철 : 배운걸 써야한다는 생각보다 완성도를 챙기고 싶은 마음으로 진행하다가 시간이 부족하여 외부 사용자가 사용할 수 있게 웹서비스는 못한 점이 아쉽다. 마지막 최종 프로젝트에서는 좀 더 잘해봐야겠다.
