# DAO, DTO, VO

## DAO
DAO(Data Access Object) 는 데이터베이스의 data에 접근하기 위한 객체입니다. DataBase에 접근 하기 위한 로직 & 비지니스 로직을 분리하기 위해 사용합니다.

<br>

## DTO
DTO(Data Transfer Object) 는 계층 간 데이터 교환을 하기 위해 사용하는 객체로, DTO는 로직을 가지지 않는 순수한 데이터 객체(getter & setter 만 가진 클래스)입니다.

유저가 입력한 데이터를 DB에 넣는 과정을 보겠습니다.

유저가 자신의 브라우저에서 데이터를 입력하여 form에 있는 데이터를 DTO에 넣어서 전송합니다.

해당 DTO를 받은 서버가 DAO를 이용하여 데이터베이스로 데이터를 집어넣습니다.

<br>

## VO
VO(Value Object) 값 오브젝트로써 값을 위해 쓰입니다. read-Only 특징(사용하는 도중에 변경 불가능하며 오직 읽기만 가능)을 가집니다.

DTO와 유사하지만 DTO는 setter를 가지고 있어 값이 변할 수 있습니다.
