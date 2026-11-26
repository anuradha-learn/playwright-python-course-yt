from playwright.sync_api import expect

def test_search_products(page):
    keywords=["fresh","organic","farm"]

    for keyword in keywords:
        page.goto("https://qa-cart.com/demoshop/")
        page.get_by_role("searchbox").fill(keyword)
        page.get_by_role("button",name="search").click()
        expect(page.get_by_text("Search results").last).to_be_visible()