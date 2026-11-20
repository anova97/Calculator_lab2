"""Testy nawigacji po stronie Wydziału Informatyki AGH"""

from playwright.sync_api import Page, expect

### homework
# 1 test sprawdzający, czy strona główna Wydziału otwiera się poprawnie
def test_open_agh_website(page: Page):
    """Test otwarcia strony wydzialu"""
    page.goto("https://www.informatyka.agh.edu.pl/pl/")

    print(page.title())

    assert page.title() != ""

# 2 test przechodzący do podstrony „O Wydziale”. Sprawdź nagłówek
def test_about_faculty(page: Page):
    """Test - o wydziale"""
    page.goto("https://www.informatyka.agh.edu.pl/pl/")

    menu = page.get_by_role("navigation")
    menu.get_by_role("link", name="Wydział", exact=True).click()

    menu.get_by_role("link", name="O Wydziale", exact=True).click()

    expect(
        page.get_by_role("heading", name="O Wydziale")
    ).to_be_visible()

# 3  test przechodzący do kierunków studiów. Sprawdź, czy oczekiwana treść.
def test_study_programs(page: Page):
    """Test - kierunki"""
    page.goto("https://www.informatyka.agh.edu.pl/pl/")

    menu = page.get_by_role("navigation")
    menu.get_by_role("link", name="Kandydaci", exact=True).click()
    menu.get_by_role("link", name="Nasze kierunki", exact=True).click()

    expect(
        page.get_by_role("heading", name="Nasze kierunki", exact=True)
    ).to_be_visible()
    expect(
        page.get_by_role("link", name="Informatyka", exact=True)
    ).to_be_visible()

# 4 test, czy po przejściu do wybranej podstrony adres URL uległ zmianie.
def test_check_url(page: Page):
    """Test - url"""
    page.goto("https://www.informatyka.agh.edu.pl/pl/")

    menu = page.get_by_role("navigation")
    menu.get_by_role("link", name="Kandydaci", exact=True).click()
    menu.get_by_role("link", name="Nasze kierunki", exact=True).click()

    expect(page).to_have_url(
        "https://www.informatyka.agh.edu.pl/pl/studenci/dla-kandydatow/kierunki/"
    )
