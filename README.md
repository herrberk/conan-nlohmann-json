[![Build Status](https://travis-ci.org/eliaskousk/conan-nl-json.svg?branch=release/2.0.9)](https://travis-ci.org/eliaskousk/conan-nl-json)

# conan-nl-json

Simple conan package for the header-only "JSON for modern C++" library by Niels Lohmann (https://github.com/nlohmann/json).

# Usage

In your conanfile, add `nl-json/2.0.9@eliaskousk/stable` in the `[requires]` section. Since the library is header-only, settings do not apply.

## Options

There is an option `path` to change the path where the header gets deployed to. The default is empty, i.e. the header gets deployed directly into the include directory of the package and can be included via `#include <json.hpp>`.

To change this, specify the relative path, e.g. use

    conan build .. -o nlJson:path=nlohmann

or add the line

    nlJson:path=nlohmann

to the `[options]` section of your `conanfile.txt`, and then include the headers via `#include <nlohmann/json.hpp>`.

