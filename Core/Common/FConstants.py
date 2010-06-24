# Copyright (C) 2006-2010 Khronos Group
# Available only to Khronos members.
# Distribution of this file or its content is strictly prohibited.

IMPORT = "Import"
EXPORT = "Export"
RENDER = "Render"
VALIDATE = "Validate"
OPERATIONS = [IMPORT, EXPORT, RENDER, VALIDATE]
OPS_NEEDING_APP = [IMPORT, VALIDATE]
SCHEMA_LOCATION = "COLLADASchema.xsd"
SCHEMA_NAMESPACE = "http://www.collada.org/2005/11/COLLADASchema"
ABSTRACT_APPLICATION = "FApplication.py"
SCRIPTS_DIR = "../Scripts"
IMAGE_COMPARATORS_DIR = "../ImageComparators" # directory where image comparators are stored
IMAGE_COMPARATORS_LABEL = "imageComparator" # tag in the config file for selected comparator
ROOT_DIR = "../StandardDataSets" # backward compatibility
DATA_SET_DIRS = ["../StandardDataSets",] # rel. path
SETTINGS_DIR = "../ApplicationSettings"
SETTING_EXT = "txt"
LOG_EXT = "log"
RUNS_FOLDER = "../TestProcedures"
MAIN_FOLDER = ".."
CSV_POSTFIX = "_Files"
HTML_POSTFIX = "_Files"
IMAGES_DIR = "images"
BLESSED_DIR = "Blessed"
BLESSED_EXECUTIONS = "executions"
BLESSED_ANIMATIONS = "animations"
BLESSED_EXECUTIONS_HASH = "executionsManager"
BLESSED_DEFAULT_FILE = "default.txt"
TEST_PROCEDURE_FILENAME = "serializedTestProcedure.obj"
TEST_PROCEDURE_COMMENTS = "comments.txt"
TEST_GUI_PREFERENCES = "prefs.obj"
ASSET_FILENAME = "../temp.txt"
TEST_FILENAME = "serializedTest.obj"
EXECUTION_FILENAME = "serializedExecution.obj"
EXECUTION_PREFIX = "Execution_"
STEP_PREFIX = "step"
TEST_PREFIX = "Test"
DCC_WORK1 = "WorkingDir"
DCC_WORK2 = "Execution"
DCC_WORK3 = "Step"
PASS = 1
FAIL = 0
CONFIGURATION_FILE = "../config.txt"
DOCUMENTATION = "../Documentation/README.doc"
FILEWATCHER = "FileWatcher.exe"
KILLER = "ProcessKiller.exe"
VERSION = "1.0.0"
PACKAGE_RESULTS_DIR = "../PackagedResults"
