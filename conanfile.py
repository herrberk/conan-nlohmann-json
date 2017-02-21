from conans import ConanFile
from conans.tools import download, check_sha256

class NlohmannJsonConan(ConanFile):
    name = 'json'
    version = '2.0.10'
    description = 'JSON for Modern C++.'
    url = 'https://github.com/jjones646/conan-nlohmann-json'
    license = 'https://github.com/nlohmann/json/blob/v2.0.10/LICENSE.MIT'
    settings = None

    def source(self):
        download_url = 'https://github.com/nlohmann/json/releases/download/v{!s}/json.hpp'.format(self.version)
        download(download_url, 'json.hpp')
        check_sha256('json.hpp', 'ec27d4e74e9ce0f78066389a70724afd07f10761009322dc020656704ad5296d')

    def build(self):
        return  # do nothing - header only

    def package(self):
        self.copy(pattern='json.hpp', dst='include/nlohmann')

    def package_id(self):
        self.info.requires.clear()
