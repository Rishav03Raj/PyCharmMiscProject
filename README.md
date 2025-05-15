# 📟 Family Portfolio Manager

A simple yet powerful **Streamlit** web app designed to help individuals or families monitor and analyze their financial portfolio. Upload your investment data and get clean, visual insights in seconds.

🔗 **Live App**: [family-portfolio-manager.streamlit.app](https://family-portfolio-manager.streamlit.app)

---

## 📊 Features

- 📁 Upload portfolio data (`.csv`)
- 📈 Visualize portfolio distribution
- 📉 Analyze asset allocation & trends
- 🧠 Intelligent insights for diversification
- 💡 Simple and interactive UI using Streamlit

---

## 🚀 How to Use

1. Visit the app: [https://family-portfolio-manager.streamlit.app](https://family-portfolio-manager.streamlit.app)
2. Upload your portfolio CSV file (sample structure below).
3. Explore charts, summaries, and asset breakdowns instantly.

---

## 📟 Sample `portfolio_data.csv`

```csv
Asset,Category,Amount
Stocks,Equity,50000
Bonds,Debt,20000
Mutual Funds,Equity,30000
Gold,Commodity,15000
Savings,Others,10000
```

---

## 🛠️ Tech Stack

- 🐍 Python
- 🌐 Streamlit
- 📊 Matplotlib / Plotly / Pandas
- 📁 CSV parsing

---

## 📂 Project Structure

```
PyCharmMiscProject/
│
├── main.py               # App launcher
├── analyse.py            # Handles portfolio analysis logic
├── script.py             # Script-based data utilities
├── ui.py                 # UI and layout helpers
├── streamlit.py          # Streamlit specific code
├── portfolio_data.csv    # Sample dataset
├── header.jpg            # Banner image
├── header2.jpg           # Secondary banner
├── qodana.yaml           # Code quality config
├── PyCharmMiscProject.iml
├── .idea/                # PyCharm IDE settings
```

---

## 🛠️ Installation (for local use)

```bash
git clone https://github.com/Rishav03Raj/PyCharmMiscProject.git
cd PyCharmMiscProject
pip install -r requirements.txt
streamlit run main.py
```

> You may need to manually create `requirements.txt` with required libraries (like `streamlit`, `pandas`, `matplotlib`, etc.).

---

## 🤝 Contributions

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📜 License

This project is open-source and free to use under the [MIT License](LICENSE).

---

## 👤 Author

**Rishav Raj**  
Connect on [GitHub](https://github.com/Rishav03Raj)
