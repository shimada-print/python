import sys
import platform
import pkg_resources
import os

def print_python_version():
    print(f"Python Version: {sys.version}")

def print_platform_info():
    print(f"Platform: {platform.system()}")
    print(f"Platform Version: {platform.version()}")
    print(f"Platform Architecture: {platform.architecture()}")

def print_installed_packages():
    print("\nInstalled Packages:")
    installed_packages = pkg_resources.working_set
    for package in sorted(installed_packages, key=lambda x: x.key):
        print(f"{package.key}=={package.version}")

def print_sys_path():
    print("\nSystem Path:")
    for path in sys.path:
        print(path)

def print_environment_variables():
    print("\nEnvironment Variables:")
    for key, value in sorted(os.environ.items()):
        print(f"{key}={value}")

if __name__ == "__main__":
    print_python_version()
    print_platform_info()
    print_installed_packages()
    print_sys_path()
    print_environment_variables()

    # エンターを押すと修了する（これを設置しないと実際は見れない）
    input("Press Enter to exit...")
