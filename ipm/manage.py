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
import click
from rich.console import Console

from .common import (
    # get_IP_history,
    # install_ip_from_manifest,
    # list_IPs_local,
    list_remote_ip_info,
    list_remote_ips,
    # opt_ipm_iproot,
    # list_IPs,
    # install_IP,
    # uninstall_IP,
    # get_IP_list,
    # check_IP,
    # check_ipm_directory,
    # precheck,
)


@click.command("ls-remote")
def ls_remote_cmd():
    """Lists all verified IPs in ipm main repository"""
    console = Console()
    console.print("[green]Verified IPs:")
    list_remote_ips(console)


# def ls_remote(category, ipm_iproot, technology):
#     """Lists all verified IPs in ipm main repository"""
#     console = Console()
#     valid = check_ipm_directory(console, ipm_iproot)
#     if valid:
#         if category is not None:
#             if category in ["digital", "comm", "analog", "dataconv"]:
#                 console.print(f"[green]Verified IPs for the {category} category:")
#                 list_IPs(console, ipm_iproot, remote=True, category=category)
#             else:
#                 console.print(
#                     "You entered a wrong category, invoke ipm ls --help for assistance"
#                 )
#         elif technology is not None:
#             if technology in ["sky130", "gf180mcu"]:
#                 console.print(f"[green]Verified IPs for the {technology} technology:")
#                 list_IPs(console, ipm_iproot, remote=True)
#             else:
#                 console.print(
#                     "You entered a wrong technology, invoke ipm ls --help for assistance"
#                 )
#         else:
#             console.print("[green]Verified IPs:")
#             list_IPs(console, ipm_iproot, remote=True)


# @click.command("ls")
# @opt_ipm_iproot
# @click.option(
#     "--category",
#     required=False,
#     help="Optionally provide the category (digital, comm, analog, dataconv)",
# )
# @click.option(
#     "--technology",
#     required=False,
#     help="Optionally provide the technology (sky130, gf180mcu)",
# )
# def ls_cmd(category, ipm_iproot, technology):
#     """Lists all locally installed IPs"""
#     console = Console()
#     IPM_DIR_PATH = os.path.join(ipm_iproot)
#     valid = check_ipm_directory(console, ipm_iproot)
#     if valid:
#         if category is not None:
#             if category in ["digital", "comm", "analog", "dataconv"]:
#                 console.print(
#                     f"[green]Installed IPs at {ipm_iproot} for the {category} category:"
#                 )
#                 list_IPs_local(console, ipm_iproot, remote=False, category=category)
#             else:
#                 console.print(
#                     "You entered a wrong category, invoke ipm ls --help for assistance"
#                 )
#         elif technology is not None:
#             if technology in ["sky130", "gf180mcu"]:
#                 console.print(
#                     f"[green]Installed IPs at {ipm_iproot} for the {technology} technology:"
#                 )
#                 list_IPs_local(console, ipm_iproot, remote=False)
#             else:
#                 console.print(
#                     "You entered a wrong technology, invoke ipm ls --help for assistance"
#                 )
#         else:
#             console.print(f"[green]Installed IPs at {IPM_DIR_PATH}:")
#             list_IPs_local(console, ipm_iproot, remote=False)


# def ls(category, ipm_iproot, technology):
#     """Lists all locally installed IPs"""
#     console = Console()
#     IPM_DIR_PATH = os.path.join(ipm_iproot)
#     valid = check_ipm_directory(console, ipm_iproot)
#     if valid:
#         if category is not None:
#             if category in ["digital", "comm", "analog", "dataconv"]:
#                 console.print(
#                     f"[green]Installed IPs at {ipm_iproot} for the {category} category:"
#                 )
#                 list_IPs_local(console, ipm_iproot, remote=False, category=category)
#             else:
#                 console.print(
#                     "You entered a wrong category, invoke ipm ls --help for assistance"
#                 )
#         elif technology is not None:
#             if technology in ["sky130", "gf180mcu"]:
#                 console.print(
#                     f"[green]Installed IPs at {ipm_iproot} for the {technology} technology:"
#                 )
#                 list_IPs_local(console, ipm_iproot, remote=False)
#             else:
#                 console.print(
#                     "You entered a wrong technology, invoke ipm ls --help for assistance"
#                 )
#         else:
#             console.print(f"[green]Installed IPs at {IPM_DIR_PATH}:")
#             list_IPs_local(console, ipm_iproot, remote=False)


# @click.command("output")
# @opt_ipm_iproot
# def output_cmd(ipm_iproot):
#     """(Default) Outputs the current IP installation path"""
#     console = Console()
#     IPM_DIR_PATH = os.path.join(ipm_iproot)
#     valid = check_ipm_directory(console, ipm_iproot)
#     if valid:
#         print(f"Your IPs will be installed at {IPM_DIR_PATH}")


# def output(ipm_iproot):
#     """(Default) Outputs the current IP installation path"""
#     console = Console()
#     IPM_DIR_PATH = os.path.join(ipm_iproot)
#     valid = check_ipm_directory(console, ipm_iproot)
#     if valid:
#         return IPM_DIR_PATH


# @click.command("install")
# @click.argument("ip")
# @click.option(
#     "--overwrite",
#     required=False,
#     is_flag=True,
#     default=False,
#     help="Overwrite IP",
# )
# @click.option("--technology", required=False, default="sky130", help="Install IP based on technology")
# @click.option("--version", required=False, help="Install IP with a specific version")
# @click.option("--ip-root", required=False, default=os.path.join(os.path.expanduser("~"), ".ipm"), help="IP installation path")
# @click.option("--man-file", required=False, help="manifest file path")
# @opt_ipm_iproot
# def install_cmd(ip, ip_root, ipm_iproot, overwrite, technology="sky130", version=None, man_file=None):
#     """Install one of the verified IPs locally"""
#     console = Console()
#     valid = check_ipm_directory(console, ipm_iproot)
#     if valid:
#         install(
#             console, ip, ip_root, overwrite, technology=technology, version=version, json_file_loc=ipm_iproot, man_file=man_file
#         )


# def install(
#     console,
#     ip,
#     ipm_iproot,
#     overwrite,
#     technology="sky130",
#     version=None,
#     json_file_loc=None,
#     man_file=None,
# ):
#     """Install one of the verified IPs locally"""
#     if json_file_loc:
#         valid = check_ipm_directory(console, json_file_loc)
#     else:
#         valid = check_ipm_directory(console, ipm_iproot)
#     if valid:
#         IP_list = get_IP_list(ipm_iproot, remote=True)
#         if ip not in IP_list:
#             print(
#                 "Please provide a valid IP name, to check all the available IPs invoke 'ipm ls'"
#             )
#         else:
#             install_IP(
#                 console=console,
#                 ipm_iproot=ipm_iproot,
#                 ip=ip,
#                 overwrite=overwrite,
#                 technology=technology,
#                 version=version,
#                 json_file_loc=json_file_loc,
#                 man_file=man_file
#             )


# @click.command("install-from-manifest")
# @click.option(
#     "--overwrite",
#     required=False,
#     is_flag=True,
#     default=False,
#     help="Overwrite IP",
# )
# @click.option("--ip-root", required=False, default=os.path.join(os.path.expanduser("~"), ".ipm"), help="IP installation path")
# @click.option("--man-file", required=False, help="manifest file path")
# @opt_ipm_iproot
# def install_from_manifest_cmd(ip_root, ipm_iproot, overwrite, man_file=None):
#     """Install one of the verified IPs locally"""
#     console = Console()
#     valid = check_ipm_directory(console, ipm_iproot)
#     if valid:
#         install_from_manifest(
#             console, ip_root, overwrite, json_file_loc=ipm_iproot, man_file=man_file
#         )


# def install_from_manifest(
#     console,
#     ipm_iproot,
#     overwrite,
#     json_file_loc=None,
#     man_file=None,
# ):
#     """Install one of the verified IPs locally"""
#     if json_file_loc:
#         valid = check_ipm_directory(console, json_file_loc)
#     else:
#         valid = check_ipm_directory(console, ipm_iproot)
#     if valid:
#         IP_list = get_IP_list(ipm_iproot, remote=True)
#         install_ip_from_manifest(
#             console=console,
#             ipm_iproot=ipm_iproot,
#             overwrite=overwrite,
#             json_file_loc=json_file_loc,
#             man_file=man_file,
#             IP_list=IP_list
#         )


# @click.command("uninstall")
# @click.argument("ip")
# @click.option("--ip-root", required=False, default=os.path.join(os.path.expanduser("~"), ".ipm"), help="IP installation path")
# @opt_ipm_iproot
# def uninstall_cmd(ip, ipm_iproot, ip_root):
#     """Uninstall one of the IPs installed locally"""
#     console = Console()
#     valid = check_ipm_directory(console, ipm_iproot)
#     if valid:
#         IP_list = get_IP_list(ipm_iproot, remote=False)
#         if ip not in IP_list:
#             print(
#                 "Please provide a valid IP name, to check all installed IPs invoke 'ipm ls'"
#             )
#         else:
#             uninstall_IP(console, ipm_iproot, ip, ip_root)


# @click.command("check")
# @click.option(
#     "--ip",
#     required=False,
#     help="Optionally provide an IP to check for its newer version",
# )
# @opt_ipm_iproot
# def check_cmd(ip, ipm_iproot):
#     """Check for new versions of all installed IPs or a specific IP."""
#     console = Console()
#     valid = check_ipm_directory(console, ipm_iproot)
#     if valid:
#         IP_list = get_IP_list(ipm_iproot, remote=False)
#         if ip is not None:
#             if ip not in IP_list:
#                 print(
#                     "Please provide a valid IP name, to check all installed IPs invoke 'ipm ls'"
#                 )
#             else:
#                 check_IP(console, ipm_iproot, ip, update=False)
#         else:
#             check_IP(console, ipm_iproot, "all", update=False)


# def check(console, ip, ipm_iproot, version):
#     """Check for new versions of all installed IPs or a specific IP."""
#     valid = check_ipm_directory(console, ipm_iproot)
#     if valid:
#         IP_list = get_IP_list(ipm_iproot, remote=False)
#         if ip is not None:
#             if ip not in IP_list:
#                 print(
#                     "Please provide a valid IP name, to check all installed IPs invoke 'ipm ls'"
#                 )
#             else:
#                 check_IP(console, ipm_iproot, ip, update=True, version=version)
#         else:
#             check_IP(console, ipm_iproot, "all", update=True, version=version)


# @click.command("update")
# @click.option("--ip", required=False, help="Provide an IP to update")
# @click.option("--all", required=False, is_flag=True, help="Updates all installed IPs")
# @opt_ipm_iproot
# def update_cmd(ip, all, ipm_iproot):
#     """Update all installed IPs to their latest versions or a specific IP."""
#     console = Console()
#     valid = check_ipm_directory(console, ipm_iproot)
#     if valid:
#         IP_list = get_IP_list(ipm_iproot, remote=False)
#         if ip is not None:
#             if ip not in IP_list:
#                 print(
#                     "Please provide a valid IP name, to check all installed IPs invoke 'ipm ls'"
#                 )
#             else:
#                 check_IP(console, ipm_iproot, ip, update=True)
#         else:
#             if all:
#                 check_IP(console, ipm_iproot, "all", update=True)
#             else:
#                 console.print(
#                     "Either provide an ip name or to update all installed IPs run 'ipm update --all'"
#                 )


# def update(ip, all, ipm_iproot):
#     """Update all installed IPs to their latest versions or a specific IP."""
#     console = Console()
#     valid = check_ipm_directory(console, ipm_iproot)
#     if valid:
#         IP_list = get_IP_list(ipm_iproot, remote=False)
#         if ip is not None:
#             if ip not in IP_list:
#                 print(
#                     "Please provide a valid IP name, to check all installed IPs invoke 'ipm ls'"
#                 )
#             else:
#                 check_IP(console, ipm_iproot, ip, update=True)
#         else:
#             if all:
#                 check_IP(console, ipm_iproot, "all", update=True)
#             else:
#                 console.print(
#                     "Either provide an ip name or to update all installed IPs run 'ipm update --all'"
#                 )


# @click.command("pre-check")
# @opt_ipm_iproot
# def precheck_cmd(ipm_iproot):
#     """Update all installed IPs to their latest versions or a specific IP."""
#     console = Console()
#     valid = check_ipm_directory(console, ipm_iproot)
#     if valid:
#         ip = input("Enter IP name: ")
#         version = input("Enter IP version: ")
#         gh_repo = input(
#             'Enter the GH repo of the IP in the form "github.com/<username>/<project_name>": '
#         )
#         precheck(console, ipm_iproot, ip, version, gh_repo)


@click.command("info")
@click.option("--ip", required=True, help="ip to get history of versions")
# @opt_ipm_iproot
def info_cmd(ip):
    """list all versions of the IP"""
    console = Console()
    list_remote_ip_info(console, ip)


# def history(ipm_iproot, ip):
#     """list all versions of the IP"""
#     console = Console()
#     valid = check_ipm_directory(console, ipm_iproot)
#     if valid:
#         get_IP_history(console, ipm_iproot, ip, remote=True)
