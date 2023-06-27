import csv
import requests

# Set your Riot API key
api_key = "API KEY HERE"

# Set the region and summoner name for the recent matches
sum_region = "na1"
match_region = "americas"
summoner_name = "SUMMONER HERE"

# Make a request to retrieve summoner information
summoner_url = f"https://{sum_region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key={api_key}"
response = requests.get(summoner_url)

def get_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def write_header(writer):
    header = [
        "assists",
        "baronKills",
        "bountyLevel",
        "consumablesPurchased",
        "damageDealtToBuildings",
        "damageDealtToObjectives",
        "damageDealtToTurrets",
        "damageSelfMitigated",
        "deaths",
        "detectorWardsPlaced",
        "doubleKills",
        "dragonKills",
        "firstBloodAssist",
        "firstBloodKill",
        "firstTowerAssist",
        "firstTowerKill",
        "gameEndedInEarlySurrender",
        "gameEndedInSurrender",
        "goldEarned",
        "goldSpent",
        "individualPosition",
        "inhibitorKills",
        "inhibitorTakedowns",
        "inhibitorsLost",
        "itemsPurchased",
        "killingSprees",
        "kills",
        "lane",
        "largestCriticalStrike",
        "largestKillingSpree",
        "largestMultiKill",
        "longestTimeSpentLiving",
        "magicDamageDealt",
        "magicDamageDealtToChampions",
        "magicDamageTaken",
        "neutralMinionsKilled",
        "nexusKills",
        "nexusLost",
        "nexusTakedowns",
        "objectivesStolen",
        "pentaKills",
        "perks",
        "physicalDamageDealt",
        "physicalDamageDealtToChampions",
        "physicalDamageTaken",
        "quadraKills",
        "role",
        "sightWardsBoughtInGame",
        "spell1Casts",
        "spell2Casts",
        "spell3Casts",
        "spell4Casts",
        "teamEarlySurrendered",
        "teamPosition",
        "timeCCingOthers",
        "timePlayed",
        "totalDamageDealt",
        "totalDamageDealtToChampions",
        "totalDamageShieldedOnTeammates",
        "totalDamageTaken",
        "totalHeal",
        "totalHealsOnTeammates",
        "totalMinionsKilled",
        "totalTimeCCDealt",
        "totalTimeSpentDead",
        "totalUnitsHealed",
        "tripleKills",
        "trueDamageDealt",
        "trueDamageDealtToChampions",
        "trueDamageTaken",
        "turretKills",
        "turretTakedowns",
        "turretsLost",
        "unrealKills",
        "visionScore",
        "visionWardsBoughtInGame",
        "wardsKilled",
        "wardsPlaced",
        "win",
    ]
    writer.writerow(header)

def write_data(writer, participant):
    row = [
        participant.get("assists", 0),
        participant.get("baronKills", 0),
        participant.get("bountyLevel", 0),
        participant.get("consumablesPurchased", 0),
        participant.get("damageDealtToBuildings", 0),
        participant.get("damageDealtToObjectives", 0),
        participant.get("damageDealtToTurrets", 0),
        participant.get("damageSelfMitigated", 0),
        participant.get("deaths", 0),
        participant.get("detectorWardsPlaced", 0),
        participant.get("doubleKills", 0),
        participant.get("dragonKills", 0),
        participant.get("firstBloodAssist", False),
        participant.get("firstBloodKill", False),
        participant.get("firstTowerAssist", False),
        participant.get("firstTowerKill", False),
        participant.get("gameEndedInEarlySurrender", False),
        participant.get("gameEndedInSurrender", False),
        participant.get("goldEarned", 0),
        participant.get("goldSpent", 0),
        participant.get("individualPosition", ""),
        participant.get("inhibitorKills", 0),
        participant.get("inhibitorTakedowns", 0),
        participant.get("inhibitorsLost", 0),
        participant.get("itemsPurchased", 0),
        participant.get("killingSprees", 0),
        participant.get("kills", 0),
        participant.get("lane", ""),
        participant.get("largestCriticalStrike", 0),
        participant.get("largestKillingSpree", 0),
        participant.get("largestMultiKill", 0),
        participant.get("longestTimeSpentLiving", 0),
        participant.get("magicDamageDealt", 0),
        participant.get("magicDamageDealtToChampions", 0),
        participant.get("magicDamageTaken", 0),
        participant.get("neutralMinionsKilled", 0),
        participant.get("nexusKills", 0),
        participant.get("nexusLost", 0),
        participant.get("nexusTakedowns", 0),
        participant.get("objectivesStolen", 0),
        participant.get("pentaKills", 0),
        participant.get("perks", {}),
        participant.get("physicalDamageDealt", 0),
        participant.get("physicalDamageDealtToChampions", 0),
        participant.get("physicalDamageTaken", 0),
        participant.get("quadraKills", 0),
        participant.get("role", ""),
        participant.get("sightWardsBoughtInGame", 0),
        participant.get("spell1Casts", 0),
        participant.get("spell2Casts", 0),
        participant.get("spell3Casts", 0),
        participant.get("spell4Casts", 0),
        participant.get("teamEarlySurrendered", False),
        participant.get("teamPosition", ""),
        participant.get("timeCCingOthers", 0),
        participant.get("timePlayed", 0),
        participant.get("totalDamageDealt", 0),
        participant.get("totalDamageDealtToChampions", 0),
        participant.get("totalDamageShieldedOnTeammates", 0),
        participant.get("totalDamageTaken", 0),
        participant.get("totalHeal", 0),
        participant.get("totalHealsOnTeammates", 0),
        participant.get("totalMinionsKilled", 0),
        participant.get("totalTimeCCDealt", 0),
        participant.get("totalTimeSpentDead", 0),
        participant.get("totalUnitsHealed", 0),
        participant.get("tripleKills", 0),
        participant.get("trueDamageDealt", 0),
        participant.get("trueDamageDealtToChampions", 0),
        participant.get("trueDamageTaken", 0),
        participant.get("turretKills", 0),
        participant.get("turretTakedowns", 0),
        participant.get("turretsLost", 0),
        participant.get("unrealKills", 0),
        participant.get("visionScore", 0),
        participant.get("visionWardsBoughtInGame", 0),
        participant.get("wardsKilled", 0),
        participant.get("wardsPlaced", 0),
        participant.get("win", False)
    ]
    writer.writerow(row)


if response.status_code == 200:
    summoner_data = response.json()
    puuid = summoner_data.get("puuid")

    # Make a request to retrieve the recent match IDs for the summoner
    match_ids_url = f"https://{match_region}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count=100&api_key={api_key}"
    match_ids = get_data(match_ids_url)

    if match_ids:
        csv_file = "champion_data.csv"

        with open(csv_file, "w", newline="") as file:
            writer = csv.writer(file)
            write_header(writer)

            for match_id in match_ids:
                try:
                    # Make a request to retrieve the match details
                    match_detail_url = f"https://{match_region}.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={api_key}"
                    match_data = get_data(match_detail_url)

                    if match_data:
                        participants = match_data.get("info", {}).get("participants", [])
                        for participant in participants:
                            write_data(writer, participant)
                except KeyError:
                    print(f"Skipping match {match_id} due to missing data")

        print(f"Champion data has been saved to {csv_file}")
    else:
        print(f"Failed to retrieve match IDs for summoner: {summoner_name}")
else:
    print(f"Failed to retrieve summoner data for summoner name: {summoner_name}")
