# AICE study
본 레포는 [시나공 AI능력시험 AICE] 교재의 내용을 정리한 레포입니다.

본 실습에 필요한 코드(.ipynb)와 데이터(.csv)는 [여기](https://aice.study/board/notice/detail/861)에서 다운받으실 수 있습니다.

본 교재의 주요 언어와 소프트웨어 버전은 다음과 같습니다.
```
python 3.9
tensorflow 2.11.0
keras 2.11.0
pandas 1.4.4
numpy 1.21.5
```

## 목차
### PART 01 기본 학습하기 - AI 핵심 이론 및 활용
#### Chapter 01 AI 작업 환경 만들기
- 기본 환경 구성하기
  - 아나콘다 활용하기
  - 구글 코랩 사용하기
  - AICE 홈페이지의 AIDU 사용하기

#### [Chapter 02 데이터 획득하기](https://github.com/minju-kim98/AICE-study/tree/main/Chapter02/summary.md)
- 파이썬 데이터 문석 라이브러리 활용하기
  - 넘파이 이용하기
  - 판다스 이용하기
- 데이터 불러오기
- 데이터 저장하기

#### [Chapter 03 데이터 구조 확인하기]((https://github.com/minju-kim98/AICE-study/tree/main/Chapter03/summary.md))
- 데이터프레임 확인하기
  - 데이터 살펴보기
  - 데이터프레임의 기본 정보 확인하기

#### [Chapter 04 기초 데이터 다루기](https://github.com/minju-kim98/AICE-study/tree/main/Chapter04/summary.md)
- 필요 데이터 선택하기
  - 칼럼명으로 데이터 선택하기
  - 행 범위를 지정하여 데이터 선택하기
  - 특정 행, 열의 범위를 선택하여 데이터를 선택하기
  - 조건으로 데이터 선택하기
- 필요 데이터 변경하기
  - 데이터 추가하기
  - 데이터 삭제하기
  - 칼럼명 변경하기
  - 데이터프레임 정렬하기
- 데이터프레임 변경하기
  - 그룹화하기
  - 피벗테이블 생성하기
  - 인덱스 및 칼럼 레벨 변경하기
- 데이터프레임 병합하기
  - concat 활용하여 병합하기
  - merge/join 활용하여 병합하기

#### [Chapter 05 데이터 이해하기](https://github.com/minju-kim98/AICE-study/tree/main/Chapter05/summary.md)
- 지표로 데이터 탐색하기
  - 일변량 비시각화 탐색하기
  - 다변량 비시각화 탐색하기
- 시각화로 데이터 탐색하기
  - 일변량 시각화 탐색하기
  - 다변량 시각화 탐색하기
  - matplotlib 활용하기
  - seaborn 시각화 라이브러리 활용하기

#### [Chapter 06 데이터 전처리하기](https://github.com/minju-kim98/AICE-study/tree/main/Chapter06/summary.md)
- 수치형 데이터 정제하기
  - 결측치 파악하기
  - 결측치 처리하기
  - 이상치 파악하기
  - 이상치 처리하기
  - 구간화하기
- 범주형 데이터 정제하기
  - 레이블 인코딩하기
  - 원핫 인코딩하기
- 스케일링하기
  - 정규화하기
  - 표준화하기
- 변수 선택하기
  - 신규 변수 생성하기
  - 변수 선택하기

#### [Chapter 07 AI 모델링 필수 개념 이해하기](https://github.com/minju-kim98/AICE-study/tree/main/Chapter07/summary.md)
- AI란 무엇인가?
  - 머신러닝 이해하기
  - 딥러닝 이해하기
- AI 학습 방법 이해하기
  - 지도학습 이해하기
  - 비지도학습 이해하기
- AI 모델링 프로세스 이해하기
  - AI 모델링 프로세스
- 학습 데이터의 분할 방법 이해하기
  - 학습 데이터 분할하기
  - k-fold 교차 검증하기
  - 학습 과정을 시각화하여 과적합 확인하기
- AI 모델 평가 이해하기
  - 분류 모델 평가하기
  - 회귀 모델 평가하기

#### [Chapter 08 지도학습으로 AI 모델링하기](https://github.com/minju-kim98/AICE-study/tree/main/Chapter08/summary.md)
- 머신러닝으로 AI 모델링하기
  - 사이킷런 라이브러리
  - 선형 회귀
  - 로지스틱 회귀
  - 의사결정나무
  - 앙상블
  - 랜덤 포레스트
  - 그래디언트 부스팅
- 딥러닝으로 AI 모델링하기
  - 인공신경망
  - 심층신경망
  - 딥러닝 프레임워크
  - 심층신경망으로 항공사 고객 만족 분류 모델 구현 실습하기

#### [Chapter 09 비지도학습으로 AI 모델링하기](https://github.com/minju-kim98/AICE-study/tree/main/Chapter09/summary.md)
- 차원 축소
  - 주성분 분석
  - t-분산 확률적 아웃 임베딩
- 군집화
  - K-평균 군집화
  - DBSCAN
  - 고객 세분화 모델 구현 실습하기

#### [Chapter 10 모델 성능 향상하기](https://github.com/minju-kim98/AICE-study/tree/main/Chapter10/summary.md)
- 모델 하이퍼파라미터 튜닝 이해하기
  - 그리드 서치
  - 랜덤 서치
- 머신러닝 모델링 및 하이퍼파라미터 튜닝 실습하기
  - [회귀] 항공권 가격 예측 모델링하기
  - [분류] 항공사 고객만족 여부 예측 모니터링

### PART 02 심화 학습하기 - AI 사례 실습
#### [Chapter 11 비데 / 정수기 렌탈 고객 해지 여부 예측하기](https://github.com/minju-kim98/AICE-study/tree/main/Chapter11/summary.md)
- AI 작업환경 만들기
  - 패키지 설치하기
  - 패키지 불러오기
  - 옵션 설정하기
- 기초 데이터 다루기와 전처리하기
  - 데이터 획득하기
  - 데이터 구조 확인하기
  - 데이터프레임 합치기
  - 결측치 처리하기
  - 데이터 유형 변경하기
  - 파생 변수 추가하기
  - 불필요한 칼럼 삭제하기
- 데이터 이해하기(EDA와 시각화)
  - 출력값 분석하기
  - 수치형 데이터 분석하기
  - 수치형 데이터의 이상치 제거하기
  - 이상치 제거 후 수치형 데이터 분석하기
  - 범주형 데이터 분석하기
- AI 모델링을 위한 전처리하기
  - 표준화와 정규화하기
  - 레이블 인코딩하기
  - 원핫 인코딩하기
  - 다중공선성 제거하기
- 모델링과 평가하기
  - 데이터 분할하기
  - 모델별 성능 그래프 그리기
  - 모델 생성하기
  - AI 모델 평가하기