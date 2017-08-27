from setuptools import setup
# from setuptools import setup

requires=['numpy', 'scipy', 'progressbar', 'pandas', 'matplotlib', 'dill', 'csv', 'phy', 'itertools', 'mpl_toolkits', 'sklearn']

setup(
  name = 'XtraDataManager',
  packages = ['XtraDataManager'], # this must be the same as the name above
  version = '1.2',
  description = 'Kilosort/phy generated extracellular data managment, including supervised and unsupervised classification of units, in order to sort them by cell type.',
  author = 'Maxime Beau',
  author_email = 'm.beau047@gmail.com',
  url = 'https://github.com/MS047/XtraDataManager', # use the URL to the github repo
  download_url = 'https://github.com/MS047/XtraDataManager/archive/1.2.tar.gz', # I'll explain this in a second
  keywords = ['XtraDataManager', 'Phy', 'Classifier', 'sklearn', 'Extracellular', 'Spike Sorting', 'units', 'cell type'], # arbitrary keywords
  classifiers = ['Development Status :: 3 - Alpha', 'Intended Audience :: Science/Research', 'License :: OSI Approved :: MIT License', 'Programming Language :: Python :: 3.5', 'Environment :: Console', 'Natural Language :: English'],
  install_requires = requires,
  python_requires = '>=3'
)