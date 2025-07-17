import streamlit as st
import pandas as pd
import plotly.express as px

def app():
    st.title("⛳ Golf Dashboard")
    st.write("Explore the legends, numbers, and history of the world’s most precise sport.")

   

    # 🌟 Intro
    st.subheader("🏌️ Why Golf Captures Precision & Patience")
    st.markdown("""
    - Originating in Scotland, golf is played in over **200 countries** today.
    - Major tournaments like **The Masters**, **U.S. Open**, **The Open Championship**, and **PGA Championship** define careers.
    - Known for **discipline, strategy**, and **longevity** — many golfers stay competitive well into their 40s and 50s.
    """)

    # 📊 Top Golfers Stats
    st.subheader("🏆 Top Golfers - Career Achievements")

    golf_data = {
        "Golfer": ["Tiger Woods", "Jack Nicklaus", "Rory McIlroy", "Phil Mickelson", "Jordan Spieth", "Dustin Johnson", "Brooks Koepka"],
        "Majors": [15, 18, 4, 6, 3, 2, 5],
        "Career Wins": [82, 73, 37, 45, 16, 28, 19],
        "Earnings (M$)": [121, 74, 70, 95, 53, 75, 48]
    }
    df = pd.DataFrame(golf_data)

    fig_wins = px.bar(df, x="Golfer", y="Career Wins", color="Golfer", title="PGA Career Wins")
    st.plotly_chart(fig_wins, use_container_width=True)

    st.subheader("💰 Earnings vs Major Wins")
    fig_majors = px.scatter(
        df,
        x="Majors",
        y="Earnings (M$)",
        text="Golfer",
        size="Career Wins",
        color="Golfer",
        title="Major Titles vs Career Earnings"
    )
    st.plotly_chart(fig_majors, use_container_width=True)

    # 📚 Iconic Moments
    st.subheader("📚 Iconic Golf Moments")
    st.markdown("""
    - 🐅 **Tiger’s Chip-in at Augusta (2005)** — one of the most famous shots in Masters history.
    - 🏌️ **Jack Nicklaus' 1986 Masters Win** at age 46 — the oldest major winner ever.
    - 🌊 **Phil Mickelson’s bunker shot** at the 2010 Masters — pure magic.
    """)

    # 🗳️ Fan Poll
    st.subheader("🗳️ What’s Your Favorite Golf Element?")
    driving = st.checkbox("Driving off the tee")
    putting = st.checkbox("Clutch putting")
    trick = st.checkbox("Creative shots")
    quiet = st.checkbox("Calm & concentration")
    picks = [opt for opt, sel in [
        ("Driving", driving),
        ("Putting", putting),
        ("Trick Shots", trick),
        ("Focus", quiet)
    ] if sel]
    if picks:
        st.info(f"You love: {', '.join(picks)}")

    # 💬 Quote
    st.subheader("💬 From the Fairway")
    st.write("> “Success in golf depends less on strength of body than upon strength of mind and character.” — Arnold Palmer")

    # 🆚 Golfer Comparison Tool
    st.markdown("---")
    st.subheader("🆚 Compare Professional Golfers")

    compare_golfers = {
        "Tiger Woods": {
            "Majors": 15, "Career Wins": 82, "Earnings": 121,
            "Image": "https://upload.wikimedia.org/wikipedia/commons/2/2f/Tiger_Woods_at_2018_US_Open.jpg"
        },
        "Jack Nicklaus": {
            "Majors": 18, "Career Wins": 73, "Earnings": 74,
            "Image": "https://upload.wikimedia.org/wikipedia/commons/7/79/Jack_Nicklaus_2006.jpg"
        },
        "Phil Mickelson": {
            "Majors": 6, "Career Wins": 45, "Earnings": 95,
            "Image": "https://upload.wikimedia.org/wikipedia/commons/4/4d/Phil_Mickelson_in_2013.jpg"
        },
        "Rory McIlroy": {
            "Majors": 4, "Career Wins": 37, "Earnings": 70,
            "Image": "https://upload.wikimedia.org/wikipedia/commons/e/ef/Rory_McIlroy_2013.jpg"
        },
        "Jordan Spieth": {
            "Majors": 3, "Career Wins": 16, "Earnings": 53,
            "Image": "https://upload.wikimedia.org/wikipedia/commons/5/57/Jordan_Spieth_2016.jpg"
        }
    }

    names = list(compare_golfers.keys())

    col1, col2 = st.columns(2)
    with col1:
        g1 = st.selectbox("Choose Golfer 1", names, index=0)
    with col2:
        g2 = st.selectbox("Choose Golfer 2", names, index=1)

    d1 = compare_golfers[g1]
    d2 = compare_golfers[g2]

    col1, col2 = st.columns(2)
    with col1:
        st.image(d1["Image"], caption=g1, use_container_width=True)
        st.metric("Majors", d1["Majors"])
        st.metric("Career Wins", d1["Career Wins"])
        st.metric("Earnings (M$)", d1["Earnings"])

    with col2:
        st.image(d2["Image"], caption=g2, use_container_width=True)
        st.metric("Majors", d2["Majors"])
        st.metric("Career Wins", d2["Career Wins"])
        st.metric("Earnings (M$)", d2["Earnings"])

    comparison_df = pd.DataFrame({
        "Stat": ["Majors", "Career Wins", "Earnings (M$)"],
        g1: [d1["Majors"], d1["Career Wins"], d1["Earnings"]],
        g2: [d2["Majors"], d2["Career Wins"], d2["Earnings"]]
    })

    st.subheader("📊 Golfer Stat Comparison Chart")
    st.bar_chart(comparison_df.set_index("Stat"))

    st.success("Use the sidebar to explore more sports!")
