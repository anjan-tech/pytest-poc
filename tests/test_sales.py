import pytest

from app.sales import apply_discount, calculate_total, clean_region, order_size


def test_calculate_total():
    assert calculate_total(100, 3) == 300


def test_calculate_total_rejects_negative_values():
    with pytest.raises(ValueError):
        calculate_total(-1, 3)


def test_apply_discount():
    assert apply_discount(200, 10) == 180.0


def test_apply_discount_rejects_invalid_percent():
    with pytest.raises(ValueError):
        apply_discount(200, 150)


def test_clean_region():
    assert clean_region("  north ") == "North"

def test_order_size():
    assert order_size(15000) == "LARGE"
    assert order_size(5000) == "MEDIUM"
    assert order_size(100) == "SMALL"