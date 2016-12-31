from conans import ConanFile
from conans.tools import download, unzip


class NLJsonConan(ConanFile):
    name = "nl-json"
    version = "2.0.9"
    url = "https://github.com/eliaskousk/conan-nl-json.git"
    license = "MIT"
    author = "Elias K."
    settings = None  # header only
    options = {"path": "ANY"}
    default_options = "path="

    def source(self):
        download("https://github.com/nlohmann/json/releases/download/v%s/json.hpp" % self.version, "json.hpp")

    def build(self):
        del self
        # Do nothing - header only

    def package(self):
        header_dir = "include"
        if self.options.path != "":
            header_dir += "/" + str(self.options.path)
        self.copy("*.hpp", dst=header_dir)

