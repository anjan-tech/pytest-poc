def calculate_total(price, quantity):
    if price < 0 or quantity < 0:
        raise ValueError("price and quantity must not be negative")
    return price * quantity


def apply_discount(amount, percent):
    if percent < 0 or percent > 100:
        raise ValueError("percent must be between 0 and 100")
    return round(amount * (1 - percent / 100), 2)


def clean_region(region):
    return region.strip().title()