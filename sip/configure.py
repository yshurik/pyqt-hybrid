import os
import sipconfig
from PyQt4 import pyqtconfig

build_file = "PyQtHybrid.sbf"
config = pyqtconfig.Configuration()
pyqt_sip_flags = config.pyqt_sip_flags

os.system(" ".join([ \
    config.sip_bin, \
    "-c", ".", \
    "-b", build_file, \
    "-I", config.pyqt_sip_dir, \
    pyqt_sip_flags, \
    "MainWindow.sip" \
]))

installs = []
installs.append(["MainWindow.sip", os.path.join(config.default_sip_dir, "PyQtHybrid")])
installs.append(["PyQtHybridConfig.py", config.default_mod_dir])

makefile = pyqtconfig.QtGuiModuleMakefile(
    configuration=config,
    build_file=build_file,
    installs=installs
)

makefile.extra_libs = ["PyQtHybrid"]
makefile.extra_lib_dirs = [".."]

makefile.generate()

content = {
    "PyQtHybrid_sip_dir":    config.default_sip_dir,
    "PyQtHybrid_sip_flags":  pyqt_sip_flags
}
sipconfig.create_config_module("PyQtHybridConfig.py", "PyQtHybridConfig.py.in", content)

