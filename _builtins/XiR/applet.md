<p align='center'>
<img src='../../_images/logo.png' width='512px'/>
</p>

# applet

<p align='left'>
<img src='https://img.shields.io/badge/type-class-green' />
<img src='https://img.shields.io/badge/since-1.0.0-green' />
</p>

The applet class provide information about the applet

## Static Properties

### `id`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)
![readonly](https://img.shields.io/badge/readonly-true-green)

Get the id of the applet.

- type: str

### `name`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)
![readonly](https://img.shields.io/badge/readonly-true-green)

Get the name of the applet.

- type: str

### `version`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)
![readonly](https://img.shields.io/badge/readonly-true-green)

Get the version number of the applet.

- type: str

### `runtime`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)
![readonly](https://img.shields.io/badge/readonly-true-green)

Obtain the minimum version environment required for the applet

- type: str

### `archicads`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)
![readonly](https://img.shields.io/badge/readonly-true-green)

Obtain the minimum version environment required for the applet

- type: list

## Static Methods

### `abort()`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

Terminate the current applet. Please note that this function does not terminate the applet immediately, but needs to wait for the system to be idle.

- parameters: `None`
- return: `None`

### `reboot()`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

Reboot the current applet. Please note that this function does not reboot the applet immediately, but needs to wait for the system to be idle.

- parameters: `None`
- return: `None`
