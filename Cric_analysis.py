import xml.etree.ElementTree as ET
import streamlit as st

def search_player():
    # Load the XML file
    tree = ET.parse('cricket_stats.xml')
    root = tree.getroot()

    # Get the player name from the search entry
    search_name = st.text_input("Search Player")

    if st.button("Search"):
        if search_name:
            # Search for the player element with the given name
            player_found = False
            for player in root.findall('player'):
                name = player.find('name').text
                if name.lower() == search_name.lower():
                    player_found = True

                    # Display the player information
                    batting_elem = player.find('batting')
                    matches = batting_elem.find('matches').text
                    innings = batting_elem.find('innings').text
                    runs = batting_elem.find('runs').text
                    average = batting_elem.find('average').text
                    strike_rate = batting_elem.find('strikeRate').text

                    st.write("Player: {}".format(name))
                    st.write("Matches: {}".format(matches))
                    st.write("Innings: {}".format(innings))
                    st.write("Runs: {}".format(runs))
                    st.write("Average: {}".format(average))
                    st.write("Strike Rate: {}".format(strike_rate))

                    break

            if not player_found:
                st.write("Player not found.")
        else:
            st.write("Please enter a player name.")


def add_player():
    # Create input fields for player information
    add_name = st.text_input("Name")
    add_matches = st.text_input("Batting Matches")
    add_innings = st.text_input("Batting Innings")
    add_runs = st.text_input("Batting Runs")
    add_average = st.text_input("Batting Average")
    add_strike_rate = st.text_input("Batting Strike Rate")

    # Create a button to save the player information
    if st.button("Save"):
        # Create player element
        player_elem = ET.Element('player')

        # Create name element
        name_elem = ET.SubElement(player_elem, 'name')
        name_elem.text = add_name

        # Create batting element
        batting_elem = ET.SubElement(player_elem, 'batting')

        # Create matches element
        matches_elem = ET.SubElement(batting_elem, 'matches')
        matches_elem.text = add_matches

        # Create innings element
        innings_elem = ET.SubElement(batting_elem, 'innings')
        innings_elem.text = add_innings

        # Create runs element
        runs_elem = ET.SubElement(batting_elem, 'runs')
        runs_elem.text = add_runs

        # Create average element
        average_elem = ET.SubElement(batting_elem, 'average')
        average_elem.text = add_average

        # Create strikeRate element
        strike_rate_elem = ET.SubElement(batting_elem, 'strikeRate')
        strike_rate_elem.text = add_strike_rate

        # Load the XML file
        tree = ET.parse('cricket_stats.xml')
        root = tree.getroot()

        # Append player element to the root
        root.append(player_elem)

        # Save changes to the XML file
        tree.write('cricket_stats.xml')

        # Display success message
        st.success("Player '{}' added.".format(add_name))

def delete_player():
    # Create input field for player name
    delete_name = st.text_input("Name")

    # Create a button to confirm deletion
    if st.button("Confirm"):
        # Load the XML file
        tree = ET.parse('cricket_stats.xml')
        root = tree.getroot()

        # Search for the player element with the given name
        player_elem = None
        for player in root.findall('player'):
            name = player.find('name').text
            if name.lower() == delete_name.lower():
                player_elem = player
                break

        if player_elem is not None:
            # Remove the player element from the root
            root.remove(player_elem)

            # Save changes to the XML file
            tree.write('cricket_stats.xml')

            # Display success message
            st.success("Player '{}' deleted.".format(delete_name))
        else:
            # Display error message
            st.error("Player not found.")

def main():
    st.title("Cricket Player Statistics Analyzer")

    # Create a sidebar menu
    menu_selection = st.sidebar.radio("Menu", ["Search Player", "Add Player", "Delete Player"])

    if menu_selection == "Search Player":
        search_player()
    elif menu_selection == "Add Player":
        add_player()
    elif menu_selection == "Delete Player":
        delete_player()

if __name__ == '__main__':
    main()
