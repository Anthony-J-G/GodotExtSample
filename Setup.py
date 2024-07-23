import os
import subprocess
import sys

def create_virtualenv(env_dir):
    if not os.path.exists(env_dir):
        print(f"Creating virtual environment in {env_dir}")
        subprocess.check_call([sys.executable, '-m', 'venv', env_dir])
    else:
        print(f"Virtual environment already exists in {env_dir}")

def install_packages(env_dir, requirements_file):
    pip_executable = os.path.join(env_dir, 'Scripts', 'pip')
    if not os.path.exists(requirements_file):
        print(f"Error: {requirements_file} does not exist.")
        sys.exit(1)
    print(f"Installing packages from {requirements_file}")
    subprocess.check_call([pip_executable, 'install', '-r', requirements_file])

def setup_build_system(env_dir):
    # Placeholder for additional build system setup tasks
    print("Setting up build system...")

def main():
    env_dir = '.venv'
    requirements_file = 'requirements.txt'

    create_virtualenv(env_dir)
    install_packages(env_dir, requirements_file)
    setup_build_system(env_dir)

    print("Build system setup complete. To activate the virtual environment, run:")
    print(f"source {env_dir}/bin/activate")

if __name__ == '__main__':
    print("Running Project Initialization")
    main()
