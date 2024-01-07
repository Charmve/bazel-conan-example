# bazel-conan-example
bazel-conan-example: Cross building with Conan


``
conan install . --build=missing

bazel build //main:demo
./bazel-bin/main/demo
``

Additional:
- WORKSPACE
- conan/dependencies.bzl 
- run_example.py
