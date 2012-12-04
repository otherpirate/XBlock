from distutils.core import setup

setup(
    name='XBlock',
    version='0.1',
    description='XBlock Core Library',
    package_dir={'xblock': ''},
    packages=['xblock'],
    entry_points={
        'xblock.v1': [
            'helloworld = xblock.core:HelloWorldBlock',
            'vertical = xblock.core:VerticalBlock',
            'problem = xblock.problem:ProblemBlock',
            'textinput = xblock.problem:TextInputBlock',
            'thumbs = xblock.thumbs:ThumbsBlock',
            'equality = xblock.problem:EqualityCheckerBlock',
        ]
    }
)
