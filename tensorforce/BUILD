load("@pip_deps//:requirements.bzl", "requirement")

py_library(
    name = "tensorforce_lib",
    srcs = glob(["**/*.py"], exclude=["*test.py"]),
    deps = [
        requirement("gym"),
        requirement("tensorflow"),
    ],
    visibility = ["//visibility:public"],
)
