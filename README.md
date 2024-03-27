# 영화 추천 및 리뷰 사이트 - 필독(Flim Docs)
- 누가 : 영화 정보를 찾는 사람들을 대상
- 무엇을 : 영화 상세 정보, 사람들의 리뷰(평론), 개인/상황에 맞는 영화 추천 기능을 제공
- 어떻게 : DRF(Django rest framework) + Vue.js를 이용하여 구현
- 왜(우리 프로그램을 사용할만한 이유) : 평론가 리뷰와 관람객 리뷰를 동시에 화면에 띄워 비교 가능, 관심 영화와 유사한 영화를 추천해주는 알고리즘
- 이름 : 영화를 하나 선택하면 예고편, 줄거리, 등장 배우, 리뷰, 관련 영화 추천 등의 관련 정보를 얻을 수 있음(영화 문서를 선택한 것과 같은 의미)
- 컨셉 : 영화와 관련된 모든 내용(감독 필모그래피, 배우 프로필/필모그래피, 영화 리뷰/평론, 영화 줄거리, 관련 영화)을 다른 페이지로 이동하지 않고 이 사이트에 전부 제공

## 기본 구현 기능
- 사용할 영화 데이터 API: TMDB(https://developer.themoviedb.org/reference)
- 첫 화면 : 메인 페이지 화면 띄우기, 화면 최상단에 nav bar 생성(왼쪽 부분 : 로고(누르면 홈으로 이동), 검색창, 추천 영화, 전체 영화 보기, option(filter) 영화 / 오른쪽 부분 : 개인 프로필, (알람) ), 영화 자동 재생
- 테마 : 블랙 & 옐로우

### 리뷰 구현
- CRUD 기능 구현
- 영화 평론(후기)를 영화 댓글란에 남길 수 있음
- 영화 detail page에서 보여주는 방식

### 로그인 기능
- 로그인 / 로그아웃
- 회원가입 - 좋아하는 영화 장르 선택지 제공 / 회원탈퇴
- 아이디와 닉네임 중복 검사 버튼
- 비밀번호와 비밀번호 재 입력 시 일치 여부 확인
- 회원정보수정
- 게시글 작성 / 영화 좋아요 / 댓글 작성 시 로그인이 필요
- 자신이 작성한 글 / 자신 계정만 수정 or 삭제 가능
- (django 관리자로 계정마다 다른 권한 부여 기능 - 확인 필요)

### 댓글
- 자신 혹은 남이 남긴 후기에 남길 수 있는 글
- 댓글에 좋아요 버튼을 구현
- 댓글을 호감순 / 최신순으로 보여줄 수 있는 선택지 제공
- 대댓글까지만 구현 - 깊이 : 1차

### 좋아요
- 영화 좋아요 기능 구현 / (별로에요 기능 구현)
- 좋아요 재 클릭 시 좋아요 취소 - 색을 통해 차이를 줌
- 리뷰 / 댓글에 좋아요 기능 구현

### 팔로우 / 팔로워 기능
- 자신이 아닌 다른 사람의 계정을 팔로우하는 기능 구현
- (자신이 팔로우한 사람의 리뷰가 항상 영화 평론창의 최상단에 위치)

### 개인 페이지(프로필 페이지)
- 자신이 작성한 댓글, 좋아요한 목록 출력(영화 : 포스터 출력)
- 자신의 팔로우 / 팔로워 수 출력
- (개인별 프로필 사진 변경 기능)
- (자신이 좋아요 누른 영화의 장르 -> 선택된 장르의 횟수에 따라 추천 정도가 달라짐)

### 영화 추천 서비스

0. 평점 & 인기도 순으로 내림차순 정렬 후, 추천 (기본 구현 - 추후 다른 추천 서비스가 구현되면 고민)

1. 날씨 연관 - 근거에 대한 자료가 필요 (구현 까다로움)
- 날씨가 사람의 기분에 영향을 끼치는 정도에 대한 근거
- 영화가 사람의 기분에 영향을 끼치는 정도에 대한 근거

2. 다양한 주제의 추천 서비스
- 일주일동안 가장 많이 좋아요가 눌린 영화
- 영화 전체에서 가장 많은 좋아요를 가진 영화
- 사용자가 좋아하는 장르의 영화(좋아요가 높은 순)
- 로그인한 사용자에게 바로 추천영화를 보여줌
(로그인창 -> 영화 추천 페이지 -> 메인 페이지)

## 추가 구현 기능

### 영화 등장인물 상세 페이지
- 웹 크롤링 영화배우 정보 인터넷에서 불러오기(구현 까다로움)
- 최적화 문제가 예상됨


### 메인 페이지 구성
- 영화 포스터 카드 형식으로 출력, 포스터 출력 시 상세 페이지로 이동
- 돌림판 형식의 카드 덱으로 구성


### 이상형 월드컵
- 데이터에 있는 영화 중 무작위로 64개를 선택해 32강을 진행
- 보여주는 2개의 영화는 모두 영화의 예고편으로 만약 영화의 예고편이 없다면 해당 영화의 포스터를 출력
- 결과 창에서 영화 상세 페이지로 이동하는 버튼과 다시 시작 버튼 2가지를 보여준다.
- 다시 시작 버튼 클릭 시, 다시 이상형 월드컵 진행
- 영화 상세 페이지 버튼 클릭 시, 해당 영화의 상세 페이지로 이동


# 역할 분담

## 주영인
- backend 폴더와 frontend 폴더 생성
  - Backend: django-admin startproject, Frontend: vue create, 
- 게시판(리뷰, reviews) 기능 구현
  - 게시판 생성: python manage.py startapp reviews, model 및 serializers 생성
- 사용자 계정 관리(accounts) 기능 구현
  - 게시판 생성: python manage.py startapp accounts, Vue로 회원가입 기능 구현 및 로그인 템플릿 생성


## 노수혁
- tmdb api로 전체 영화 리스트 가져오기 
  - Postman으로 영화 리스트 불러오기 : params에 key : api_key,  Value : TMDB API key 를 넣고 get 방식으로 실행
- Movie(movies) 출력 기능 구현
  - movies 내에 fixtures 폴더 생성, TMDB에 API_KEY를 활용해 영화 리스트를 불러오고 이를 JSON 형식으로 저장
  - genre와 movie 둘 다 100개씩 데이터를 저장해서 model에 맞게 데이터 처리 후 DB에 저장
- Django와 Vue CORS policy를 위해 사이트 허용 부분 추가

사용 프로그램 : 노션(하루에 진행할 내용 정리 및 하루가 끝날 때 마지막 점검 및 내일 일정 확인),
trello(당일에 진행할 내용을 todo에, 자신이 진행중인 부분을 doing에, commit까지 끝나면 done에 올리기),
github(기능 구현 시 commit 후 push), gitlab(결과물 upload)


# 요구사항 명세서

- 개발 환경
- Python 3.9.x
- Front-end : Vue 2, Vuex, Vue router
- Back-end : Django 3.2.x, Django REST framework
- DB : sqlite 3
- 개발 도구 : Git, VScode, npm, Postman

## Commit 규칙
- 참고 :  https://dejavuhyo.github.io/posts/patterns-for-writing-better-git-commit-messages/

```
01 [type](optional scope): [subject]

02 [optional body]

- 예시 -
Feat(Create): Add Create method in vue
vue에 게시글 작성 기능에 해당하는 Create라는 이름의 함수 기능 구현
```

1. type(타입)
   
|타입|설명|
|----|----------|
|create|새로운 폴더나 파일 생성|
|feat|새로운 기능 추가|
|fix|버그 수정|
|docs|문서 수정|
|style|코드 formatting, 세미콜론(;) 누락, 코드 변경이 없는 경우|
|refactor|코드 리팩터링|
|test|테스트 코드, 리팩터링 테스트 코드 추가(프로덕션 코드 변경 X)|
|design|CSS 등 사용자 UI 디자인 변경|
|build|관련 변경 사항 빌드|
|omment|필요한 주석 추가 및 변경|
|revert|되돌리기|
|rename|파일 혹은 폴더명을 수정하거나 옮기는 작업만인 경우|
|remove|파일을 삭제하는 작업만 수행한 경우|
|!BREAKING CHANGE|커다란 API 변경의 경우|
|!HOTFIX|급하게 치명적인 버그를 고쳐야 하는 경우|

2. scope
- 선택사항이며, 변경된 부분을 직접적으로 표기한다.
- 함수가 변경되었으면 함수명, 메소드가 추가되었으면 클래스 명을 입력한다.

3. subject
- 첫 글자는 대문자로 입력한다.
- 마지막에는 .(period)을 찍지 않으며 영문 기준 최대 50자를 넘지 않는다.
- 제목은 명령문의 형태로 작성한다. (동사원형 사용)
  
4. body
- 각 줄은 최대 72자를 넘지 않도록 한다.
- 어떻게 변경했는지보다, 무엇을 변경했고, 왜 변경했는지를 설명한다.


### 1. 영화 리뷰
  - 사용자가 영화 상세 페이지의 리뷰란에서 영화에 대한 평론 / 리뷰를 남길 수 있도록 구현
  - 리뷰란은 크게 두 섹션으로 구성, 평론가 리뷰 란과 사용자 리뷰 란
  - 평론가 리뷰 란에는 좋아요 기능만 구현, 댓글은 달지 못하도록 설정
  - 평론가 리뷰는 호감순(좋아요가 높은 순) / 이름순 선택이 가능하며, 선택에 맞게 리뷰가 노출 
  - 사용자 리뷰 란에는 좋아요와 댓글 기능 구현, 댓글을 대댓글까지만 가능하도록 설정(깊이 : 1차)
  - 사용자 리뷰는 호감순(좋아요가 높은 순) / 최신순 선택이 가능하며, 선택에 맞게 리뷰가 노출
  - 영화 / 리뷰에 싫어요 기능 구현, 영화에 싫어요 기능 구현 시, 유저의 싫어하는 장르에 해당 영화 장르를 포함 -> 선택 사항
  - 좋아요 와 싫어요는 하나 클릭 시 반대편은 클릭될 수 없도록 구현 -> 선택 사항


### 2. 사용자 계정 관리 기능
  - 로그인과 로그아웃, 회원가입과 회원 탈퇴 기능 구현
  - 회원정보 수정 기능 구현
  - 회원 가입 시 아이디, 비밀번호, 비밀번호 확인, 닉네임, 좋아하는 장르(선택지 버튼을 제공) 입력란이 있도록 구현
  - 개인 프로필에는 개인 프로필 사진, 닉네임 출력, 팔로우 팔로워 수(자신의 계정에서는 팔로우 버튼 안보이도록 구현), 좋아요 누른 영화 목록(영화 포스터로 출력, 영화 포스터 클릭 시 영화 상세페이지로 이동)과 영화 장르, 좋아요 누른 댓글, 남긴 리뷰(리뷰는 영화 제목까지 출력하도록 구현, 댓글이나 리뷰 클릭 시 해당 영화 상세페이지로 이동)가 보이도록 구현
  - 계정 닉네임 클릭 시 해당 유저의 프로필 란으로 이동
  - 개인 프로필에 미니홈피처럼 방문자 글 남길 수 있도록 설정, 댓글 1차까지만 가능하도록 설정 -> 선택 사항


### 3. 영화 검색 기능
  - 해당 검색어를 포함하는 이름을 가진 영화 목록을 출력(높은 유사성을 가진 제목부터 출력)
  - 해당 검색어를 장르로 갖는 영화 목록을 출력
  - 영화 배우 이름 검색 시 출연 영화 목록 출력
  - 해당 검색어를 포함하는 내용을 가진 영화 목록 -> 선택 사항
  - 검색을 했을 때 띄어쓰기를 기준으로 단어 포함 여부에 따라 검색결과 출력


### 4. 영화 추천 기능
  - 자신이 좋아하는 장르에서 무작위 / 평점순 / 인기순 / 좋아요 순 에 따라 영화 추천
  - 자신이 좋아요 누른 장르에는 가중치를 추가함
  - 추천할 영화가 좋아요 목록에 있다면 다음 영화를 추천하도록 설정 -> 선택 사항
  - 만약 추천 영화가 좋아요 목록에 있지만 좋아요를 누른지 오랜 시간이 지났다면 그대로 추천 -> 선택 사항
  - 추천 영화가 싫어요 목록에 있다면 다른 영화를 추천 -> 선택 사항
  - 날씨 api를 통해 날씨에 따른 영화 추천(날씨와 사람의 감정 혹은 영화와 사람의 감정 사이의 통계 자료나 논문을 찾았을 경우 적용)
  - 특정 기간동안 가장 많이 좋아요가 눌린 영화 추천
  - 전체 영화에서 가장 좋아요가 많은 영화 추천
  - 가장 싫어요가 많은 영화 추천 -> 선택 사항


## 프로젝트 작성 순서 초안
기본 프로젝트 구조 생성 -> 영화 전체 데이터 불러와서 화면에 띄우기 -> 게시판 기능 구현 -> 사용자 정보 관리 기능 구현(게시판 기능과 결합)
-> 영화 전체보기 페이지 구성(필터 기능 추가) -> 영화 상세 페이지 내부 구성 -> 영화 추천 알고리즘 작성 및 영화 추천 -> 영화 검색 기능 구현 -> 영화 상세페이지의 감독/배우 페이지 생성
-> 평론가 리뷰와 사용자 리뷰 크롤링 / api 사용 -> 이상형 월드컵 구현


# DB Schema 구성 및 ERD 작성

### User model
|필드명|Field Type|
|----|----------|
|id|Integer|
|password|varChar|
|last_login|datetime|
|is_superuser|boolean|
|username|varChar|
|first_name|varChar|
|last_name|varChar|
|email|varChar|
|is_staff|boolean|
|is_active|boolean|
|date_joined|datetime|
|followings|ManyToMany('self', symmetrical=False, related_name="followers")|


### Movie model
|필드명|Field Type|
|----|----------|
|id|Integer|
|title|Char|
|released_date|Date|
|poster_url|VarChar|
|overview|Text|
|vote_average|Float|
|genres|ManyToMany(Genre)|
|movie_like_users|ManyToMany(settings.AUTH_USER_MODEL, related_name="movielike")|
|movie_dislike_users|ManyToMany(settings.AUTH_USER_MODEL, related_name="moviedislike")|


### MovieLike model
|필드명|Field Type|
|----|----------|
|id|Integer|
|movie_id|BigInt|
|user_id|BigInt|


### MovieDislike model(선택)
|필드명|Field Type|
|----|----------|
|id|Integer|
|movie_id|BigInt|
|user_id|BigInt|


### Genre model(영화 장르)
|필드명|Field Type|
|----|----------|
|id|Integer|
|name|varChar|


### Comment model(평론 or 후기)
|필드명|Field Type|
|----|----------|
|id|Integer|
|content|Text|
|movie_title|ForeignKey(Movie)|
|created_at|datetime|
|updated_at|datetime|
|user_id|BigInt|
|like_users|ManyToMany(settings.AUTH_USER_MODEL, related_name="likecomment")|
|dislike_users|ManyToMany(settings.AUTH_USER_MODEL, related_name="dislikecomment")|


### Follow model(팔로우 / 팔로워)
|필드명|Field Type|
|----|----------|
|id|Integer|
|from_user_id|BigInt|
|to_user_id|BigInt|


### CommentLike model(평론 or 후기 좋아요)
|필드명|Field Type|
|----|----------|
|id|Integer|
|review_id|BigInt|
|user_id|BigInt|


### CommentDisLike model(선택)
|필드명|Field Type|
|----|----------|
|id|Integer|
|review_id|BigInt|
|user_id|BigInt|


### Review model(선택)
|필드명|Field Type|
|----|----------|
|id|Integer|
|content|Text|
|user_id|ForeignKey|
|review_id|BigInt|
|like_users|ManyToMany(settings.AUTH_USER_MODEL, related_name="likereview")|
|dislike_users|ManyToMany(settings.AUTH_USER_MODEL, related_name="dislikereview")|


### ReviewLike model(선택)
|필드명|Field Type|
|----|----------|
|id|Integer|
|review_id|BigInt|
|user_id|BigInt|


### ReviewDisLike model(선택)
|필드명|Field Type|
|----|----------|
|id|Integer|
|review_id|BigInt|
|user_id|BigInt|


# ERD 구조

![image1](/image/ERD_first_1.png)
![image2](/image/ERD_first_2.png)
![image3](/image/ERD_first_3.PNG)


# URL 구성

## backend
- movies 앱과 관련된 모든 주소는 `movies/` 로 시작
- reviews 앱과 관련된 모든 주소는 `reviews/` 로 시작
- accounts 앱과 관련된 모든 주소는 `accounts/` 로 시작

### movies
- 전체 영화 리스트를 불러오는 페이지 : 빈 URL
- 상세 영화 정보를 불러오는 페이지 : `<int:movie_pk>/`
- 추천 영화 정보를 불러오는 페이지 : `recommend/`

### reviews
- 해당 영화의 전체 리뷰를 보여주는 페이지 : `<int:movie_pk>/`
- 해당 영화의 특정 리뷰 하나를 자세히 보여주는 페이지 : `<intLmovie_pk>/<int:review_pk>/`

### accounts
- 회원가입 보여주는 페이지 : `signup/`
- 로그인 창을 보여주는 페이지 : `login/`
- 회원정보 수정 창을 보여주는 페이지 : `update/`
