import streamlit as st
import pandas as pd
import plotly.express as px

def app():
    st.title("🏀 Basketball Dashboard")
    st.write("Dive into the stats, legends, and legacy of the NBA and global basketball.")



    # 🌟 Intro
    st.subheader("🏀 Why Basketball Inspires Generations")
    st.markdown("""
    - Invented in 1891, now played in over **200 countries**.
    - The **NBA** is the top professional league, drawing millions of fans globally.
    - Legends like **Michael Jordan**, **LeBron James**, and **Kobe Bryant** shaped the modern game.
    """)

    # 📊 Top Players Stats
    st.subheader("🔥 Top NBA Players - Career Points")

    players_data = {
        "Player": ["LeBron James", "Kevin Durant", "Stephen Curry", "Giannis Antetokounmpo", "Nikola Jokic", "Luka Doncic", "Joel Embiid"],
        "Points": [39000, 27000, 26000, 16000, 14000, 12000, 13000],
        "Assists": [10600, 4200, 5600, 3500, 4100, 3400, 2900],
        "Games": [1500, 1000, 950, 750, 700, 500, 550],
        "Team": ["Lakers", "Suns", "Warriors", "Bucks", "Nuggets", "Mavericks", "76ers"]
    }
    df = pd.DataFrame(players_data)

    fig_points = px.bar(df, x="Player", y="Points", color="Team", title="Top NBA Players - Total Career Points")
    st.plotly_chart(fig_points, use_container_width=True)

    # 📈 Assists vs Points
    st.subheader("🎯 Assists vs Points")
    fig_assists = px.scatter(
        df,
        x="Assists",
        y="Points",
        text="Player",
        color="Team",
        size="Games",
        title="NBA Players - Assists vs Points (Bubble = Games Played)"
    )
    st.plotly_chart(fig_assists, use_container_width=True)

    # 📚 Famous Moments
    st.subheader("📚 Legendary Basketball Moments")
    st.markdown("""
    - 🐐 **Michael Jordan's Flu Game** – 1997 NBA Finals, Game 5.
    - 🏆 **LeBron's Block** – 2016 Finals Game 7, a title for Cleveland.
    - 🎯 **Steph Curry's 3-Point Revolution** – changed basketball forever.
    """)

    # 🗳️ Fan Poll
    st.subheader("🗳️ What's Your Favorite Part of the Game?")
    threes = st.checkbox("3-Point Shooting")
    dunks = st.checkbox("Slam Dunks")
    buzzer = st.checkbox("Buzzer Beaters")
    defense = st.checkbox("Lockdown Defense")
    picks = [opt for opt, sel in [
        ("3-Point Shooting", threes),
        ("Dunks", dunks),
        ("Buzzer Beaters", buzzer),
        ("Defense", defense)
    ] if sel]
    if picks:
        st.info(f"You love: {', '.join(picks)}")

    # 💬 Quote
    st.subheader("💬 From the Court")
    st.write("> “Some people want it to happen, some wish it would happen, others make it happen.” — Michael Jordan")

    # 🔁 Player Comparison Tool
    st.markdown("---")
    st.subheader("🆚 Compare Basketball Players")

    compare_players = {
        "LeBron James": {
            "Points": 39000, "Assists": 10600, "Games": 1500,
            "Image": "https://upload.wikimedia.org/wikipedia/commons/2/2f/LeBron_James_Lakers.jpg"
        },
        "Stephen Curry": {
            "Points": 26000, "Assists": 5600, "Games": 950,
            "Image": "https://upload.wikimedia.org/wikipedia/commons/8/81/Stephen_Curry_Warriors_2017.jpg"
        },
        "Kevin Durant": {
            "Points": 27000, "Assists": 4200, "Games": 1000,
            "Image": "https://upload.wikimedia.org/wikipedia/commons/9/94/Kevin_Durant_2019.jpg"
        },
        "Giannis Antetokounmpo": {
            "Points": 16000, "Assists": 3500, "Games": 750,
            "Image": "https://upload.wikimedia.org/wikipedia/commons/d/de/Giannis_Antetokounmpo_2021.jpg"
        },
        "Nikola Jokic": {
            "Points": 14000, "Assists": 4100, "Games": 700,
            "Image": "https://upload.wikimedia.org/wikipedia/commons/e/e1/Nikola_Jokic_Nuggets.jpg"
        }
    }

    player_names = list(compare_players.keys())

    col1, col2 = st.columns(2)
    with col1:
        player1 = st.selectbox("Choose Player 1", player_names, index=0)
    with col2:
        player2 = st.selectbox("Choose Player 2", player_names, index=1)

    p1 = compare_players[player1]
    p2 = compare_players[player2]

    col1, col2 = st.columns(2)
    with col1:
        st.image(p1["Image"], caption=player1, use_container_width=True)
        st.metric("Points", p1["Points"])
        st.metric("Assists", p1["Assists"])
        st.metric("Games", p1["Games"])

    with col2:
        st.image(p2["Image"], caption=player2, use_container_width=True)
        st.metric("Points", p2["Points"])
        st.metric("Assists", p2["Assists"])
        st.metric("Games", p2["Games"])

    comparison_df = pd.DataFrame({
        "Stat": ["Points", "Assists", "Games"],
        player1: [p1["Points"], p1["Assists"], p1["Games"]],
        player2: [p2["Points"], p2["Assists"], p2["Games"]]
    })

    st.subheader("📊 Stat Comparison Chart")
    st.bar_chart(comparison_df.set_index("Stat"))

    st.success("Use the sidebar to explore other sports!")
