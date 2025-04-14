# Streamlit Overview
Streamlit is a powerful and user-friendly framework for building interactive data dashboards. It offers a wide range of widgets and has strong community support with numerous packages available to enhance formatting and functionality.

## Event Loop Behavior
New users might find Streamlit's event loop model unintuitive at first. The app is reactive — it re-executes the entire script from top to bottom on every user interaction (e.g., clicks, keystrokes, widget updates). This re-evaluation can make maintaining state across interactions tricky, especially when persistent connections or incremental data updates are involved.

In my experience, I've often needed to create auxiliary scripts to handle startup data and use well-structured data containers to maintain a clear and consistent program state across runs.

## Widgets and State Handling
Widgets are Streamlit's primary method for collecting user input. However, their values are not immediately available outside the rerun context. Due to the reactive nature of the event loop, all local variables reset on each interaction, and widget values are only updated when their respective lines of code are executed again.

To maintain data across runs, it is recommended to store values in st.session_state, which allows you to persist data for the duration of the user's session.

## Session State
st.session_state is where per-user data lives. It persists across reruns within the same browser session but is reset if the page is hard-refreshed (e.g., with F5) or if the script is restarted. It’s ideal for tracking user interactions and preserving temporary data throughout the session lifecycle.

## Server State
For shared state across multiple clients, the [streamlit-server-state](https://github.com/whitphx/streamlit-server-state) package provides server_state. Unlike session_state, which is unique to each user, server_state is accessible by all connected clients. This is especially useful for caching large, shared datasets that rarely change but need to remain accessible to everyone.

From experience, it's best to manage shared resources (like datasets or file structure reports) in separate background threads to avoid blocking the main app thread. Ensure that these threads are started within a context manager and include proper cleanup logic to handle termination safely and gracefully.

## Displaying Data
Streamlit applications can become noticeably slow when loading large datasets, especially if the data is reloaded into memory on every page interaction. One major inefficiency stems from re-downloading or reloading the dataset each time the script reruns — a direct consequence of Streamlit's reactive event loop.

To mitigate this, it's recommended to cache the dataset using `st.session_state`. By loading the data once and storing it in the session state, you can avoid redundant I/O operations and significantly improve performance. This approach ensures the data remains available throughout the user's session, without needing to be reloaded unless explicitly refreshed.

Streamlit also provides built-in caching mechanisms such as `@st.cache_data` and `@st.cache_resource`, which can persist data and resources across reruns and sessions. However, in my experience, I prefer to manage state explicitly through `session_state` to avoid relying on hidden functionality and to maintain clearer control over when and how data is loaded or refreshed.

```
if not "df" in st.session_state:
    df = st.session_state['df'] = pd.read_csv("../data/stock_details_5_years.csv")
else:
    df = st.session_state['df']
...
```

## Recommendation
* Use Streamlit for:
    * MVP dashboards
    * Internal tools
    * One-off data visualizations
* Can be used for:
    * User feedback
    * Data manipulation
    * Live metrics
