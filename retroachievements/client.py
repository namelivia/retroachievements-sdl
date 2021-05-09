import requests


class RetroAchievementsWebApiClient:
    API_URL = "https://retroachievements.org/API/"

    def __init__(self, user, api_key):
        self.ra_user = user
        self.ra_api_key = api_key

    def _AuthQS(self):
        return "?z=" + self.ra_user + "&y=" + self.ra_api_key

    def _GetRAURL(self, target, params=""):
        print(self.API_URL + target + self._AuthQS() + f"&{params}")
        return requests.get(
            self.API_URL + target + self._AuthQS() + f"&{params}"
        ).json()

    def GetTopTenUsers(self):
        return self._GetRAURL("API_GetTopTenUsers.php")

    def GetGameInfo(self, gameID):
        return self._GetRAURL("API_GetGame.php", f"i={gameID}")

    def GetGameInfoExtended(self, gameID):
        return self._GetRAURL("API_GetGameExtended.php", f"i={gameID}")

    def GetConsoleIDs(self):
        return self._GetRAURL("API_GetConsoleIDs.php")

    def GetGameList(self, consoleID):
        return self._GetRAURL("API_GetGameList.php", "i=consoleID")

    def GetFeedFor(self, user, count, offset=0):
        return self._GetRAURL("API_GetFeed.php", "u=user&c=count&o=offset")

    def GetUserRankAndScore(self, user):
        return self._GetRAURL("API_GetUserRankAndScore.php", "u=user")

    def GetUserProgress(self, user, gameIDCSV):
        return self._GetRAURL(
            "API_GetUserProgress.php", "u=user&i=" + gameIDCSV.strip()
        )

    def GetUserRecentlyPlayedGames(self, user, count, offset=0):
        return self._GetRAURL(
            "API_GetUserRecentlyPlayedGames.php", "u=user&c=count&o=offset"
        )

    def GetUserSummary(self, user, numRecentGames):
        return self._GetRAURL(
            "API_GetUserSummary.php", f"u={user}&g={numRecentGames}&a=5"
        )

    def GetGameInfoAndUserProgress(self, user, gameID):
        return self._GetRAURL("API_GetGameInfoAndUserProgress.php", "u=user&g=gameID")

    def GetAchievementsEarnedOnDay(self, user, dateInput):
        return self._GetRAURL(
            "API_GetAchievementsEarnedOnDay.php", "u=user&d=dateInput"
        )

    def GetAchievementsEarnedBetween(self, user, dateStart, dateEnd):
        dateFrom = dateStart.strftime("%s")
        dateTo = dateEnd.strftime("%s")
        return self._GetRAURL(
            "API_GetAchievementsEarnedBetween.php", f"u=user&f={dateFrom}&t={dateTo}"
        )

    def GetUserGamesCompleted(self, user):
        return self._GetRAURL("API_GetUserCompletedGames.php", "u=user")
