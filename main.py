import json


def main():
    try:
        # Open the following file
        with open("/Applications/InstagramFollowers/InstagramFollowersDiff/following.json", "r") as file:
            data = json.load(file)

        # Extract all values
        valuesFollowing = set()
        for item in data["relationships_following"]:
            for string_data in item["string_list_data"]:
                valuesFollowing.add(string_data["value"])

        # Open the followers file
        with open("/Applications/InstagramFollowers/InstagramFollowersDiff/followers_1.json", "r") as file:
            dataFollowers = json.load(file)
        
        valuesFollowers = set()
        for item in dataFollowers:
            for string_data in item["string_list_data"]:
                myId = string_data["value"]
                valuesFollowers.add(myId)
        
        valuesNotFollowing = set()
        for myValue in valuesFollowing:
            if myValue not in valuesFollowers:
                valuesNotFollowing.add(myValue)

            # Write values to file
        with open("output.txt", "w") as file:
            file.write("Following Length: " + str(len(valuesFollowing)) + "\n")
            file.write("Followers Length: " + str(len(valuesFollowers)) + "\n")
            file.write("=====================================" + "\n\n")
            for value in valuesNotFollowing:
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