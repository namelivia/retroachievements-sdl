import requests
from datetime import datetime


class RetroAchievementsWebApiClient:
    API_URL = "https://retroachievements.org/API/"

    def __init__(self, user, api_key):
        self.ra_user = user
        self.ra_api_key = api_key

    def _AuthQS(self) -> str:
        return f"?z={self.ra_user}&y={self.ra_api_key}"

    def _GetRAURL(self, target: str, params: str = "") -> dict:
        return requests.get(f"{self.API_URL}{target}{self._AuthQS()}&{params}").json()

    def GetTopTenUsers(self) -> dict:
        return self._GetRAURL("API_GetTopTenUsers.php")

    def GetGameInfo(self, gameID: str) -> dict:
        return self._GetRAURL("API_GetGame.php", f"i={gameID}")

    def GetGameInfoExtended(self, gameID: str) -> dict:
        return self._GetRAURL("API_GetGameExtended.php", f"i={gameID}")

    def GetConsoleIDs(self) -> dict:
        return self._GetRAURL("API_GetConsoleIDs.php")

    def GetGameList(self, consoleID: str) -> dict:
        return self._GetRAURL("API_GetGameList.php", f"i={consoleID}")

    def GetFeedFor(self, user: str, count: int, offset: int = 0) -> dict:
        return self._GetRAURL("API_GetFeed.php", f"u={user}&c={count}&o={offset}")

    def GetUserRankAndScore(self, user: str) -> dict:
        return self._GetRAURL("API_GetUserRankAndScore.php", f"u={user}")

    def GetUserProgress(self, user: str, gameIDCSV: str) -> dict:
        return self._GetRAURL(
            "API_GetUserProgress.php", f"u={user}&i={gameIDCSV.strip()}"
        )

    def GetUserRecentlyPlayedGames(
        self, user: str, count: int, offset: int = 0
    ) -> dict:
        return self._GetRAURL(
            "API_GetUserRecentlyPlayedGames.php", f"u={user}&c={count}&o={offset}"
        )

    def GetUserSummary(self, user: str, numRecentGames: int) -> dict:
        return self._GetRAURL(
            "API_GetUserSummary.php", f"u={user}&g={numRecentGames}&a=5"
        )

    def GetGameInfoAndUserProgress(self, user: str, gameID: str) -> dict:
        return self._GetRAURL(
            "API_GetGameInfoAndUserProgress.php", f"u={user}&g={gameID}"
        )

    def GetAchievementsEarnedOnDay(self, user: str, dateInput: datetime) -> dict:
        date = dateInput.strftime("%s")

        return self._GetRAURL(
            "API_GetAchievementsEarnedOnDay.php", f"u={user}&d={date}"
        )

    def GetAchievementsEarnedBetween(
        self, user: str, dateStart: datetime, dateEnd: datetime
    ) -> dict:
        dateFrom = dateStart.strftime("%s")
        dateTo = dateEnd.strftime("%s")
        return self._GetRAURL(
            "API_GetAchievementsEarnedBetween.php", f"u=user&f={dateFrom}&t={dateTo}"
        )

    def GetUserGamesCompleted(self, user: str) -> dict:
        return self._GetRAURL("API_GetUserCompletedGames.php", f"u={user}")
