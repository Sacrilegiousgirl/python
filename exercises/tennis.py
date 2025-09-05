import requests
import json

if __name__ == "__main__":
    url = "https://api.api-tennis.com/tennis/?method=get_livescore&tournament_key=1217&APIkey=5b2c880bb072d9b28c9a334adc17cb70541a828013390e07745dbf8cc4692da7"
    response = requests.get(url)

    if response.status_code == 200:
        player_data = response.json()
        # print(player_data)
        # Save into a JSON file
        with open("livescoresusopen.json", "w", encoding="utf-8") as f:
            json.dump(player_data, f, ensure_ascii=False, indent=4)

        print("Data saved to atp_standings.json")
    else:
        print("Failed")