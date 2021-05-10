<p align='center'>
<img src='../../_images/logo.png' width='512px'/>
</p>

# isolate

<p align='left'>
<img src='https://img.shields.io/badge/type-class-green' />
<img src='https://img.shields.io/badge/since-1.0.0-green' />
</p>

The isolate class provide information about the path of the applet isolation environment

## Static Properties

### `applet`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)
![readonly](https://img.shields.io/badge/readonly-true-green)

Get the current working path of the applet. `os.getcwd()` and `os.getcwdb()` has been locked to return the applet working path

- type: str

### `storage`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)
![readonly](https://img.shields.io/badge/readonly-true-green)

Get the current storage path of the applet. `os.getswd()` has been locked to return the applet working path

> Please save the data in the storage path, otherwise the data may be lost

- type: str
