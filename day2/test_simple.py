from datetime import datetime, timedelta


# 재품코드
def add(a:int, b:int) -> int:
    return  a + b

# 테스트 코드
def test_simple() -> None:
    # 버그는 "경계"를 좋아합니다. -> int의 경우에는 -1, 0, 1
    try:
        1/0
    except ZeroDivisionError:
        print("FBI!!")

def test_add() -> None:
    # Given : 재료를 준비합니다.
    a, b = 1, 1

    # when : 테스트 대상이 되는 함수를 호출합니다.
    result = add(a, b)

    # Then:
    assert result == 2
    if not result == 2 : raise AssertionError()
    
# 택배 테스트
def get_eta(purchase_date: datetime) -> datetime:
    due = 2
    # literal을 쓰지 않고 상수를 쓰는 이유 -> "2" 라는 숫자가 "배송일" 이라는 사실을 알려줌
    # magic number 를 쓰지 않는 이유 -> 코드의 가독성을 높히면서 유지보수가 쉬워짐
    now = purchase_date
    while due > 0 :
        now += timedelta(days=1)
        if now.weekday() == 6:
            continue

        due -= 1
    return now

def test_get_eta_2023_12_01() -> None:
    result = get_eta(datetime(2023, 12, 1))
    assert result == datetime(2023, 12 ,4)

def test_get_eta_2024_12_31() -> None:
    result = get_eta(datetime(2024, 12, 31))
    assert result == datetime(2025, 1 ,2)

def test_get_eta_2024_02_28() -> None:
    result = get_eta(datetime(2024, 2, 28))
    assert result == datetime(2024, 3 ,1)

def test_get_eta_2023_02_28() -> None:
    result = get_eta(datetime(2023, 2, 28))
    assert result == datetime(2023, 3 ,2)