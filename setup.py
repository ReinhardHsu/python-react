from setuptools import setup
import react

setup(
    name='react',
    version=react.__version__,
    packages=['django_react'],
    install_requires=[
        'optional-django==0.2.1'
    ],
    description='Server-side rendering, client-side mounting, JSX translation, and component bundling',
    long_description='Documentation at https://github.com/markfinger/python-react',
    author='Mark Finger',
    author_email='markfinger@gmail.com',
    url='https://github.com/markfinger/python-react',
)
