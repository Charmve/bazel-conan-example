#include <cstdlib>
#include <fmt/core.h>

#include <iostream>
#include <boost/version.hpp>

int main() {
    std::cout << "Hello, World! Using Boost version: " << BOOST_VERSION << std::endl;
    fmt::print("{} - The C++ Package Manager!\n", "Conan");
    return EXIT_SUCCESS;
    return 0;
}
