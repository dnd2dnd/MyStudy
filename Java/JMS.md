# JMS
JMS(Java Message Service)는 어플리케이션간의 통신을 메시지 기반으로 수행하기 위한 Java 표준 API를 정의한 것

JMS 프로바이더는 JSM API를 구현한 메시징 시스템

Ex) Apache ActiveMQ, IBM MQ, RabbitMQ, ActiveMQ Artemis, Oracle WebLogic JMS

JMS 프로바이더는 JMS 클라이언트와 메시징 시스템 간의 중간 계층으로 작동하여 메시지의 전송, 수신 및 관리를 처리


<br>

## 특징
- 느슨한 결합 구조
 
    메시지 송신자와 수신자는 서로에 대해 알 필요가 없습니다.
- 비동기 통신

    메시지 수신자는 요청하지 않아도 서버에 도착하는 대로 메시지를 전달받을 수 있다.
- 신뢰성 있는 메시지 전달

    메시지가반드시 한 번(Once-and-Only-Once) 전달되는 것을 보장합니다.

<br>

## 메시징 모델
JMS는 큐(Queue)와 토픽(TOpic)이라는 두 가지 메시징 모델을 지원합니다

1. 큐
- 일대일(One-to-One) 통신을 위해 사용합니다.
- 송신자와 수신자의 직접적인 연결을 통해 메시지를 안정하게 전송합니다.

2. 토픽
- 일대다(One-to-Many) 통신을 위해 사용합니다.
- 송신자는 메시지를 발행하고 수신자는 구독한 메시지를 받게 됩니다.
- 이를 발행-구독 방식이라고 하며, 한 번에 여러 수신자에게 메시지를 전달할 수 있습니다.

<br>

## JSM 사용
JMS 클라이언트 어플리케이션의 구조
1. ConnectionFactory 연결
2. Connection 생성
3. Session 생성
4. Destination 지정
5. Message Producer 또는 Message Consumer를 만들어 Message Listener 등록
6. Connection 시작
7. 어떤 특정한 작업의 어플리케이션 실행
8. Connection 종료

<br>

### Java 예제 코드

간단한 메시지 전송 및 수신을 보여주기 위한 예제 코드입니다.

``` java
public class JMSExample {

    // JMS 브로커(Broker)의 URL
    private static final String BROKER_URL = "tcp://localhost:{포트번호}";

    // 큐 이름
    private static final String QUEUE_NAME = "example.queue";

    public static void main(String[] args) {
        // JMS 연결 팩토리 생성
        ConnectionFactory connectionFactory = new ActiveMQConnectionFactory(BROKER_URL);

        try {
            // 연결 생성
            Connection connection = connectionFactory.createConnection();
            connection.start();

            // 세션 생성
            Session session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);

            // 큐 생성
            Queue queue = session.createQueue(QUEUE_NAME);

            // 송신자 생성
            MessageProducer producer = session.createProducer(queue);

            // 메시지 생성
            TextMessage message = session.createTextMessage("Hello, JMS!");

            // 메시지 보내기
            producer.send(message);
            System.out.println("메시지를 보냈습니다.");

            // 수신자 생성
            MessageConsumer consumer = session.createConsumer(queue);

            // 메시지 받기
            Message receivedMessage = consumer.receive();
            if (receivedMessage instanceof TextMessage) {
                String text = ((TextMessage) receivedMessage).getText();
                System.out.println("받은 메시지: " + text);
            }

            // 리소스 정리
            session.close();
            connection.close();
        } catch (JMSException e) {
            e.printStackTrace();
        }
    }
}
```