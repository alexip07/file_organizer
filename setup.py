from cx_Freeze import setup, Executable

setup(
    name="File Organizer",
    version="1.0",
    description="The application can be used to manage files on the PC, from a certain folder, in the given example, from the Downloads folder",
    executables=[Executable("main.pyw")]
)
