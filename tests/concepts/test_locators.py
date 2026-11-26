def test_add_to_cart_button_click(page):
    page.goto("https://qa-cart.com/demoshop/")
    page.get_by_role("button", name="Add To Cart").first.click()
