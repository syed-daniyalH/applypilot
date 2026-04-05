# ApplyPilot - LinkedIn AI Auto Job Applier
This is a powerful web automation engine designed to simplify and accelerate your job search on LinkedIn. It intelligently searches for roles in your niche, automatically answers complex application forms, and can even tailor your resume using AI (OpenAI, Gemini, or DeepSeek) to match job requirements. 

## Key Features
- **Smart Search**: Automated filtering and location-based job discovery.
- **AI-Powered Answering**: Real-time form filling using LLMs for high accuracy.
- **Modern Dashboard**: Track your applications and stats in a high-tech UI.
- **Browser Stealth**: Human-like interaction and stealth mode to ensure account safety.
- **Custom CV Integration**: Auto-uploads your best-fit resume for every application.

## How to Install
1. **Python 3.12+**: Download from [python.org](https://www.python.org/).
2. **Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Google Chrome**: Ensure you have the latest version of Chrome installed.
4. **Driver Setup**: Use `setup/windows-setup.bat` to automatically install the correct ChromeDriver.

## Configuration Guide
1. **`config/personals.py`**: Enter your contact details and basic info.
2. **`config/questions.py`**: Configure how the bot should handle unknown questions.
3. **`config/search.py`**: Set your job search keywords and location filters.
4. **`config/secrets.py`**: Add your LinkedIn credentials and AI API keys (OpenAI/Gemini/DeepSeek).
5. **`config/settings.py`**: Adjust stealth mode, background run, and click intervals.

## How to Use
1. **Launch the Bot**: Run `python runAiBot.py`.
2. **Set Your Target**: Enter the number of jobs you want to apply to when prompted.
3. **Monitor Progress**: Open `http://localhost:5000` after running `python app.py` to see your live dashboard.

## Security & Ethics
This tool is built for personal productivity. Please adhere to LinkedIn's Terms of Service and use responsibly. Usage is at your own risk.

---
**Dedicated to Job Search Success.**  
Author: [Daniyal](https://github.com/syed-daniyalH)
