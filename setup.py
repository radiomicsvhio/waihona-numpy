from distutils.core import setup
setup(
  name = 'waihonanumpy',                                                                 # How you named your package folder (MyLib)
  packages = ['waihonanumpy'],                                                           # Chose the same as "name"
  version = 'v0.0.1',                                                                        # Start with a small number and increase it with every change you make
  license='cc-by-sa-4.0',                                                                 # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Store and retreive Numpy Array data.',                                   # Give a short description about your library
  author = 'Camilo A. Monreal',                                                           # Type in your name
  author_email = 'camilomonreal@vhio.net',                                                # Type in your E-Mail
  url = 'https://github.com/radiomicsvhio/waihona-numpy',                                 # Provide either the link to your github or to your website
  download_url = 'https://github.com/radiomicsvhio/waihona-numpy/archive/v0.0.1.tar.gz',    # I explain this later on
  keywords = ['redis', 'numpy', 'store'],                                                 # Keywords that define your package best
  install_requires=[                                                                      # I get to this in a second
          'redis',
          'msgpack',
          'msgpack-numpy',
          'more-itertools'
          'numpy'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',                                                    # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',                                                    # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: Creative Commons Attribution Share Alike 4.0 License',    # Again, pick a license
    'Programming Language :: Python :: 3',                                                # Specify which python versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)