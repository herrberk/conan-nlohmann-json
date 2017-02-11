from conan.packager import ConanMultiPackager
import os

username = os.getenv('CONAN_USERNAME', 'keysight')
os.environ['CONAN_USERNAME'] = username
channel = os.getenv('CONAN_CHANNEL', 'stable')
os.environ['CONAN_CHANNEL'] = channel
log_run = os.getenv('CONAN_LOG_RUN_TO_FILE', '1')
os.environ['CONAN_LOG_RUN_TO_FILE'] = log_run

if __name__ == "__main__":
    builder = ConanMultiPackager(
        args='-o json:no_exceptions=False',
        gcc_versions=['4.9', '5.2', '5.3', '5.4'],
        apple_clang_versions=['6.1', '7.0', '7.3', '8.0'],
        visual_versions=['14'],
        visual_runtimes=['MT'],
        archs=['x86_64'],
        use_docker=False,
        upload=False,
        username=username,
        channel=channel,
        reference='json/2.1.0',
    )
    builder.add_common_builds(pure_c=False)
    builder.run()

    builder = ConanMultiPackager(
        args='-o json:no_exceptions=True',
        gcc_versions=['5.4'],
        apple_clang_versions=['8.0'],
        visual_versions=['14'],
        visual_runtimes=['MT'],
        archs=['x86_64'],
        use_docker=False,
        upload=False,
        username=username,
        channel=channel,
        reference='json/2.1.0',
    )
    builder.add_common_builds(pure_c=False)
    builder.run()
