#!/usr/bin/env python
import os
import sys
import shutil

PROJECT_FOLDER = "demo"
LIBRARY_NAME = "libgdexample"


env = SConscript("godot-cpp/SConstruct")

# For reference:
# - CCFLAGS are compilation flags shared between C and C++
# - CFLAGS are for C-specific compilation flags
# - CXXFLAGS are for C++-specific compilation flags
# - CPPFLAGS are for pre-processor flags
# - CPPDEFINES are for pre-processor defines
# - LINKFLAGS are for linking flags


def copy_extension_file():
    """
    Copies a file from source_path to target_path only if the file does not already exist at target_path.

    :param source_path: The path to the source file.
    :param target_path: The path to the target file.
    :return: None
    """
    source_path = "config/gdexample.gdextension"
    target_path = f"{PROJECT_FOLDER}/bin/gdexample.gdextension"
    if not os.path.exists(target_path):
        shutil.copy2(source_path, target_path)
        print(f"File copied from {source_path} to {target_path}.")
    else:
        print(f"File already exists at {target_path}. Copy operation skipped.")


# tweak this if you want to use different folders, or more folders, to store your source code in.
env.Append(CPPPATH=["src/"])
sources = Glob("src/*.cpp")

if env["platform"] == "macos":
    library = env.SharedLibrary(
        (
            f"{PROJECT_FOLDER}/bin/" + 
            f"{LIBRARY_NAME}.{env['platform']}.{env['target']}.framework/" +
            f"{LIBRARY_NAME}.{env['platform']}.{env['target']}"
        ),
        source=sources,
    )
else:
    library = env.SharedLibrary(
        (
            f"{PROJECT_FOLDER}/bin/" +
            f"{LIBRARY_NAME}{env['suffix']}{env['SHLIBSUFFIX']}"
        ),
        source=sources,
    )

Default(library)
copy_extension_file()
