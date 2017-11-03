from setuptools import find_packages
from setuptools import setup


extras_require = {
    'tests': [
        'plone.app.testing',
        'unittest2',
        'ftw.builder',
        'ftw.testbrowser',
        'ftw.testing',
    ],
}

setup(name='arctic.web',
      version='1.0.0.dev0',
      author='4teamwork AG',
      url='https://github.com/4teamwork/arctic.web',
      license='GPL2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['arctic'],
      include_package_data=True,
      zip_safe=False,

      install_requires=[
          'Plone',
          'collective.editmodeswitcher',
          'ftw.file',
          'ftw.footer',
          'ftw.htmlblock',
          'ftw.iframeblock',
          'ftw.inflator [dexterity]',
          'ftw.lawgiver',
          'ftw.mobile',
          'ftw.news',
          'ftw.redirector',
          'ftw.simplelayout [contenttypes, mapblock]',
          'ftw.sliderblock',
          'ftw.statusmap',
          'ftw.subsite',
          'ftw.upgrade',
          'plone.app.caching',
          'plonetheme.blueberry',
          'setuptools',
      ],

      tests_require=extras_require['tests'],
      extras_require=extras_require,

      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
