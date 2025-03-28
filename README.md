# 🐾 Tanuki Card Proxy Maker 1.0🃏

**A powerful tool to generate professional-quality card sheets for printing TCG proxies.**

Support for custom sizes, A3/A4 layouts, and margin precision.

---

## ✨ Features

- 🖼️ Resize images to TCG-standard (Yu-Gi-Oh, MTG, Pokémon, etc.)
- 📄 Automatically layout multiple cards per page (A3/A4)
- 🧮 Custom margins for easy cutting
- 🖨️ Optimized for high-resolution printing (300 DPI)
- 🔁 CLI support to customize pattern and page type
- 📂 Auto-organized output folders
- 💥 Built for flexibility and expansion

---

## 📂 Folder Structure

```
tanuki-card-proxy-maker/
├── src/
│   ├── config/     # Configuration logic
│   ├── enums/      # Pattern and sheet types
│   ├── services/   # Resizing and sheet-joining logic
├── assets/
│   └── images/
│       ├── raw/    # Place your raw card images here
│       └── resized/ # Auto-generated resized images
├── index.py        # CLI entry point
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the project

```bash
git clone https://github.com/PauloKaedo/tanuki-card-proxy-maker.git
cd tanuki-card-proxy-maker
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 🧪 Usage

### 🖼️ Image Input

Place all your card images in:

```bash
assets/images/raw/
```

Supported formats: .png, .jpg, .jpeg, .bmp

### 💻 CLI Options

```bash
python src/index.py [options]
```

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| --pattern | Choose the card pattern | default, yugioh | default |
| --sheet | Choose output sheet size | a3, a4 | a3 |

### 🔁 Example:

```bash
python src/index.py --pattern yugioh --sheet a4
```

### 📤 Output

Generated files will be saved to:

```bash
assets/images/resized/
```

Each sheet will be named like:

```
resized_cards_01.png
resized_cards_02.png
...
```

## 🧠 Configuration

All card sizes, DPI, margins, and layout logic live in:

```
src/configs/config.py
```

You can tweak:

- DPI
- Margin between cards
- External sheet margin
- Supported formats
- Sheet type & paper sizes

## 🧙‍♂️ Author

Paulo Lima

Built with  Python

## 📜 License

MIT License.
