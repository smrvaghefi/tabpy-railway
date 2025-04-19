from tabpy.tabpy_server.app.app import TabPyApp
import os
from pathlib import Path

# ایجاد فایل رمز عبور موقت
password_content = "admin:admin123"  # یا از متغیر محیطی بخوانید: os.getenv('TABPY_CREDENTIALS')
password_file = Path('/tmp/tabpy_passwords.txt')
password_file.write_text(password_content)

# تنظیم مسیر فایل در محیط
os.environ['TABPY_PWD_FILE'] = str(password_file)

# اجرای سرور
app = TabPyApp(config_file='tabpy.conf')
app.run()
