import json

def parse_followers_json(file: str):
    with open(file, "r") as file:
        content = json.load(file)
    
    data = set()
    for item in content["relationships_following"]:
        for string_data in item["string_list_data"]: 
            info = string_data["value"]
            data.add(info)

    return data

def parse_following_json(file: str):
    with open(file, "r") as file:
        content = json.load(file)
    
    data = set()
    for item in content:
        for string_data in item["string_list_data"]: 
            info = string_data["value"]
            data.add(info)

    return data

def main():
    try:
        following = parse_followers_json("following.json")
        
        followers = parse_following_json("followers_1.json")
        
        notFollowing = following.difference(followers)

        # Write values to file
        with open("output.txt", "w") as file:
            file.write("Following Length: " + str(len(following)) + "\n")
            file.write("Followers Length: " + str(len(followers)) + "\n")
            file.write("=====================================" + "\n\n")
            for value in notFollowing:
                file.write(value + "\n")

        print("Values written to 'output.txt'.")

    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
    except IndexError:
        print("Error: No value found in 'string_list_data'.")
    except KeyError as e:
        print(f"Error: Key not found - {e}")
    except Exception as e:
        print(f"Error: An unexpected error occurred - {e}")

main()