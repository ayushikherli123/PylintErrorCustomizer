from pylint_error_customizer import PylintErrorCustomizer

BASE_DIR = "Base directory path"
FILTER_PATTERN = "Regex pattern to filter errors"

py_cust = PylintErrorCustomizer(BASE_DIR)

# Method is used to find pylint errors, a file named
# "pylint_errors.txt" will be generated after successful
# execution of below method
py_cust.find_pylint_errors()

# Method is used to filter pylint errors, A regex pattern needs
# to be provided as method argument
# A file named "filered_pylint_errors.txt" will be generated after
# successful execution of below method
# Note : This method is used to filter errors from "pylint_errors.txt"
# file previously generated, if one wants to provide his/her file,
# the new file can be set to `OUTPUT_FILE` variable provided in script
py_cust.filter_pylint_errors(FILTER_PATTERN)
