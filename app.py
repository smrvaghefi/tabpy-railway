from tabpy.tabpy_server.app.app import TabPyApp
import os

# ایجاد فایل رمز عبور با فرمت صحیح
with open('/tmp/tabpy_pass.txt', 'w') as f:
    f.write("admin:admin123")  # بدون هیچ کاراکتر اضافه
    
# اجرای سرور
app = TabPyApp(config_file='tabpy.conf')
app.run()
