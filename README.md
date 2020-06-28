# MYSQL
  - mySql 설치 후, 환경 변수 설정에 MYSQL server8.x\bin 추가
  
```
  ## 데이터 베이스 생성 ##
      > CREATE DATABASE [생성할 데이터 베이스];
  ## 사용자 생성 ##
      > CREATE USER '[생성 할 사용자]'@'localhost' IDENTIFIED BY '[비밀번호]';
        *** Unable to load authentication plugin 'caching_sha2_password'. ***
          위와 같은 에러가 생기면 비밀번호를 RSA 보안을 사용해주지않아서 발생
          그럴 땐, 방법 1: 암호를 변경하는 , 방법 2: my.ini파일 수정하고 재기동한 이후의 생성 user만 적용
          방법1.
            - ALTER USER '[생성 한 사용자]'@'localhost' IDENTIFIED WITH mysql_native_password BY '[비밀번호]';
          방법2.
            - [mysqld]
            - default_authentication_plugin=mysql_native_password
   ## 권한 설정 ##
      > GRANT ALL PRIVILEGES on [생성된 데이터 베이스].* TO '[생성한 사용자]'@'localhost';
        ** 일부 권한만 주고 싶은 경우는 권한 줄 명령어를 나열
          - GRANT INSERT,UPDATE,INDEX,ALTER ON on testdb.* TO 'testuser'@'localhost';
   ## 끝으로(아래의 명령어를 잊지말고 실행) ##
      > FLUSH PRIVILEGES;
   ## 데이터 베이스 조회 ##
      > show databases;
   ## 사용자 정보 조회 ##
    - 사용자 정보는 user 테이블에 저장된다.
    - user 테이블은 mysql 데이터베이스에 존재하므로 use mysql문을 먼저 실행해야한다.
      > use [생성된 데이터 베이스];
      > SELECT host, user FROM user;
   ## 사용자 권한 조회 ##
      > SHOW GRANTS FOR '[생성한 사용자]'@'localhost'
```

# To Do List
```
  1. 얼굴 인식 후의 alert창 표시
  2. 동일날짜 동일인물 얼굴 인식 중복 막기(sql작업)
  3. 웹페이지 수정
  4. 교수님한테 보낼 자료 작성
```
