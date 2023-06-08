import streamlit as st
import webbrowser
import itertools
import ui

st.set_page_config(
    page_title="Snowflake Summit 2023 Demo Apps",
    page_icon="https://streamlit.io/favicon.svg",
)

def navbar():
    """Shows a sticky navigation bar with links to other apps at the top of the page."""
    st.write(
        """
        <style>
            /* Add a black background color to the top navigation */
            .topnav-container {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 3.5rem;
                border-bottom: 1px solid rgba(38, 39, 48, 0.2);
                /* padding-left: 60px; */
                /* padding-top: 0.5rem;
                padding-bottom: 0.5rem; */
                /* padding-right: 100px; */
                background-color: white;
                z-index: 98;
                
                line-height: 3.5rem;
                
                flex: 1 1 0%;
                
            }
            
            .topnav {
                overflow: hidden;
                /* position: relative;
                top: -50px; */
                padding-left: 1rem;
                padding-right: 1rem;
            
                max-width: 730px;
                margin: 0 auto;
                
                display: flex;
                /*justify-content: space-between;*/
                justify-content: center;
                align-items: center;
                
                vertical-align: middle;
            }
            
            /* Style the links inside the navigation bar */
            .topnav a {
                color: rgb(38, 39, 48);
                text-align: center;
                text-decoration: none;
                /* font-size: 17px; */
            }
            
            /* Change the color of links on hover */
            .topnav a:hover {
                color: #e24768;
            }
            
            /* Add a color to the active/current link */
            .topnav a.active {
                color: #e24768;
            }
            
            /*.topnav-right a {
                margin-left: 3rem;
            }*/
            
            .topnav-right {
                display: none;
            }
            
            @media screen and (max-width: 800px) {
                .topnav-right {
                    display: none;
                }
                
                .topnav {
                    justify-content: center;
                }
            }
            
            .topnav-title {
                margin-left: 1rem;
                font-weight: 500;
            }
        </style>
        
        <div class="topnav-container">
            <nav class="topnav">
                <div class="topnav-left">
                    <a href="https://share.streamlit.io/jrieke/st-frontpage/main">
                        <img src="https://streamlit.io/images/brand/streamlit-mark-color.png" width=35>
                        <span class="topnav-title">View all apps</span>
                    </a>
                </div>
                <div class="topnav-right">
                    <a href="https://share.streamlit.io/jrieke/st-frontpage/main">View all apps</a>
                    <a href="https://share.streamlit.io/" target="_blank"><img src="https://screenshots.imgix.net/mui-org/material-ui-icons/account-circle-outlined/~v=3.9.2/e6ffca0e-87fa-4e5b-92ca-05c6079b5f9e.png?ixlib=js-1.2.0&s=c0f87e872aac058178a34a41422a425d" width=35 style="border-radius: 100%; margin-left: 1rem;"></a>
                </div>
            </nav>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=100)
st.title("Snowflake Summit Demo Apps")

st.markdown(
    """
    <style>
        .screenshot {
            border: 1px solid rgba(38, 39, 48, 0.2);
            border-radius: 0.25rem;
        }
        
        h3 {
            padding-top: 1rem;
        }
        
        h3 a {
            color: var(--text-color) !important;
            text-decoration: none;
        }
        
        small a {
            color: var(--text-color) !important;
            text-decoration: none;
        }
        
        a:hover {
            text-decoration: none;
        }
    </style>
    
    <!-- Open links in new tabs by default. Required for Streamlit sharing to not open links within the iframe. -->
    <base target="_blank">
    """,
    unsafe_allow_html=True,
)

category_colors_cycle = itertools.cycle(
    [
        # ui.color("red-70"),
        ui.color("orange-70"),
        ui.color("light-blue-70"),
        ui.color("blue-green-70"),
        ui.color("blue-70"),
        ui.color("violet-70"),
        ui.color("red-70"),
        ui.color("green-70"),
    ]
)


def category(name, description=None):
    # if current_category_index != 0:
    # st.write("---")
    # st.write("")
    # pass
    # ui.colored_header(name, "rgba(38, 39, 48, 0.6)")
    ui.colored_header(name, next(category_colors_cycle), description)
    # st.header(name)
    st.write("")

    # current_category_index += 1

def app(name, description, image, link, repo_link):
    ui.linked_image(image, link)
    st.subheader(f"[{name}]({link})")
    st.caption(description)
#     st.caption(f"[{description}]({link})")
#     clone_code = "git clone {} ".format(repo_name)
#     st.code(clone_code, language="python")
#     repo_link = "https://github.com/streamlit/{0}/".format(repo_name)
    st.write(f"[View App]({link})")
    st.write("[View GitHub Repo](%s)" % repo_link)
    st.write("")

category("🗣️ Large Language Models")
col1, col2, col3 = st.columns(3)
with col1:
    app(
        "GPT Lab",
        "Make data apps to interactively explore data. In this case, check out NYC Uber pickups.",
        "images/GPTLab.png",
        "https://gptlab.streamlit.app/",
        "https://github.com/dclin/gptlab-streamlit",
    )
with col2:
    app(
        "Ask my PDF",
        "Explore data from a CSV by uploading the CSV and converting it into an interactive dataframe.",
        "images/AskMyPDF.png",
        "https://ask-my-pdf.streamlit.app/",
        "https://github.com/mobarski/ask-my-pdf",

    )
with col3:
    app(
        "HugChat",
        "Look at live data and compare trends. This app uses the Binance API to explore crypto data.",
        "images/HugChat.png",
        "https://hugchat.streamlit.app/",
        "https://github.com/dataprofessor/hugchat",
    )
    
col1, col2, col3 = st.columns(3)
with col1:
    app(
        "KnowledgeGPT",
        "Make data apps to interactively explore data. In this case, check out NYC Uber pickups.",
        "images/KnowledgeGPT.png",
        "https://knowledgegpt.streamlit.app/",
        "https://github.com/mmz-001/knowledge_gpt",
    )
with col2:
    app(
        "rephraise",
        "Explore data from a CSV by uploading the CSV and converting it into an interactive dataframe.",
        "images/rephraise.png",
        "https://stefanrmmr-gpt3-email-generator-streamlit-app-ku3fbq.streamlit.app/",
        "https://github.com/stefanrmmr/GPT_email_generator",

    )
with col3:
    app(
        "GPT-4 Auto Coder",
        "Look at live data and compare trends. This app uses the Binance API to explore crypto data.",
        "images/gpt-4-auto-coder.png",
        "https://gpt4autocoder.streamlit.app/",
        "https://github.com/echohive42/gpt4_autocoder",
    )

category("❄️ Snowflake Powered")
col1, col2, col3 = st.columns(3)
with col1:
    app(
        "Model Debugger",
        "Visualize your model to debug the output. This app uses Tensorflow and GAN to generate photorealistic images.",
        "images/ABTesting.png",
        "https://share.streamlit.io/streamlit/demo-face-gan/",
        "demo-face-gan",
    )
with col2:
    app(
        "ML Tools",
        "Create machine learning tools for others to use your models. This app generates images using the Deep Dream technique.",
        "images/ABTesting.png",
        "https://share.streamlit.io/streamlit/demo-deepdream/master",
        "demo-deepdream",
    )
with col3:
    app(
        "Data Browser",
        "Explore large datasets for input into ML models. This app displays self-driving car data and does real-time detection using YOLO.",
        "images/ABTesting.png",
        "https://share.streamlit.io/streamlit/demo-self-driving/master",
        "demo-self-driving",
    )

category("📊 Data Visualization")
col1, col2, col3 = st.columns(3)
with col1:
    app(
        "Info Sharing",
        "Share data or information with others. This app pulls Streamlit's roadmap via the Notion API.",
        "images/ABTesting.png",
        "https://share.streamlit.io/streamlit/roadmap",
        "roadmap",
    )
with col2:
    app(
        "A/B Testing",
        "Upload your experiment results to explore the statistical significance of an A/B test.",
        "images/ABTesting.png",
        "https://share.streamlit.io/streamlit/example-app-ab-testing/main",
        "example-app-ab-testing",
    )
    
category("🏆 Summit Hackathon Winners")
col1, col2, col3 = st.columns(3)
with col1:
    app(
        "Database Example",
        "Easily collect data from users and write to a database.",
        "images/ABTesting.png",
        "https://share.streamlit.io/streamlit/example-app-bug-report/main",
        "example-app-bug-report",
    )
with col2:
    app(
        "File Generation",
        "Quickly generate a PDF file using data collected from user input.",
        "images/ABTesting.png",
        "https://share.streamlit.io/streamlit/example-app-pdf-report/main",
        "example-app-pdf-report",
    )
with col3:
    app(
        "Collaboration",
        "Allow viewers of your app to collaborate via a commenting feature.",
        "images/ABTesting.png",
        "https://share.streamlit.io/streamlit/example-app-commenting/main",
        "example-app-commenting",
    )
    
st.header("🤩 Want more example apps?")
gallery_link = "https://streamlit.io/gallery"
st.write("[Check out our app gallery!](%s)" % gallery_link)
