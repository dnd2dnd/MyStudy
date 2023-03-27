# Kafka Monitor

## 환경 설정
```
$ export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-11.0.12.0.7-0.el7_9.x86_64 >> ~/.bashrc
$ export PATH=$JAVA_HOME/bin:$PATH >>~/.bashrc
```

ssh 접속시 bashrc가 저장이 안되는 문제 _ 해결해야함 

<br>

# 순서

## 1. Kafka 압축 해제

```
& tar xvfz kafka_2.13-3.3.1.tgz
```

<br>

## 2. zookeeper.properties 값 변경

zookeeper.properties는 압축해제한 kafka 파일의 config에 존재

```
zookeeper.properties 파일

dataDir=data/zookeeper
clientPort=32181
```
$ bin/zookeeper-server-start.sh config/zookeeper.properties

<br>

## 3. server.properties 값 변경
server.properties는 압축해제한 kafka 파일의 config에 존재

```
server.properties 파일

zookeeper.connect=localhost:32181
log.dirs=data/kafka-logs
listeners=PLAINTEXT://:32182
advertised.listeners=PLAINTEXT://192.168.10.9:32182
```
$ bin/kafka-server-start.sh config/server.properties 
- Test를 원하지 않을 시에 해당 명령어를 실행하지 않고 4번으로 넘어가면 된다.

<br>
<br>

### < Test 방법 > 
```
$ bin/kafka-topics.sh --create --topic test.1 --bootstrapserver 192.168.10.9:32182

$ /home/rnddev/kafka_2.12-2.3.0/bin/kafka-console-consumer.sh --topic test1 --from-beginning --bootstrap-server 192.168.10.9:32182

$ /home/rnddev/kafka_2.12-2.3.0/bin/kafka-console-producer.sh --topic test1 --broker-list 192.168.10.9:32182
```

번외 
```
$ /home/rnddev/kafka_2.12-2.3.0/bin/kafka-console-producer.sh --topic test1 --bootstrap-server 192.168.10.9:32182을 사용하면 bootstrap-server is not a recognized option 오류가 나온다 
오류 이유는 보통 Kafka 버전 호환성 문제라고 한다.
```

<br>
<br>

## 4. jolokia
 https://github.com/rhuss/jolokia/releases 

$ unzip jolokia-1.7.2-bin.zip

```
$ export KAFKA_JMX_OPTS="-javaagent:/home/rnddev/jolokia-1.7.2/agents/jolokia-jvm.jar=port=32183,host=0.0.0.0" >>~/.bashrc

$ bin/kafka-server-start.sh config/server.properties
```
curl http://192.168.10.9:32183/jolokia/version

<br>
<br>

## 5. telegraf 
```
$ wget https://dl.influxdata.com/telegraf/releases/telegraf1.25.0_linux_amd64.tar.gz

$ tar xf telegraf-1.25.0_linux_amd64.tar.gz

```
<br>

압축 해제 후 telegraf-1.25.0에  99_jolkia-kafka.conf 파일 생성

<br>

99_jolki-kafka.conf
```
 [[outputs.file]]
   files = ["stdout"]
   data_format="json"
 [[outputs.nats]]
   servers=["nats://192.168.10.9:32190"]
   subject="test.kafka.monitor"
   data_format="json"

 [[inputs.kafka_consumer]]
   brokers=["192.168.10.9:32182"]
   topics=["test1"]
 # Read Kafka metrics
 [[inputs.jolokia2_agent]]
   name_prefix = "kafka_"
   urls = ["http://192.168.10.9:32183/jolokia"]
```
저장 후
```
$ export TELEGRAF_CONFIG_PATH=/home/rnddev/telegraf-1.25.0/99_jolokia-kafka.conf
$ usr/bin/telegraf
```
<br>
<br>

## 6. nats
https://github.com/nats-io/nats-server/releases/tag/v2.9.10

```
$ unzip nats-server-v2.9.10-linux-amd64.zip
$ ./nats-server --port 32190 --http_port 32191
```
-> http://192.168.10.9:32191











