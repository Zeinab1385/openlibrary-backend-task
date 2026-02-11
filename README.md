<div align="center">

# 📚 OpenLibrary Backend Task
### 🔎 Python API Integration • Data Processing • CSV Export • Backend Workflow

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Backend](https://img.shields.io/badge/Focus-Backend-purple.svg)
![API](https://img.shields.io/badge/API-OpenLibrary-orange.svg)
![Data](https://img.shields.io/badge/Data-Processing-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)

A **mentor-ready, portfolio-level** Python project demonstrating a complete backend workflow: fetching, filtering, transforming, and exporting book data from the Open Library API into a clean CSV file.

</div>

---

## ✨ Project Overview

**OpenLibrary Backend Task** is a realistic backend data pipeline project illustrating:

1. Fetching live book data from OpenLibrary REST API.
2. Validating and filtering records based on business rules (books published after 2000).
3. Transforming JSON responses into structured datasets.
4. Exporting clean, human-readable CSV files.
5. Writing modular and maintainable Python code suitable for production-level backend tasks.

**Goal:** Showcase practical backend and data processing skills for real-world projects and portfolio demonstration.

---

## 🧩 Features

- 🌐 Fetch live book data from OpenLibrary API
- 🧠 Filter books published after 2000
- 📊 Extract essential information:
  - Title
  - Language
  - Publish Year
  - Ebook Access
  - Edition Count
  - Author Names
- 🧾 Export results in a readable CSV file (`books.csv`)
- ⚡ Lightweight, modular, and reusable code
- 🔧 Fully customizable queries and filters

---

## 🏗 Architecture & Workflow

```mermaid
flowchart LR
    A[Fetch Books from OpenLibrary API] --> B[Validate & Filter Data]
    B --> C[Transform JSON to Structured Format]
    C --> D[Export Clean CSV File]
