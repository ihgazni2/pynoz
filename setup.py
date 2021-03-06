from setuptools import setup, find_packages


requirements = []

setup(
      name="pynoz",
      version = "0.0.9", #@version@#
      description="simple tools for time date timezone",
      author="ihgazni2",
      url="https://github.com/ihgazni2/pynoz",
      author_email='', 
      license="MIT",
      long_description = "refer to .md files in https://github.com/ihgazni2/pynoz",
      classifiers=[
          'Environment :: Console',
          'Environment :: Web Environment',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'Programming Language :: Python',
          ],
      packages= find_packages(),
      entry_points={
          'console_scripts': [
              'pynoz=pynoz.bin:main'
          ]
      },
      package_data={
          'resources':['RESOURCES/*']
      },
      include_package_data=True,
      install_requires=requirements,
      py_modules=['pynoz'], 
)


# python3 setup.py bdist --formats=tar
# python3 setup.py sdist








