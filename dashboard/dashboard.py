import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def usersBehaviour(df, bywhat):
    users_behaviour = df.groupby(by=bywhat).cnt.sum().sort_values(ascending=False).reset_index()
    return users_behaviour

df = pd.read_csv("dashboard/main_data.csv")
df["dteday"] = pd.to_datetime(df["dteday"])

min_date = df["dteday"].min()
max_date = df["dteday"].max()

sns.set_theme(style='dark')

with st.sidebar:
    st.header("Ahmad Ghozali")
    start_date, end_date = st.date_input(
        label="Filter by Date", min_value=min_date, max_value=max_date, value=[min_date, max_date]
    )

df_filtered = df[(df["dteday"] >= pd.to_datetime(start_date)) & (df["dteday"] <= pd.to_datetime(end_date))]

st.header("Bike Sharing Dashboard 🚲")

st.subheader("Environment Info :cloud:")
env_col1, env_col2, env_col3 = st.columns(3)

with env_col1:
    temp = int(df_filtered["temp"].mean() * 41)
    st.metric("Average Temperature", value=f"{temp} °C")
with env_col2:
    hum = int(df_filtered["hum"].mean() * 100)
    st.metric("Average Humadity", value=f"{hum}%")
with env_col3:
    wind = int(df_filtered["windspeed"].mean() * 67)
    st.metric("Average Wind", value=f"{wind} mph")

st.subheader("Users Behaviour")
tab1, tab2, tab3 = st.tabs(["By Day", "By Weather", "By Season"])

with tab1:
    user_by_day = usersBehaviour(df_filtered, "weekdaytext")
    colors = ["#B7B7B7"] * len(user_by_day)
    colors[0] = '#379777'
    colors[len(colors)-1] = '#D91656'
    fig, ax = plt.subplots(nrows = 1, ncols = 1, figsize=(10,6))

    sns.barplot(x="weekdaytext", y="cnt", data=user_by_day, palette=colors)
    ax.set_xlabel("Day")
    ax.set_ylabel("Users Count")
    ax.set_title("Number of user by day")
    for index, value in enumerate(user_by_day["cnt"]):
        ax.text(
            index, value, str(value), color="black", ha="center", va="bottom"
        )
    st.pyplot(fig)
    
with tab2:
    user_by_weather = usersBehaviour(df_filtered, "weathertext")
    colors = ["#B7B7B7"] * len(user_by_weather)
    colors[0] = '#379777'
    colors[len(colors)-1] = '#D91656'
    fig, ax = plt.subplots(nrows = 1, ncols = 1, figsize=(10,6))
    weatherText = user_by_weather["weathertext"].unique().tolist()
    truncateText = [newText[:20-3]+"..." for newText in weatherText]

    sns.barplot(x="weathertext", y="cnt", data=user_by_weather, palette=colors)
    ax.set_xlabel("Weather")
    ax.set_ylabel("Users Count")
    ax.set_title("Number of user by weather")
    ax.set_xticklabels(truncateText, rotation=40)
    for index, value in enumerate(user_by_weather["cnt"]):
        ax.text(
            index, value, str(value), color="black", ha="center", va="bottom"
        )
    st.pyplot(fig)
    
with tab3:
    user_by_season = usersBehaviour(df_filtered, "seasontext")
    colors = ["#B7B7B7"] * len(user_by_season)
    colors[0] = '#379777'
    colors[len(colors)-1] = '#D91656'
    fig, ax = plt.subplots(nrows = 1, ncols = 1, figsize=(10,6))

    sns.barplot(x="seasontext", y="cnt", data=user_by_season, palette=colors)
    ax.set_xlabel("Season")
    ax.set_ylabel("Users Count")
    ax.set_title("Number of user by season")
    for index, value in enumerate(user_by_season["cnt"]):
        ax.text(
            index, value, str(value), color="black", ha="center", va="bottom"
        )
    st.pyplot(fig)


st.subheader(f"Bike Sharing Performance :fire:")

perf_col1, perf_col2, perf_col3 = st.columns(3)

perf_all = df_filtered.groupby(by="dteday").cnt.sum().reset_index()
perf_casual = df_filtered.groupby(by="dteday").casual.sum().reset_index()
perf_registered = df_filtered.groupby(by="dteday").registered.sum().reset_index()

with perf_col1:
    st.text(f"Total Users: {df_filtered['cnt'].sum()}")
with perf_col2:
    st.text(f"Casual Users: {df_filtered['casual'].sum()}")
with perf_col3:
    st.text(f"Registered Users: {df_filtered['registered'].sum()}")

fig2, ax2 = plt.subplots(nrows = 1, ncols = 1, figsize=(12,6))
sns.lineplot(data=perf_all, x=df_filtered["dteday"], y=df_filtered["cnt"], marker="o", ax=ax2, label="All Users (Casual & Registered)")
sns.lineplot(data=perf_casual, x=df_filtered["dteday"], y=df_filtered["casual"], marker="o", ax=ax2, label="Casual Users")
sns.lineplot(data=perf_registered, x=df_filtered["dteday"], y=df_filtered["registered"], marker="o", ax=ax2, label="Registered Users")
ax2.legend()
ax2.set_ylim(0)
ax2.set_xlabel("Date")
ax2.set_ylabel("User Count")
ax2.set_title(f"Bike Sharing Performance {start_date} - {end_date}")
ax2.set_xticklabels(df_filtered["dteday"].dt.strftime("%Y-%m-%d").unique().tolist(), rotation=40)
st.pyplot(fig2)

st.caption('Copyright (c) Ahmad Ghozali 2024')