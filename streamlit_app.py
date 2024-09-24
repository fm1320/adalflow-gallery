import streamlit as st
import pandas as pd

# Set up page configuration
st.set_page_config(
    page_title="Adalflow Community App Gallery",
    page_icon="https://raw.githubusercontent.com/SylphAI-Inc/LightRAG/main/docs/source/_static/images/adalflow-logo.png",
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
st.image("https://raw.githubusercontent.com/SylphAI-Inc/LightRAG/main/docs/source/_static/images/adalflow-logo.png", width=300)
st.title("Adalflow Community App Gallery")

# Data for the apps with tags
apps = [
    {
        "name": "GPT Lab",
        "description": "Interactively explore data with GPT Lab, focusing on NYC Uber pickups.",
        "image": "images/GPTLab.png",
        "link": "https://gptlab.streamlit.app/",
        "repo": "https://github.com/dclin/gptlab-streamlit",
        "tags": ["#LLM", "#AI"]
    },
    {
        "name": "Ask my PDF",
        "description": "Explore data by uploading your PDFs and turning them into interactive dataframes.",
        "image": "images/AskMyPDF.png",
        "link": "https://ask-my-pdf.streamlit.app/",
        "repo": "https://github.com/mobarski/ask-my-pdf",
        "tags": ["#Data", "#Finance"]
    },
    {
        "name": "HugChat",
        "description": "Analyze live crypto data using the Binance API and visualizing trends.",
        "image": "images/HugChat.png",
        "link": "https://hugchat.streamlit.app/",
        "repo": "https://github.com/dataprofessor/hugchat",
        "tags": ["#Crypto", "#AI"]
    },
    {
        "name": "KnowledgeGPT",
        "description": "Explore knowledge bases interactively with KnowledgeGPT.",
        "image": "images/KnowledgeGPT.png",
        "link": "https://knowledgegpt.streamlit.app/",
        "repo": "https://github.com/mmz-001/knowledge_gpt",
        "tags": ["#NLP", "#Knowledge"]
    },
    {
        "name": "rephraise",
        "description": "Generate paraphrased emails and content using AI.",
        "image": "images/rephraise.png",
        "link": "https://stefanrmmr-gpt3-email-generator-streamlit-app-ku3fbq.streamlit.app/",
        "repo": "https://github.com/stefanrmmr/GPT_email_generator",
        "tags": ["#AI", "#Content"]
    },
    {
        "name": "GPT-4 Auto Coder",
        "description": "Automatically generate code with GPT-4 based on user input.",
        "image": "images/gpt-4-auto-coder.png",
        "link": "https://gpt4autocoder.streamlit.app/",
        "repo": "https://github.com/echohive42/gpt4_autocoder",
        "tags": ["#Coding", "#AI", "#Automation"]
    },
]

# Convert app data into a DataFrame for easy manipulation
apps_df = pd.DataFrame(apps)

# Get all unique tags
all_tags = sorted(set(tag for tags in apps_df['tags'] for tag in tags))

# Search bar for filtering apps by tags
selected_tags = st.multiselect("Search by Tags", options=all_tags)

# Filter apps based on selected tags
if selected_tags:
    filtered_apps = apps_df[apps_df['tags'].apply(lambda tags: any(tag in tags for tag in selected_tags))]
else:
    filtered_apps = apps_df

# Function to style tags as badges
def style_tags(tags):
    return " ".join([f"<span class='tag'>{tag}</span>" for tag in tags])

# Add custom CSS for tags
st.markdown(
    """
    <style>
    .tag {
        display: inline-block;
        background-color: #e0e0e0;
        border-radius: 12px;
        padding: 0.3em 0.6em;
        margin: 0.2em;
        font-size: 0.85em;
        color: #333;
        font-weight: 500;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display apps in a 2x2 grid
cols = st.columns(2)  # Create two columns

for index, app in filtered_apps.iterrows():
    col = cols[index % 2]  # Alternate columns for each app
    with col:
        st.image(app['image'], use_column_width=True)
        st.subheader(app['name'])
        st.write(app['description'])
        st.markdown(style_tags(app['tags']), unsafe_allow_html=True)
        st.markdown(f"[View App]({app['link']})")
        st.markdown(f"[View GitHub Repo]({app['repo']})")
        st.markdown("---")

# Message when no apps match the search term
if filtered_apps.empty:
    st.info("No apps found. Try selecting different tags.")
