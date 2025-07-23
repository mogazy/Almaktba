bot_username = "Maktabatylastbot"  # اسم مستخدم البوت
deep_link_command = "/jdwl"

# إنشاء رابط الديب لينك
telegram_deep_link = f"https://t.me/{bot_username}?start={deep_link_command.lstrip('/')}"
print(f"رابط الديب لينك لفتح الأمر /jdwl في بوت @{bot_username}:")
print(telegram_deep_link)

# يمكنك فتح هذا الرابط في متصفحك لتجربته:
import webbrowser
webbrowser.open(telegram_deep_link)
