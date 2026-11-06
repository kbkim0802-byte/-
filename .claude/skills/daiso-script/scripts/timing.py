#!/usr/bin/env python3
"""쇼츠 나레이션 길이 계산기.

사용법:
    python3 timing.py 대본.txt            # 파일
    echo "대본" | python3 timing.py -      # 표준 입력
    python3 timing.py 대본.txt --rate 7.2  # 속도 변경

기준 속도 6.8자/초는 꿀템줍줍 쇼츠 실측값 (한글, 숫자, 영문 글자 수 기준).
빈 줄과 '#', '>'로 시작하는 줄은 건너뛴다.
"""
import argparse
import re
import sys

DEFAULT_RATE = 6.8
TARGET_SECONDS = 23.0


def count(line: str) -> int:
    return len(re.findall(r"[가-힣0-9A-Za-z]", line))


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("file", help="대본 파일 경로, '-'는 표준 입력")
    p.add_argument("--rate", type=float, default=DEFAULT_RATE, help="초당 글자 수")
    p.add_argument("--target", type=float, default=TARGET_SECONDS, help="목표 초")
    a = p.parse_args()

    text = sys.stdin.read() if a.file == "-" else open(a.file, encoding="utf-8").read()
    total = 0
    for line in text.splitlines():
        s = line.strip()
        if not s or s.startswith(("#", ">")):
            continue
        n = count(s)
        total += n
        print(f"{total / a.rate:5.1f}초  {n:3d}자  {s}")

    secs = total / a.rate
    limit = int(a.target * a.rate)
    print(f"\n합계 {total}자, 약 {secs:.1f}초 (초당 {a.rate}자 기준)")
    if total > limit:
        print(f"목표 {a.target:.0f}초를 넘어요. {total - limit}자 줄이세요 (최대 {limit}자).")
    else:
        print(f"목표 {a.target:.0f}초 안에 들어와요 (최대 {limit}자).")


if __name__ == "__main__":
    main()
