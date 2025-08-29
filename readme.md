# 👗 AI-Powered Outfit Suggester

## 📌 Project Overview
This project is an **AI-powered outfit suggestion system** built to demonstrate how **Large Language Models (LLMs)** can generate creative and context-aware recommendations.  
The AI suggests outfits based on prompts, user preferences, and different sampling strategies (`Top-P`, `Temperature`, and `Top-K`).

---

## 🎯 Features
1. **Zero-Shot Prompting**  
   - AI suggests outfits with no prior examples.  
   - Demonstrates baseline generation capability.

2. **Dynamic Prompting**  
   - Takes **user input** (e.g., occasion, mood, weather).  
   - Generates more **personalized outfit ideas**.

3. **Sampling Strategies**
   - **Top-P (Nucleus Sampling):** Controls how “broad” or “narrow” the model samples.  
   - **Temperature:** Controls the “creativity” of responses.  
   - **Top-K:** Restricts sampling to the top `k` most probable tokens.

---

## 🛠️ Technical Implementation
- **Backend**: Python-based scripts using:
  - [OpenAI API](https://platform.openai.com) for GPT-powered generation.  
  - [HuggingFace Transformers](https://huggingface.co/transformers/) for open-source demos of sampling strategies.  
  - `dotenv` for environment variable management.  

- **Flow**:
  1. User provides input (occasion, mood, style).  
  2. Backend generates an AI prompt.  
  3. LLM processes input with chosen **sampling strategy**.  
  4. Resulting outfit suggestions are returned.  


