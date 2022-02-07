from conans import ConanFile, CMake

class BaseClassesConan(ConanFile):
    name = "base-classes"
    version = "1.0.0"
    license = "Apache-2.0"
    url = "https://docs.microsoft.com/en-us/windows/win32/directshow/using-the-directshow-base-classes"
    description = "DirectShow Base Classes"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"
    exports_sources = "CMakeLists.txt", "*.cpp", "*.h" 
        
    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

        # Explicit way:
        # self.run('cmake "%s/src" %s' % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["base-classes", "strmiids"]