# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The program to use to edit the cache.
CMAKE_EDIT_COMMAND = /usr/bin/cmake-gui

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/saksham/work/freescale/validation/modelling/ASFT/stm_python

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/saksham/work/freescale/validation/modelling/ASFT/stm_python

# Include any dependencies generated for this target.
include CMakeFiles/stp-example.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/stp-example.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/stp-example.dir/flags.make

CMakeFiles/stp-example.dir/example.c.o: CMakeFiles/stp-example.dir/flags.make
CMakeFiles/stp-example.dir/example.c.o: example.c
	$(CMAKE_COMMAND) -E cmake_progress_report /home/saksham/work/freescale/validation/modelling/ASFT/stm_python/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building C object CMakeFiles/stp-example.dir/example.c.o"
	/usr/bin/cc  $(C_DEFINES) $(C_FLAGS) -o CMakeFiles/stp-example.dir/example.c.o   -c /home/saksham/work/freescale/validation/modelling/ASFT/stm_python/example.c

CMakeFiles/stp-example.dir/example.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/stp-example.dir/example.c.i"
	/usr/bin/cc  $(C_DEFINES) $(C_FLAGS) -E /home/saksham/work/freescale/validation/modelling/ASFT/stm_python/example.c > CMakeFiles/stp-example.dir/example.c.i

CMakeFiles/stp-example.dir/example.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/stp-example.dir/example.c.s"
	/usr/bin/cc  $(C_DEFINES) $(C_FLAGS) -S /home/saksham/work/freescale/validation/modelling/ASFT/stm_python/example.c -o CMakeFiles/stp-example.dir/example.c.s

CMakeFiles/stp-example.dir/example.c.o.requires:
.PHONY : CMakeFiles/stp-example.dir/example.c.o.requires

CMakeFiles/stp-example.dir/example.c.o.provides: CMakeFiles/stp-example.dir/example.c.o.requires
	$(MAKE) -f CMakeFiles/stp-example.dir/build.make CMakeFiles/stp-example.dir/example.c.o.provides.build
.PHONY : CMakeFiles/stp-example.dir/example.c.o.provides

CMakeFiles/stp-example.dir/example.c.o.provides.build: CMakeFiles/stp-example.dir/example.c.o

# Object files for target stp-example
stp__example_OBJECTS = \
"CMakeFiles/stp-example.dir/example.c.o"

# External object files for target stp-example
stp__example_EXTERNAL_OBJECTS =

stp-example: CMakeFiles/stp-example.dir/example.c.o
stp-example: CMakeFiles/stp-example.dir/build.make
stp-example: /usr/local/lib/libstp.so.2.0.99
stp-example: /usr/lib/x86_64-linux-gnu/libboost_program_options.so
stp-example: /usr/local/lib/libminisat.so
stp-example: CMakeFiles/stp-example.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking C executable stp-example"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/stp-example.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/stp-example.dir/build: stp-example
.PHONY : CMakeFiles/stp-example.dir/build

CMakeFiles/stp-example.dir/requires: CMakeFiles/stp-example.dir/example.c.o.requires
.PHONY : CMakeFiles/stp-example.dir/requires

CMakeFiles/stp-example.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/stp-example.dir/cmake_clean.cmake
.PHONY : CMakeFiles/stp-example.dir/clean

CMakeFiles/stp-example.dir/depend:
	cd /home/saksham/work/freescale/validation/modelling/ASFT/stm_python && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/saksham/work/freescale/validation/modelling/ASFT/stm_python /home/saksham/work/freescale/validation/modelling/ASFT/stm_python /home/saksham/work/freescale/validation/modelling/ASFT/stm_python /home/saksham/work/freescale/validation/modelling/ASFT/stm_python /home/saksham/work/freescale/validation/modelling/ASFT/stm_python/CMakeFiles/stp-example.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/stp-example.dir/depend
