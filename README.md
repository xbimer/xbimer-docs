<p align='center'>
<img src='./_images/logo.png' width='512px'/>
</p>
<p align='center'>
<img src='https://img.shields.io/pypi/v/xbimer_cli?label=cli%20latest' />
<img src='https://img.shields.io/github/v/release/xbimer/xbimer-xir?label=xir%20latest' />
</p>

<p align='center'>
  <a href='https://www.xbimer.com'>Official website</a>
</p>

xBIMer is a python sdk plugin designed for Archicad. It allows developers to use python to develop plugins for archicad. Since you need to install a huge IDE when using the official C++ sdk to develop plug-ins, it is not very friendly to developers. Secondly, the official only provides c++ sdk as the only choice for archicad, not as many choices as Revit. This indirectly makes it difficult for other developers to integrate into the development of archicad plugins.

xBIMer is a solution between the official C++SDK and the official Python API, and will support Archicad 22 or above. It allows developers to use python language to access the functions in Archicad's C++SDK (if allowed), such as menus, dialog and other C++ interfaces. In addition, you can also use the official python api module in xBIMer (Requires Archicad 24 or above).Using xBIMer you will not need to install `visual studio` (on windows system), `Xcode` (on macos system, mac system will be supported in the future) can develop plug-ins for Archicad. You can write the code once and run it in the Windows system and the macos system, without the need for adaptation between different systems. Not only that, the plug-ins you develop based on xBIMer can be easily extended to different versions of Archicad without the need for additional compilation and adaptation. At the same time, with the help of Python's perfect package management mechanism, you can also easily add third-party modules on the PyPi website to the Archicad plug-in.

## Components

- [XiR](https://github.com/xbimer/xbimer-xir): Python runtime for Archciad
  - [Install](./xir/install.md)
  - [Update](./xir/update.md)
  - [Builtins](./_builtins/README.md)
  - [Hooks](./_hook/README.md)
  - [Example](./_example/README.md)
  - Supported
    - Windows
      - Archicad 22
      - Archicad 23
      - Archicad 24
    - MacOS
      - in future
- [CLI](https://github.com/xbimer/xbimer-cli): Command line tools for xBIMer
  - [Install](./cli/install.md)
  - [Update](./cli/update.md)
  - [Usage](./cli/commands/README.md)
- [Modules](https://github.com/xbimer/xbimer-modules)
  - [Type Conversions](./_modules/TypeConversions.md)
  - [GSRoot](./_modules/gsroot/README.md)

## Feature

- Use python as a development language
- Full Python 3.7.5 features
- Hot debugging (you can re-run the new code without closing Archicad)
- Log level

## Tutorials

- [Videos](https://www.xbimer.com/videos)

## Subscribe

- Twitter: @xbimerOfficial

## Feedback

- [Creat issue on github](https://github.com/xbimer/xbimer-docs/issues/new)
- Click ★ <kbd> Star </kbd> on the right conner of this page if `xbimer` project helps you

## Join project

You can send an email to 502554248@qq.com. Whenever there is the latest feature update, you will be the first to experience it.
Or you can `fork` these items([modules](https://github.com/xbimer/xbimer-modules),[docs](https://github.com/xbimer/xbimer-docs)) and submit them to us through `pull request` after modification

## Service providers

- [Github](https://github.com/xbimer)
- [Youtube](https://www.youtube.com/channel/UCDZAh_-VJj_GsEXzi3KMA2Q)
- [Vultr](https://www.vultr.com)
- [IFTTT](https://ifttt.com/)
- [PyPi](https://pypi.org/project/xbimer-cli/)
