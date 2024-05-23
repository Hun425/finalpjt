# 📖 영화 추천 웹 서비스 개발 README


<img src="https://github.com/Hun425/finalpjt/assets/147483675/db05ea92-d341-424d-b2c7-416245dfdf36" alt="Logo >




<br>

## 프로젝트 소개

- 20대 이상 사용자에게 추억의 영화를 선호하는 장르를 기준으로 추천해주는 사이트입니다.
- 20대 미만 사용자들에게는 최근 영화를 장르에 맞춰 추천해줍니다.
- 영화의 기본 정보들을 알 수 있고, 사용자들이 어떤 영화를 얼마나 좋아하는지 알 수 있습니다.
- 자신이 좋아하는 영화를 저장하고, 목록으로 모아서 볼 수 있습니다.
- 심심할 때, 간단한 정보가 필요할 때, 챗 봇을 통해 정보를 얻을 수 있습니다.
- 자신이 관심있는 영화에 댓글을 달고, 다른 사용자들과 소통 할 수 있습니다.
- 원하는 영화 정보를 검색해 볼 수 있습니다.

<br>

## 팀원 구성

<div align="center">

| **채기훈** | **황민채** |
| :------: |  :------: |
| [<img src="https://avatars.githubusercontent.com/Hun425?v=4" height=150 width=150> <br/> @Hun425](https://github.com/Hun425) | [<img src="https://avatars.githubusercontent.com/trick0846?v=4" height=150 width=150> <br/> @trick0846](https://github.com/trick0846) |

</div>

<br>

## 1. 개발 환경

- Front :  js,  Vue
- Back-end : Django
- 버전 및 이슈관리 : Github
- 협업 툴 : Jira, Discord
- 디자인 : [Figma](https://www.figma.com/file/fAisC2pEKzxTOzet9CfqML/README(oh-my-code)?node-id=39%3A1814)

<br>

## 2. 채택한 개발 기술과 브랜치 전략


### Vue, Django

- SSAFY 관통 프로젝트의 필수 조건을 위해 채택했습니다.


### prettier

- 정해진 규칙에 따라 자동적으로 코드 스타일을 정리해 코드의 일관성을 유지하고자 했습니다.
- 코드 포맷팅은 prettier에 일임해 사용했습니다.


### 브랜치 전략

- 기본적으로 큰 틀을 Jira를 통해 세분화했습니다
- 각 세분화된 기능들을 branch로 생성해 main에 merge 하는 방식으로 협업을 진행했습니다.


<br>

## 3. 프로젝트 구조

```
├─backEnd
│─accounts
   │  ├─migrations
   │  
   ├─movies
   │  ├─management
   │  │  └─commands
   │  ├─migrations
   │    
   ├─movieweb
   │  
   └─static
      └─images
└─front-project
    ├─.vscode
    ├─public
    └─src
        ├─assets
        ├─components
        │  ├─actor
        │  ├─common
        │  └─movie
        ├─router
        ├─stores
        └─views
```

<br>

## 4. 역할 분담

    
### 👻채기훈

- **기능**
    - 백엔드 서버 기본 기능 개발, DB 구성, 챗봇 및 검색 기능 개발, 영화 추천 및 검색 알고리즘 작성, 기초 CSS 디자인

<br>



### 🐬황민채


- **기능**
    - 
    
<br>

## 5. 개발 기간 및 작업 관리

### 개발 기간

- 전체 개발 기간 : 2024-05-16 ~ 2024-05-23
- UI 구현 : 2024-05-18 ~ 2024-05-22
- 기능 구현 : 2024-05-16 ~ 2024-05-20

<br>

### 작업 관리

- 
- 

<br>


<br>

## 7. 페이지별 기능

### [초기화면]




| 초기화면/박스오피스 |
|----------|
|![image](https://github.com/Hun425/finalpjt/assets/147483675/db106f19-73b1-4ba2-a455-b9360be97184)|

- 오늘자 / 이번주자 영화진흥위원회 기준 1위부터 5위까지의 영화들을 불러옵니다.
- 박스오피스의 화면 배경은 오늘자 1위 영화의 배경화면으로 갱신됩니다.
- 영화 카드에 마우스를 올리면 네이버 예메 링크가 나옵니다.

  
<br>


### [네비게이션 바](수정예정)



| 네비게이션 바 |
|----------|
|![image](https://github.com/Hun425/finalpjt/assets/147483675/6c0233ac-33e7-4db0-b33b-01d8c592e82e)|

- 각각의 기능을 담당하는 페이지로 이동시켜줍니다.

<br>

#### 1. 영화 목록 페이지



##### 전체 영화 목록


| 전체영화 목록 |
|----------|
|![image](https://github.com/Hun425/finalpjt/assets/147483675/4179150d-a509-4f88-a75d-973fe1dd042c)|

- 전체 영화 목록을 보여주는 페이지입니다.
- 만약 로그인이 되어있는 경우 사용자의 나이에 따라서 관람등급에 맞지 않는 영화는 보여주지 않습니다.
- 로그인하지 않은 사용자에게는 모든 영화 목록을 노출합니다.

<br>

##### 최신 영화 목록


| 최신 영화 목록 |
|----------|
|![image](https://github.com/Hun425/finalpjt/assets/147483675/288ea531-62dd-4412-b953-6cb24e895850)|

- 현재 날짜 기준으로 30일 전까지 개봉한 영화들의 목록을 보여줍니다.
- 기본 정렬 순서는 평점 순서로 보여줍니다.

<br>

#### 2. 영화 추천


| 추천 |
|----------|
|![login]()|

- 사용자에게 맞는 영화를 랜덤으로 최대 10개를 뽑아서 추천해줍니다.
- 추천 기준은 사용자의 나이 등급에 맞는 영화 중에서, 사용자가 좋아요를 누른 영화 목록 중 가장 많이 선택한 장르로 추천해줍니다.
- 사용자가 좋아요를 누른 영화가 5개 이하 일때는 추천해주지 않습니다.

<br>

#### 3.커뮤니티


| 커뮤니티 |
|----------|
|![image](https://github.com/Hun425/finalpjt/assets/147483675/d6eabcb0-06a9-48c3-8321-9b1a459861b6)|

- 작성된 모든 리뷰를 최신순으로 보여줍니다.
- 작성된 리뷰의 영화 포스터, 리뷰 제목, 리뷰 줄거리 요약, 좋아요 개수, 댓글 개수를 보여줍니다.
- 리뷰 카드를 누르면 해당 리뷰가 적힌 페이지로 이동합니다.

<br>

#### 4. 영화 검색


| 영화 검색 |
|----------|
|![image](https://github.com/Hun425/finalpjt/assets/147483675/648de90b-40c5-432d-83e8-dbf335dc84aa)|

- 사용자가 원하는 영화를 한글로 입력하면 데이터베이스에 있는 영화중에 입력한 글자와 유사한 영화를 보여줍니다.
- 결과를 클릭하면 해당 영화의 링크로 이동합니다.
- 초성으로도 검색이 가능합니다.

<br>


#### 5. 로그인/회원가입


| 로그인/회원가입 |
|----------|
|![search]()|

- 왼쪽을 누르면 로그인, 오른쪽을 누르면 회원가입페이지가 나오게됩니다.
- 회원가입도중, 유저이름 또는 이메일이 중복되게되면 실시간으로 사용자에게 알려줍니다.
- 로그인/회원가입이 성공하거나 실패하면 알림 팝업창으로 알려줍니다.


<br>

#### 마이페이지


| 마이페이지 |
|----------|
|![image](https://github.com/Hun425/finalpjt/assets/147483675/e9779f4f-f53a-496a-9bf8-ab2e18b8c6e0)|

- 로그인된 사용자 정보를 볼 수 있습니다.
- 프로필 사진을 변경할 수 있습니다.
- 사용자가 좋아요누른 영화 목록 및 개수를 보여줍니다.
- 사용자가 좋아요 누른 리뷰 목록 및 개수를 보여줍니다.

<br>

### [챗봇]


| 챗봇 |
|----------|
|![search]()|

- 사용자가 인공지능과 소통이 가능한 채팅방입니다.
- 비로그인 사용자가 메세지를 보낼시, 로그인 요청 메세지로 응답합니다.
- clear 버튼을 통해 지금까지 보낸 메세지를 초기화 할 수 있습니다.

<br>


### [영화 상세페이지]

#### 1. 영화 상세 정보

| 영화 상세 정보 |
|----------|
|![image](https://github.com/Hun425/finalpjt/assets/147483675/93880e33-305b-47a6-af14-baa981132a53)|

- 영화의 상세정보을 열람 할 수 있습니다.
- 평점을 별점으로 간략하게 확인 할 수 있습니다.
- 리뷰작성 또는 트레일러 페이지로 이동 할 수 있습니다.


<br>

#### 2. 영화 리뷰 정보
| 리뷰 생성 |
|----------|
|![image](https://github.com/Hun425/finalpjt/assets/147483675/133df785-c924-4a77-ab45-a43de6fb78a7)|


| 리뷰 수정 & 삭제 |
|----------|
|![image](https://github.com/Hun425/finalpjt/assets/147483675/bdfd4e08-c739-4706-81ed-ea2b10d0a5d9)|

- 영화 리뷰를 수정, 삭제 또는 생성 할 수 있습니다.
- 별 아이콘을 클릭해서 개당 2점의 평점으로 최대 10점까지 줄 수 있습니다.
- 자기 자신이 쓴 글만 수정 및 삭제가 가능합니다.
<br>

#### 3. 좋아요와 댓글


| 좋아요 & 댓글 |
|----------|
|![image](https://github.com/Hun425/finalpjt/assets/147483675/883150de-0f88-444f-976b-a0e25e170f3d)|

- 로그인한 사용자는 좋아요 버튼과 댓글 생성 버튼을 누를 수 있습니다.
- 좋아요 개수와 댓글 개수를 표시해 줍니다.
- 자기 자신이 단 댓글만 삭제가 가능합니다.
- 좋아요를 이미 누른상태에서 한 번 더 누르게 되면 좋아요를 취소합니다.

<br>






## 8. 트러블 슈팅



<br>


## 9. 개선 목표

- 토큰 유효기간
- 유저간의 유사도를 기반으로한 추천시스템

<br>

## 10. 프로젝트 후기


### 👻 채기훈


<br>


### 🐬 황민채

