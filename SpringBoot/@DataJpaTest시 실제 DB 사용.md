# @DataJpaTest 시 실제 DB 사용
@DataJpaTest는 기본적으로 인메모리 데이터베이스인 H2를 기반으로 테스트용 데이터베이스를 구축합니다.

하지만 이때 실제 DB를 사용하게 되면 DataSource 오류가 발생하게 됩니다.

이를 해결하기 위해 Spring Boot 어노테이션을 확인해보겠습니다.

<br>

## Error

@DataJpaTest를 이용해서 단위 테스트를 진행하려고 했지만 사진과 같은 에러가 발생하였습니다.

dataSourceScriptDatabaseInitializer인 dataSource 빈을 생성하는데 에러가 발생하고, Failed to replace DataSource with an embedded database for tests. DataSource를 내장 데이터베이스로 교체하는데에 실패했다고 하고 @AutoConfigureTestDatabase를 확인하라고 알려주고 있습니다.

<br>

## Annotation

### DataJpaTest
``` java
@Target(ElementType.TYPE)
@Retention(RetentionPolicy.RUNTIME)
@Documented
@Inherited
@BootstrapWith(DataJpaTestContextBootstrapper.class)
@ExtendWith(SpringExtension.class)
@OverrideAutoConfiguration(enabled = false)
@TypeExcludeFilters(DataJpaTypeExcludeFilter.class)
@Transactional
@AutoConfigureCache
@AutoConfigureDataJpa
@AutoConfigureTestDatabase
@AutoConfigureTestEntityManager
@ImportAutoConfiguration
public @interface DataJpaTest {
}
```
@DataJpaTest에는 여러 옵션이 있는데 그 중에 @AutoConfigureTestDatabase가 있습니다.

<br>

### @AutoConfigureTestDatabase
``` java
@Target({ ElementType.TYPE, ElementType.METHOD })
@Retention(RetentionPolicy.RUNTIME)
@Documented
@Inherited
@ImportAutoConfiguration
@PropertyMapping("spring.test.database")
public @interface AutoConfigureTestDatabase {
  @PropertyMapping(skip = SkipPropertyMapping.ON_DEFAULT_VALUE)
  Replace replace() default Replace.ANY;

  EmbeddedDatabaseConnection connection() default EmbeddedDatabaseConnection.NONE;

  enum Replace {
    ANY,
	AUTO_CONFIGURED,
	NONE
  }
}
```
해당 Annotation을 보게 되면 replace, connection에 대해서 변경이 가능합니다.

replace()
- replace 설정에 따라서 embeddedDatabase를 할지 안할지 선택하게 됩니다.
- ANY -> 자동 or 수동 상관없이 DataSource bean을 교체
- AUTO_CONFIGURED -> 자동 구성된 경우에만 DataSource bean 교체
- NONE -> DataSource를 교체 하지 않음

connection()
- embeddedDatabase를 연결

또한 여기서 @PropertyMapping("spring.test.database")로 되어있는데


### @PropertyMapping
``` java
@Retention(RUNTIME)
@PropertyMapping("my.example")
public @interface Example { 
    String name();
}

@Example(name="Spring")
public class MyTest {
}
```
@PropertyMapping에 대한 예시, 해당 코드처럼 사용하게 된다면 my.example.name 이라는 property의 값을 사용하게 된다는 의미입니다.
- MyTest에서 my.example.name의 값은 Spring


### TestDatabaseAutoConfigurationPermalink
``` java
@Configuration(proxyBeanMethods = false)
@AutoConfigureBefore(DataSourceAutoConfiguration.class)
public class TestDatabaseAutoConfiguration {
  @Bean
  @ConditionalOnProperty(prefix = "spring.test.database", name = "replace", havingValue = "AUTO_CONFIGURED")
  @ConditionalOnMissingBean
  public DataSource dataSource(Environment environment) {
    return new EmbeddedDataSourceFactory(environment).getEmbeddedDatabase();
  }

  @Bean
  @ConditionalOnProperty(prefix = "spring.test.database", name = "replace", havingValue = "ANY",
		matchIfMissing = true)
  public static EmbeddedDataSourceBeanFactoryPostProcessor embeddedDataSourceBeanFactoryPostProcessor() {
    return new EmbeddedDataSourceBeanFactoryPostProcessor();
  }
}
```
- TestDatabaseAutoConfiguration에 보면 ConditionalOnProperty으로 property의 값이 어떤 값이면 해당 bean이 등록될 수 있게 되어 있다.
- 앞에서 봤던 AutoConfigureTestDatabase에 replace 값에 따라서 어떤 bean이 등록될지 설정되는 것이다.
- 기본값은 spring.test.database.replace: any로 셋팅 되므로 아래쪽 EmbeddedDataSourceBeanFactoryPostProcessor가 Bean으로 등록이 된다.

<br>

### EmbeddedDatabase
``` java
private static class EmbeddedDataSourceFactory {
  private final Environment environment;
  EmbeddedDataSourceFactory(Environment environment) {
    this.environment = environment;
  }

  EmbeddedDatabase getEmbeddedDatabase() {
    EmbeddedDatabaseConnection connection = this.environment.getProperty("spring.test.database.connection",
				EmbeddedDatabaseConnection.class, EmbeddedDatabaseConnection.NONE);
    if (EmbeddedDatabaseConnection.NONE.equals(connection)) {
      connection = EmbeddedDatabaseConnection.get(getClass().getClassLoader());
    }
    Assert.state(connection != EmbeddedDatabaseConnection.NONE,
				"Failed to replace DataSource with an embedded database for tests. If "
						+ "you want an embedded database please put a supported one "
						+ "on the classpath or tune the replace attribute of @AutoConfigureTestDatabase.");
    return new EmbeddedDatabaseBuilder().generateUniqueName(true).setType(connection.getType()).build();
  }
}

public enum EmbeddedDatabaseConnection {
  NONE(null, null, null),
  H2(EmbeddedDatabaseType.H2, "org.h2.Driver", "jdbc:h2:mem:%s;DB_CLOSE_DELAY=-1;DB_CLOSE_ON_EXIT=FALSE"),
  DERBY(EmbeddedDatabaseType.DERBY, "org.apache.derby.jdbc.EmbeddedDriver", "jdbc:derby:memory:%s;create=true"),
  HSQL(EmbeddedDatabaseType.HSQL, "org.hsqldb.jdbcDriver", "jdbc:hsqldb:mem:%s");
}

```
- EmbeddedDataSourceFactory 클래스의 getEmbeddedDatabase()에서 connection이 EmbeddedDatabaseConnection.get(getClass().getClassLoader()); 에서 추가된 라이브러리에 따라서 설정되는 값이 정해진 것을 확인 할 수 있다.

- EmbeddedConnection으로 제공하고 있는 것은 H2, DERBY, HSQL, NONE을 제공한다.


### 해결 방법
``` java
@DataJpaTest
@AutoConfigureTestDatabase(replace = Replace.NONE)
class UnitTestClass {
}
```
- @DataJpaTest를 사용하면 자동으로 EmbeddedDatabase를 사용해버리기 때문에 mysql을 사용할 수 없던 것이였다. 이를 해결하기 위해 @AutoConfigureTestDatabase를 덮어써서 해당 설정이 동작하지 않게 변경한다.

- NONE 설정을 사용하여 TestDataSourceAutoConfiguration에서 DataSource가 bean으로 등록되지 않게되면 DataSourceAutoConfiguration에 의해서 DataSource가 등록되게 된다.
- 그러면 property에 설정한 dataSource의 설정 값을 확인하여 적절한 DataSource를 생성하게 된다. SpringBoot 2.0 이상부터는 HikariDataSource가 Default로 등록이 되게 된다.
- 이런식으로 DataJpaTest를 이용하면서 실제 데이터베이스로 테스트를 해보기 위해서는 AutoConfigureTestDatabase를 이용해서 EmbeddedDatabase 설정이 되지 않게 해주어야 한다.


### 마무리
JPA를 사용한 단위 테스트 중 @DataJpaTest를 사용하게 되면서 실제 DB로 테스트를 진행하다 보니 해당 문제를 경험하게 되었다.

해당 문제를 겪기전에 DB 컬럼 Mapping이 잘못되어 계속 오류가 나고 있어 에러 메시지를 제대로 확인을 못했었는데 확인을 잘해야겠다.

또한 Annotaion에 어떠한 내용이 들어있는지 확인하는 것은 해당 문제에 대한 원인과 해결방안을 알 수 있다는 사실을 알게 되었다.

<br>

해당 내용들은 하단에 있는 링크에 대한 내용들을 대부분 가져오거나 재구성한 내용입니다.


<br>
<br>

## 참조
- https://kangwoojin.github.io/programing/auto-configure-test-database/
- https://docs.spring.io/spring-boot/docs/1.1.0.M1/reference/html/howto-database-initialization.html