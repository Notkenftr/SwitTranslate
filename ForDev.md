If you want to integrate this module into your bot, follow these steps:

1. Create a folder named **Module** inside your bot’s source directory.  
2. Copy the following files and folders into it:  
   - `Module/Translate`  
   - `Module/cooldown.py`  
   - `Module/__init__.py`  
   - `config.yml`  
   - `bot_reply.json`  

3. Add this line inside your bot’s `on_ready` (or bot_ready) function:
```py
await {your_bot_object}.add_cog(TranslateCommand(app=app))

```

You don't necessarily need to bring the entire config.yml.<br>
You can copy only the essential parts such as "Gemini" and "translate_command"<br>
and paste them into your own configuration file.