from distutils.core import setup
# from setuptools import setup
setup(
  name = 'XtraDataManager',
  packages = ['XtraDataManager'], # this must be the same as the name above
  version = '0.2',
  description = 'Kilosort/phy generated extracellular data managment, including supervised and unsupervised classification of units, in order to sort them by cell type.',
  author = 'Maxime Beau',
  author_email = 'm.beau047@gmail.com',
  url = 'https://github.com/MS047/XtraDataManager', # use the URL to the github repo
  download_url = 'https://github.com/MS047/XtraDataManager/archive/0.2.tar.gz', # I'll explain this in a second
  keywords = ['Kilosort', 'Phy', 'Classifier', 'sklearn', 'Extracellular', 'Spike Sorting'], # arbitrary keywords
  classifiers = [],
)