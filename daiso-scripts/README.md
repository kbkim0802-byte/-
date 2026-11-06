# 다이소대본 프로젝트

JUU_PICK 채널 다이소 스타일 쇼츠 대본 작업 폴더.

- 스킬: `.claude/skills/daiso-script/` (Claude Code에서 "다이소대본으로 써줘" 또는 `/daiso-script`)
  - `SKILL.md`: 작업 순서와 규칙
  - `references/structure.md`: 고정 7단 구조 (후킹 → 반전 → 기능1~3 → 마지막 도약 → 구매 전환)
  - `references/channel-patterns.md`: 꿀템줍줍, 홈딱, 일본 쿠라시 계정 분석
  - `scripts/timing.py`: 대본 길이 계산 (목표 22~23초, 최대 156자)
  - `scripts/channel_top.py`: 채널 쇼츠 조회수 순 목록
- `output/`: 완성된 대본 (`YYYY-MM-DD_제품명.md`)

## 사용법
제품 스크린샷과 참고 영상을 올리고 "다이소대본으로 써줘"라고 하면 된다.
