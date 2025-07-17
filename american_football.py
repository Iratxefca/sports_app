import streamlit as st
import pandas as pd
import plotly.express as px

def app():
    st.title("🏈 American Football Dashboard")
    st.write("Explore stats, legends, and unforgettable moments from the NFL and beyond.")



    # 🏟️ Intro
    st.subheader("🏟️ Why American Football Rules the Fall")
    st.markdown("""
    - The NFL is one of the most-watched leagues in the world, especially in the U.S.
    - Super Bowl Sunday is a cultural event, with over **100 million viewers** yearly.
    - Football blends power, precision, teamwork, and strategy like no other sport.
    """)

    # 📊 Player Stats
    st.subheader("🔥 Top NFL Quarterbacks - Career Stats")

    nfl_data = {
        "Player": ["Tom Brady", "Peyton Manning", "Drew Brees", "Aaron Rodgers", "Patrick Mahomes", "Josh Allen", "Lamar Jackson"],
        "Touchdowns": [649, 539, 571, 475, 192, 176, 125],
        "Passing Yards": [89000, 71940, 80558, 59855, 28000, 22000, 16000],
        "Games": [335, 266, 287, 231, 96, 86, 82],
        "Team": ["Retired", "Retired", "Retired", "Jets", "Chiefs", "Bills", "Ravens"]
    }
    df = pd.DataFrame(nfl_data)

    fig_td = px.bar(df, x="Player", y="Touchdowns", color="Team", title="Top QBs - Career Touchdowns")
    st.plotly_chart(fig_td, use_container_width=True)

    st.subheader("🎯 Passing Yards vs Touchdowns")
    fig_scatter = px.scatter(
        df,
        x="Passing Yards",
        y="Touchdowns",
        text="Player",
        color="Team",
        size="Games",
        title="Career Passing Yards vs TDs (Bubble = Games Played)"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

    # 📚 Legendary Moments
    st.subheader("📚 NFL History-Making Moments")
    st.markdown("""
    - 🐐 **Brady's 28–3 Comeback** – Super Bowl LI, Patriots vs Falcons.
    - 💥 **David Tyree's Helmet Catch** – Super Bowl XLII, Giants vs Patriots.
    - 🧊 **The Ice Bowl (1967)** – Packers vs Cowboys, in -15°F weather.
    """)

    # 🗳️ Fan Poll
    st.subheader("🗳️ What Makes Football Awesome?")
    hits = st.checkbox("Big Hits")
    plays = st.checkbox("Insane Trick Plays")
    comebacks = st.checkbox("Epic Comebacks")
    tactics = st.checkbox("Smart Coaching")
    fans = [opt for opt, sel in [
        ("Big Hits", hits),
        ("Trick Plays", plays),
        ("Comebacks", comebacks),
        ("Coaching", tactics)
    ] if sel]
    if fans:
        st.info(f"You love: {', '.join(fans)}")

    # 💬 Quote
    st.subheader("💬 From the Locker Room")
    st.write("> “The difference between ordinary and extraordinary is that little extra.” — Jimmy Johnson")

    # 🆚 Player Comparison Tool
    st.markdown("---")
    st.subheader("🆚 Compare NFL Quarterbacks")

    compare_qbs = {
        "Tom Brady": {
            "Touchdowns": 649, "Yards": 89000, "Games": 335,
            "Image": "https://upload.wikimedia.org/wikipedia/commons/e/e8/Tom_Brady_2021.jpg"
        },
        "Peyton Manning": {
            "Touchdowns": 539, "Yards": 71940, "Games": 266,
            "Image": "https://upload.wikimedia.org/wikipedia/commons/1/14/Peyton_Manning_2012.jpg"
        },
        "Aaron Rodgers": {
            "Touchdowns": 475, "Yards": 59855, "Games": 231,
            "Image": "https://upload.wikimedia.org/wikipedia/commons/8/88/Aaron_Rodgers_2021.jpg"
        },
        "Patrick Mahomes": {
            "Touchdowns": 192, "Yards": 28000, "Games": 96,
            "Image": "https://upload.wikimedia.org/wikipedia/commons/d/d6/Patrick_Mahomes_Super_Bowl_LIV.jpg"
        },
        "Josh Allen": {
            "Touchdowns": 176, "Yards": 22000, "Games": 86,
            "Image": "https://upload.wikimedia.org/wikipedia/commons/7/75/Josh_Allen_2020.jpg"
        },
        "Lamar Jackson": {
            "Touchdowns": 125, "Yards": 16000, "Games": 82,
            "Image": "https://upload.wikimedia.org/wikipedia/commons/3/3d/Lamar_Jackson_2021.jpg"
        }
    }

    player_names = list(compare_qbs.keys())

    col1, col2 = st.columns(2)
    with col1:
        qb1 = st.selectbox("Choose QB 1", player_names, index=0)
    with col2:
        qb2 = st.selectbox("Choose QB 2", player_names, index=1)

    q1 = compare_qbs[qb1]
    q2 = compare_qbs[qb2]

    col1, col2 = st.columns(2)
    with col1:
        st.image(q1["Image"], caption=qb1, use_container_width=True)
        st.metric("Touchdowns", q1["Touchdowns"])
        st.metric("Yards", q1["Yards"])
        st.metric("Games", q1["Games"])

    with col2:
        st.image(q2["Image"], caption=qb2, use_container_width=True)
        st.metric("Touchdowns", q2["Touchdowns"])
        st.metric("Yards", q2["Yards"])
        st.metric("Games", q2["Games"])

    comparison_df = pd.DataFrame({
        "Stat": ["Touchdowns", "Yards", "Games"],
        qb1: [q1["Touchdowns"], q1["Yards"], q1["Games"]],
        qb2: [q2["Touchdowns"], q2["Yards"], q2["Games"]]
    })

    st.subheader("📊 Stat Comparison Chart")
    st.bar_chart(comparison_df.set_index("Stat"))

    st.success("Use the sidebar to explore more sports!")
