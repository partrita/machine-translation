# Machine translate

이 저장소는 외국어로 작성된 내용을 한국어로 기계 번역하고, Quarto를 사용하여 웹북 형태로 호스팅하기 위한 템플릿입니다.

## 프로젝트 구조

- `mybook/`: Quarto 책 소스 파일들이 포함되어 있습니다.
  - `index_ko.qmd`: 한국어 번역본 메인 파일.
  - `index.qmd`: 영문 원본 파일.
- `images/`: 책에 사용된 이미지 파일들에 대한 심볼릭 링크.
- `pixi.toml`: 의존성 관리 도구 ([Pixi](https://prefix.dev/)) 설정 파일.
- `.github/workflows/publish.yml`: GitHub Pages에 자동으로 책을 빌드하고 게시하는 워크플로.

## 사용법

### 필수 조건

- 시스템에 [Pixi](https://prefix.dev/)가 설치되어 있어야 합니다.

### 로컬 개발 및 미리보기

1.  저장소 클론:

    ```bash
    git clone https://github.com/partrita/mastering-python-bioinformatics.git
    cd mastering-python-bioinformatics
    ```

2.  책 미리보기:

    Pixi를 사용하여 Quarto를 실행하고 라이브 미리보기 서버를 시작합니다:

    ```bash
    pixi run quarto preview mybook
    ```

3.  렌더링 (정적 파일 생성):

    ```bash
    pixi run quarto render mybook
    ```

### 의존성 관리

이 프로젝트는 `pixi`를 사용하여 의존성을 관리합니다.

```bash
pixi add python pandas biopython  # 필요한 라이브러리 추가 예시
```

## 배포

`main` 브랜치에 푸시하면 GitHub Actions가 자동으로 `mybook` 디렉토리의 내용을 빌드하여 `gh-pages` 브랜치로 배포합니다.
