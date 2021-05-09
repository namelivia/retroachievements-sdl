from retroachievements.client import RetroAchievementsWebApiClient
from mock import patch
from datetime import datetime


class TestClient:
    @patch("requests.get")
    def test_get_top_ten_users(self, m_requests):
        client = RetroAchievementsWebApiClient("test_user", "test_user_key")
        client.GetTopTenUsers()
        m_requests.assert_called_once_with(
            "https://retroachievements.org/API/API_GetTopTenUsers.php?z=test_user&y=test_user_key&"
        )

    @patch("requests.get")
    def test_get_game_info(self, m_requests):
        client = RetroAchievementsWebApiClient("test_user", "test_user_key")
        client.GetGameInfo("test_game")
        m_requests.assert_called_once_with(
            "https://retroachievements.org/API/API_GetGame.php?z=test_user&y=test_user_key&i=test_game"
        )

    @patch("requests.get")
    def test_get_game_info_extended(self, m_requests):
        client = RetroAchievementsWebApiClient("test_user", "test_user_key")
        client.GetGameInfoExtended("test_game")
        m_requests.assert_called_once_with(
            "https://retroachievements.org/API/API_GetGameExtended.php?z=test_user&y=test_user_key&i=test_game"
        )

    @patch("requests.get")
    def test_get_console_ids(self, m_requests):
        client = RetroAchievementsWebApiClient("test_user", "test_user_key")
        client.GetConsoleIDs()
        m_requests.assert_called_once_with(
            "https://retroachievements.org/API/API_GetConsoleIDs.php?z=test_user&y=test_user_key&"
        )

    @patch("requests.get")
    def test_game_list(self, m_requests):
        client = RetroAchievementsWebApiClient("test_user", "test_user_key")
        client.GetGameList("test_console")
        m_requests.assert_called_once_with(
            "https://retroachievements.org/API/API_GetGameList.php?z=test_user&y=test_user_key&i=test_console"
        )

    @patch("requests.get")
    def test_get_feed_for(self, m_requests):
        client = RetroAchievementsWebApiClient("test_user", "test_user_key")
        client.GetFeedFor("test_user", 12, 3)
        m_requests.assert_called_once_with(
            "https://retroachievements.org/API/API_GetFeed.php?z=test_user&y=test_user_key&u=test_user&c=12&o=3"
        )

    @patch("requests.get")
    def test_get_user_rank_and_score(self, m_requests):
        client = RetroAchievementsWebApiClient("test_user", "test_user_key")
        client.GetUserRankAndScore("test_user")
        m_requests.assert_called_once_with(
            "https://retroachievements.org/API/API_GetUserRankAndScore.php?z=test_user&y=test_user_key&u=test_user"
        )

    @patch("requests.get")
    def test_get_user_progress(self, m_requests):
        client = RetroAchievementsWebApiClient("test_user", "test_user_key")
        client.GetUserProgress("test_user", "test_game")
        m_requests.assert_called_once_with(
            "https://retroachievements.org/API/API_GetUserProgress.php?z=test_user&y=test_user_key&u=test_user&i=test_game"
        )

    @patch("requests.get")
    def test_get_user_recently_played_games(self, m_requests):
        client = RetroAchievementsWebApiClient("test_user", "test_user_key")
        client.GetUserRecentlyPlayedGames("test_user", 12, 2)
        m_requests.assert_called_once_with(
            "https://retroachievements.org/API/API_GetUserRecentlyPlayedGames.php?z=test_user&y=test_user_key&u=test_user&c=12&o=2"
        )

    @patch("requests.get")
    def test_get_user_summary(self, m_requests):
        client = RetroAchievementsWebApiClient("test_user", "test_user_key")
        client.GetUserSummary("test_user", 12)
        m_requests.assert_called_once_with(
            "https://retroachievements.org/API/API_GetUserSummary.php?z=test_user&y=test_user_key&u=test_user&g=12&a=5"
        )

    @patch("requests.get")
    def test_get_game_info_and_user_progress(self, m_requests):
        client = RetroAchievementsWebApiClient("test_user", "test_user_key")
        client.GetGameInfoAndUserProgress("test_user", "test_game")
        m_requests.assert_called_once_with(
            "https://retroachievements.org/API/API_GetGameInfoAndUserProgress.php?z=test_user&y=test_user_key&u=test_user&g=test_game"
        )

    @patch("requests.get")
    def test_get_achievements_earned_on_day(self, m_requests):
        client = RetroAchievementsWebApiClient("test_user", "test_user_key")
        client.GetAchievementsEarnedOnDay("test_user", datetime(2021, 3, 12))
        m_requests.assert_called_once_with(
            "https://retroachievements.org/API/API_GetAchievementsEarnedOnDay.php?z=test_user&y=test_user_key&u=test_user&d=1615503600"
        )

    @patch("requests.get")
    def test_get_achievements_earned_between(self, m_requests):
        client = RetroAchievementsWebApiClient("test_user", "test_user_key")
        client.GetAchievementsEarnedBetween(
            "test_user", datetime(2021, 3, 12), datetime(2021, 3, 16)
        )
        m_requests.assert_called_once_with(
            "https://retroachievements.org/API/API_GetAchievementsEarnedBetween.php?z=test_user&y=test_user_key&u=user&f=1615503600&t=1615849200"
        )

    @patch("requests.get")
    def test_get_user_games_completed(self, m_requests):
        client = RetroAchievementsWebApiClient("test_user", "test_user_key")
        client.GetUserGamesCompleted("test_user")
        m_requests.assert_called_once_with(
            "https://retroachievements.org/API/API_GetUserCompletedGames.php?z=test_user&y=test_user_key&u=test_user"
        )
