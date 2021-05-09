from retroachievements.client import RetroAchievementsWebApiClient
from mock import patch


class TestClient:
    @patch("requests.get")
    def test_get_top_ten_users(self, m_requests):
        client = RetroAchievementsWebApiClient("test_user", "test_user_key")
        client.GetTopTenUsers()
        m_requests.assert_called_once_with(
            "https://retroachievements.org/API/API_GetTopTenUsers.php?z=test_user&y=test_user_key&"
        )
