from my_project_bdd_alerte.pages.alerts_page import AlertsPage
from my_project_bdd_alerte.pages.home_page import HomePage


def before_all(context):
    context.home_page = HomePage()
    context.alerts_page = AlertsPage()

def after_all(context):
    context.browser.close_browser()