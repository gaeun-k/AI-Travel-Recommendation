# ✈️ K-Travel CLIP: Emotion-Driven Travel Discovery System

**An AI-native cross-modal search engine that understands the "vibe" and "emotion" of travel destinations beyond simple keyword matching.**

---

## 📌 Project Overview
This project addresses the limitations of conventional travel search systems by enabling **semantic and emotional searches**. Users can find destinations using natural language captions (e.g., *"Quiet Hanok village with a peaceful atmosphere"*) or by uploading photos with a specific mood. 

## 🛠️ Key Features
* **Dual-Head Architecture**: Simultaneously performs Scene Classification (13 categories) and Emotional Alignment.
* **Cross-Modal Search**: Supports both **Text-to-Image** and **Image-to-Image** retrieval.
* **Vector Search Engine**: Built with **FAISS** for high-speed similarity search across large-scale datasets.

## 📊 Data Strategy & Dataset
Following a **Data-centric AI** approach, I prioritized data integrity and semantic richness over simple model scaling.

### 1. Data Acquisition & Taxonomy
* **Sources**: Public tourism datasets and targeted web scraping for domestic travel destinations.
* **Taxonomy**: 13 distinct categories for scene classification:
  > *Sea, Mountain, Forest, City, Lake, Street, Traditional, Park, Landmark, Sculpture, Cafe, Spa, and Exhibition.*

### 2. Technical Safety Net: Preprocessing & Cleaning
To ensure **System Integrity**, I implemented a rigorous preprocessing pipeline to handle real-world "dirty" data:
* **Duplicate Extension Handling**: Automated scripts to fix irregular file extensions (e.g., `.JPG.jpg`) and unify case sensitivity.
* **NFC Normalization**: Resolved broken Korean text/encoding issues in metadata through **NFC (Normalization Form C)**.
* **Integrity Validation**: Performed a full-scale scan to verify physical image existence and filtered out corrupted or missing data.
* **AI-Driven Refinement**: Used LLMs to generate and refine semantic captions for unstructured metadata, ensuring the CLIP model understands nuanced "vibes."

## 🏗️ Model Architecture
### 1. Backbone (Frozen)
* **Image Encoder**: Pre-trained CLIP (ViT-B/32)
* **Text Encoder**: Multilingual DistilBERT (768-dim)

### 2. Trainable Heads
* **Scene Classification Head**: 13-class classification.
* **Projection Head**: Aligns image and text features into a common 256-dim space.

### 3. Objective Function
$$L = L_{CLIP} + \lambda_1 L_{SupCon} + \lambda_2 L_{CE}$$

## 🧪 Model Evaluation
[`model_select/`](./model_select) contains a Streamlit app for human evaluation of the recommendation model variants (`stage2` / `stage2_1` / `stage2_2`, see `AI/`). Reviewers compare the top-5 recommendations from each variant side by side and pick the best one; responses are logged to a Google Sheet. See [`model_select/README.md`](./model_select/README.md) for setup.
