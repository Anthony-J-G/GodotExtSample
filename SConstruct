#!/usr/bin/env python
import os
import sys
import shutil

PROJECT_FOLDER = "demo"
LIBRARY_NAME = "libgdexample"
EXTENSION_CONFIG_NAME = "gdexample"

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
    source_path = f"config/{EXTENSION_CONFIG_NAME}.gdextension"
    target_path = f"{PROJECT_FOLDER}/bin/{EXTENSION_CONFIG_NAME}.gdextension"
    bin_path = f"{PROJECT_FOLDER}/bin"

    if not os.path.exists(bin_path):
        os.mkdir(bin_path)

    if not os.path.exists(target_path):
        shutil.copy2(source_path, target_path)
        print(f"File copied from {source_path} to {target_path}.")
    else:
        print(f"File already exists at {target_path}. Copy operation skipped.")


# Create pseudo-builder and add to environment
def pre_process(env, source):
    env = env.Clone()
    env.Replace(OBJSUFFIX = '.E')
    env.AppendUnique(CCFLAGS = '-E')    
    return env.Object(source)

env.AddMethod(pre_process, 'PreProcess')

# Target for external dependencies
# env.Append(LIBPATH=[f'{PROJECT_FOLDER}/bin'])
# env.Append(LIBS=['libauxdungeon'])

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

# Preprocessor build
env.Alias('preprocess', env.PreProcess("src/gdexample.cpp"))

# Copies Extension file to build folder
copy_extension_file()


