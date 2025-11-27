# 📦 Swit<br><br>

      /$$$$$$                /$$   /$$
     /$$__  $$              |__/  | $$
    | $$  \__/ /$$  /$$  /$$ /$$ /$$$$$$
    |  $$$$$$ | $$ | $$ | $$| $$|_  $$_/
     \____  $$| $$ | $$ | $$| $$  | $$
     /$$  \ $$| $$ | $$ | $$| $$  | $$ /$$
    |  $$$$$$/|  $$$$$/$$$$/| $$  |  $$$$/
     \______/  \_____/\___/ |__/   \___/

SwitTranslate is a Discord bot that helps you translate plugin configuration files quickly and easily.

**First:** This file was translated by LLM because I don't know English 😙.

# 🗒️ Requirements<br>
**Python**: 3.8+ <br>
**Operating System**: Windows, macOS, or Linux<br>
**packages:**<br>
> discord.py >= 2.5<br>
> google-genai >= 1.52.0<br>
> pyyaml >= 6.0<br>
  
# ✨ How to setup

## Step 1. Create discord bot
> 1. Go to https://discord.com/developers/applications
> 2. Click the “New Application” button.
> 3. After the application is created, open it and go to the Bot tab.
> 4. Click “Reset Token” to generate a new bot token.
> 5. Copy the generated token and paste it into the token field inside your config.yml file.

## Step 2. Get gemini api key
> 1. Visit https://aistudio.google.com/
> 2. Click “Get API Key”.
> 3. Select “Create API Key”.
> 4. If you don’t have a project yet, create one by choosing “Create project”.
> 5. Enter a name for your API key.
> 6. Copy the generated key and paste it into the api_key field in config.yml.

## Step 3. Run Bot
> 1. Install the required libraries using this command:
```
pip install discord.py google-genai pyyaml
```
> 2. Start the bot by running:
```
python app.py
```

## Issue

### 1. Missing Python Installation
> Your computer might not have Python installed, or the version is too old.
Fix: Install Python 3.10+ from the official website.<br>
> Python website: https://www.python.org/

### 2. Missing Packages
> If you run the bot and see errors like “Module not found”, it means some packages aren’t installed.<br>
> Fix:
> ```
> pip install discord.py google-genai pyyaml

3. Wrong Python Command
> Some systems use python, others use python3.<br>
> Fix: Try both commands until one works.


MIT License

Copyright (c) 2025 kenftr

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


