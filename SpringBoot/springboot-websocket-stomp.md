# Spring WebSocket Stomp 
STOMP(Simple Text Oriented Messaging Protocol)는 WebSocket 위에서 동작하는 간단한 텍스트 기반 메시지 프로토콜로, 클라이언트와 서버가 전송할 메시지의 유형, 형식, 내용들을 정의합니다.

pub/sub 기반으로 동작하고 WebSocketHandler를 직접 구현할 필요 없이 @MessaingMapping 같은 어노에티션을 사용해서 메시지 발행 시 엔드포인트를 별도로 분리해서 관리할 수 있다.

<br>

## 구현
``` java
@Getter
@Setter
@ToString
public class Message {
    private String message;
    private String type;
    private String monitorId;
}

@Configuration
@EnableWebSocketMessageBroker
public class WebSocketConfig implements WebSocketMessageBrokerConfigurer {

    @Override
    public void registerStompEndpoints(StompEndpointRegistry registry) {
        registry.addEndpoint("/ws")
                .setAllowedOriginPatterns("*")
//         client가 sockjs로 개발되어 있을 때만 필요, client가 java면 필요없음
//                .withSockJS()
        ;
    }

    @Override
    public void configureMessageBroker(MessageBrokerRegistry registry) {
        registry.setApplicationDestinationPrefixes("/pub");
        registry.enableSimpleBroker("/sub");
    }
}

@Controller
@RequiredArgsConstructor
public class MessageController {
    private final SimpMessageSendingOperations simpMessageSendingOperations;

    @MessageMapping("/sendMessage")
    public void sendMessage(Message message) {
        simpMessageSendingOperations.convertAndSend("/sub/monitor/" + message.getMonitorId(), message);
    }
}
```

- @EnableWebSocketMessageBroker : WebSocket 메시지 브로커를 활성화하여 실시간 양방향 통신을 지원하는 어노테이션
- 웹 소켓 서버의 엔드포인트는 /ws로 정의

### setApplicationDestinationPrefixes 
- 클라이언트가 메시지를 보낼 때 사용하는 목적지의 prefix를 설정
- 주로 @MessageMapping 이 지정된 컨트롤러 메서드와 매핑
- 만약 @Messagemapping("/sendMessage) 일 경우, 클라이언트에서 '/pub/sendMessage'로 메시지 전송


### enableSimpleBroker
- 내장된 SimpleBroker를 활성화시킵니다.
- SimpleBroker는 메시지 브로커의 구현체로, 클라이언트 서버간의 메시지를 중개하는 역할을 담당합니다.
- 클라이언트는 해당 브로커를 통해 구독하고 메시지를 수신할 수 있습니다.

위 코드와 같이 '/sub'를 구독 접두사로 설정한 경우 클라이언트는 '/sub/monitor'와 같은 토픽을 구독하여 해당 토픽으로부터 메시지를 수신할 수 있습니다.

setApplicationDestinationPrefixes를 사용하여 클라이언트의 메시지 목적지를 설정하고 enableSimpleBroker를 사용하여 내장된 SimpleBroker를 활성화하여 클라이언트가 구독하고 메시지를 수신할 수 있는 구독 토픽을 설정합니다.


<br>
<br>

## 결과
### 1. /sub/monitor/1 구독
![](../image/stomp_1.png)

- ws://localhost:8080/ws : 웹소켓 엔드포인트
- Subscription URL : /sub/monitor/1, 구독 URL

<br>

### 2. Pub Message
![](../image/stomp_2.png)
- Destination Queue : /pub/sendMessage
- JSON에 보낼 Message 클래스 값 정의


<br>

### 3. Message

![](../image/stomp_3.png)


메세지가 성공적으로 받아온 것을 확인할 수 있다.

<br>

### 외부 메세지 브로커가 필요한 이유
위와 같이 내장된 메시지 브로커만 사용할 시 scale out 상황에서 서로 다른 서버간의 메시지 전송이 불가능해진다.

이를 해결하기 위해 외부 메시지 브로커를 사용해 서로 다른 서버간에도 메시지 전송이 가능하도록 한다.

<br>
<br>

### 참조
- https://brunch.co.kr/@springboot/695