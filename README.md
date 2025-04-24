# 🍽️ Restaurant Management MCP Server

A smart Model Context Protocol (MCP) Server that integrates with Claude Desktop to help restaurant managers streamline operations like:

- 📊 Tracking daily top-selling menu items  
- 📦 Monitoring inventory levels  
- 🧑‍🍳 Generating staff schedules  
- 🛒 Managing stock additions  
- 💬 Summarizing customer feedback  

---

## 📂 Project Overview

This MCP server allows you to interact naturally with Claude Desktop using queries such as:

- `"Show me today's top-selling items"`
- `"What ingredients are running low?"`
- `"Generate tomorrow’s staff schedule"`
- `"Add 30 Cheese to the inventory"`
- `"Summarize yesterday’s feedback"`

---

## 🔧 Features

- ✅ Real-time top-selling dish report  
- ✅ Inventory alerts for low stock items  
- ✅ Automatic staff scheduling  
- ✅ Smart inventory updates  
- ✅ Feedback summarization from the previous day  
- ✅ Easy Claude Desktop integration  

---

## 📦 Prerequisites

- Python 3.8+
- Claude Desktop (running locally)
- [uv](https://github.com/astral-sh/uv) package manager (recommended)

## Setup steps

- Install Claude Desktop
- Install uv by running ```pip install uv```
- Run ```uv init restaurant-mcp-server``` to create a project directory
- Run ```uv add "mcp[cli]"``` to add mcp cli in your project
- Few folks may get type errors for which you can run ```pip install --upgrade typer``` to upgrade typer library to its latest version
- Write code in main.py for leave management server
- Install this server inside Claude desktop by running ```uv run mcp install main.py``` in the project directory
- Kill any running instance of Claude from Task Manager. Restart Claude Desktop
- In Claude desktop, now you will see tools from this server

@All rights reserved. Rohan Thite (TechSpire)


