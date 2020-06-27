import setuptools


setuptools.setup(name='wave_checker',
      version="1.0.0",
      url = "https://github.com/cristinafareizaga/wave_checker.git",
      description='Easy way to find the best waves by analyzing windguru',
      author='Cristina Areizaga',
      author_email='cristinafareizaga@gmail.com',
      packages=setuptools.find_packages(),
      install_requires=['bs4','selenium','pandas','matplotlib','seaborn','lxml'],
      classifiers=[
       "Programming Language :: Python :: 3",
       "License :: OSI Approved :: MIT License"
       ],
     )