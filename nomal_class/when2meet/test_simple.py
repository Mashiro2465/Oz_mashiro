from datetime import datetime, timedelta


def add(a: int, b: int) -> int:
    return a + b


def test_add() -> None:
    # Given : 재료를 준비
    a, b = 1, 1

    # When : 테스트 대상이 되는 함수를 호출
    result = add(a, b)

    # Then : 결과 검증
    assert result == 2


# 배송일
DELIVERY_DAYS = 2


def _is_holiday(day: datetime) -> bool:
    return day.weekday() > 5


def get_eta(purchase_date: datetime) -> datetime:
    current_date = purchase_date
    remaining_days = DELIVERY_DAYS

    while remaining_days > 0:
        current_date += timedelta(days=1)
        if not _is_holiday(current_date):
            remaining_days -= 1

    return current_date


def test_eta() -> None:
    result = get_eta(datetime(2023, 12, 1))
    assert result == datetime(2023, 12, 4)
