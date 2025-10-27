# -TEXT-SUMMARIZATION-TOOL
A TOOL THAT SUMMARIZES  LENGTHY ARTICLES USING NATURAL  LANGUAGE PROCESSING.

#  Text Summarizer using NLP

This is my first internship task — a simple **Text Summarizer Tool** built using Python and Natural Language Processing (NLP).
The goal was to create a script that can take a long paragraph or article and turn it into a shorter, easy-to-read summary.

## What it Does

The tool reads your input text and gives you three different summary sizes:

* **1 → Small** – a very short version
* **2 → Medium** – a balanced summary
* **3 → Large** – a slightly detailed one

It works using a basic **extractive summarization** method, meaning it picks out the most important sentences from your text instead of creating new ones

##  How it Works (in simple terms)

Here’s what happens behind the scenes:

1. The text is cleaned (extra spaces, numbers, etc. removed).
2. It’s broken down into **sentences and words**.
3. Common words like *is, and, the* are filtered out.
4. Every remaining word gets a score based on how often it appears.
5. Sentences containing important words get higher scores.
6. The top-scoring sentences are picked to form the summary.

So basically — the tool keeps the meaningful parts and drops the filler stuff.



## Tools & Libraries Used

* **Python 3**
* **NLTK** (for tokenizing and removing stopwords)
* **Regex (re)** for text cleaning
* **Heapq** to pick the best sentences efficiently

---

##  Project Files

```
Text-Summarizer/
│
├── main.py         # Main script where user enters text and gets summary
├── summarizer.py   # The logic for summarizing text
└── README.md       # This file
```

---

## 🚀 How to Run the Project

**Step 1:** Clone or download the repo

```bash
git clone https://github.com/your-username/Text-Summarizer.git
cd Text-Summarizer
```

**Step 2:** (Optional) Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate      # On Windows
# or
source venv/bin/activate   # On Mac/Linux
```

**Step 3:** Install the required libraries

```bash
pip install nltk
```

**Step 4:** Download NLTK data (only once)

```python
import nltk
nltk.download('punkt_tab')
nltk.download('stopwords')
```

**Step 5:** Run the script

```bash
python main.py
```

---



##  What I Learned

* How to clean and preprocess raw text using NLP.
* How to find important words and sentences mathematically.
* How extractive summarization works under the hood.
* How to connect multiple Python files (main + logic) into one working app.

---

##  Author
Mohammed Fahad Ali
AI / ML Intern | Generative AI Engineer
[LinkedIn](Mohammed Fahad Ali) • [GitHub](Fahadaliha)

---

## License

This project is open-source under the **MIT License**.
Feel free to use or improve it!

