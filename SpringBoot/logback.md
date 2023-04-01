# Logback
자바 오픈소스 로깅 프레임워크로 스프링 부트의 기본으로 설정되어 있어서 사용시 별도로 라이브러리를 추가하지 않아도 된다.


## <b>설정</b>
1) 스프링, 일반 자바 일경우
- logback.xml 파일을 resources 디렉토리에 만들어서 참조한다.

2) 스프링 부트 일 경우
- logback-spring.xml 파일을 resources 디렉토리에 만들어서 참조한다.

<br>

## <b>로그 레벨 순서</b>
ERROR > WARN > INFO > DEBUG > TRACE

로그의 레벨은 5가지가 있다.

1. ERROR : 요청을 처리하는 중 오류가 발생한 경우 표시한다.
2. WARN : 처리 가능한 문제, 향후 시스템 에러의 원인이 될 수 있는 경고성 메시지를 나타낸다.
3. INFO : 상태변경과 같은 정보성 로그를 표시한다.
4. DEBUG : 프로그램을 디버깅하기 위한 정보를 표시한다.
5. TRACE : 추적 레벨은 DEBUG 보다 훨씬 상세한 정보를 나타낸다.

출력 레벨의 설정에 따라 설정 레벨 이상의 로그를 출력한다.
- EX) 로그 레벨이 "INFO" 일경우 "DEBUG", "TRACE" 레벨은 무시한다.

<br>
<br>

## <b>logback-spring.xml </b>
- 대소문자를 구별하지 않는다.
- name attribute를 반드시 지정해야 한다.
- appender와 logger로 크게 두개로 구분된다.
- Dynamic Reloading 기능을 지원한다.

<br>

### <b>appender</b>

- log의 형태를 설정, 로그 메시지가 출력될 대상을 결정하는 요소 

<br >

### appender class 종류

ch.qos.logback.core.ConsoleAppender
- 콘솔에 로그를 찍음, 로그를 OutputStream에 작성하여 콘솔에 출력되도록 한다.
ch.qos.logback.core.FileAppender
- 파일에 로그를 찍음, 최대 보관 일 수 등을 지정할 수 있다.
ch.qos.logback.core.rolling.RollingFileAppender
- 여러개의 파일을 순회하며서 로그를 찍는다.
ch.qos.logback.classic.net.SMTPAppender
- 로그를 메일에 찍어 보낸다.
ch.qos.logback.classic.db.DBAppender
- DB에 로그를 찍는다.

추가적인 클래스
 - (https://logback.qos.ch/manual/appenders.html)

<br>

### <b> root, logger</b>

root 
- 전역 설정, 지역적으로 선언된 logger 설정이 있다면 해당 logger 설정이 default로 적용된다.

logger
- 지역설정, additvity 값은 root 설정 상속 유무 설정, default = true

<br>

### <b>property</b>
- 설정 파일에서 사용될 변수값 선언

<br>

### <b>layout, encoder</b>
layout
- 로그의 출력 포맷을 지정한다.

encoder 
- Appender에 포함되어 사용자가 지정한 형식으로 표현 될 로그 메시지를 변환하는 역할을 담당하는 요소

<br>

### <b>pattern</b>

- %Logger{length} : Logger name을 축약할 수 있다. {length}는 최대 자리 수, ex)logger{35}
- %-5level : 로그 레벨, -5는 출력의 고정폭 값(5글자)
- %msg : - 로그 메시지 (=%message)
- ${PID:-} : 프로세스 아이디
- %d : 로그 기록시간
- %p : 로깅 레벨
- %F : 로깅이 발생한 프로그램 파일명
- %M : 로깅일 발생한 메소드의 명
- %l : 로깅이 발생한 호출지의 정보
- %L : 로깅이 발생한 호출지의 라인 수
- %thread : 현재 Thread 명
- %t : 로깅이 발생한 Thread 명
- %c : 로깅이 발생한 카테고리
- %C : 로깅이 발생한 클래스 명
- %m : 로그 메시지
- %n : 줄바꿈(new line)
- %% : %를 출력
- %r : 애플리케이션 시작 이후부터 로깅이 발생한 시점까지의 시간(ms)

<br>

### <b>etc</b>
`<`file>
- 기록할 파일명과 경로를 지정한다.

`<`rollingPolicy class>
- ch.qos.logback.core.rolling.TimeBasedRollingPolicy - 일자별 적용
- ch.qos.logback.core.rolling.SizeAndTimeBasedFNATP - 일자+크기별 적용

`<`fileNamePattern>
- 파일 쓰기가 종료된 log 파일명의 패턴을 지정한다.
- .gz, .zip으로 자동으로 압축할 수도 있다.

`<`maxFileSize>
- 한 파일당 최대 파일 용량을 지정
- log 내용 크기도 IO성능에 영향을 미치기 때문에 되도록 너무 크지 않는 사이즈로 지정한다.
- KB, MB, GB 3가지로 지정 가능하다.
- RollingFile 이름 패턴에 .gz, .zip을 입력할 경우 로그파일을 자동으로 압축해주는 기능도 있다.

`<`maxHistory>
- 최대 파일 생성 갯수
- maxHistory가 30, Rolling 정책을 일 단위로 하면 30일동안만 저장한다.

`<`Filter>
- 해당 패키지에 무조건 로그를 찍는 것말고도 필터링이 필요한 경우에 사용하는 기능












