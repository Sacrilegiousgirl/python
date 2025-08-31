import requests

url = "https://api.api-tennis.com/tennis/?method=get_players&player_key=137&APIkey=!_your_account_APIkey_!"

def get_player_info(player):
    response = requests.get(url)

    if response.status_code == 200:
        player_data = response.json()
        return player_data
    else:
        print(f"Failed to retrieve data {response.status_code}")


player = input("Type the name of the player (last name only): ")
player_info = get_player_info(player)

print(player_info)

# if player_info:
#     print("Name:", player_info["player_name"])
#     print("Coutry:", player_info["player_country"])
#     print("Birthday: ", player_info["player_bday"])
#     print("Stats:", player_info["player_stats"])