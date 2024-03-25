from apps.data_loader import DataLoader
from apps.report_sender import ReportSender
from config.config import Config

config = Config()
report_sender = ReportSender()
data_loader = DataLoader()

config.init()

data_loader.load()
report_sender.send()

config.close()
