from tabpy.tabpy_server.app.app import TabPyApp
from tabpy.tabpy_server.app.util import parse_pwd_file
import os

# تنظیمات امنیتی (اختیاری)
os.environ["TABPY_PWD_FILE"] = "passwords.txt"  # فایل رمز عبور

# اجرای سرور TabPy
app = TabPyApp()
app.run()
