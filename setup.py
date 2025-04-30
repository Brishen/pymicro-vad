# Available at setup time due to pyproject.toml
from pybind11.setup_helpers import Pybind11Extension
from setuptools import setup

__version__ = "1.0.2"

# Define all paths as relative
microvad_dir = "micro_vad"
frontend_dir = f"{microvad_dir}/tensorflow/lite/experimental/microfrontend/lib"
kissfft_dir = f"{microvad_dir}/kissfft"

# Define source files with relative paths
sources = [f"{microvad_dir}/micro_vad.cpp"]
frontend_files = [
    "kiss_fft_int16.cc",
    "fft.cc",
    "fft_util.cc",
    "filterbank.cc",
    "filterbank_util.cc",
    "frontend.cc",
    "frontend_util.cc",
    "log_lut.cc",
    "log_scale.cc",
    "log_scale_util.cc",
    "noise_reduction.cc",
    "noise_reduction_util.cc",
    "pcan_gain_control.cc",
    "pcan_gain_control_util.cc",
    "window.cc",
    "window_util.cc",
]

# Add frontend sources with proper paths
for f in frontend_files:
    sources.append(f"{frontend_dir}/{f}")

# Add kissfft sources
sources.append(f"{kissfft_dir}/kiss_fft.cc")
sources.append(f"{kissfft_dir}/tools/kiss_fftr.cc")

flags = ["-DFIXED_POINT=16"]
ext_modules = [
    Pybind11Extension(
        name="micro_vad_cpp",
        language="c++",
        cxx_std=17,
        extra_compile_args=flags,
        sources=sorted(sources + ["python.cpp"]),
        define_macros=[("VERSION_INFO", __version__)],
        include_dirs=[microvad_dir, kissfft_dir],
    ),
]

setup(
    name="pymicro_vad2",
    version=__version__,
    author="Michael Hansen",
    author_email="mike@rhasspy.org",
    url="https://github.com/Brishen/pymicro-vad",
    description="Self-contained voice activity detector",
    long_description="",
    packages=["pymicro_vad"],
    ext_modules=ext_modules,
    zip_safe=False,
    python_requires=">=3.7",
    classifiers=["License :: OSI Approved :: Apache Software License"],
)
