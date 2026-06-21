from ..steps.upcoming_matches_helper import UpcomingMatchesHelper


class UI:
    def __init__(self, wd, base_url, user):
        self.wd = wd
        self.base_url = base_url
        self.user = user
        self.home_page = f"{base_url}/?user-id={self.user}"
        self.upcoming_matches = UpcomingMatchesHelper(self)

    def go_to_home_page(self):
        self.wd.get(self.home_page)

    def close(self):
        self.wd.quit()
