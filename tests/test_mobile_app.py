import allure
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


@allure.tag("mobile")
@allure.label("qa", "Timur")
@allure.feature("Wikipedia app_Mobile tests examples")
@allure.story("'Explore' screen check ")
def test_explore_screen_wikipedia():
    with step('Skip onboarding screen'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_skip_button")).click()

    with step('Verify welcome screen'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/view_announcement_text'))
        results.should(be.present)

    with step('Press Saved button on bottom menu'):
        browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/navigation_bar_item_icon_view")).element(1).click()

    with step('Verify Saved screen'):
        results = browser.all((AppiumBy.CLASS_NAME, 'android.widget.TextView'))
        results.should(be.present)
        results.first.should(have.text('Saved'))

    with step('Press Search button on bottom menu'):
        browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/navigation_bar_item_icon_view")).element(2).click()

    with step('Verify Search screen'):
        results = browser.all((AppiumBy.CLASS_NAME, 'android.widget.TextView'))
        results.should(be.present)
        results.first.should(have.text('Search'))

    with step('Press Edits button on bottom menu'):
        browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/navigation_bar_item_icon_view")).element(3).click()

    with step('Verify Edits screen'):
        results = browser.all((AppiumBy.CLASS_NAME, 'android.widget.TextView'))
        results.should(be.present)
        results.first.should(have.text('Edits'))


@allure.tag("mobile")
@allure.label("qa", "Timur")
@allure.feature("Wikipedia app_Mobile tests examples")
@allure.story("Onboarding screens check")
def test_getting_started():
    with step('Open welcome screen and verify welcome screen'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(have.text('The Free '
                                                                                                  'Encyclopedia\n…in '
                                                                                                  'over 300 languages'))

    with step('Tap "Continue" button'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    with step('Verify "New ways to explore" screen'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(have.text('New ways to '
                                                                                                  'explore'))
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/secondaryTextView')).should(have.text(
            'Dive down the Wikipedia rabbit hole with a constantly updating Explore feed. \nCustomize the feed to '
            'your interests – whether it’s learning about historical events On this day, or rolling the dice with '
            'Random.'))

    with step('Tap "Continue" button'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    with step('Verify "Reading list with sync" screen'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(have.text('Reading lists '
                                                                                                  'with sync'))
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/secondaryTextView')).should(have.text(
            'You can make reading lists from articles you want to read later, even when you’re offline. \nLogin to '
            'your Wikipedia account to sync your reading lists. Join Wikipedia'))

    with step('Tap "Continue" button'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    with step('Verify "Data & Privacy" screen'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(have.text('Data & Privacy'))
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/secondaryTextView')).should(have.text(
            'We believe that you should not have to provide personal information to participate in the free knowledge '
            'movement. Usage data collected for this app is anonymous. Learn more about our privacy policy and terms '
            'of use.'))