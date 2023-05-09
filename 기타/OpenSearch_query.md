# OpenSearch_Query


### 스크롤 조회

```
GET index/_search?scroll=1m
{
    "size": 1000,
    "sort" : { "collectDate" : "desc" }
}
```

<br>

### 스크롤 아이디 조회

```
POST /_search/scroll 
{
    "scroll" : "1m", 
    "scroll_id" : "FGluY2x1ZGVfY29udGV4dF91dWlkDXF1ZXJ5QW5kRmV0Y2gBFjR3M3BjZUotU2lDOWI0eE5hRDd5VEEAAAAAAAbBTBZ6ako2TUlKV1R3Q2hsaFBPUk1yam9B" 
}
```

<br>

### <b>Match 조회</b>

```
GET index/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "field": "value"
          }          
        },
        {
          "match: {
            "field": "value"
          }
        }       
      ]
    } 
  }
}
```
<br>

### <b>Like 조회</b>
```
GET index/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "wildcard": {
            "{필드명}.keyword": "{필드값}"
          }          
        },
        {
          "wildcard: {
            "{필드명}.keyword": "{필드값}"
          }
        }       
      ]
    } 
  }
}
```
<br>

### <b>범위 조회</b>
```
GET index/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "range": {
            "{필드명}": {
              "gte":"{필드값}",
              "lte":"{필드값}"
            }
          }          
        }
      ]
    }
  }
}
```
- gt 초과, gte 이상, lt 미만, lte 이하

<br>

### <b>집계 조회</b>
```
GET index/_search
{
  "size":0,
  "aggs": {
    "{집계명}": {
      "{집계함수: terms, sum, max, min, avg}": {
        "field": "{필드명}",
        "size": 1000
      }
    }
  }
}
```
- 집계된 조회만 필요하기때문에 size:0 을 사용한다.
- OpenSearch는 size값이 없으면 10개만 조회되기된다. 집계된 필드 수가 10개 이상일 수 있으므로 aggs안에 size값을 부여한다.

<br>

### <b>시간별 조회</b>
```
GET index/_search
{
  "aggs": {
    "count": {
      "date_histogram": {
        "field": "{필드명}",
        "interval": "{시간 간격 : second, minute, hour, day, month}"
      },
      "aggs": {
        "{집계명}": {
          "{집계함수: terms, sum, max, min, avg}": {
            "field": "{필드명}",
            "size": 1000
          }
        }
      }
    }
  }
}
```
<br>

### <b>집계 조건 조회</b>
```
GET index/_search
{
  "size":0,
  "aggs": {
    "{집계명}": {
      "{집계함수: terms, sum, max, min, avg}": {
        "field": "{필드명}",
        "size": 1000
      }
    }
  }, 
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "{필드명}": "{필드값}"
          }    
        },
        {
          "wildcard": {
            "{필드명}.keyword": "{필드값}"
          } 
        } 
      ] 
    } 
  } 
}
```

<br>

### <b>Nest 조회</b>
```
GET index/_search
{
  "query": {
    "nested": {
      "path": "{path명}",
        "query": {
          "wildcard": {
            "{필드명}": "{필드값}"
          }
        },
      "inner_hits": {
      }
    }
  },"_source": "inner_hits"
}
```
<br>

### <b>Nest 집계 </b>
```
GET index/_search
{
  "size":0,
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "{필드명}": "{필드값}"
          }    
        },
        {
          "wildcard": {
            "{필드명}.keyword": "{필드값}"
          }    
        }  
      ]
    }
  },
  "aggs": {
    "{집계명}": {
      "nested": {
        "path": "{path명}"
      },
      "aggs": {
        "{집계명}": {
          "{집계함수: terms, sum, max, min, avg}": {
            "field": "{필드명}",
            "size": 1000
          }
        }
      }
    }
  }
}
```