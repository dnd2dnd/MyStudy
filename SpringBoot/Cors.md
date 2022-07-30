# CORS
## CORS란
웹에서 보안적인 이유로 cross-origin HTTP 요청들을 제한한다. cross-origin HTTP를 사용하기 위해서 서버에 요청하고 서버가 동의한다면 웹에서 사용할 수 있다
CORS(Cross-Origin Resource Sharing)은 가져오는 리소스들이 안전한지 검사하는 정책이다.

<br>

## Origin(출처)
CORS에 대해서 알기전에 Origin이 무엇을 의미하는지 이해해야한다.
서버의 위치를 의미하는 URL의 구성들은 각각 의미하는 바가 있다.


출처는 Protocol과 Host, Port까지 모두 합친 것을 의미한다.
이들 중 하나라도 일치하지 않는다면 Cross-origin이고 모두 일치하다면 Same Origin이다

<br>

## CORS 동작
### Simple requset
단순 요청은 예비 요청을 보내지않고 서버에 직행을 본 요청을 보낸 후, 서버가 이에 대한 응답의 헤더에 Access-Control-Allow-Origin과 같은 값을 보내주면 브라우저가 CORS정책 위반여부를 검사하는 방식

<br>

HTTP Method : 
- GET
- POST
- HEAD

Header 
- Accept
- Accept-Language
- Content-Language
- Content-Type

자동으로 설정한 헤더외에는 CORS-safelisted request-header로 정의된 헤더만 사용할 수 있다.

<br>

Content-Type을 사용하는 경우
- application/x-www-form-urlencoded
- multipart/form-data
- text/plain


### Preflight request
예비요청은 요청을 보내기 전에 브라우저 스스로 안전한 요청인지 확인하는 것이다.

요청 헤더
- Origin
- Access-Control-Request-Method : 실제 요청에서 사용할 메소드
- Access-Control-Request-Headers : 실제 요청에서 사용할 헤더

응답 헤더
- Access-Control-Allow-Origin : 해당 Origin이 자원에 접근할 수 있도록 허용
- Access-Control-Expose-Headers : 브라우저가 엑세스할 수 있는 서버 리스트 
- Access-Control-Max-Age : 얼마나 오랫동안 요청이 캐싱될 수 있는지 나타냄
- Access-Control-Allow-Credentials : Credentials가 true일 때 요청에 대한 응답이 노출 될 수 있는지 나타냄
- Access-Control-Allow-Methods : 요청에 대한 응답으로 허용할 메소드
- Access-Control-Allow-Headers : 요청에 대한 응답으로 허용할 헤더

