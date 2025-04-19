from tabpy.tabpy_server.app.app import TabPyApp
import os
from pathlib import Path

# 1. ایجاد فایل رمز عبور با بررسی خطا
try:
    pass_file = Path('pass.txt')
    pass_file.write_text("admin:admin123", encoding='utf-8')
    
    # نمایش محتوا برای اطمینان (مشاهده در لاگهای Render)
    print(f"Password file created at: {pass_file.absolute()}")
    print(f"File content: '{pass_file.read_text(encoding='utf-8')}'")
    
except Exception as e:
    print(f"Error creating password file: {str(e)}")
    raise

# 2. اجرای سرور با بررسی پیکربندی
try:
    app = TabPyApp(config_file='tabpy.conf')
    print("TabPy server initialized successfully")
    app.run()
except Exception as e:
    print(f"Failed to start TabPy: {str(e)}")
    raise
