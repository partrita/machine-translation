import sys

content = r"""<!-- ====== Section from: 24-data.qmd ====== -->


# 데이터 (Data) {#sec-data}

실증 마케팅 연구의 신뢰성은 그 이면에 있는 데이터의 신뢰성에 전적으로 달려 있으며, 연구자가 획득할 수 있는 데이터는 어떤 연구 질문을 던질 수 있는지를 점차 규정하고 있다. 이 장은 마케팅 과학의 원재료—기업 재무 데이터, 광고 및 인게이지먼트 지표, 가계 지출, 소비자의 관심에 대한 디지털 흔적—를 **획득(acquiring)**하고, 그에 못지않게 각 데이터 출처가 실제로 무엇을 측정하는지 이해하기 위한 실무 지침서이다. 데이터 획득은 결코 중립적이지 않다. 모든 데이터셋에는 표본추출 틀(sampling frame), 측정 모형, 그리고 일련의 선택 메커니즘이 내재되어 있으며, 이들은 모든 후속 추정치로 전파된다. 6,000가구를 분기별로 조사하는 패널, 검색량을 자체 최댓값으로 재조정한 지수, 1,400회 호출 후 조용히 요청을 제한하는 API는 각각 분석가가 학습할 수 있는 정보에 구조적 제약을 가한다.

본 장은 출처별로 내용을 구성하되, 전체를 관통하는 핵심 축은 **측정(measurement)**이다. 각 출처에 대해 출처가 허용하는 한 가장 정밀하게 **추정 대상 모수(estimand)**—관심 대상인 모집단 수치—와 해당 출처가 실제로 제공하는 **관측치(observable)**를 명시한다. 대부분의 실증적 오류는 이 둘 사이의 간극에서 발생하기 때문이다. 검색 관심도는 검색량이 아니며, 상대 지수는 절대적 빈도가 아니고, 이름 기반의 인구통계학적 예측은 사실(fact)이 아니라 사후 확률(posterior probability)이다. 이러한 구분을 대수롭지 않게 취급할 때, 그럴듯해 보이는 분석 파이프라인이 편향된 계수를 산출하게 된다.

또한 이 장은 의도적으로 재현 가능하도록 구성되었다. 연결 레시피, 쿼리 패턴, 재조정 알고리즘을 실행 가능한 코드로 제시하여, 독자가 문서화되지 않은 API를 역공학할 필요 없이 "이 데이터셋이 존재한다"에서 "분석 가능한 정돈된(tidy) 데이터프레임을 확보했다"로 바로 나아갈 수 있도록 하였다. 속도 제한, OAuth 범위, 스키마 등 타사 플랫폼의 자체 문서가 권위 있는 참조 자료인 경우에는 일시적인 세부 정보를 복제하기보다 그 메커니즘을 짚어준다. 전체적으로 직관을 먼저 제시하고, 공식적인 대상을 다룬 후, 실행 가능한 코드를 제공하는 구성을 유지한다.

[@fig-data-landscape]는 연구 설계에서 가장 중요한 두 가지 차원, 즉 관측 단위(기업, 가계, 또는 개별 소비자)와 데이터가 **행동적(behavioral)**(행동으로 드러남)인지 아니면 **설문 도출(survey-elicited)**(응답자가 보고함)인지에 따라 본 장에서 다루는 출처들을 배치한다.

```{mermaid}
%%| label: fig-data-landscape
%%| fig-cap: "관측 단위 및 명시된 행동 포착 여부에 따라 정리된 본 장의 데이터 출처. 행동 흔적은 풍부하고 시의적절하지만 잠재 구성개념에 대한 노이즈가 섞인 대리 변수임. 설문 도구는 구성개념을 직접 측정하지만 비용이 많이 들고 시차가 발생하며 보고 편향이 존재함."
flowchart TB
  subgraph FIRM["기업 수준"]
    WRDS["WRDS / Compustat<br/>재무, R&D, 광고비"]
  end
  subgraph HH["가계 수준"]
    CE["소비자 지출 조사 (CE)<br/>도출된 지출 (패널 + 가계부)"]
  end
  subgraph IND["개인 / 키워드 수준"]
    GT["구글 트렌드<br/>상대적 검색 관심도"]
    BD["바이두 지수<br/>검색량"]
    YT["유튜브<br/>조회수, 댓글, 인게이지먼트"]
    NAME["이름 기반 추론<br/>성별 / 연령 / 국적"]
  end
  WRDS -->|"드러난 행동 (회계)"| OUT["연구 설계:<br/>추정 모수 vs. 관측치"]
  CE -->|"도출된 응답 (설문)"| OUT
  GT -->|"드러난 행동 (행태)"| OUT
  BD -->|"드러난 행동 (행태)"| OUT
  YT -->|"드러난 행동 (행태)"| OUT
  NAME -->|"추론됨 (모형)"| OUT
```

## 기업 재무 데이터: WRDS {#sec-data-wrds}

대부분의 마케팅-재무 연구([@sec-marketing-finance])와 전략 연구의 상당 부분은 표준화된 기업 재무 데이터에 의존한다. 와튼 연구 데이터 서비스(WRDS)는 이러한 데이터에 접근하는 지배적인 학술 게이트웨이이다. WRDS는 단일 SQL 인터페이스 이면에 Compustat(회계 펀더멘털), CRSP(주가 및 수익률), I/B/E/S(애널리스트 예측치) 및 수십 개의 다른 라이브러리를 통합하고 있다. 마케팅 연구자에게 매력적인 점은 구체적이다. Compustat의 연차 펀더멘털 파일(`funda`)에 있는 광고비(`xad`)와 연구개발비(`xrd`)는 기업의 마케팅 및 혁신 집약도를 나타내는 대표적인 대리 변수이며, [@sec-marketing-finance] 전반에서 사용되는 토빈의 $q$나 비정상 수익률과 같은 시장 기반 성과와 깔끔하게 결합된다.

연결은 표준 PostgreSQL 세션으로 이루어진다. WRDS는 네트워크를 통해 데이터웨어를 노출하므로 일반적인 관계형 데이터베이스에 사용되는 `DBI` 관용구를 동일하게 적용할 수 있다. 인증 정보는 소스 코드에 하드코딩하지 않고 환경 변수에서 읽어와 공유 시 안전을 유지해야 한다.

```{r wrds-connect, message=FALSE, eval=FALSE}
library(RPostgres)
library(tidyverse)

wrds <- dbConnect(
  Postgres(),
  host    = "wrds-pgdata.wharton.upenn.edu",
  port    = 9737,
  dbname  = "wrds",
  sslmode = "require",
  user    = Sys.getenv("wrds_user"),
  pass    = Sys.getenv("wrds_pass")
)
```

데이터웨어하우스는 `information_schema`를 통해 자체 구조를 기술하므로, 테이블 이름을 추측하기보다 이를 통해 가용한 정보를 탐색하는 것이 체계적인 접근법이다. 세 개의 중첩 쿼리는 신규 사용자가 갖는 세 가지 질문(어떤 **라이브러리(스키마)**가 존재하는가, 선택한 라이브러리에 어떤 **테이블**이 있는가, 선택한 테이블이 어떤 **열(컬럼)**을 갖는가)에 답해준다.

```{r wrds-explore, eval=FALSE}
# 구독 계정에서 사용 가능한 라이브러리 (스키마) 목록
dbGetQuery(wrds, "
  select distinct table_schema
  from information_schema.tables
  order by table_schema")

# 특정 라이브러리 내 테이블 목록
dbGetQuery(wrds, "
  select distinct table_name
  from information_schema.columns
  where table_schema = 'comp_na_daily_all'
  order by table_name")

# 특정 테이블 내 컬럼 목록
dbGetQuery(wrds, "
  select column_name
  from information_schema.columns
  where table_schema = 'comp_na_daily_all'
    and table_name   = 'funda'
  order by column_name")
```

대표적인 추출 예제로 10년간의 광고비와 R&D 지출을 가져온 후, 기업 식별자인 `gvkey`로 결합하여 각 기업-연도 데이터를 산업 분류 정보로 보강한다. R에서 필터링하는 대신 `WHERE` 절에 필터(`fyear`, non-null `xad`/`xrd`)를 밀어 넣으면 전송 데이터 크기를 최소화할 수 있다. 이는 `funda` 데이터가 수백만 행에 달할 때 매우 중요하다.

```{r wrds-extract, eval=FALSE}
fin <- dbGetQuery(wrds, "
  select gvkey, fyear, xad, xrd
  from comp_na_daily_all.funda
  where fyear between 2000 and 2010
    and xad is not null
    and xrd is not null") |>
  distinct()

industry <- dbGetQuery(wrds, "
  select gvkey, gind, gsubind, naics, sic
  from comp_na_daily_all.names")

panel <- fin |>
  left_join(industry, by = "gvkey")

head(panel)
```

실무에서 자주 나타나며 후속 식별에 영향을 미치는 두 가지 주의사항이 있다. 첫째, `xad`는 **공시된(reported)** 광고비이다. 회계 기준상 많은 기업이 마케팅 비용을 별도로 구분하지 않고 비용 처리하므로 결측은 무작위가 아니다. 즉, 기업 규모, 산업, 공시 체제와 상관되어 있다. `is null`을 "별도로 공시되지 않음"이 아니라 "광고비 없음(0원)"으로 취급하면 결과 변수와 상관된 변수를 기준으로 표본을 선택하게 되어 교과서적인 선택 편향(selection bias)이 발생한다. 둘째, `funda`는 `indfmt`, `datafmt`, `popsrc`, `consol` 플래그로 구분되는 여러 **포맷**(연결 vs. 개별, 표준 vs. 수정)으로 제공된다. 북미 제조/서비스 기업의 표준 스크리닝 조건은 `indfmt='INDL' and datafmt='STD' and popsrc='D' and consol='C'`이며, 이를 생략하면 동일 기업-연도가 중복 집계된다. 두 주의사항 모두 사소해 보이지만 추정치가 왜곡될 때까지 눈에 띄지 않는 함정이다.

::: {.callout-note}

WRDS 외에도 아래에서 다루는 **소비자 지출 조사(CE)** 및 상용 스캐너 패널(예: IRI, Nielsen)은 기업 재무 데이터가 다룰 수 없는 수요 측면의 행동을 포괄한다. 관측 단위를 추정 모수와 일치시켜야 한다는 일반 원칙은 [@sec-measurement-scales]에서 전개된다.

:::

## 로컬 문서 저장소: MongoDB {#sec-data-mongo}

모든 마케팅 데이터가 관계형 데이터인 것은 아니다. 소셜 미디어 게시물, 스크래핑된 리뷰, API 응답은 중첩되고 유연한 JSON 형식으로 수신되며, MongoDB와 같은 문서 데이터베이스는 사전에 사각형 테이블 스키마를 강제하지 않고 이를 저장한다. 대규모 수집 시 첫 번째 실무 질문은 데이터가 **물리적으로 어디에 저장되는가**이며, 실행 중인 서버는 `mongo` 셸에서 실행하는 관리 명령을 통해 이를 보고한다.

```
db.adminCommand("getCmdLineOpts")
```

반환된 문서에는 데이터 파일의 디스크 내 위치인 `storage.dbPath`가 포함되어 있어 용량 계획, 백업, 대규모 수집이 예상 위치에 정상적으로 기록되는지 확인하는 데 유용하다. 보다 넓은 관점에서의 구조적 요점은 다음과 같다. 문서 저장소는 쓰기 시의 유연성을 위해 WRDS 스타일 출처의 관계형 보증(고정 스키마, 참조 무결성, 선언적 조인)을 양보한다. 이러한 절충은 이질적이고 계속 진화하는 웹 데이터에는 적합하지만 대부분의 계량경제학 추정량이 요구하는 정돈된 패널 데이터에는 부적합하다. 따라서 일반적인 파이프라인은 원시 데이터를 MongoDB에 **적재(land)**한 후, 모델링 전에 분석 가능한 평탄화된 데이터프레임으로 **투영(project)**하여 R이나 관계형 저장소로 가져오는 방식을 취한다.

## 검색 관심도: Google 트렌드 {#sec-data-gtrends}

집계된 검색 행동은 시의적절하고 세분화되어 있으며 관심의 선행 지표 역할을 하므로 마케팅에서 가장 유용한 행동 신호 중 하나이다. 대중의 관심과 그 제도적 반영은 함께 움직이지만 서로 다른 시차를 갖는다. 온라인 검색량과 뉴스 보도는 강한 상관관계를 보이는 반면, 학술 출판은 동료 평가와 출판에 내재된 지연으로 인해 대중의 관심보다 뒤처진다 [@nghiem2016]. 구조적으로 볼 때 뉴스 미디어는 연구 커뮤니티와 대중 사이의 전달자 역할을 하며, 온라인 검색은 이러한 교환에서 대중 측면을 보여주는 가장 즉각적인 기압계이다.

### Google 트렌드가 측정하는 대상

Google 트렌드는 검색량을 보고하지 **않는다**. Google 트렌드가 보고하는 것은 **상대적 검색 관심도 지수(relative search interest index)**이며, 이 구분을 이해하는 것이 이 데이터 출처에서 가장 중요하다. 키워드 $k$, 지역 $g$, 선택된 시간 창에 대해, 기간 $t$의 기저 검색 쿼리 볼륨을 $v_{k,t}$라 하자(이 자체도 표본 추출 및 개인정보 보호 필터링을 거친 수치임). 트렌드는 다음과 같이 재조정된 시계열을 반환한다.

$$
I_{k,t} \;=\; 100 \times \frac{v_{k,t}}{\displaystyle\max_{s \in W} v_{k,s}},
$$ {#eq-gtrends-index}

여기서 $W$는 요청된 기간 창이다. [@eq-gtrends-index]로부터 세 가지 결과가 도출되며, 이를 간과하면 오류에 빠지게 된다.

첫째, 지수는 **기간 창에 의존적(window-dependent)**이다. 분모는 **요청된 기간 창 내에서의 최댓값**이므로, 동일한 키워드를 서로 다른 두 기간 창으로 쿼리하면 겹치는 날짜에 대해서도 일반적으로 서로 다른 지수 값이 반환된다. 시계열이 고정된 척도에 고정되어 있지 않은 것이다. 둘째, 지수는 **단일 요청 내의 키워드 간에 공동 정규화(co-normalized)**된다. 여러 키워드를 함께 제출하면 단일 분모(모든 키워드에 걸친 전체 최댓값)를 공유하므로, 단일 요청 **내에서는** 키워드 간 비교가 유효하지만 서로 다른 별도 요청 **간에는** 비교가 유효하지 않다. 셋째, 데이터는 **표본 추출(sampled)**되므로 동일한 쿼리를 반복해도 약간씩 다른 지수가 반환된다. 안정적인 추정치를 얻으려면 여러 번 추출하여 평균을 낸다.

기간 창은 Google이 반환하는 **시간 단위(granularity)**도 결정하며, 이는 요청된 기간의 길이에 따라 고정된다.

| 데이터 단위 | 기간 창 길이 |
|---|---|
| 시간별 (Hourly) | 최근 7일 |
| 일별 (Daily) | 9개월 미만 |
| 주별 (Weekly) | 9개월 ~ 5년 |
| 월별 (Monthly) | 5년 초과 |

: 요청된 기간 창 길이에 따라 Google 트렌드가 반환하는 기본 시간 세분성. 긴 기간 창은 자동으로 거칠어지므로, 긴 일별 시계열을 복원하려면 [@sec-data-gtrends-daily]의 연결 절차가 필요함. {#tbl-gtrends-granularity}

다년도 기간 창에 걸쳐 두 브랜드의 주별 상대적 관심도를 추출해 보자. `gtrendsR` 패키지는 공개 엔드포인트를 래핑하며, `interest_over_time`에 지수 시계열이 담긴다.

```{r gtrends-basic, eval=FALSE}
library(gtrendsR)
library(tidyverse)

trends <- gtrends(
  keyword = c("7eleven", "3m"),
  geo     = "US",
  time    = "2010-01-01 2012-01-30",  # 지원되는 가장 이른 시작일은 2004년임
  gprop   = "web"                       # web | news | images | froogle | youtube
)

time_trend <- trends$interest_over_time   # 이 기간 창에 대한 주별 지수
```

[@eq-gtrends-index]가 상대적 표본 시계열을 생성하므로 원시 데이터를 그대로 플롯하면 신호와 계절 노이즈가 함께 나타난다. 평활기(smoother)를 적용하면 모수적 계절 모형을 가정하지 않고도 연중 계절성에서 추세 성분을 분리할 수 있다.

```{r gtrends-plot, eval=FALSE}
library(ggplot2)

ggplot(time_trend, aes(x = date, y = hits, group = keyword, colour = keyword)) +
  geom_line(alpha = 0.4) +
  geom_smooth(span = 0.5, se = FALSE) +
  labs(x = "시간", y = "상대적 관심도 (주별)",
       title = "Google 검색 관심도", colour = NULL) +
  theme_bw() +
  theme(legend.position = "bottom")
```

### 장기 일별 시계열 복원 {#sec-data-gtrends-daily}

[@tbl-gtrends-granularity]의 세분성 규칙은 실질적인 문제를 일으킨다. 연구자는 다년도 기간에 걸친 **일별** 데이터를 필요로 하지만 다년도 쿼리는 주별(또는 월별) 데이터만 반환하기 때문이다. 해결책은 [@eq-gtrends-index]의 공동 정규화 특성을 활용하는 것이다. 두 가지 복원 전략이 존재하며 고빈도 시계열과 저빈도 시계열을 조정하는 방식에서 차이가 있다.

**스케일링(중첩) 방법(Scaling / overlapping method)**이 둘 중 더 신뢰할 수 있다. 일별 단위로 짧은 기간 창을 쿼리하고 전체 기간을 저빈도로 쿼리하여 기간 가중치를 얻은 다음, 각 월의 일별 지수에 해당 월의 상대 가중치를 곱하여 일별 조각들을 재조정한다. 공식적으로 $d_{k,t}$를 월 $m(t)$를 포괄하는 짧은 기간 창 쿼리에서 얻은 일별 지수라 하고, $w_{k,m}$을 장기 쿼리에서 도출된 $m$월 가중치(해당 월의 집계 지수를 월별 집계 최댓값으로 나눈 값)라 하자. 복원된 일별 시계열은 다음과 같은 곱으로 표현된다.

$$
\hat{v}_{k,t} \;=\; d_{k,t} \times w_{k,m(t)},
$$ {#eq-gtrends-scaling}

이는 월 내의 일별 형태를 유지하면서 월 간 공통 척도를 복원한다. 반면 **단순 연결(정규화) 방법(Concatenation / normalization method)**은 1개월 단위 일별 쿼리를 끝과 끝으로 이어 붙인 후 주별 시계열에 맞춰 정규화한다. 실증 비교 결과 스케일링 방법이 우수하므로 [@eq-gtrends-scaling]이 권장되는 추정량이다.[^gtrends-attrib] 이 복원 방식은 긴 시계열의 일별 검색 데이터를 필요로 하는 학술 논문의 기초가 되며 [@risteski2014], 일별 검색량 추출을 위한 관련 접근법들이 문헌에 문서화되어 있다 [@liugoogle2019].

[^gtrends-attrib]: 중첩-스케일링 절차는 Alex Dyachenko가 대중화한 접근법을 따르며, 단순 연결 변형은 `pytrends` 라이브러리의 `dailydata` 루틴을 반영한다. 둘 다 아래 함수에 구현되어 있다.

아래 함수는 [@eq-gtrends-scaling]을 엔드투엔드로 구현한다. 단일 집계 쿼리를 실행하여 월별 승수 `mult`를 도출하고, 월별로 루프를 돌며 일별 데이터를 가져온 후 둘을 결합하여 복원된 일별 추정치 `est_hits`를 생성한다. 약 **4시간당 1,400회 요청**이라는 속도 제한 예산에 유의해야 한다. 장기 복원 시 이를 준수하지 않으면 루프가 빈 프레임을 반환하기 시작한다.

```{r gtrends-daily, eval=FALSE}
library(gtrendsR)
library(tidyverse)
library(lubridate)

get_daily_gtrend <- function(keyword = c("7eleven", "3M"),
                             geo  = "US",
                             from = "2013-01-01",
                             to   = "2013-02-15") {
  # 현재 진행 중인 (미완료) 월의 종료일은 허용하지 않음
  if (ymd(to) >= floor_date(Sys.Date(), "month")) {
    to <- floor_date(ymd(to), "month") - days(1)
    if (to < from) stop("현재 월의 종료일은 허용되지 않습니다.")
  }

  # 장기 쿼리 -> 월별 승수 w_{k,m}
  aggregated <- gtrends(keyword = keyword, geo = geo, time = paste(from, to))
  if (is.null(aggregated$interest_over_time)) {
    message("해당 쿼리에 대한 Google 트렌드 데이터가 없습니다.")
    return(invisible(NULL))
  }

  mult_m <- aggregated$interest_over_time |>
    mutate(hits = as.integer(ifelse(hits == "<1", "0", hits))) |>
    group_by(month = floor_date(date, "month"), keyword) |>
    summarise(hits = sum(hits), .groups = "drop") |>
    mutate(ym = format(month, "%Y-%m"), mult = hits / max(hits)) |>
    select(month, ym, keyword, mult)

  # 월별 일별 쿼리 -> d_{k,t}
  windows <- tibble(
    s = seq(ymd(from), ymd(to), by = "month"),
    e = seq(ymd(from), ymd(to), by = "month") + months(1) - days(1)
  )

  raw_daily <- map2_dfr(windows$s, windows$e, function(s, e) {
    curr <- gtrends(keyword, geo = geo, time = paste(s, e))
    if (is.null(curr$interest_over_time)) return(tibble())
    curr$interest_over_time
  })

  trend_d <- raw_daily |>
    transmute(date, keyword,
              ym   = format(date, "%Y-%m"),
              hits = as.integer(ifelse(hits == "<1", "0", hits)))

  # 복원: est_hits = d_{k,t} * w_{k,m(t)}   (eq-gtrends-scaling)
  trend_d |>
    left_join(mult_m, by = c("ym", "keyword")) |>
    mutate(est_hits = hits * mult, date = as.Date(date)) |>
    select(date, keyword, est_hits)
}

daily_trend <- get_daily_gtrend(
  keyword = c("7eleven", "3M"), geo = "US",
  from = "2013-01-01", to = "2013-02-01")
head(daily_trend)
```

### 절대 검색량

연구 응용이 [@eq-gtrends-index]의 상대 지수가 아니라 **절대적** 검색 건수를 진정으로 필요로 하는 경우(예: 관심 추적보다 시장 규모 산정이 목적인 경우), 상대적 관심도 엔드포인트는 잘못된 출처이다. Google은 BigQuery를 통해 절대 검색 수치를 노출하는 별도의 인기 검색어 데이터셋을 게시하며, 수준(level) 추정에는 트렌드 지수가 아닌 해당 웨어하우스가 적절한 입력 데이터이다.

## 중국 내 검색량: 바이두 지수 (Baidu Index) {#sec-data-baidu}

Google이 서비스되지 않는 시장에서는 지배적인 현지 검색 엔진에서 유사한 행동 신호를 얻을 수 있다. 중국의 경우 바이두이며, **바이두 지수(Baidu Index)**가 다른 지역의 Google 트렌드 역할을 수행한다. 바이두는 대량 추출을 위한 공개 API를 제공하지 않으므로, 연구자들은 검색량 시계열을 수집하기 위해 크롤러를 구축해 왔다. @liu2019 는 이를 위한 자바 기반 스파이더를 문서화하였다. 지수는 잠재적 관심에 대한 재조정되고 표본 추출된 대리 변수이지 절대 빈도가 아니라는 동일한 측정상의 주의사항이 적용되므로, [@sec-data-gtrends]의 추정 모수 대 관측치 원칙이 그대로 적용된다.

## 동영상 인게이지먼트: YouTube {#sec-data-youtube}

동영상은 현재 주요 광고 및 인게이지먼트 채널이며, YouTube는 동영상, 재생목록, 채널 수준에서 조회수, 좋아요, 댓글, 시청 지표 등 풍부한 행동 데이터를 제공한다. 두 가지 접근 경로가 존재하며 둘 중의 선택은 편의성이 아닌 데이터 거버넌스의 결정이다.

첫 번째 경로는 단순한 API 키를 사용하여 모든 동영상이나 채널의 **공개적으로 표시되는** 통계를 제공하는 **공개 Data API**이다. 두 번째는 **소유자 비공개** 지표(노출수, 시청자 유지율, 수익)를 제공하는 **Analytics 및 Reporting API**이며, 요청된 데이터를 소유한 채널 또는 콘텐츠 소유자의 OAuth 인증을 필요로 한다. [@tbl-youtube-apis]는 둘을 대비한다. 작동 원칙은 일반 시청자가 볼 수 없는 모든 데이터는 소유자의 위임된 동의를 필요로 한다는 점이다.

| 차원 | Data API (API 키) | Analytics / Reporting (OAuth) |
|---|---|---|
| 인증 방식 | API 키 | OAuth 2.0 (소유자 위임) |
| 데이터 범위 | 공개 통계 | 소유자 비공개 지표 |
| 대표 필드 | 조회수, 좋아요, 댓글 | 노출수, 시청자 유지율, 수익 |
| 호출 권한 | 키를 가진 누구나 | 해당 채널/콘텐츠 소유자 |
| 활용 사례 | 경쟁사/시장 분석 스캔 | 1자(first-party) 성과 분석 |

: YouTube 데이터에 대한 두 가지 접근 경로. 경계는 동의(consent)임. 공개 통계는 API 키만 필요하지만 소유자 비공개 분석은 데이터 소유자의 OAuth 인증을 요구함. {#tbl-youtube-apis}

### `tuber`를 통한 OAuth 경로

`tuber` 패키지는 인증된 엔드포인트를 래핑한다. 인증은 Google Cloud 콘솔에서 발급받은 자격 증명을 사용하여 일회성 OAuth 핸드셰이크로 수행되며, 이후 세션 토큰을 통해 동영상 통계, 상세 정보, 자막, 검색, 댓글 스레드 호출을 승인한다.

```{r youtube-oauth, eval=FALSE}
library(tuber)

# Google Cloud 콘솔에서 app_id / app_secret을 설정한 후:
yt_oauth(app_id = "YOUR_APP_ID", app_secret = "YOUR_APP_SECRET")

get_stats(video_id = "N708P-A45D0")          # 공개 통계
get_video_details(video_id = "N708P-A45D0")  # 스니펫 메타데이터
get_captions(video_id = "yJXTXN4xrI8")       # 자막 트랙
yt_search(term = "test")                      # 코퍼스 검색
get_comment_threads(c(video_id = "N708P-A45D0"))  # 최상위 댓글
get_all_comments(video_id = "a-UQz7fqR3w")    # 댓글 + 대댓글
```

흔한 연구 과업은 특정 채널의 **모든** 동영상 패널을 구축하는 것이다. YouTube는 채널의 업로드 목록을 숨겨진 재생목록으로 모델링하므로, 추출 레시피는 다음과 같다. 채널의 `relatedPlaylists$uploads` ID를 읽고, 해당 재생목록 항목을 페이징하여 동영상 ID를 수집한 다음, ID 목록에 통계 호출을 매핑하여 결과를 데이터프레임으로 결합한다.

```{r youtube-channel, eval=FALSE}
chan <- list_channel_resources(
  filter = c(channel_id = "UCT5Cx1l4IS3wHkJXNyuj4TA"),
  part   = "contentDetails")

uploads_id <- chan$items[[1]]$contentDetails$relatedPlaylists$uploads
vids       <- get_playlist_items(filter = c(playlist_id = uploads_id))
vid_ids    <- as.vector(vids$contentDetails.videoId)

stats_df <- do.call(rbind, lapply(vid_ids, function(id) data.frame(get_stats(id))))
head(stats_df)
```

### Data API를 통한 API 키 경로

공개 통계만 필요한 경우 원시 REST 엔드포인트를 직접 호출하는 것이 OAuth 세션보다 가볍다. 요청 URL을 작성하고, JSON을 파싱하며, 정돈된 데이터프레임을 반환하는 소규모 헬퍼 함수 패턴(리소스 유형별 1개씩: 동영상, 재생목록, 채널)을 사용할 수 있다.

```{r youtube-api, eval=FALSE}
library(jsonlite)
library(dplyr)

API_key <- Sys.getenv("YOUTUBE_API_KEY")   # 키를 하드코딩하지 말 것

video_stats <- function(video_id, key) {
  url <- paste0("https://www.googleapis.com/youtube/v3/videos",
                "?part=snippet,statistics&id=", video_id, "&key=", key)
  res <- fromJSON(url)
  data.frame(
    name  = res$items$snippet$channelTitle,
    res$items$statistics,
    title = res$items$snippet$title,
    date  = res$items$snippet$publishedAt
  )
}

channel_stats <- function(channel_id, key) {
  url <- paste0("https://www.googleapis.com/youtube/v3/channels",
                "?part=snippet,contentDetails,statistics&id=", channel_id,
                "&key=", key)
  res <- fromJSON(url)
  data.frame(
    name = res$items$snippet$title,
    res$items$statistics,
    uploads = res$items$contentDetails$relatedPlaylists$uploads
  )
}
```

이러한 데이터프레임은 Google 트렌드에서 보았던 `ggplot2` 관용구를 사용하여 총 채널 조회수나 경쟁 채널 간의 댓글 및 좋아요 시계열과 같은 비교 시각화로 바로 이어진다. 인게이지먼트 수치(`viewCount`, `commentCount`)는 문자열로 수신되므로 플로팅 전에 숫자형으로 변환해야 한다.

::: {.callout-warning}

검색 결과 HTML을 페이징하는 `requests` 및 `BeautifulSoup` 기반 스크래퍼는 API 키 없이도 동영상 ID를 가져올 수 있지만, 렌더링된 페이지를 스크래핑하는 것은 취약하며 서비스 약관을 위반할 수 있고 프론트엔드 마크업이 변경될 때마다 중단된다. 공식 엔드포인트를 우선시하고, HTML 스크래핑은 프로토타이핑을 위한 최후의 수단으로만 사용해야 하며 프로덕션에는 사용하지 않아야 한다.

:::

## 가계 지출: 소비자 지출 조사 (CE) {#sec-data-ce}

연구 질문이 **가계가 무엇을 구매하는가**(예산 점유율, 카테고리 수요, 제품군의 소득 탄력성)에 관한 것일 때, 미국의 대표적인 출처는 노동통계국(BLS)이 주관하는 소비자 지출 조사(Consumer Expenditure Survey, CE)이다. 설문의 표본 설계는 상세히 이해할 가치가 있다. 설문의 구조가 어떤 추정 모수를 어떤 빈도로 뒷받침할 수 있는지를 규정하기 때문이다.

CE의 관측 단위는 **소비자 단위(consumer unit)**이며, 함께 거주하면서 주요 지출의 대부분에 대한 책임을 공유하는 단일 개인 또는 집단으로 정의된다.

> 소비자 단위는 단일 개인이거나, 함께 거주하며 대부분의 주요 지출에 대한 책임을 공유하는 개인들의 집단이다.

각 단위 내에서 **기준 인물(reference person)**은 응답자가 "이 주택을 소유하거나 임차하는 데 책임이 있는 사람이 누구인가?"라는 질문에 첫 번째로 지명한 개인이다. 이는 가구주를 결정론적으로 고정하여 설문 간 연계를 명확하게 해주는 관례이다.

조사는 단일 도구가 아니라 상호 보완적인 두 가지 도구로 구성되며, 이는 회상 정확도와 포괄 범위 간의 측정 트레이드오프에서 비롯된 설계 선택이다. 고가의 비정기적 구매는 잘 기억되지만 발생 빈도가 낮고, 소액의 빈번한 구매는 빠르게 잊히지만 건수 기준으로 예산의 대부분을 차지한다. 단일 도구로는 둘 다 잘 측정할 수 없으므로 CE는 이를 분리한다.

- **면접 조사(Interview Survey)**는 고가 품목 및 반복 지출, 그리고 일부 카테고리에 대한 전반적 추정치를 포착한다. 이는 순환 패널(rotating-panel) 조사이다. 각 소비자 단위는 4개 분기 동안 3개월에 한 번씩 인터뷰를 받으며 매 분기 표본 크기는 약 6,000가구이다. 패널 구조는 1년 내 가구 내 변화를 뒷받침하지만 4분기 상한으로 인해 여러 해에 걸쳐 동일 가구를 추적할 수는 없다.
- **가계부 조사(Diary Survey)**는 회상 기반 인터뷰가 놓치기 쉬운 소액의 빈번한 구매 품목을 포착한다. 이는 면접 부문과 독립적이며 매년 참여 가구로부터 약 14,000개의 가계부를 수집한다.

발행되는 집계표는 여러 시간 형식으로 제공된다. **연간** 집계표는 1월~12월을 다루며(1984년부터 제공), 회계연도 기준으로는 7월~6월을 다룬다(2013년부터 제공). **2개년** 집계표는 1차년도 1월부터 2차년도 12월까지를 포괄한다(1986년부터 제공). 표준 집계표 외에도 BLS는 요청 시 밀레니얼이나 X세대와 같은 세대 집단이나 소득 세부 정보를 다루는 **실험적(experimental)** 연구 집계표를 제공한다. 연구 설계에 대한 실무적 시사점은 순환 4분기 패널이 연중 가구 내 분석 질문에 적합한 틀인 반면, 다년간의 동태적 분석은 동일 가구를 추적하기보다 반복 횡단면 데이터를 통합하여 분석해야 한다는 점이다.

## 이름 기반 인구통계학적 추론 {#sec-data-names}

마케팅 연구에서 자주 발생하는 요구 중 하나는 이름만 있고 자체 보고된 인구통계 정보가 없는 기록(고객 명단, 리뷰 작성자, 소셜 미디어 게시자 등)에 성별, 연령, 국적과 같은 인구통계 속성을 부여하는 것이다. 일련의 웹 서비스가 정확히 이러한 추론을 수행한다(genderize.io의 성별, agify.io의 연령, nationalize.io의 국적). 각 서비스는 쿼리된 이름에 대해 신뢰도와 함께 예측된 속성을 반환한다.

이러한 출력물을 있는 그대로 이해하는 것이 필수적이다. 즉, 참값 라벨이 아니라 **이름 빈도 분류기에서 도출된 사후 확률(posterior probabilities)**로 읽어야 한다. 기저 논리는 단순한 베이지안 분류기이다. $n$을 관측된 이름이라 하고 $g$를 후보 속성 값(예: 성별)이라 하자. 서비스들은 실질적으로 다음을 보고한다.

$$
\Pr(g \mid n) \;=\; \frac{\Pr(n \mid g)\,\Pr(g)}{\displaystyle\sum_{g'} \Pr(n \mid g')\,\Pr(g')},
$$ {#eq-name-bayes}

이는 속성 태그가 지정된 방대한 이름 레지스트리로부터 추정되며, $\Pr(n \mid g)$는 속성 값 $g$를 가진 개인들 사이에서 이름 $n$의 빈도이고 $\Pr(g)$는 참조 모집단에서 $g$의 기저율(base rate)이다. [@eq-name-bayes]의 세 가지 특성이 책임 있는 사용을 규율한다. 첫째, 예측은 **참조 모집단의 구성**을 상속한다. 주로 한 지역의 레지스트리로 훈련된 분류기는 다른 지역에서 흔한 이름에 대해 체계적으로 잘못 예측하므로 기저율 $\Pr(g)$는 보편적이지 않다. 둘째, 보고된 신뢰도는 **사후 확률 그 자체**이므로 유니섹스 이름이나 희귀한 이름은 분산이 크고 신뢰도가 낮은 사후 확률을 산출하며 이를 결정론적 라벨로 굳혀서는 안 된다. 셋째, 추론된 속성은 **생성된 회귀변수(generated regressor)**이므로 이를 후속 모형의 공변량으로 사용하면 분류 오차가 모형에 주입된다. 이로 인한 감쇄 편향과 1단계 불확실성을 전파해야 하는 필요성은 [@sec-measurement-scales]에서 다룬다. 이러한 주의사항을 염두에 두고 사용할 때 이름 기반 추론은 대략적인 인구통계 구조를 복원하는 경제적인 방법이지만, 단순하게 사용할 경우 이름 출신지와 상관된 측정 오차를 만들어내게 된다.

## 함정과 식별 (Pitfalls and Identification) {#sec-data-pitfalls}

본 장의 데이터 출처들은 단위, 빈도, 출처에서 차이가 있지만 유효한 추론을 위협하는 요인들은 소수의 구조적 원인을 공유한다. [@fig-data-pitfalls]는 각 흔한 함정을 가장 치명적인 데이터 출처 및 그 해결책과 매핑한다.

```{mermaid}
%%| label: fig-data-pitfalls
%%| fig-cap: "본 장의 데이터 출처 전반에서 반복되는 타당성 위협 요인과 해결책. 각 위협은 추정 대상 모수와 출처가 실제로 제공하는 관측치 사이의 간극임."
flowchart LR
  A["비무작위 결측<br/>(Compustat의 미공시 xad)"] --> A2["공시 행태 모델링;<br/>NULL을 0으로 처리 금지"]
  B["상대적·기간의존적 지수<br/>(Google 트렌드, 바이두)"] --> B2["중첩 스케일링 방법으로<br/>재조정 (eq-gtrends-scaling)"]
  C["지수 내 표본 추출 노이즈<br/>(트렌드 추출 변동)"] --> C2["반복 쿼리 평균화"]
  D["생성된 회귀변수 오차<br/>(이름 기반 인구통계)"] --> D2["1단계 불확실성의<br/>후속 전파"]
  E["회상 vs. 포괄범위 절충<br/>(CE 설문)"] --> E2["추정 모수에 도구 일치<br/>(면접 vs. 가계부)"]
  F["속도 제한 / 이용약관<br/>(API, 스크래퍼)"] --> F2["요청 예산 관리;<br/>공식 엔드포인트 선호"]
```

통합적인 규율은 서두에서 밝힌 바와 같다. 추정 대상 모수를 명시하고, 출처가 제공하는 관측치를 명시하며, 그 차이를 단순한 불편함이 아닌 모델링 문제로 다루어야 한다. 공시된 광고비는 실제 광고비가 아니며, 상대 지수는 절대 볼륨이 아니고, 이름 기반 예측은 인구통계학적 사실이 아니다. 각 간극은 명시적으로 드러낼 때 다룰 수 있으며 간과할 때 치명적이다.

## 핵심 요약 (Key Takeaways)

- **관측 단위를 추정 대상 모수와 일치시켜라.** WRDS는 기업 수준 재무 데이터를, CE 조사는 가계 지출을, 검색/인게이지먼트 API는 개인의 행동 흔적을 제공하며, 어떤 출처도 다른 출처를 대체할 수 없다 ([@fig-data-landscape]).
- **공시된 것은 측정된 것과 다르다.** Compustat의 `xad`는 **공시된** 광고비를 기록한다. 결측은 비무작위적이며 `NULL`을 0으로 처리하면 결과 변수와 상관된 변수로 표본을 선택하게 된다 ([@sec-data-wrds]).
- **상대 지수는 절대 볼륨이 아니다.** Google 트렌드는 기간 창의 최댓값으로 재조정된다 ([@eq-gtrends-index]). 긴 일별 시계열은 중첩-스케일링 방법([@eq-gtrends-scaling])으로 복원해야 하며, 절대 건수는 완전히 다른 출처를 요구한다.
- **설문 설계는 회상과 포괄 범위 간의 절충을 반영한다.** CE는 고가 품목 회상(면접 패널)과 빈번한 구매 포괄(가계부)을 분리하므로 적절한 도구 선택은 카테고리에 달려 있다 ([@sec-data-ce]).
- **이름 기반 인구통계는 사후 확률이지 라벨이 아니다.** 이는 베이지안 이름-빈도 분류기([@eq-name-bayes])를 따르며, 그 오차는 이름 출신지와 상관되므로 후속 모형으로 전파되어야 한다 ([@sec-data-names]).
- **플랫폼 계약을 준수하라.** 소유자 비공개 지표는 OAuth를, 공개 지표는 API 키를 요구한다 ([@tbl-youtube-apis]). 속도 제한을 준수하고 취약한 스크래퍼보다 공식 엔드포인트를 선호해야 한다.
"""

with open('mybook/marketing_research_complete/sections_ko/sec_033_24-data.qmd', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully wrote sec_033")
