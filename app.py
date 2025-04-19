from tabpy.tabpy_server.app.app import TabPyApp
import os

with open('pass.txt', 'w') as f:
    f.write("admin:admin123")
    
# اجرای سرور
app = TabPyApp(config_file='tabpy.conf')
app.run()
