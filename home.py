import streamlit as st
import pandas as pd
import plotly.express as px
import random
from datetime import datetime
import requests

# Simulated GPT sports assistant
SPORTS_FAKE_CHATBOT = {
    "who has the most world cup wins": "Brazil holds the record with 5 FIFA World Cup titles!",
    "who is the nba all time top scorer": "LeBron James is the NBA's all-time leading scorer.",
    "who has the most golf majors": "Jack Nicklaus holds the record with 18 major championships.",
    "who won the last super bowl": "The Kansas City Chiefs won Super Bowl LVIII."
}

def app():
    st.title("🏠 Welcome to the Sports Popularity Dashboard!")
    st.markdown("Explore iconic sports, stats, mini games, and live fun!")

    # Quick Stats
    st.subheader("📊 Quick Glance at Sports")
    cols = st.columns(4)
    stats = [
        ("⚽ Soccer", "4B Fans", 100),
        ("🏀 Basketball", "2.4B Fans", 60),
        ("🏈 Football", "400M Fans", 10),
        ("⛳ Golf", "450M Fans", 15),
    ]
    for col, (label, value, prog) in zip(cols, stats):
        with col:
            st.metric(label, value)
            st.progress(prog)

    st.divider()

    # Interesting Information Section
    st.subheader("📖 Did You Know These Cool Facts?")
    st.markdown("""
    - The FIFA World Cup trophy has been stolen twice in history.
    - Basketball games used to be played with a soccer ball.
    - The NFL Super Bowl is one of the most-watched events globally, with ads costing millions.
    - Tiger Woods made his first hole-in-one at just 8 years old.
    - The average soccer player runs about 7 miles per game!
    """)

    st.divider()

    # 🔁 Did You Know? Rotating Sports Facts
    st.subheader("🧠 Did You Know?")
    import time
    import itertools
    facts = itertools.cycle([
        "The World Cup is the most-watched sports event on Earth.",
        "Basketball was invented by a Canadian PE teacher in 1891.",
        "The Super Bowl costs over $6M per 30-second ad.",
        "Golf is the only sport played on the Moon.",
        "The Olympic Games date back to 776 BC.",
        "Michael Jordan was cut from his high school basketball team."
    ])
    if st.button("🔄 Show Me a Fun Fact"):
        st.info(next(facts))

    st.divider()

    # 📊 Fan Prediction Poll
    st.subheader("📣 Fan Prediction: Who Will Win the Next Major Event?")
    poll_question = "🏆 Which team will win the next championship?"
    teams = ["Argentina", "France", "Brazil"]
    vote = st.radio(poll_question, teams)

    if "votes" not in st.session_state:
        st.session_state.votes = {team: 0 for team in teams}

    if st.button("Vote!"):
        st.session_state.votes[vote] += 1
        st.success(f"Thanks for voting for {vote}!")

    poll_df = pd.DataFrame({
        "Team": list(st.session_state.votes.keys()),
        "Votes": list(st.session_state.votes.values())
    })
    st.bar_chart(poll_df.set_index("Team"))

    st.divider()

    # Fun Fact
    st.subheader("🌐 Random Fun Fact")
    st.info(random.choice([
        "The World Cup is the most-watched sports event on Earth.",
        "Basketball was invented by a Canadian PE teacher in 1891.",
        "The Super Bowl costs over $6M per 30-second ad.",
        "Golf is the only sport played on the Moon."
    ]))

    st.divider()

    # Mini Game 1: Trivia
    st.subheader("🎮 Trivia Time!")
    trivia = [
        {"q": "Most FIFA World Cups won?", "opts": ["Germany", "Brazil", "Argentina"], "a": "Brazil"},
        {"q": "NBA scoring leader all-time?", "opts": ["LeBron James", "Jordan", "Kareem"], "a": "LeBron James"},
        {"q": "Most golf majors?", "opts": ["Tiger", "Phil", "Jack Nicklaus"], "a": "Jack Nicklaus"}
    ]
    if "triv" not in st.session_state:
        st.session_state.triv = random.choice(trivia)
        st.session_state.triv_answered = False

    q = st.session_state.triv
    ans = st.radio(q["q"], q["opts"])
    if st.button("Submit Answer"):
        if ans == q["a"]:
            st.success("✅ Correct!")
        else:
            st.error(f"❌ Correct answer: {q['a']}")
        st.session_state.triv_answered = True

    if st.session_state.triv_answered and st.button("Next Question"):
        st.session_state.triv = random.choice(trivia)
        st.session_state.triv_answered = False

    st.divider()

    # Mini Game 2: Guess the Player
    st.subheader("🌟 Who's That Player?")
    players = [
        {"name": "Messi", "Goals": 820, "Assists": 350},
        {"name": "Ronaldo", "Goals": 860, "Assists": 270},
        {"name": "Mbappe", "Goals": 270, "Assists": 120},
        {"name": "Haaland", "Goals": 220, "Assists": 60},
    ]
    if "mystery" not in st.session_state:
        st.session_state.mystery = random.choice(players)
        st.session_state.played = False

    stats = st.session_state.mystery
    st.info(f"Goals: {stats['Goals']} | Assists: {stats['Assists']}")
    opts = [p["name"] for p in random.sample(players, k=3)]
    if stats["name"] not in opts:
        opts[random.randint(0, 2)] = stats["name"]
    guess = st.radio("Guess the player", opts, key="guess")
    if st.button("Submit Guess"):
        if guess == stats["name"]:
            st.success("✅ Correct!")
        else:
            st.error(f"❌ It was {stats['name']}")
        st.session_state.played = True

    if st.session_state.played and st.button("Play Again"):
        st.session_state.mystery = random.choice(players)
        st.session_state.played = False

    st.divider()

    # Mini Game 3: This or That
    st.subheader("🎯 This or That: Choose Your Favorite")
    choices = [
        ("Messi", "Ronaldo"),
        ("LeBron", "Jordan"),
        ("Brady", "Mahomes")
    ]
    matchup = random.choice(choices)
    vote = st.radio(f"{matchup[0]} or {matchup[1]}?", matchup)
    if st.button("Cast Vote"):
        st.success(f"You chose: {vote}!")

    st.divider()

    # New Interactive Section: Sports Emoji Memory Challenge
    st.subheader("🔎 Emoji Memory Match!")
    emoji_pairs = [
        ("⚽", "Soccer"),
        ("🏀", "Basketball"),
        ("🏈", "Football"),
        ("⛳", "Golf")
    ]
    random.shuffle(emoji_pairs)
    if "memory_choice" not in st.session_state:
        st.session_state.memory_choice = None

    col1, col2 = st.columns(2)
    for emoji, name in emoji_pairs:
        if col1.button(emoji):
            st.session_state.memory_choice = name
        if col2.button(name):
            if st.session_state.memory_choice == name:
                st.success(f"✅ Correct match: {name}!")
            else:
                st.error("❌ Nope, try again!")

    st.divider()

    # Suggestion Box
    st.subheader("📣 What Should We Add Next?")
    with st.form("suggestion_form", clear_on_submit=True):
        user_name = st.text_input("Your Name")
        suggestion = st.text_area("What features or games should we add?")
        submitted = st.form_submit_button("Send Suggestion")
        if submitted and user_name and suggestion:
            st.success(f"Thanks {user_name}! We appreciate your input.")

    st.success("Use the sidebar to explore other sports!")
