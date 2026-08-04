import sys

file_path = "/Users/fkt/Downloads/repo/mastering-bioinformatics/mybook/rust/rustc-dev-guide.qmd"

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Line 12024 is index 12023, Line 12131 is index 12130
start_idx = 12023
end_idx = 12130

new_text = """### 축약표현 (Shorthands)

`Ty`는 심각한 재귀 구조를 띨 수 있어 각 `Ty`를 날것 그대로 직렬화하면 크레이트 메타데이터가 비정상적으로 팽창하게 됩니다. 이를 해결하기 위해 각 `TyEncoder`는 이미 직렬화했던 타입들의 파일 내 위치 캐시를 보관합니다. 인코딩 대상 타입이 캐시 내에 존재하는 경우 타입을 원래대로 직렬화하는 대신 출력 파일 내의 바이트 오프셋을 대신 인코딩합니다. `ty::Predicate`에 대해서도 유사한 기법을 적용합니다.

### `LazyValue<T>`

크레이트 메타데이터는 최초 `TyCtxt<'tcx>`가 생성되기 전에 로드되므로, 일부 역직렬화 작업은 최초 메타데이터 로드 시점 이후로 지연(defer)되어야 합니다.
[`LazyValue<T>`] 타입은 `T`가 직렬화된 크레이트 메타데이터 내부의 (상대) 오프셋을 감쌉니다. 유사한 변형 타입으로 [`LazyArray<T>`] 및 [`LazyTable<I, T>`]도 존재합니다.

`LazyArray<[T]>` 및 `LazyTable<I, T>` 타입은 `Lazy<Vec<T>>` 및 `Lazy<HashMap<I, T>>` 대비 다음과 같은 우월한 기능을 선사합니다:

- `Vec<T>`로 사전에 수집(collect)할 필요 없이 `Iterator`로부터 `LazyArray<T>`를 직접 인코딩할 수 있습니다.
- `LazyTable<I, T>` 항목을 인덱싱할 때 읽어 들이려는 대상 외의 타 항목들을 디코딩할 필요가 없습니다.

**참고**: `LazyValue<T>`는 최초 역직렬화된 직후 그 결과 값을 내부 캐싱하지 않습니다. 대신 쿼리 시스템 자체가 해당 결과를 캐싱하는 메인 주체 역할을 이행합니다.

[`LazyArray<T>`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_metadata/rmeta/struct.LazyValue.html
[`LazyTable<I, T>`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_metadata/rmeta/struct.LazyValue.html
[`LazyValue<T>`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_metadata/rmeta/struct.LazyValue.html

### 특수화 (Specialization)

`DefId`와 같은 소수의 타입들은 각기 다른 `Encoder`들에 대해 특수화된 별도 구현체를 가져야만 합니다. 이는 현재 임시 특수화 방식으로 다루어지는데, 예를 들어: `DefId`는 `Encodable<E>`에 대해 기본(`default`) 구현체를 가지는 동시에 `Encodable<CacheEncoder>`를 위한 특수화 구현체를 별도 구비합니다.


## 병렬 컴파일 (Parallel compilation) {#parallel-rustc}

<div class="warning">
2024년 11월 기준, 병렬 프론트엔드가 활발한 구조 변경을 겪고 있으므로 본 페이지의 일부 내용이 오래되었을 수 있습니다.

트래킹 이슈: <https://github.com/rust-lang/rust/issues/113349>
</div>

2024년 11월 기준, Rust 컴파일러의 대부분의 파트들이 현재 병렬화(parallelized)되었습니다.

- 코드 생성(codegen) 파트는 기본적으로 병렬 동시 실행됩니다.
  `-C codegen-units=n` 옵션을 사용해 동시 구동 태스크 수량을 제어할 수 있습니다.
- HIR 로어링 이후부터 codegen에 이르는 단계들(타입 검사, 대여 검사, MIR 최적화 등)은 나이틀리 버전에 병렬화 구현이 포함되어 있습니다.
  현재는 기본적으로 순차(serial) 실행되며, 사용자가 `-Z threads=n` 옵션을 지정하여 병렬화를 직접 활성화할 수 있습니다.
- 어휘 파싱, HIR 로어링, 매크로 확장 등 타 파트들은 여전히 순차 모드로 실행됩니다.

<div class="warning">
아래 섹션들은 정보 보존을 위해 남겨두었으나 다소 이전 정보에 해당합니다.
</div>

---

[codegen]: #backend-codegen

### 코드 생성 (Code generation)

모노모피제이션(단일형화) 동안 컴파일러는 생성할 모든 코드를 _codegen units_라 불리는 더 작은 조각들로 분할합니다.
이 조각들은 병렬 구동되는 독립된 LLVM 인스턴스들에 의해 생성됩니다.
마지막에 링커가 구동되어 모든 codegen unit들을 단일 바이너리로 결합합니다.
이 프로세스는 [`rustc_codegen_ssa::base`] 모듈 내부에서 일어납니다.

[`rustc_codegen_ssa::base`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_codegen_ssa/base/index.html

### 데이터 구조 (Data structures)

병렬 컴파일러 내부에서 채택되는 근본적인 스레드 안전(thread-safe) 데이터 구조들은 [`rustc_data_structures::sync`] 모듈에서 찾아볼 수 있습니다.
이 데이터 구조들은 `parallel-compiler` 설정 플래그의 활성화 여부에 따라 다르게 구현됩니다.

| 데이터 구조 | 병렬 모드 (parallel) | 비병렬 모드 (non-parallel) |
| -------------------------------- | --------------------------------------------------- | ------------ |
| Lock\<T> | (parking_lot::Mutex\<T>) | (std::cell::RefCell) |
| RwLock\<T> | (parking_lot::RwLock\<T>) | (std::cell::RefCell) |
| ReadGuard | parking_lot::RwLockReadGuard | std::cell::Ref |
| MappedReadGuard | parking_lot::MappedRwLockReadGuard | std::cell::Ref |
| WriteGuard | parking_lot::RwLockWriteGuard | std::cell::RefMut |
| MappedWriteGuard | parking_lot::MappedRwLockWriteGuard | std::cell::RefMut |
| LockGuard | parking_lot::MutexGuard | std::cell::RefMut |

- 이러한 스레드 안전 데이터 구조들은 컴파일 도중 도처에서 산재되어 호출되므로, 스레드 수량이 4개를 넘어 증가함에 따라 락 경합(lock contention)을 유발하여 성능을 저하시킬 가능성이 존재합니다. 따라서 이러한 데이터 구조의 사용 실태를 면밀히 감사(audit)하여 공유 상태 채택을 줄이도록 리팩터링하거나 원자성(atomicity) 및 락 순서를 명시하는 문서를 작성합니다.\n"""

lines[start_idx:end_idx] = [new_text]

with open(file_path, "w", encoding="utf-8") as f:
    f.writelines(lines)

print("SUCCESS BY INDEX")
