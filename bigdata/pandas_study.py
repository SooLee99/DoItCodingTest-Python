B. pandas basic
# pandas 의 기본자료구조, Serise, DataFrame
# Serise : 컬럼이 없음, 인덱스만 존재하는 자료구조
# DataFrame: 인덱스와 컬럼이 존재하는 자료구조

s= pd.Series([1,2,3]) # 리스트 또는 배열을 시리즈로 변환, 인덱스는 0,1,2...자동
s= pd.Series(np.array([1,2,3]))
s= pd.Series({'a':5, 'b':6}) # 딕셔너리를 시리즈로 변환, 인덱스는 a, b가 됨
s= pd.Series([1,2,3], index=['a','b','c']) # 인덱스 설정가능
# 시리즈는 index와 value로 구성되어있음.
# 데이터프레임은 index, column, value로 구성

df= pd.DataFrame([2,3,4,5]) 와 df= pd.DataFrame([[2,3,4,5]])의 차이점
df= pd.DataFrame(2, index=[1,2], columns=['갑','을']) # 2*2, 값을 2로 채움
df= pd.DataFrame([[2,3],[4,5]], index=[1,2], columns=['갑','을']) # 2*2 값이 2,3,4,5로 채워짐
a= pd.Series([1,4,np.nan,6]) # 시리즈의 생성
a= pd.date_range('20180830', periods=7) # 날짜형을 연속으로 구성
# 인덱스와 컬럼은 리스트로 부여, values는 스칼라, 리스트 또는 배열가능, 단 리스트일 경우 행열차원이 맞아야함.
df= pd.DataFrame(values, index=dates, columns=cols)
df= pd.DataFrame({'key':['K0','K4'], 'A':['A0','A1']}) #딕셔너리로 데이터 프레임 생성, 컬럼은 key, A가 되고 index는 디폴트로 0,1,2~
df= pd.DataFrame(a) # 시리즈에서 바로 데이터프레임 생성 , index와 column은 디폴트로 0,1,2~
df=pd.DataFrame(a, index=[1,2,3,4,5], columns=['숫자']) # index와 column 지정
df.head(), df.tail(), df.columns, df.index,
df.values # ndarray형식으로 나옴
df.info() # 데이터프레임의 개요
df.describe() # 데이터프레임의 통계적 개요 (개수, 평균, 표준편차, 최소/최대, 25%/50%/75% 지점 정보)
df.sort_values(by='B', ascending=False) # B열 기준 내림차순
df.sort_index(ascending= False) # 인덱스 내림차순
df['C'] # 특정컬럼 데이터만 보기 -> 시리즈 형식, 차원축소
df.C # 위와 동일
df[1:3] # (행)슬라이싱, 차원유지
df['2018-08-31':'2018-09-02'] # 인덱스 값을 사용해 (행)슬라이싱
df.loc['2018-08-31'] # location 정보를 옵션으로 하여 슬라이싱 지원->컬럼명이 인덱스가 됨->시리즈형식, 차원축소
df.loc[:,['A','B']] # (열)슬라이싱
df.loc[:,df.columns[:2]] # (열)슬라이싱
df.loc[1:2, ['B','C']] # 안된다.
df.loc['2018-09-01':'2018-09-03', ['B','C']] # 행과열 슬라이싱
df.loc[df.index[2:5], df.columns[1:3]]
df.loc['2018-09-01', ['B','C']] # 차원축소
df.loc['2018-09-01', 'B'] # 인덱싱 2번, 데이터프레임->시리즈->값 (차원축소2번)
df.iloc[1] # 펜시인덱싱방식과 유사, 행과 열의 번호를 이요하여 데이터를 접근
df.iloc[1,2] 와 df.iloc[[1,2]]의 차이점
df.iloc[2:5, 1:3]
df.iloc[[1,4,2],[0,2]] # 통상 슬라이싱은 데이터가 붙어있을때 가능, 인덱스지정이 떨어져있어도(불연속) 지정가능
df.[df.C > 0] # C열 기준 0보다 큰 데이터를 가진 가로열 데이터만 모아서 출력
df.[df > 0] # 조건에 해당되지 않을때 NaN으로 처리
df.copy() 와 df[:] 동일함. 복제 df1=df와 차이점?

# 기존 df에 데이터 추가 df['new_col']= 리스트
# df['new_col']= 시리즈 ? 인덱스가 같으면 가능함?
# 해당컬럼안에 특정값있는지 체크, df['해당컬럼'].isin(['특정값','특정값'])
# 누적합 df.apply(np.cumsum)

# 컬럼 이름바꾸기
df.rename(index={'kim':'A'}, columns={'best':'1'})
# 인덱스 바꾸기
df.reset_index() 아래와 반대되는 개념으로 index를 0,1,2~ 로 만든다.
df1= df.set_index(['c','d']) 하나이상의 칼럼(c,d)을 색인으로 하는 새로운 df를 생성할수있다.
df1= df.reindex(['a','b','c','d']), 새로운 색인 a~d으로 설정한다. 색인값이 비어있다면 Nan또는 새로 추가가능

# NaN값 처리
df['A'].isnull() # df A칼럼에서 nan값을 가지는 항목을 true로 반환
nanIdx = df[df['A'].isnull()].index  # df A칼럼에서 nan값을 가지는 항목의 id를 얻는다.
if nanIdx.any():
    TR.loc[nanIdx, 'A'] = 0 # df['A'].fillna(0)과 동일
df.dropna(subset=['A']) # df A칼럼에서 nan값을 가지는 항목을 삭제한다.
df['A'].fillna(df['A'].median, inplace= True) # df A칼럼에서 nan값을 가지는 항목을 중간값으로 채워넣는다.

# 열 또는 행 제거하기
df.drop(['E'], inplace=True, axis=1), E열 삭제, 또는 df.drop('E', axis=1) 또는 del df['E']
df.drop(['행1', '행2']) # 디폴트로 axis=0, 행삭제임.

# 데이터프레임 합치기 merge, join, concat
# 각 데이터프레임을 컬럼기준으로 합치기
pd.merge(df1, df2, on='A') # 두개의 df를 공통으로 있는(이름이 동일한) A컬럼을 기준으로 합친다. 교집합
pd.merge(df3, df4, left_on='L', right_on='R') # 두개의 df에 공통컬럼이 없다면 따로 지정해준다. 교집합
pd.merge(df1, df2, on='A', how='outer') # left 기본 교집합에 왼쪽 모든로우를 포함, right, outer 합집합 inner 교지합
pd.merge(df1, df2, on=['A','B'], how='outer') # 여러개의 key로 병합할때는 리스트

# 각 데이터프레임을 인덱스기준으로 합치기
pd.merge(left, right, how='outer', left_index= True, right_index= True)
left2.join(right2, how='outer') # 상기 동일

pd.merge(df1, s.to_frame(), left_index= True, right_index= True) # 기존 df1에 시리즈s를 병합하려면 공통된 인덱스를 기준으로
df1.merge(s.to_frame() .....) # 상기동일, 시리즈를 우선 데이터프레임으로 변환시킨다음 병합시킨다.

pd.merge(df1, s.to_frame(), left_index= True, right_index= True, how='left')
left2.join(right2) # 상기동일, join의 기본값은 left2의 index값을 기준으로 합친다. 왼쪽 우선조인
df1['컬럼']= s # 상기동일, 동일한 키가 아닐경우 NaN값으로 채워진다. df1의 인덱스기준으로 합친다.

# concat
pd.concat([s1,s2,s3]) # concat은 axis=0을 기본값으로 하고 새로운 시리즈 객체를 생성한다.
pd.concat([s1,s2,s3], axis=1) # axis1은 컬럼방향(가로)를 의미한다. 데이터프레임을 생성한다.
pd.concat([s1,s1,s3], keys=['one', 'two', 'three']) # 계층적 색인 생성
pd.concat([s1,s1,s3], axis=1, keys=['one', 'two', 'three']) # keys는 컬럼제목이 된다.
데이터프레임에 대해서도 위와 같은 방식으로 적용가능하다.

# stack과 unstack
stack은 컬럼을 로우로 회전시킨다.
unstack은 로우를 컬럼으로 회전시킨다.

시리즈 map(), apply()
데이터프레임 apply(), applymap(), groupby
applymap은 데이터프레임의 개별값을 인자로 받는다.
apply는 데이터프레임의 시리즈(컬럼)을 인자로 받는다.

# map(), apply()
df['class']= df['class'].map({'Kim':'A', 'Seo':'B', 'Han':'C'}) # 치환
df['A']= df['A'].apply(lambda v:1 if v>=1.3 else 0)
df['C'] df.apply(lambda r:r['A']*r['B'], axis=1) # axis 1은 인덱스방향, 0은 컬럼방향

# applymap() , 데이터프레임 전체 데이터셀에 적용한다.
df.applymap(lambda v: np.log(v) if isinstance(v, float) else v
df.applymap(lambda x: x if not '$' in str(x) else x.replace('$', ''))

# groupby()
df.groupby('A')['B'].mean()
df['B']groupby('A').mean()