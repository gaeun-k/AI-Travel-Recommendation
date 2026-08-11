import streamlit as st
import pandas as pd
import random
import os
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

@st.cache_resource
def connect_sheet():

    scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

    creds = Credentials.from_service_account_file(
        "service_account.json",
        scopes=scope
    )

    client = gspread.authorize(
        creds
    )

    sheet = client.open(
        "Travel Evaluation"
    ).sheet1

    return sheet

#################################################
# PAGE
#################################################

st.set_page_config(
    page_title="여행지 추천 모델 평가",
    layout="wide"
)

st.title("여행지 추천 모델 평가")

#################################################
# LOAD
#################################################

@st.cache_data
def load_data():

    return pd.read_csv(
        "eval_results.csv"
    )

df = load_data()

sheet = connect_sheet()

#################################################
# 랜덤 3개 선정
#################################################

all_images = (
    df["test_image"]
    .unique()
    .tolist()
)

if "selected_images" not in st.session_state:

    st.session_state.selected_images = (
        random.sample(
            all_images,
            min(3, len(all_images))
        )
    )

#################################################
# 평가 UI
#################################################

all_choices = {}

for test_image in st.session_state.selected_images:

    st.divider()

    st.header("입력 이미지")

    input_path = os.path.join(
        "images_abroad",
        test_image
    )

    st.image(
        input_path,
        width=400
    )

    image_df = df[
        df["test_image"] == test_image
    ]

    cols = st.columns(4)

    model_order = [
        ("stage2", "추천안 A"),
        ("stage2_1", "추천안 B"),
        ("stage2_2", "추천안 C")
    ]

    for col, (model_name, label) in zip(
        cols,
        model_order
    ):

        row = image_df[
            image_df["model"] == model_name
        ].iloc[0]

        with col:

            st.subheader(label)

            st.write(
                f"**1순위:** {row['rank1_place']}"
            )

            img1 = os.path.join(
                "eval_images",
                str(row["rank1_image"])
            )

            if os.path.exists(img1):

                st.image(
                    img1,
                    use_container_width=True
                )

            st.write(
                f"**2순위:** {row['rank2_place']}"
            )

            img2 = os.path.join(
                "eval_images",
                str(row["rank2_image"])
            )

            if os.path.exists(img2):

                st.image(
                    img2,
                    use_container_width=True
                )
            st.write(
                f"**3순위:** {row['rank3_place']}"
            )

            img3 = os.path.join(
                "eval_images",
                str(row["rank3_image"])
            )

            if os.path.exists(img3):

                st.image(
                    img3,
                    use_container_width=True
                )
            st.write(
                f"**4순위:** {row['rank4_place']}"
            )
            
            img4 = os.path.join(
                "eval_images",
                str(row["rank4_image"])
            )
            
            if os.path.exists(img4):

                st.image(
                    img4,
                    use_container_width=True
                )
                
            st.write(
                f"**5순위:** {row['rank5_place']}"
            )  
            img5 = os.path.join(
                "eval_images",
                str(row["rank5_image"])
            )
            
            if os.path.exists(img5):
                st.image(
                    img5,
                    use_container_width=True
                )


    choice = st.radio(
        "가장 적절한 추천을 선택해주세요",
        [
            "추천안 A",
            "추천안 B",
            "추천안 C"
        ],
        key=test_image
    )

    all_choices[test_image] = choice

#################################################
# 제출
#################################################

if st.button("제출"):

    for image_name, choice in all_choices.items():

        sheet.append_row([
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            image_name,
            choice
        ])

    st.success(
        "응답 제출 완료!"
    )