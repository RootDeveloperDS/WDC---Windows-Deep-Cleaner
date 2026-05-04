# 🧹 WDC — Windows Deep Cleaner

**WDC (Windows Deep Cleaner)** is a lightweight, one-click desktop tool built with Python & Tkinter that deep-cleans your Windows PC by removing junk files, clearing browser caches, and flushing system temp folders — all through a simple GUI.

---

## 📥 Get WDC .exe from my WEBSITE:

**WDC- Windows Deep Cleaner (Windows) | RootDeveloperDS :-**

👉 https://rootdeveloperds.odoo.com/shop/wdc-windows-deep-cleaner-windows-5

---

## ✨ Features

- 🗑️ Clears **TEMP** & **Windows Temp** folders
- ⚡ Clears **Prefetch** files
- 🚮 Empties the **Recycle Bin**
- 🔄 Stops/Starts **Windows Update Service** and clears its download cache
- 🌐 Cleans browser caches:
  - **Google Chrome**
  - **Microsoft Edge**
  - **Mozilla Firefox**
- 📊 Real-time **progress bar** during cleaning
- 🖥️ Clean, minimal **GUI** — no command line needed

---

## 🚀 How to Use

### Option 1 — Use the .exe (Recommended)
1. Download the `.exe` from the website link above.
2. **Right-click → Run as Administrator** *(required for system-level cleaning)*.
3. Click **"Start Deep Cleaning"** and wait for the process to finish.

### Option 2 — Run from Python Source
1. Make sure Python 3 is installed.
2. Install dependencies:
   ```bash
   pip install pillow
   ```
3. Run the script:
   ```bash
   python "py/deep_clean_v-1&2.py"
   ```
4. **Run your terminal / IDE as Administrator** for full cleaning capability.

---

## ⚠️ Note

> **Administrator privileges are required** for this tool to work properly.  
> Without admin rights, certain cleaning tasks (such as clearing `C:\Windows\Temp`, `C:\Windows\Prefetch`, and Windows Update cache) **will be skipped or fail silently**.  
> Always **run the `.exe` or your terminal as Administrator** before starting the cleaner.  
> This tool only deletes **temporary/cache files** — it does **not** touch your personal files or installed applications.

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **GUI:** Tkinter
- **Image Handling:** Pillow (PIL)
- **Packaging:** PyInstaller (for the `.exe` release)

---

## 👤 Author

**Root Developer D.S.**  
🔗 GitHub: [https://github.com/RootDeveloperDS](https://github.com/RootDeveloperDS)  
🌐 Website: [https://rootdeveloperds.odoo.com](https://rootdeveloperds.odoo.com)

---

*Version 1.0 — Built by Root Developer D.S.*
