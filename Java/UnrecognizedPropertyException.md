# UnrecognizedPropertyException 에러 
해당 에러는 JSON 데이터에는 특정 property가 존재하나, 객체에는 해당 field가 존재하지 않아서 데이터를 mapping 하지 못하여 발생하는 현상

https://www.notion.so/6d0e29fe05fb463e81bc5a4bbd789981?pvs=4#0bfc99c852b24a39823e51c99f7cb3a4

## 해결방안

### 객체 단위에서 해결
- 객체 클래스 위에 @JsonIgnoreProperties를 선언하여 무시

<br>

``` java
@JsonIgnoreProperties(ignoreUnknown = true)
public class dto{
}
```

### mapping시 필드 무시
- ObjectMapper 객체에 UNKNOWN_PROPERTIES를 무시하도록 설정

<br>

``` java
new ObjectMapper()
    .configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false);
```

<br>
<br>

## 참조
- https://github.com/FasterXML/jackson-annotations
