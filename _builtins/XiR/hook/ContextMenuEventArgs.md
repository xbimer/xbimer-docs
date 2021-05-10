<p align='center'>
<img src='../../../_images/logo.png' width='512px'/>
</p>

# ContextMenuEventArgs

<p align='left'>
<img src='https://img.shields.io/badge/type-class-green' />
<img src='https://img.shields.io/badge/since-1.0.0-green' />
</p>

## Methods

### `AddItem(text,fn,isEnabled,isChecked)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

Add a context menu.

- parameters:
  - text: `str`
  - fn: `Function`
  - isEnabled: `bool`,default `True`
  - isChecked: `bool`,default `False`
- return: `None`

### `AddSeparator()`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

Add a separator to the context menu.

- parameters: `None`
- return: `None`

### `StartPopupMenu(name)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

Start popup menu

- parameters:
  - name: `str`
- return: `None`

### `EndPopupMenu()`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

End popup menu

- parameters: `None`
- returnType: `None`
