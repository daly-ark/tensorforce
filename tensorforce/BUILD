load("@pip_deps//:requirements.bzl", "requirement")

py_library(
    name = "tensorforce_lib",
    srcs = glob(["**/*.py"], exclude=["*test.py"]),
    deps = [
        requirement("gym"),
        requirement("h5py"),
        requirement("matplotlib"),
        requirement("msgpack"),
        requirement("msgpack-numpy"),
        requirement("numpy"),
        requirement("Pillow"),
        requirement("tensorflow"),
        requirement("tqdm"),
    ],
    visibility = ["//visibility:public"],
)
