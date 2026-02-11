<div align="center">

# 📚 OpenLibrary Backend Task
### 🔎 Python Data Fetching • API Integration • Structured CSV Export

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Backend](https://img.shields.io/badge/Focus-Backend%20Practice-purple.svg)
![API](https://img.shields.io/badge/API-OpenLibrary-orange.svg)
![Data](https://img.shields.io/badge/Data-Processing-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

A backend-oriented Python project that fetches real-world book data from the Open Library API, filters modern publications, and exports structured results into a clean, formatted CSV dataset.

</div>

---

## ✨ Project Overview

This project simulates a small backend data-processing workflow:

1. Fetch live book data from an external REST API
2. Validate and filter records based on business logic
3. Transform raw JSON into structured datasets
4. Export results into a readable CSV file

The main goal is to demonstrate practical backend development skills including API communication, data processing, and clean scripting.

---

## 🎯 Key Learning Objectives

- Working with external REST APIs
- Handling JSON responses
- Writing clean and modular Python functions
- Data filtering & transformation
- Structured file output
- Backend-style scripting workflows

---

## ⚙️ How It Works

### 1️⃣ Data Fetching
The script sends an HTTP request to the OpenLibrary Search API and retrieves book data related to Python programming.

### 2️⃣ Data Filtering
Books are filtered based on:

- Availability of publish year
- Published after the year **2000**

### 3️⃣ Data Transformation
Each valid record is transformed into a structured format containing:

- Title
- Language
- First Publish Year
- Ebook Access Status
- Edition Count
- Author Names

### 4️⃣ Data Export
Filtered results are exported into a formatted CSV file:

