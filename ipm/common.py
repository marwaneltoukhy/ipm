#!/usr/bin/env python3
# Copyright 2022 Efabless Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import json
import requests
import shutil
import tarfile
from datetime import datetime
from typing import Callable

import rich
from rich.table import Table
import click

# Datetime Helpers
ISO8601_FMT = "%Y-%m-%dT%H:%M:%SZ"


def date_to_iso8601(date: datetime) -> str:
    return date.strftime(ISO8601_FMT)


def date_from_iso8601(string: str) -> datetime:
    return datetime.strptime(string, ISO8601_FMT)


# ---

IPM_REPO_OWNER = os.getenv("IPM_REPO_OWNER") or "efabless"
IPM_REPO_NAME = os.getenv("IPM_REPO_NAME") or "ipm"
IPM_REPO_ID = f"{IPM_REPO_OWNER}/{IPM_REPO_NAME}"
IPM_REPO_HTTPS = f"https://github.com/{IPM_REPO_ID}"
IPM_REPO_API = f"https://api.github.com/repos/{IPM_REPO_ID}"
IPM_DEFAULT_HOME = os.path.join(os.path.expanduser("~"), ".ipm")

LOCAL_JSON_FILE_NAME = "Installed_IPs.json"
MANIFEST_FILE_NAME = "manifest.json"
REMOTE_VERIFIED_IPS_URL = (
    "https://raw.githubusercontent.com/efabless/ipm/main/Verified_IPs.json"
)

class RemoteIP:
    def __init__(self, console: rich.console.Console):
        self.console = console

    def get_ip_info(self, name, technology="sky130"):
        resp = requests.get(REMOTE_VERIFIED_IPS_URL)
        data = json.loads(resp.text)
        for key, values in data.items():
            for value in values:
                if value["name"] == name and value["technology"] == technology:
                    self.name = value["name"]
                    self.repo = value["repo"]
                    self.author = value["author"]
                    self.email = value["email"]
                    self.type = value["type"]
                    self.category = value["category"]
                    self.status = value["status"]
                    self.width = value["width"]
                    self.height = value["height"]
                    self.technology = value["technology"]
                    self.release = value["release"]
                    self.versions = []
                    self.dates = []
                    for versions in value["release"]:
                        self.versions.append(versions["version"])
                        self.dates.append(versions["date"])

    def get_all_ips(self):
        resp = requests.get(REMOTE_VERIFIED_IPS_URL)
        if resp.status_code == 404:
            self.console.print("[red]couldn't connect to server")
            exit(1)
        data = json.loads(resp.text)
        return data


class LocalIP:
    def __init__(self, local_json):
        self.json_file = local_json

    def get_ip_info(self, name, ip_root, technology="sky130"):
        with open(self.json_file) as f:
            data = json.load(f)
        for key, values in data.items():
            for value in values:
                if value["name"] == name and value["technology"] == technology and value["ip_root"] == ip_root:
                    self.name = value["name"]
                    self.repo = value["repo"]
                    self.author = value["author"]
                    self.email = value["email"]
                    self.type = value["type"]
                    self.category = value["category"]
                    self.status = value["status"]
                    self.width = value["width"]
                    self.height = value["height"]
                    self.technology = value["technology"]
                    self.release = value["release"]
                    self.version = value["version"]
                    self.date = value["date"]
                    self.ip_root = value["ip_root"]

def list_remote_ips(console: rich.console.Console):
    remote_ip = RemoteIP(console)
    all_ip_data = remote_ip.get_all_ips()

    table = Table()

    table.add_column("Category", style="cyan")
    table.add_column("IP Name", style="magenta")
    table.add_column("Release")
    table.add_column("Author")
    table.add_column("Date")
    table.add_column("Type")
    table.add_column("Status")
    table.add_column("Width (mm)")
    table.add_column("Height (mm)")
    table.add_column("Technology", style="cyan")

    for key, values in all_ip_data.items():
        for value in values:
            if value:
                table.add_row(
                    key,
                    value["name"],
                    value["release"][-1]["version"],
                    value["author"],
                    value["release"][-1]["date"],
                    value["type"],
                    value["status"],
                    value["width"],
                    value["height"],
                    value["technology"],
                )

    console.print(table)

def list_remote_ip_info(console: rich.console.Console, ip):
    remote_ip = RemoteIP(console)
    all_ip_data = remote_ip.get_all_ips()

    table = Table()

    table.add_column("Category", style="cyan")
    table.add_column("IP Name", style="magenta")
    table.add_column("Release")
    table.add_column("Author")
    table.add_column("Date")
    table.add_column("Type")
    table.add_column("Status")
    table.add_column("Width (mm)")
    table.add_column("Height (mm)")
    table.add_column("Technology", style="cyan")

    for key, values in all_ip_data.items():
        for value in values:
            if value["name"] == ip:
                for i in range(0, len(value["release"])):
                    table.add_row(
                        key,
                        value["name"],
                        value["release"][i]["version"],
                        value["author"],
                        value["release"][i]["date"],
                        value["type"],
                        value["status"],
                        value["width"],
                        value["height"],
                        value["technology"],
                    )

    console.print(table)
