# This Bazel module should be loaded by your WORKSPACE file.
# Add these lines to your WORKSPACE one (assuming that you're using the "bazel_layout"):
# load("@//conan:dependencies.bzl", "load_conan_dependencies")
# load_conan_dependencies()

def load_conan_dependencies():
    native.new_local_repository(
        name="fmt",
        path="/home/qcraft/.conan2/p/b/fmt68614a6cb8d0a/p",
        build_file="/qcraft/bazel/toolchains/string_formatter/conan/fmt/BUILD.bazel",
    )
    native.new_local_repository(
        name="boost",
        path="/home/qcraft/.conan2/p/b/boost27585be15b35c/p",
        build_file="/qcraft/bazel/toolchains/string_formatter/conan/boost/BUILD.bazel",
    )
    native.new_local_repository(
        name="zlib",
        path="/home/qcraft/.conan2/p/b/zliba02b8689705f2/p",
        build_file="/qcraft/bazel/toolchains/string_formatter/conan/zlib/BUILD.bazel",
    )
    native.new_local_repository(
        name="bzip2",
        path="/home/qcraft/.conan2/p/b/bzip21fd48b2f8176b/p",
        build_file="/qcraft/bazel/toolchains/string_formatter/conan/bzip2/BUILD.bazel",
    )
    native.new_local_repository(
        name="libbacktrace",
        path="/home/qcraft/.conan2/p/b/libbaa10a7f4089297/p",
        build_file="/qcraft/bazel/toolchains/string_formatter/conan/libbacktrace/BUILD.bazel",
    )
