from playwright.sync_api import expect

def test_search_products(page):
    page.goto("https://qa-cart.com/demoshop/")
    page.get_by_role("searchbox").fill("fresh")
    page.get_by_role("button",name="search").click()
    expect(page.get_by_text("Search results").last).to_be_visible()