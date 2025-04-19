from tabpy.tabpy_server.app.app import TabPyApp
import os
from pathlib import Path

# ایجاد فایل رمز عبور با فرمت صحیح
password_file = Path('/tmp/tabpy_passwords.txt')
password_file.write_text("admin:admin123")  # فقط این خط بدون هیچ کاراکتر اضافه

# تأیید محتوای فایل (برای دیباگ)
print("Password file content:", repr(password_file.read_text()))

# اجرای سرور
app = TabPyApp(config_file='tabpy.conf')
app.run()
