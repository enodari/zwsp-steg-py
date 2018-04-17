from setuptools import find_packages, setup

setup(
    name='zwsp-steg-py',
    version=__import__('zwsp_steg').__version__,
    description='Zero-Width Space Steganography, encodes/decodes hidden messages as non printable/readable characters.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Edoardo Nodari',
    author_email='info@nodari.me',
    url='https://github.com/enodari/zwsp-steg-py',
    packages=find_packages(),
    include_package_data=True,
    license='Apache 2.0',
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.6',
    ],
)
