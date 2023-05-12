# 다중 DB 연결
Spring Boot를 사용하던 도중 2개 이상의 Database를 사용해야하는 상황

<br>

## DB 1개 일 때
application.properties 
```
spring.datasource.url=jdbc:mysql://IP:PORT/DBNAME
spring.datasource.username=ID
spring.datasource.password=PASS
spring.datasource.driver-class-name=com.mysql.jdbc.Driver
```

연결해야할 DB가 1개 일 경우에는 application.properties에 하나의 Connection 정보만 작성하면 된다.

<br>

## DB 2개 일 때
application.properties 
```
spring.post-datasource.jdbc-url=jdbc:mysql://IP:PORT/DBNAME
spring.post-datasource.username=ID
spring.post-datasource.password=PASS
spring.post-datasource.driver-class-name=com.mysql.jdbc.Driver

spring.mysql-datasource.jdbc-url=jdbc:mysql://IP:PORT/DBNAME
spring.mysql-datasource.username=ID
spring.mysql-datasource.password=PASS
spring.mysql-datasource.driver-class-name=com.mysql.jdbc.Driver
```

spring.().{jdbc-url, username, password, driver-class-name}

- ()에는 jdbc를 구분할 수 있는 것을 작성하고 대문자, 특수문자, '-', '_'는 사용 할 수 없다
- 기존에 사용한 url -> jdbc-url로 수정한다.

<br>

### Config 추가
각 Datasource 별 config를 추가한다.

<br>

### PostDatasourceConfig
``` java
@Configuration
@PropertySource({"classpath:application.properties"})  // 해당 Configuration 클래스가 읽을 properties 명시
@EnableJpaRepositories(
        basePackages = "해당 DataSource를 사용할 패키지 경로",
        entityManagerFactoryRef = "postEntityManager", // entity manager bean 이름
        transactionManagerRef = "postTranscationManager" // transaction manager bean 이름
)
public class PostDatasourceConfig {

    @Autowired
    private Environment environment;

    // @Primary : 우선적으로 적용될 Bean임을 명시 
    @Primary
    @Bean
    public LocalContainerEntityManagerFactoryBean postEntityManager() {
        final LocalContainerEntityManagerFactoryBean em = new LocalContainerEntityManagerFactoryBean();
        em.setDataSource(postDataSource());
        // EntityManager가 사용할 엔티티 패키지 경로
        em.setPackagesToScan("적용될 instance 패키지 경로");

        final HibernateJpaVendorAdapter vendorAdapter = new HibernateJpaVendorAdapter();
        em.setJpaVendorAdapter(vendorAdapter);
        final HashMap<String, Object> properties = new HashMap<String, Object>();
        // hibernate에 지정할 속성값
        properties.put("hibernate.show_sql",environment.getProperty("properties 설정한 Key값"));
        properties.put("hibernate.dialect",environment.getProperty("properties 설정한 Key값"));
        em.setJpaPropertyMap(properties);
        return em;
    }

    @Primary
    @Bean
    @ConfigurationProperties(prefix="post-datasource")
    public DataSource postDataSource() {
        return DataSourceBuilder.create().build();
    }

    @Primary
    @Bean
    public PlatformTransactionManager postTranscationManager() {
        final JpaTransactionManager transactionManager = new JpaTransactionManager();
        transactionManager.setEntityManagerFactory(postEntityManager().getObject());
        return transactionManager;
    }
}
```

<br>

### MysqlDatasourceConfig
``` java
@Configuration
@PropertySource({"classpath:application.properties"})  // 해당 Configuration 클래스가 읽을 properties 명시
@EnableJpaRepositories(
        basePackages = "해당 DataSource를 사용할 패키지 경로",
        entityManagerFactoryRef = "mysqlEntityManager", // entity manager bean 이름
        transactionManagerRef = "mysqlTranscationManager" // transaction manager bean 이름
)
public class MysqlDatasourceConfig {

    @Autowired
    private Environment environment;

    // @Primary : 우선적으로 적용될 Bean임을 명시 
    @Primary
    @Bean
    public LocalContainerEntityManagerFactoryBean mysqlEntityManager() {
        final LocalContainerEntityManagerFactoryBean em = new LocalContainerEntityManagerFactoryBean();
        em.setDataSource(mysqlDataSource());
        // EntityManager가 사용할 엔티티 패키지 경로
        em.setPackagesToScan("적용될 instance 패키지 경로");

        final HibernateJpaVendorAdapter vendorAdapter = new HibernateJpaVendorAdapter();
        em.setJpaVendorAdapter(vendorAdapter);
        final HashMap<String, Object> properties = new HashMap<String, Object>();
        // hibernate에 지정할 속성값
        properties.put("hibernate.show_sql",environment.getProperty("properties 설정한 Key값"));
        properties.put("hibernate.dialect",environment.getProperty("properties 설정한 Key값"));
        em.setJpaPropertyMap(properties);
        return em;
    }

    @Primary
    @Bean
    @ConfigurationProperties(prefix="mysql-datasource")
    public DataSource mysqlDataSource() {
        return DataSourceBuilder.create().build();
    }

    @Primary
    @Bean
    public PlatformTransactionManager mysqlTranscationManager() {
        final JpaTransactionManager transactionManager = new JpaTransactionManager();
        transactionManager.setEntityManagerFactory(mysqlEntityManager().getObject());
        return transactionManager;
    }
}
```

<br>

## 설명
### @EnableJpaRepositories
- JPA Repository Bean을 활성화하는 어노테이션
- basePackages 속성을 주지 않으면 @SpringBootApplication에 설정한 Bean scan 범위로 지정
- entityManagerFactoryRef, transactionManagerRef 명시

### @Primary
- 하나의 타입에 빈 객체가 여러 개인 경우 그 중 우선순위를 갖는 Bean이라는 것을 지정하는 것

### LocalContainerEntityManagerFactoryBean
- SessionFactoryBean과 동일하게 DataSource와 Hibernate Property, Entity가 위치한 package를 지정
- Hibernate 기반으로 동작을 지정하는 JpaVendor를 설정
- Hibernate vendor과 JPA간의 Adapter 설정

### PlatformTransactionManager
- @Transactional이 포함된 메소드가 호출될 경우, PlatformTransactionManager를 사용하고 트랜잭션을 시작, 정상 여부에 따라 Commit 또는 Rollback 한다