# MediSense NLP - Frontend Web Portal
**Authors:** K. Priya & CH. Harshini  
**Department:** Computer Science & Engineering, Warangal  

This directory contains the responsive web user interface for the MediSense NLP Healthcare system.

---

### Folder Contents
| File / Directory | Description |
| :--- | :--- |
| `index.html` | Complete web portal layout: NLP Feedback Analyzer, Live Database Feed, Hospital Analytics Charts, Lab Report Simplifier with Telugu Translation & Audio, and OPD Consultation Booking. |
| `css/style.css` | Comprehensive stylesheet with clean healthcare dashboard styling, badges, grids, and responsive design. |
| `js/main.js` | Interactive frontend logic: AJAX API calls to backend (`http://127.0.0.1:5000`), Chart.js rendering, audio playback, and fallback local intelligence. |
| `audio/` | Generated Telugu text-to-speech audio files (`.mp3`). |
| `open_frontend.bat` | 1-Click launcher to open `index.html` directly in your browser. |

---

### How to Open Frontend
- **Option 1 (Full-Stack Recommended):** Run `START_APPLICATION.bat` in the root folder (or `backend/run_backend.bat`), which starts Flask & opens `http://localhost:5000`.
- **Option 2 (Direct Folder View):** Double-click `open_frontend.bat` or double-click `index.html` directly. The page will render with full CSS styles and automatically connect to the backend at `http://127.0.0.1:5000`.
