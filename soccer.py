import streamlit as st
import pandas as pd
import plotly.express as px

def app():
    st.title("⚽ Soccer Dashboard")
    st.write("Explore stories, live data, and top player stats from global football!")


    # 🌍 Why Soccer
    st.subheader("🌍 Why Soccer Captivates the World")
    st.markdown("""
    - **250+ million players** and **4 billion fans** globally — nearly half the planet!
    - A **90‑minute match**: simple rules, complex emotions.
    - Major events like the **FIFA World Cup** bring nations together every four years.
    """)

    # 🏆 World Cup Titles
    st.subheader("🏆 World Cup Titles by Country")
    wc_data = {
        "Country": ["Brazil", "Germany", "Italy", "Argentina", "France", "Uruguay", "England", "Spain"],
        "Titles": [5, 4, 4, 3, 2, 2, 1, 1]
    }
    wc_df = pd.DataFrame(wc_data)
    selected = st.multiselect("Choose countries to compare:", wc_df["Country"], default=["Brazil", "Germany", "Argentina"])
    filtered = wc_df[wc_df["Country"].isin(selected)]
    fig_wc = px.bar(filtered, x="Country", y="Titles", color="Country", title="FIFA World Cup Titles")
    st.plotly_chart(fig_wc, use_container_width=True)

    # 📚 Historic Moments
    st.subheader("🏆 Historic Moments That Defined Soccer")
    st.markdown("""
    1. **1966 – Wimbledon Echoes**: England’s iconic World Cup victory at home.  
    2. **1970 – Pele’s Brilliance**: Brazil’s stellar tournament in Mexico.  
    3. **1986 – Hand of God & Maradona’s Magic**: Glory and controversy in Mexico.  
    4. **2005 – Istanbul Night**: Liverpool's unbelievable comeback in the Champions League.  
    5. **2014 – Brazil vs Germany**: Shock 7–1 semi-final that stunned the world.
    """)

    # 📢 Fan Story
    st.subheader("📢 Share Your Soccer Moment")
    user_story = st.text_area("Tell us about your favorite soccer memory")
    if st.button("Share Moment"):
        if user_story.strip():
            st.success("Thanks for sharing 🎉")
            st.write("Your moment:", user_story)
        else:
            st.warning("Write something first!")

    # 🗳️ Fan Poll
    st.subheader("🗳️ Fan Poll: How Do You Prefer to Watch Soccer?")
    options = {
        "Streaming live online": st.checkbox("Streaming live online"),
        "In a stadium": st.checkbox("In a stadium"),
        "At a sports bar": st.checkbox("At a sports bar"),
        "With family/friends at home": st.checkbox("With family/friends at home")
    }
    picks = [opt for opt, sel in options.items() if sel]
    if picks:
        st.info(f"You love watching via: {', '.join(picks)}")

    # 💬 Quote
    st.subheader("💬 Legendary Fans Know:")
    st.write("> “Some people think football is a matter of life and death. I assure you, it's much more serious than that.” — Bill Shankly")

    # 📊 Top Players Stats
    st.subheader("🥅 Top Soccer Players Stats")
    players_data = {
        "Player": ["Lionel Messi", "Cristiano Ronaldo", "Kylian Mbappé", "Erling Haaland", "Neymar Jr", "Mohamed Salah", "Kevin De Bruyne"],
        "Goals": [821, 873, 300, 270, 450, 270, 130],
        "Assists": [360, 240, 100, 80, 250, 150, 220],
        "Matches": [1050, 1200, 400, 320, 600, 500, 550],
        "Club": ["Inter Miami", "Al Nassr", "PSG", "Man City", "Al Hilal", "Liverpool", "Man City"]
    }
    df_players = pd.DataFrame(players_data)

    fig_goals = px.bar(
        df_players,
        x="Player",
        y="Goals",
        color="Club",
        title="Top Soccer Players - Total Goals"
    )
    st.plotly_chart(fig_goals, use_container_width=True)

    st.subheader("🎯 Player Comparison: Goals vs Assists")
    fig_assists = px.scatter(
        df_players,
        x="Assists",
        y="Goals",
        text="Player",
        color="Club",
        size="Matches",
        title="Assists vs Goals (Bubble Size = Matches Played)"
    )
    st.plotly_chart(fig_assists, use_container_width=True)

    # 🔁 Player Comparison Tool
    st.markdown("---")
    st.subheader("🆚 Compare Soccer Players")

    compare_players = {
        "Lionel Messi": {"Goals": 821, "Assists": 360, "Matches": 1050, "Image": "https://upload.wikimedia.org/wikipedia/commons/8/89/Leo_Messi_vs_Nigeria_2018.jpg"},
        "Cristiano Ronaldo": {"Goals": 873, "Assists": 240, "Matches": 1200, "Image": "https://upload.wikimedia.org/wikipedia/commons/8/8c/Cristiano_Ronaldo_2018.jpg"},
        "Neymar Jr": {"Goals": 450, "Assists": 250, "Matches": 600, "Image": "https://upload.wikimedia.org/wikipedia/commons/f/f6/Neymar_in_2018.jpg"},
        "Kylian Mbappé": {"Goals": 300, "Assists": 100, "Matches": 400, "Image": "https://upload.wikimedia.org/wikipedia/commons/7/75/Kylian_Mbappe_2019.jpg"},
        "Erling Haaland": {"Goals": 270, "Assists": 80, "Matches": 320, "Image": "https://upload.wikimedia.org/wikipedia/commons/5/57/Erling_Haaland_2022.jpg"}
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
        st.metric("Goals", p1["Goals"])
        st.metric("Assists", p1["Assists"])
        st.metric("Matches", p1["Matches"])

    with col2:
        st.image(p2["Image"], caption=player2, use_container_width=True)
        st.metric("Goals", p2["Goals"])
        st.metric("Assists", p2["Assists"])
        st.metric("Matches", p2["Matches"])

    comparison_df = pd.DataFrame({
        "Stat": ["Goals", "Assists", "Matches"],
        player1: [p1["Goals"], p1["Assists"], p1["Matches"]],
        player2: [p2["Goals"], p2["Assists"], p2["Matches"]]
    })

    st.subheader("📊 Stat Comparison Chart")
    st.bar_chart(comparison_df.set_index("Stat"))

    st.success("Use the sidebar to explore more sports!")
