def test_homepage_loads(page):
    page.goto("https:/qa-cart.com")
    assert page.title()=="QA TEST AUTOMATION DEMO STORE BY ANURADHA AGARWAL1"
    #assert page.title()=="Wrong Title"