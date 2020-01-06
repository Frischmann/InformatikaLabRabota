from cx_Freeze import setup, Executable

executables = [Executable('PyLab.py')]

options = {
    'build_exe': {
        'include_msvcr': True,
    }
}


setup(name='LabRabota',
      version='0.0.1',
      description='LabRabota',
      executables=executables)