import streamlit as st
import pandas as pd
import re

# Set up page configuration
st.set_page_config(
    page_title="Community App Gallery",
    page_icon="https://streamlit.io/favicon.svg",
)

# Navbar function
def navbar():
    st.markdown(
        """
        <style>
            .topnav-container {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 3.5rem;
                border-bottom: 1px solid rgba(38, 39, 48, 0.2);
                background-color: white;
                z-index: 98;
                line-height: 3.5rem;
                display: flex;
                justify-content: center;
                align-items: center;
            }
            
            .topnav a {
                color: rgb(38, 39, 48);
                text-align: center;
                text-decoration: none;
            }

            .topnav a:hover {
                color: #e24768;
            }
        </style>

        <div class="topnav-container">
            <nav class="topnav">
                <a href="https://streamlit.io/gallery">View all apps</a>
            </nav>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Navbar call
navbar()

# Set up the title and introductory image
st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=100)
st.title("Community App Gallery")

# Data for the apps
apps = [
    {
        "name": "GPT Lab",
        "description": "Interactively explore data with GPT Lab, focusing on NYC Uber pickups.",
        "image": "images/GPTLab.png",
        "link": "https://gptlab.streamlit.app/",
        "repo": "https://github.com/dclin/gptlab-streamlit"
    },
    {
        "name": "Ask my PDF",
        "description": "Explore data by uploading your PDFs and turning them into interactive dataframes.",
        "image": "images/AskMyPDF.png",
        "link": "https://ask-my-pdf.streamlit.app/",
        "repo": "https://github.com/mobarski/ask-my-pdf"
    },
    {
        "name": "HugChat",
        "description": "Analyze live crypto data using the Binance API and visualizing trends.",
        "image": "images/HugChat.png",
        "link": "https://hugchat.streamlit.app/",
        "repo": "https://github.com/dataprofessor/hugchat"
    },
    {
        "name": "KnowledgeGPT",
        "description": "Explore knowledge bases interactively with KnowledgeGPT.",
        "image": "images/KnowledgeGPT.png",
        "link": "https://knowledgegpt.streamlit.app/",
        "repo": "https://github.com/mmz-001/knowledge_gpt"
    },
    {
        "name": "rephraise",
        "description": "Generate paraphrased emails and content using AI.",
        "image": "images/rephrase.png",
        "link": "https://stefanrmmr-gpt3-email-generator-streamlit-app-ku3fbq.streamlit.app/",
        "repo": "https://github.com/stefanrmmr/GPT_email_generator"
    },
    {
        "name": "GPT-4 Auto Coder",
        "description": "Automatically generate code with GPT-4 based on user input.",
        "image": "images/gpt-4-auto-coder.png",
        "link": "https://gpt4autocoder.streamlit.app/",
        "repo": "https://github.com/echohive42/gpt4_autocoder"
    },
]

# Convert app data into a DataFrame for easy manipulation
apps_df = pd.DataFrame(apps)

# Search bar for filtering apps
search_term = st.text_input("Search Apps", "").lower()

# Highlight matching terms in the descriptions
def highlight_keywords(text, keywords):
    """
    Highlights keywords in the text. Returns highlighted snippets around the keywords.
    """
    pattern = '|'.join(re.escape(word) for word in keywords)
    matches = re.finditer(pattern, text, re.IGNORECASE)
    snippets = []

    for match in matches:
        start, end = match.span()
        snippet = text[max(0, start - 30):min(len(text), end + 30)]
        highlighted = re.sub(pattern, lambda m: f"<mark>{m.group(0)}</mark>", snippet, flags=re.IGNORECASE)
        snippets.append(highlighted)

    return '... '.join(snippets)

# Filter apps based on search input
filtered_apps = apps_df[
    apps_df['name'].str.contains(search_term) | 
    apps_df['description'].str.contains(search_term)
] if search_term else apps_df

# Display apps in a 2x2 grid
cols = st.columns(2)  # Create two columns

for index, app in filtered_apps.iterrows():
    col = cols[index % 2]  # Alternate columns for each app
    with col:
        st.image(app['image'], use_column_width=True)
        st.subheader(app['name'])
        if search_term:
            highlighted_description = highlight_keywords(app['description'], search_term.split())
            st.markdown(f"<p>{highlighted_description}</p>", unsafe_allow_html=True)
        else:
            st.write(app['description'])
        st.markdown(f"[View App]({app['link']})")
        st.markdown(f"[View GitHub Repo]({app['repo']})")
        st.markdown("---")

# Message when no apps match the search term
if filtered_apps.empty:
    st.info("No apps found. Try searching with different keywords.")
