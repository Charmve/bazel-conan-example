import os
import platform
import shutil

from test.examples_tools import run, tmp_dir

# ############# Example ################
print("\n- Use the BazelToolchain and BazelDeps generators -\n")

if platform.system() != "Linux":
    print(f"SKIPPED TEST BECAUSE BAZEL IS NOT INSTALLED IN {platform.system()} PLATFORM YET.")
    exit(0)

output = run("bazel --version")

profile = """

[settings]
os=Linux
os.api_level=21
arch=armv8
compiler=clang
compiler.version=16
compiler.libcxx=c++_static
compiler.cppstd=17
build_type=Debug    

[conf]
tools:clang_path={}
"""

toolchain_path = {"Darwin": "/opt/homebrew/share/android-ndk", "Linux": "/qcraft_cache/bazel/5f6cfd791ed6436cd7d0a9ad06515f99/external/llvm_repo/llvm/bin"}.get(platform.system())

if toolchain_path:
    profile = profile.format(toolchain_path)
    with tmp_dir("tmp"):
        with open("j5", "w") as _f:
            _f.write(profile)
        run("conan new -d name=foo -d version=1.0 cmake_lib")
        output = run("conan create . --profile ./j5")

try:
    print("\n- Conan installing all the files into the build folder -\n")
    run("conan install . --build=missing")
    print("\n- Running bazel build command to compile the demo bazel target -\n")
    run("bazel --bazelrc=./conan/conan_bzl.rc build --config=conan-config //main:demo")
    print("\n- Running the application 'demo' created -\n")
    run("./bazel-bin/main/demo")
finally:
    # Remove all the bazel symlinks and clean its cache
    run("bazel clean")
    shutil.rmtree("conan", ignore_errors=True)

