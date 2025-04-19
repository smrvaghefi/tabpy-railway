from tabpy.tabpy_server.app.app import TabPyApp
import os


config_file = os.path.join(os.path.dirname(__file__), 'tabpy.conf')
port = int(os.environ.get("PORT", 9004))

os.environ['TABPY_PWD_FILE'] = 'admin:admin123'
app = TabPyApp(config_file=config_file)
app.run()
