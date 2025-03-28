# Chapter 02 데이터 획득하기
## Section 01 파이썬 데이터 분석 라이브러리 활용하기
- 대표적인 데이터 분석 라이브러리로 넘파이(Numpy)와 판다스(Pandas)가 있음.
- 넘파이는 수치 데이터를 다루는데 활용하는 파이썬 라이브러리.
- 판다스는 데이터 배열이나 테이블 형태의 데이터(tabular data)등의 자료구조를 처리하기 위한 라이브러리.
### 넘파이 이용하기
- `import numpy as np`

### 판다스 이용하기
- `import pandas as pd`
- `변수명 = pd.Series(data, index=index, name=name)`
- 데이터프레임은 시리즈가 여러 개 합쳐진 자료형

## Section 02 데이터 불러오기
- 판다스에서는 다양한 형태의 데이터를 불러오기 위해 'read_XXX' 함수를 주로 사용
  - read_csv
  - read_html
  - read_json
  - 등등
- `변수 = pd.read_csv(filepath, encoding, ...)`
 
## Section 03 데이터 저장하기
- 판다스에서 데이터를 저장할 때는 'to_csv' 함수를 사용한다.
- read_csv 함수가 가지는 다양한 파라미터를 이용하여 원하는 칼럼만 가지고 데이터프레임을 구성할 수도 있다.
- crosstab은 판다스 라이브러리에서 범주형 데이터 2개를 비교 분석할 때 사용한다.