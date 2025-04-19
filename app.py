from tabpy.tabpy_server.app.app import TabPyApp
import os

# مسیر فایل کانفیگ
config_file = os.path.join(os.path.dirname(__file__), 'tabpy.conf')

# تنظیم پورت برای Render
port = int(os.environ.get("PORT", 9004))

# اجرای سرور
app = TabPyApp(config_file=config_file)
app.run(host='0.0.0.0', port=port)
