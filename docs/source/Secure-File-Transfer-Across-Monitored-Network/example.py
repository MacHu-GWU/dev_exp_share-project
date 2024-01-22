# -*- coding: utf-8 -*-

from pathlib_mate import Path
from app import App, BotoSesManager

app = App.new(
    bsm=BotoSesManager(profile_name="bmt_app_dev_us_east_1"),
    bucket="bmt-app-dev-us-east-1-data",
    folder="projects/secure-file-transfer-across-monitored-network",
    password="mypassword",
)

# ------------------------------------------------------------------------------
# File
# ------------------------------------------------------------------------------
# --- upload
# s3path = app.upload(archive_name="test_file", path="test-file.txt")
# print(s3path.console_url)
# --- download
# app.download(archive_name="test_file", path="tmp/test-file.txt")

# ------------------------------------------------------------------------------
# Folder
# ------------------------------------------------------------------------------
# --- upload
# s3path = app.upload(archive_name="test_dir", path=Path.dir_here(__file__).joinpath("test-dir"))
# print(s3path.console_url)

# --- download
app.download(archive_name="test_dir", path=Path.dir_here(__file__).joinpath("tmp"))
