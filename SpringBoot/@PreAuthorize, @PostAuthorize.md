# @PreAuthorize, @PostAuthorize
Spring Security를 하던 도중 사용자 본인만 할 수 있는 기능을 구현함에 있어서 사용자 본인을 어떻게 확인할까라는 의문에서 시작되서 알게되었다.

기존에는 SecurityContextHolder.getContext().getAuthentication()를 사용하여 현재 사용자의 정보를 들고와 확인하는 코드를 만들었지만 이런 방법이 아닌 다른 방법이 있는가해서 알게된 것이 바로 @PreAuthorize, @PostAuthorize이다.

<br>


## @PreAuthorize, @PostAuthorize 이란
- @PreAuthorize : 함수를 실행하고 클라이언트한테 응답하기 직전에 권한을 검사하는 어노테이션
- @PostAuthorize: 요청이 들어와 함수를 실행하기 전에 권한을 검사하는 어노테이션

<br>

## 표현식
- hasRole([role]) : 현재 사용자의 권한이 파라미터의 권한과 동일한 경우 true

- hasAnyRole([role1,role2]) : 현재 사용자의 권한디 파라미터의 권한 중 일치하는 것이 있는 경우 true

- principal : 사용자를 증명하는 주요객체(User)를 직접 접근할 수 있다.

- authentication : SecurityContext에 있는 authentication 객체에 접근 할 수 있다.

- permitAll : 모든 접근 허용

- denyAll : 모든 접근 비허용

- isAnonymous() : 현재 사용자가 익명(비로그인)인 상태인 경우 true

- isRememberMe() : 현재 사용자가 RememberMe 사용자라면 true

- isAuthenticated() : 현재 사용자가 익명이 아니라면 (로그인 상태라면) true

- isFullyAuthenticated() : 현재 사용자가 익명이거나 RememberMe 사용자가 아니라면 true


<br>


## @PostAuthorize
```java
@PostAuthorize("isAuthenticated() and (( returnObject.name == principal.name ) or hasRole('ROLE_ADMIN'))")
@RequestMapping( value = "/{seq}", method = RequestMethod.GET )
public User getuser( @PathVariable("seq") long seq ){
    return userService.findOne(seq);
}
```
위의 @PostAuthoriz 어노테이션은 로그인 상태인가? 그리고 반환되는 사용자의 이름과 현재 사용자의 이름이 일치 한가? 또는 사용자가 관리자 권한을 가지고 있는가?


<br>


## @PreAuthorize
```java
@PreAuthorize("isAuthenticated() and (( #user.name == principal.name ) or hasRole('ROLE_ADMIN'))")
@RequestMapping( value = "", method = RequestMethod.PUT)
public ResponseEntity<Message> updateUser( User user ){
    userService.updateUser( user );
    return new ResponseEntity<Message>( new Message(), HttpStatus.OK );
}
```

위의 @PreAuthorize 어노테이션은 로그인 상태인가? 그리고 파라미터 user의 이름과 현재 사용자의 이름이 일치 한가? 또는 사용자가 관리자 권한을 가지고 있는가?


<br>
<br>

## 참조
https://steemit.com/kr-dev/@igna84/spring-security-preauthorize-postauthorize

