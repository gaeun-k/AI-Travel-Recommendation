# model_select

Streamlit app for human evaluation of the recommendation models (`stage2` / `stage2_1` / `stage2_2`, see `../AI/`). For each test image, a reviewer picks the best of the three model outputs; responses are logged to a "Travel Evaluation" Google Sheet.

Moved here from the standalone [gaeun-k/model_select](https://github.com/gaeun-k/model_select) repo. The image folders (`eval_images/`, `images_abroad/`, ~39MB) were left out to keep this repo light — pull them from the original repo if you need to run the app locally.

## Setup

```bash
pip install -r requirements.txt
```

Place a Google service account credentials file at `service_account.json` (scoped for Sheets + Drive) and share the "Travel Evaluation" sheet with that service account.

## Run

```bash
streamlit run app.py
```

Requires `eval_images/` and `images_abroad/` folders alongside `app.py` (see `eval_results.csv` for the expected filenames), and `eval_results.csv` in this directory.
